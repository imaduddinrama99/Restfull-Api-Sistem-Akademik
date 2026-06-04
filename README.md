# Sistem Akademik Kampus

Aplikasi CRUD (Create, Read, Update, Delete) data mahasiswa sederhana yang dibangun menggunakan framework Python Flask dan integrasi basis data cloud Supabase.

---

## 1. Persiapan & Instalasi

Jalankan perintah berikut di Terminal atau Command Prompt (CMD) secara berurutan untuk menyiapkan proyek dan mengisolasi library menggunakan Virtual Environment:

```bash
# 1. Buat folder baru dan masuk ke dalamnya
mkdir sistem-akademik && cd sistem-akademik

# 2. Buat lingkungan terisolasi (Virtual Environment)
python -m venv venv

# 3. Aktifkan Virtual Environment sesuai OS kamu
# Windows (PowerShell):
venv\Scripts\activate

# Windows (CMD):
venv\Scripts\activate.bat

# Linux / macOS:
source venv/bin/activate

# 4. Install library Flask dan Supabase Client di dalam environment
pip install Flask supabase
```

## 2. Konfigurasi Database Supabase

Sebelum menjalankan aplikasi, pastikan kamu sudah membuat tabel di dashboard Supabase dengan ketentuan berikut:

* **Nama Tabel:** `mahasiswa`
* **Keamanan (RLS):** Nonaktifkan (*Disabled*) Row Level Security pada tabel ini, atau buat kebijakan (*Policy*) akses publik agar aplikasi Flask dapat melakukan operasi CRUD.

### Struktur Skema Kolom Tabel

| Nama Kolom | Tipe Data | Keterangan                                      |
| ---------- | --------- | ----------------------------------------------- |
| `id`       | `uuid`    | Primary Key, Default Value: `gen_random_uuid()` |
| `nim`      | `text`    | Menyimpan nomor induk mahasiswa (unik)          |
| `nama`     | `text`    | Menyimpan nama lengkap                          |
| `prodi`    | `text`    | Menyimpan nama program studi                    |
| `angkatan` | `integer` | Menyimpan tahun angkatan (contoh: 2024)         |

> ⚠️ Penting: Buka file `app.py`, lalu sesuaikan variabel `url` dan `key` menggunakan kredensial API dari dashboard Supabase.

## 3. Menjalankan Aplikasi

Pastikan Virtual Environment sudah aktif, kemudian jalankan:

```bash
python app.py
```

Buka browser dan akses:

```text
http://127.0.0.1:5000
```
