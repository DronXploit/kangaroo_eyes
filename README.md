# 🦘 Kangaroo Eyes - Network Reconnaissance Tool

**Kangaroo Eyes** adalah alat rekayasa jaringan (network reconnaissance) berbasis Python yang dirancang untuk membantu profesional keamanan siber, administrator jaringan, dan pengembang dalam melakukan analisis infrastruktur jaringan dengan cepat dan efisien.

## 🌟 Fitur Utama

- 🔍 **Pengecekan DNS (bukan DNA)** - Temukan semua record DNS terkait domain
- 📜 **IP Historia** - Lacak perubahan alamat IP historis
- 🚪 **Scan Port** - Identifikasi port terbuka dengan Nmap integration
- 🕵️ **WHOIS Lookup** - Dapatkan informasi registrasi domain lengkap


## 🛠️ Instalasi

### Prasyarat
- Python 3.8+
- Nmap (untuk fitur port scanning)
- API Key dari [WHOISXMLAPI](https://www.whoisxmlapi.com/)

### Langkah Instalasi
```bash
# Clone repository
git clone https://github.com/username/kangaroo-eyes.git
cd kangaroo-eyes

# Setup environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -e .
```

## 🚀 Cara Menggunakan

```bash
# Jalankan tool
kangaroo-eyes
```

Atau langsung via Python:
```bash
python -m kangaroo_eyes
```

### Menu Utama
```
=== NETWORK RECONNAISSANCE TOOL ===

[1] Masukkan URL  
[2] Rekaman DNS  
[3] IP Historia  
[4] Scan Port  
[5] WHOIS bruh  
[6] Exit
```

## 📝 Konfigurasi

Buat file `.env` di root project:
```ini
WHOISXML_API_KEY=your_api_key_here
```

## 🧩 Modul

| File | Deskripsi |
|------|-----------|
| `cli.py` | Interface command line |
| `scanner.py` | Modul scanning utama |
| `api.py` | Integrasi dengan WHOISXML API |
| `utils.py` | Fungsi utilitas dan helper |
| `const.py` | Konstanta dan konfigurasi |

## 🎯 Contoh Penggunaan

```bash
# 1. Set target domain
Select option (1-6): 1
Enter target domain: example.com

# 2. Lakukan DNS enumeration
Select option (1-6): 2

# 3. Cek historical IP
Select option (1-6): 3
```

## 📊 Contoh Output
```
=== DNS ENUMERATION RESULTS ===

Domain:       example.com
IP Addresses: 
  - 93.184.216.34
  - 2606:2800:220:1:248:1893:25c8:1946
Total Found:  2
Nameservers:  ['8.8.8.8', '1.1.1.1']
```

## 🤝 Berkontribusi

Kami menyambut kontribusi! Silakan:
1. Fork project ini
2. Buat branch fitur baru (`git checkout -b fitur-baru`)
3. Commit perubahan (`git commit -am 'Tambahkan fitur baru'`)
4. Push ke branch (`git push origin fitur-baru`)
5. Buat Pull Request

## 📜 Lisensi

Distributed under the MIT License. See `LICENSE` for more information.

## ✉️ Kontak

Author - [https://instagram.com/dronxploit] (Follow me:Instagram)  
Support me: [https://saweria.co/dronxploit] - [Saweria] 

---

**Kangaroo Eyes** 🦘 - Your Network's Best Watchman!
