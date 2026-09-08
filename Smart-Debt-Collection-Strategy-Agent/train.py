import pandas as pd
from stable_baselines3 import DQN
from debt_collection_env import DebtCollectionEnv
from stable_baselines3.common.env_checker import check_env

# 1. Adımda oluşturduğumuz veriyi yükle
df = pd.read_csv('synthetic_customer_data.csv')

# 2. Adımda oluşturduğumuz ortamı başlat
env = DebtCollectionEnv(df_customers=df)

# Ortamın Stable-Baselines3 standartlarına uygunluğunu kontrol et (önemli!)
check_env(env)

# Modeli oluştur (DQN - MlpPolicy)
model = DQN('MlpPolicy', env, 
            verbose=1, 
            learning_rate=1e-4,
            buffer_size=50000,
            learning_starts=1000,
            batch_size=32,
            gamma=0.99, # Gelecekteki ödüllere verilen önem
            exploration_fraction=0.1, # Ne kadar süre keşif yapacağı
            exploration_final_eps=0.02,
            tensorboard_log="./dqn_debt_collection_tensorboard/")

# Modeli eğit (100,000 adımda)
model.learn(total_timesteps=100000, progress_bar=True)

# Eğitilmiş modeli kaydet
model.save("dqn_debt_collector")

print("Model eğitimi tamamlandı ve 'dqn_debt_collector.zip' olarak kaydedildi.")

# Tensorboard'u başlatmak için terminale şunu yazın:
# tensorboard --logdir ./dqn_debt_collection_tensorboard/