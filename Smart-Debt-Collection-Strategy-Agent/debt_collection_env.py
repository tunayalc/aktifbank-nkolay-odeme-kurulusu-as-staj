import gymnasium as gym
from gymnasium import spaces
import numpy as np
import pandas as pd

class DebtCollectionEnv(gym.Env):
    def __init__(self, df_customers):
        super(DebtCollectionEnv, self).__init__()
        
        self.df = df_customers
        self.current_customer = None
        
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=np.array([0, 0, 0]), 
                                            high=np.array([1, 1, 1]), 
                                            dtype=np.float32)

        self.max_debt = self.df['initial_debt'].max()
        self.max_days = 120
        self.max_history_score = 10

    def _get_observation(self):
        obs = np.array([
            self.current_debt / self.max_debt,
            self.current_days_overdue / self.max_days,
            self.current_history_score / self.max_history_score
        ])
        return obs.astype(np.float32)

    def reset(self, seed=None):
        super().reset(seed=seed)
        
        self.current_customer = self.df.sample(n=1).iloc[0]
        self.current_debt = self.current_customer['initial_debt']
        self.current_days_overdue = self.current_customer['initial_days_overdue']
        self.current_history_score = self.current_customer['payment_history_score']
        self.persona = self.current_customer['persona']
        
        return self._get_observation(), {}

    def step(self, action):
        terminated = False
        reward = 0
        payment_made = False

        # ÇÖZÜM 1: Daha dengeli maliyet yapısı
        action_costs = {0: -1, 1: -1.5, 2: -3, 3: -0.5}  # Arama maliyeti düşürüldü
        reward += action_costs[action]
        
        if action == 3: # Bekle
            self.current_days_overdue += 7

        payment_prob = 0
        churn_prob = 0.02

        ### PERSONA BAZLI STRATEJI ###
        if self.persona == "Unutkan":
            if action in [0, 1]: payment_prob = 0.8
            if action == 2: 
                payment_prob = 0.9  # Arama daha etkili
                churn_prob = 0.1   # Churn riski düşük
        
        elif self.persona == "Sıkıntıda":
            if action in [0, 1]: 
                payment_prob = 0.0
                churn_prob = 0.25
            if action == 2: 
                payment_prob = 0.8  # Yüksek başarı şansı
                churn_prob = 0.03   # Düşük churn

        elif self.persona == "Güçlükte":
            if action in [0, 1]: 
                payment_prob = 0.1
                churn_prob = 0.4
            if action == 2: 
                payment_prob = 0.3
                churn_prob = 0.2

        elif self.persona == "Dijital_Olmayan":
            if action in [0, 1]: payment_prob = 0.0
            if action == 2: 
                payment_prob = 0.85  # Çok yüksek başarı
                churn_prob = 0.05

        # Ödeme gerçekleşti mi?
        if np.random.rand() < payment_prob:
            # ÇÖZÜM 2: Arama ile tahsilatta BÜYÜK ödül
            if action == 2:
                base_reward = 200  # Arama ödülü artırıldı
                # BONUS: Zor personalar için ekstra ödül
                if self.persona in ["Sıkıntıda", "Dijital_Olmayan"]:
                    base_reward += 50  # Ekstra ödül
                reward += base_reward
            else:
                reward += 100  # Standart ödül
            
            terminated = True
            payment_made = True
            info = {'event': 'payment'}
        
        # Müşteri terk etti mi (churn)?
        if not payment_made and np.random.rand() < churn_prob:
            reward -= 200 
            terminated = True
            info = {'event': 'churn'}
        
        # Bölüm sonu koşulu (max gün)
        if not terminated and self.current_days_overdue >= self.max_days:
            terminated = True
            reward -= 150 
            info = {'event': 'timeout'}
            
        if not terminated:
            info = {}

        return self._get_observation(), reward, terminated, False, info


# ÇÖZÜM 3: Model yeniden eğitimi için hyperparameter önerileri
"""
Model yeniden eğitirken şunları deneyin:

1. Exploration artırın:
   - epsilon_start = 1.0
   - epsilon_end = 0.05
   - epsilon_decay = 0.998

2. Learning rate artırın:
   - learning_rate = 0.001 (veya 0.0005)

3. Daha fazla episod:
   - total_episodes = 50000 (mevcut 20000 yerine)

4. Experience replay buffer:
   - buffer_size = 100000
   - batch_size = 64

5. Target network güncelleme:
   - target_update_frequency = 1000
"""