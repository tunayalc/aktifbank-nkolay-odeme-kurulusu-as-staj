# Smart-Debt-Collection-Strategy-Agent

N Kolay Ödeme Kuruluşu A.Ş. stajım sırasında geliştirdiğim reinforcement learning odaklı borç tahsilat stratejisi prototipi

## Genel Bakış

`Smart-Debt-Collection-Strategy-Agent`, borç tahsilat sürecini kural tabanlı değil, durum bazlı karar alan bir ajan perspektifiyle ele almak için geliştirildi. Proje, farklı borçlu profilleri için hangi aksiyonların hangi koşullarda daha uygun olabileceğini reinforcement learning yaklaşımıyla modellemeyi amaçlıyor.

## Çalışmanın Kapsamı

| Katman | İçerik |
| --- | --- |
| Veri Üretimi | sentetik borçlu / müşteri profilleri |
| Ortam Tasarımı | özel Gymnasium environment |
| Aksiyon Modeli | ajan karar seti |
| Ödül Mekanizması | tahsilat başarısını yansıtan reward mantığı |
| Eğitim | DQN tabanlı agent training |
| Değerlendirme | tekrar eden episode'lar üzerinde performans analizi |

## Dosya Bazlı Yapı

### `DataFrame.py`

Simülasyonda kullanılacak sentetik veri ve profil mantığını oluşturan bölüm.

### `debt_collection_env.py`

Projenin merkezindeki özel environment tanımı. Gözlem uzayı, aksiyonlar ve ödül mekanizması burada kuruluyor.

### `train.py`

Stable-Baselines3 kullanılarak DQN ajanını eğiten ana akış.

### `evaluate.py`

Eğitilmiş ajanın davranışını test eden ve episode bazlı sonuçları inceleyen değerlendirme bölümü.

## Repo Yapısı

```text
Smart-Debt-Collection-Strategy-Agent/
|-- DataFrame.py
|-- debt_collection_env.py
|-- train.py
|-- evaluate.py
|-- requirements.txt
`-- README.md
```

## Kullanılan Teknolojiler

- Python
- Gymnasium
- Stable-Baselines3
- DQN
- reinforcement learning
