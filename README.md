# Sistem Akademik Kampus

Aplikasi CRUD data mahasiswa menggunakan 
---

## 1. Persiapan

Jalankan perintah berikut di Terminal / CMD:

```bash
# Buat folder baru dan masuk ke dalamnya
mkdir sistem-akademik && cd sistem-akademik

# Install library Flask dan Supabase
pip install Flask supabase
```

## 2. Jalankan Aplikasi

```bash
python app.py
```

Buka browser dan akses:

```
http://127.0.0.1:5000
```

## Skema Tabel Supabase

Buat tabel **mahasiswa** dengan kolom berikut:

- `id` (int8 / uuid - Primary Key)
- `nim` (text)
- `nama` (text)
- `prodi` (text)
- `angkatan` (integer)