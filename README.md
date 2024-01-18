# Sistem Pakar Pakan Ikan

Ini adalah project Sistem pakar untuk menentukan pakan yang tepat bagi ikan berdasarkan jenis dan umur ikan menggunakan Flask. Sistem ini dapat membantu praktisi budidaya ikan dalam menentukan pakan yang tepat bagi ikan berdasarkan jenis dan umur ikan. Sistem ini menggunakan metode backward chaining

## Struktur Project

```
MyProject
├── __pycache__
│   └── app.cpython-310.pyc
├── .devcontainer
│   └── devcontainer.json
├── .github/workflows
│   ├── jekyll-gh-pages.yml
│   ├── python-publish.yml
│   └── static.yml
├── static 
├── templates 
│   └── main.css 
├── index.html 
├── app.py 
├── .gitignore.txt 
├── LICENSE 
├── README.md 
└── requirements.txt  
```

## Deskripsi

Project ini adalah implementasi Sistem Pakar Pakan Ikan menggunakan metode backward chaining. Project menggunakan Flask sebagai framework web untuk menyajikan antarmuka pengguna.

## Modul Basis Pengetahuan

File `app.py` mengandung modul basis pengetahuan yang berisi fakta-fakta tentang jenis ikan, umur ikan, dan jenis pakan ikan. Selain itu, terdapat aturan-aturan yang digunakan untuk menentukan pakan ikan berdasarkan jenis dan umur ikan.

- Fakta-fakta: Jenis ikan, umur ikan, dan jenis pakan ikan.
- Aturan-aturan: Aturan inferensi berdasarkan jenis dan umur ikan.

## Modul Mesin Inferensi

Modul mesin inferensi terdapat pada fungsi `backward_chaining` di dalam file `app.py`. Fungsi ini digunakan untuk menentukan pakan ikan berdasarkan aturan yang telah ditentukan.

## Antarmuka Pengguna

Antarmuka pengguna terdapat pada file `index.html`, dan project ini menggunakan Bootstrap untuk tata letak dan gaya. Formulir konsultasi memungkinkan pengguna memilih jenis dan umur ikan, dan hasilnya akan menampilkan rule yang digunakan serta pakan ikan yang tepat.

## Pengembangan menggunakan DevContainer

Project ini dapat dikembangkan menggunakan Docker dan DevContainer. File `devcontainer.json` mengandung konfigurasi untuk lingkungan pengembangan Docker, termasuk spesifikasi CPU dan pengaturan port.

## Endpoints

- **GET /**: Halaman utama untuk konsultasi.
- **POST /**: Menangani formulir konsultasi dan menampilkan hasil.

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

5. Untuk menghentikan aplikasi, tekan `Ctrl+C` di terminal.

## Lisensi

This project is licensed under the MIT License. See `LICENSE` for more information.



