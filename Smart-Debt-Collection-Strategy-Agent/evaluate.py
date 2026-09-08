import pandas as pd
from stable_baselines3 import DQN
from debt_collection_env import DebtCollectionEnv
import numpy as np
import os # Dosya kontrolü için eklendi

# --- KOD BAŞLANGICI ---

# Model dosyasının adını bir değişkene atayalım
MODEL_PATH = "dqn_debt_collector.zip"

# 1. Gerekli dosyaların varlığını kontrol edelim
if not os.path.exists('synthetic_customer_data.csv'):
    print("Hata: 'synthetic_customer_data.csv' dosyası bulunamadı.")
    print("Lütfen önce 'generate_data.py' dosyasını çalıştırın.")
    exit()

if not os.path.exists(MODEL_PATH):
    print(f"Hata: '{MODEL_PATH}' model dosyası bulunamadı.")
    print("Lütfen önce 'train.py' dosyasını çalıştırarak modeli eğitin.")
    exit()

# 2. Veri ve ortamı yükle
df = pd.read_csv('synthetic_customer_data.csv')
env = DebtCollectionEnv(df_customers=df)

# 3. Eğitilmiş modeli yükle
model = DQN.load(MODEL_PATH)

# 4. Test etme
num_episodes = 500
total_rewards = []
actions_taken = {0:0, 1:0, 2:0, 3:0} # SMS, Email, Call, Wait
events = {'payment': 0, 'churn': 0, 'timeout': 0}

print(f"\nEğitilmiş model '{MODEL_PATH}' ile {num_episodes} bölüm (müşteri senaryosu) test ediliyor...")

for i in range(num_episodes):
    obs, info = env.reset()
    done = False
    episode_reward = 0
    
    # while döngüsü, bir müşteri için süreç tamamlanana kadar devam eder
    while not done:
        # Modelden deterministik (en iyi) eylemi tahmin etmesini iste
        action_array, _states = model.predict(obs, deterministic=True)
        
        # === ANA DÜZELTME BURADA ===
        # model.predict'ten gelen numpy array'ini basit bir tam sayıya (integer) çeviriyoruz.
        action = int(action_array)
        
        # Seçilen eylemi say
        actions_taken[action] += 1
        
        # Ortama eylemi gönder ve sonucu al
        # env.step fonksiyonuna artık 'action' olarak bir array değil, bir integer gidiyor.
        obs, reward, done, _, info = env.step(action)
        
        # Toplam ödülü güncelle
        episode_reward += reward
        
    # Bölüm (episode) bittiğinde olayı kaydet
    if info.get('event'):
        events[info['event']] += 1
        
    total_rewards.append(episode_reward)

# 5. Sonuçları Yazdır
print("\n--- Değerlendirme Sonuçları ---")
print(f"Ortalama Toplam Ödül: {np.mean(total_rewards):.2f}")
print(f"Minimum Ödül: {np.min(total_rewards):.2f}")
print(f"Maksimum Ödül: {np.max(total_rewards):.2f}")

print("\n--- Ajanın Eylem Stratejisi ---")
total_actions = sum(actions_taken.values())
print(f"  - SMS Gönder:      {actions_taken[0]} kez (%{100 * actions_taken[0] / total_actions:.1f})")
print(f"  - E-posta Gönder:  {actions_taken[1]} kez (%{100 * actions_taken[1] / total_actions:.1f})")
print(f"  - Arama Yap:       {actions_taken[2]} kez (%{100 * actions_taken[2] / total_actions:.1f})")
print(f"  - Bekle:           {actions_taken[3]} kez (%{100 * actions_taken[3] / total_actions:.1f})")

print("\n--- Senaryo Sonuçları ---")
print(f"  - Başarılı Tahsilat (Payment): {events['payment']} kez")
print(f"  - Müşteri Kaybı (Churn):       {events['churn']} kez")
print(f"  - Zaman Aşımı (Timeout):       {events['timeout']} kez")
print("-" * 30)

# --- KOD SONU ---