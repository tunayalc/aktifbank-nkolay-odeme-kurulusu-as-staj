# Aktifbank / N Kolay Ödeme Kuruluşu A.Ş. — Staj Projeleri

N Kolay Ödeme Kuruluşu A.Ş. stajım sırasında geliştirdiğim yapay zekâ, otomasyon ve görüntü işleme projelerini bir araya getiren monorepo.

## Projeler

| Proje | Kapsam | Teknolojiler |
| --- | --- | --- |
| [Ollama & n8n Toolkit](./ollama-n8n-toolkit/) | Pazar/rakip analizi, kullanıcı geri bildirimi ve yerel LLM otomasyonu | Python, Ollama, n8n, Flask |
| [Smart Financial Strategist](./smart-financial-strategist/) | Araç kullanan LLM, nicel finans ve RAG ile finansal strateji prototipi | Streamlit, LangChain, Chroma, Ollama |
| [Smart Debt Collection Strategy Agent](./Smart-Debt-Collection-Strategy-Agent/) | Sentetik borçlu profilleri üzerinde pekiştirmeli öğrenme ile tahsilat stratejileri | Gymnasium, Stable-Baselines3, DQN |
| [Banknote Detector](./Banknote-Detector/) | Veri hazırlama, etiketleme, eğitim ve canlı banknot tespiti | Ultralytics YOLOv8, OpenCV |

## Kullanım

Her proje kendi klasöründe bağımsızdır. Projeye ait README dosyasını okuyun ve komutları ilgili proje klasöründen çalıştırın. Bağımlılıkları proje bazında ayrı bir sanal ortama kurun; veri setleri, model ağırlıkları ve yerel servis gereksinimleri projeye göre değişir.

## Repo düzeni

```text
aktifbank-nkolay-odeme-kurulusu-as-staj/
├── ollama-n8n-toolkit/
├── smart-financial-strategist/
├── Smart-Debt-Collection-Strategy-Agent/
├── Banknote-Detector/
└── README.md
```

## Geçmiş

Dört kaynak reponun Git geçmişi korunarak her proje aynı adı taşıyan alt klasöre taşınmıştır. Kaynak dosyalar birleştirme sırasında değiştirilmemiştir.
