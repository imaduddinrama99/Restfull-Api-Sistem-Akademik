# Sistem Akademik Kampus 


# Struktur Direktori

```text
AKADEMIK/
│
├── backend/                     # REST API Server
│   ├── routes/                  # URL Endpoints (Flask Blueprints)
│   ├── services/                # Logika Database (Supabase)
│   ├── app.py                   # Entry Point Server
│   ├── config.py                # Konfigurasi Database
│   ├── requirements.txt         # Daftar Library Python
│   └── .env                     # Kredensial Rahasia (Tidak di-push ke Git)
│
└── frontend/                    # Client UI
    ├── index.html               # Halaman Login
    ├── dashboard.html           # Halaman Dashboard
    └── edit.html                # Halaman Edit Data
```

---

## Fitur Utama

* **Autentikasi Pengguna** — Sistem Login & Logout yang aman menggunakan token JWT.
* **CRUD Terintegrasi** — Tambah, Baca, Perbarui, dan Hapus data mahasiswa secara real-time.
* **Dark Mode Support** — Antarmuka responsif yang mendukung tema gelap dan terang.
* **Modular Architecture** — Backend distrukturkan menggunakan Flask Blueprint (Routes & Services).

---

# Cara Instalasi & Menjalankan Aplikasi

Ikuti langkah-langkah berikut untuk menjalankan aplikasi di komputer lokal.

## 1. Persiapan Backend (Flask API)

Pastikan Python sudah terinstal di komputer Anda.

### Masuk ke folder backend

```bash
cd backend
```

### Buat dan aktifkan Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Instal dependensi

```bash
pip install -r requirements.txt
```

### Konfigurasi Environment Variables

Buat file `.env` di dalam folder `backend/` lalu isi dengan kredensial Supabase Anda:

```env
SUPABASE_URL=https://<id-project-anda>.supabase.co
SUPABASE_KEY=<kunci-anon-public-anda>
```

### Jalankan Server Backend

```bash
python app.py
```

Server API akan berjalan pada:

```text
http://127.0.0.1:5000
```

---

## 2. Menjalankan Frontend

Karena frontend dibuat menggunakan HTML, CSS, dan Vanilla JavaScript, Anda tidak memerlukan server tambahan seperti Node.js.

1. Buka folder `frontend/`.
2. Klik dua kali file `index.html`.
3. File akan terbuka di browser (Chrome, Edge, Firefox, dan lainnya).
4. Untuk pengalaman pengembangan yang lebih baik, gunakan ekstensi **Live Server** pada Visual Studio Code.

---

# Akun Uji Coba (Demo Login)

Gunakan akun berikut untuk mencoba aplikasi:

| Email                                     | Password |
| ----------------------------------------- | -------- |
| [ahmad@gmail.com](mailto:ahmad@gmail.com) | 12345    |

---


## Catatan

* Pastikan backend berjalan terlebih dahulu sebelum membuka frontend.
* Jangan mengunggah file `.env` ke GitHub.
* Simpan kredensial Supabase dengan aman.
* Gunakan akun demo untuk pengujian awal sistem.

---

## Proyek ini dibuat untuk kebutuhan pembelajaran akademik kampus.
