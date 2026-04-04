# Gerekli kütüphaneler
import pandas as pd
import numpy as np

# Müşteri sayısı
num_customers = 1000

# Persona dağılımları
personas = ["Unutkan", "Sıkıntıda", "Güçlükte", "Dijital_Olmayan"]
persona_distribution = [0.4, 0.3, 0.2, 0.1] # Müşterilerin %40'ı unutkan, %30'u sıkıntıda vs.

# Veri seti için listeler
customer_ids = []
initial_debts = []
initial_days_overdue = []
payment_history_scores = [] # 1 (kötü) ile 10 (mükemmel) arası
customer_personas = []

for i in range(num_customers):
    customer_id = 1000 + i
    persona = np.random.choice(personas, p=persona_distribution)

    if persona == "Unutkan":
        debt = np.random.uniform(100, 1000)
        days_overdue = np.random.randint(5, 20)
        history_score = np.random.randint(8, 11)
    elif persona == "Sıkıntıda":
        debt = np.random.uniform(500, 5000)
        days_overdue = np.random.randint(15, 45)
        history_score = np.random.randint(5, 8)
    elif persona == "Güçlükte":
        debt = np.random.uniform(200, 10000)
        days_overdue = np.random.randint(30, 90)
        history_score = np.random.randint(1, 5)
    else: # Dijital_Olmayan
        debt = np.random.uniform(150, 2000)
        days_overdue = np.random.randint(10, 30)
        history_score = np.random.randint(6, 9)

    customer_ids.append(customer_id)
    initial_debts.append(round(debt, 2))
    initial_days_overdue.append(days_overdue)
    payment_history_scores.append(history_score)
    customer_personas.append(persona)

# DataFrame oluşturma
df_customers = pd.DataFrame({
    'customer_id': customer_ids,
    'initial_debt': initial_debts,
    'initial_days_overdue': initial_days_overdue,
    'payment_history_score': payment_history_scores,
    'persona': customer_personas
})

# CSV olarak kaydetme
df_customers.to_csv('synthetic_customer_data.csv', index=False)

print("Sentetik veri başarıyla oluşturuldu ve 'synthetic_customer_data.csv' olarak kaydedildi.")
print(df_customers.head())