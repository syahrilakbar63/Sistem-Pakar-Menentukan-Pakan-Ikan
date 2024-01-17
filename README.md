# Sistem Pakar Pakan Ikan

Ini adalah proyek Sistem Pakar Pakan Ikan menggunakan Flask.

## Struktur Proyek

```
myProject
├── templates
│   └── index.html
└── app.py
```

## Deskripsi

Proyek ini adalah implementasi Sistem Pakar Pakan Ikan menggunakan metode backward chaining. Proyek menggunakan Flask sebagai framework web untuk menyajikan antarmuka pengguna.

## Penggunaan

1. Pastikan Python sudah terinstall di sistem Anda. Jika belum, Anda dapat mengunduh dan menginstalnya dari [python.org](https://www.python.org/downloads/).

2. Install dependencies:

   ```bash
   pip install flask
   ```

3. Jalankan aplikasi:

   ```bash
   python app.py
   ```

4. Buka browser dan akses [http://localhost:5000/](http://localhost:5000/)

## Struktur HTML (index.html)

File `index.html` berisi antarmuka pengguna untuk melakukan konsultasi terkait pilihan jenis dan umur ikan.

## Struktur Python (app.py)

File `app.py` berisi implementasi Flask dan mesin inferensi backward chaining untuk menentukan pakan ikan yang tepat.

## Modul Basis Pengetahuan

- Fakta-fakta: Jenis ikan, umur ikan, dan jenis pakan ikan.
- Aturan-aturan: Aturan inferensi berdasarkan jenis dan umur ikan.

## Modul Mesin Inferensi

Fungsi `backward_chaining` digunakan untuk menentukan pakan ikan berdasarkan jenis dan umur ikan.

## Endpoints

- **GET /**: Halaman utama untuk konsultasi.
- **POST /**: Menangani formulir konsultasi dan menampilkan hasil.

## Lisensi

This project is licensed under the MIT License. See `LICENSE` for more information.



