# 🕵️ Stealer Log Inspector

**Stealer Log Inspector**, Telegram üzerinden dağıtılan RedLine, Raccoon, Vidar gibi stealer loglarının otomatik olarak analiz edilmesini sağlayan açık kaynaklı bir Python aracıdır. Proje, log dosyalarının ayrıştırılması, IOC (Indicator of Compromise) çıkarımı, dosya bütünlüğü (hash) hesaplaması ve JSON formatında rapor üretimi işlemlerini uçtan uca gerçekleştirmeyi hedefler.

---

## 🚀 Özellikler

- `.zip` ve `.rar` arşivlerini açarak içerik çıkarımı
- Dosya türlerine göre sınıflandırma (`passwords.txt`, `wallets.json`, `system_info.txt` vs.)
- Regex tabanlı IOC çıkarımı: e-posta, IP, BTC/ETH cüzdanı, Discord token
- SHA256 dosya hash hesaplama
- JSON formatında rapor üretimi (`/reports/` dizinine)
- CLI üzerinden kolay kullanım

---

## 📁 Proje Yapısı

```
stealer_log_inspector/
├── run.py                  # Ana çalıştırıcı (CLI arayüz)
├── main.py                 # Tüm işlem akışı burada
├── requirements.txt        # Bağımlılıklar
├── README.md               # Bu dosya
├── test_logs/              # Örnek log arşivleri (.zip/.rar)
├── reports/                # Otomatik IOC rapor çıktıları
├── log_parser/             # Temel modüller
│   ├── extractor.py        # Arşiv açıcı
│   ├── classifier.py       # Dosya türü tanımlayıcı
│   ├── ioc_finder.py       # IOC çıkarıcı
│   ├── hasher.py           # Dosya hash’leme
│   └── utils.py            # Yardımcı fonksiyonlar
```

---

## ⚙️ Kurulum

### 1. Virtual environment oluşturun:

```bash
python3 -m venv venv
source venv/bin/activate   # (Windows: venv\Scripts\activate)
```

### 2. Gereken kütüphaneleri yükleyin:

```bash
pip install -r requirements.txt
```

### 3. `unrar` yüklü olduğundan emin olun (RAR desteği için):

**macOS:**
```bash
brew install unar
```

**Linux:**
```bash
sudo apt install unrar
```

---

## 🧪 Kullanım

```bash
python run.py test_logs/sample_log.zip
```

Çıktılar `reports/` klasörüne `.json` olarak kaydedilir.

---

## 📦 Örnek IOC JSON Raporu

```json
{
  "emails": ["user@example.com"],
  "btc_wallets": ["1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"],
  "ips": ["192.168.1.105"],
  "eth_wallets": ["0x742d35Cc6634C0532925a3b844Bc454e4438f44e"]
}


