Nama : Muhammad Fachrel N.a

Nim : 2025102004

Mata-kuliah : Struktur Data

Praktikum Python: Aliasing dan Eksplorasi Tipe Data

📖 Deskripsi
Repository ini berisi implementasi sederhana dalam bahasa Python untuk memahami konsep dasar pemrograman, yaitu:
Aliasing (referensi objek) pada list
Eksplorasi tipe data dan penggunaan memori
Praktikum ini bertujuan untuk membantu mahasiswa memahami bagaimana Python mengelola objek di memori serta perbedaan karakteristik antar tipe data.

🎯 Tujuan Praktikum
Setelah mempelajari program ini, mahasiswa diharapkan mampu:
Memahami konsep aliasing (referensi objek)
Menjelaskan perbedaan antara copy dan referensi
Mengidentifikasi tipe data dalam Python
Menganalisis penggunaan memori pada berbagai tipe data
Menggunakan fungsi sys.getsizeof() untuk evaluasi memori

📂 Struktur Program

├── aliasing.py

└── explorasi_tipe_data.py


🔁 1. Analisis Program Aliasing (aliasing.py)

📌 Konsep Dasar
Aliasing adalah kondisi di mana dua atau lebih variabel mereferensikan objek yang sama di dalam memori.

Contoh implementasi:

a = [1, 2, 3, 4]

b = a

Pada kode tersebut:

Variabel b tidak membuat objek baru

a dan b menunjuk ke alamat memori yang sama

⚠️ Hasil Pengujian

Ketika dilakukan perubahan pada salah satu variabel:

a.append(5)

Maka hasilnya:

List A: [1, 2, 3, 4, 5]

List B: [1, 2, 3, 4, 5]


🧠 Analisis

Hal ini terjadi karena list merupakan mutable object, sehingga perubahan pada satu referensi akan memengaruhi referensi lainnya.

✅ Solusi (Menghindari Aliasing)

Gunakan metode copy:

b = a.copy()

🧠 2. Analisis Eksplorasi Tipe Data (explorasi_tipe_data.py)

📌 Konsep Dasar

Python menyediakan berbagai tipe data dengan karakteristik dan penggunaan memori yang berbeda.

Program ini menggunakan modul:

import sys

Untuk mengukur ukuran memori:

sys.getsizeof()

🔍 Data yang Digunakan
Integer: 80

List: [3]

String: "Hello, World!"

🖨️ Hasil Output

Tipe data: <class 'int'>, Ukuran memori: 28 bytes

Tipe data: <class 'list'>, Ukuran memori: 64 bytes

Tipe data: <class 'str'>, ukuran memori: 62 bytes

🧠 Analisis

Integer memiliki ukuran kecil karena menyimpan satu nilai

List lebih besar karena menyimpan struktur data dan referensi elemen

String bergantung pada panjang karakter

⚖️ Perbandingan Tipe Data

Tipe Data	Sifat	Ukuran Memori	Keterangan

Integer	Immutable	Kecil	Efisien untuk angka

List	Mutable	Lebih besar	Menyimpan banyak elemen

String	Immutable	Variatif	Bergantung panjang

🚀 Cara Menjalankan Program

Pastikan Python sudah terinstal

Jalankan melalui terminal atau command prompt:

python aliasing.py

python explorasi_tipe_data.py

📌 Kesimpulan

Python menggunakan sistem referensi objek, bukan penyalinan nilai secara otomatis

Aliasing dapat menyebabkan perubahan tidak terduga jika tidak dipahami

Setiap tipe data memiliki karakteristik dan penggunaan memori yang berbeda

Pemahaman konsep ini penting dalam pengembangan program yang efisien

👨‍🎓 Kegunaan dalam Dunia Akademik

Materi ini relevan untuk:

Mata kuliah Dasar Pemrograman
Struktur Data
Pemrograman Berorientasi Objek (OOP)

✍️ Penulis

Disusun sebagai bagian dari praktikum pembelajaran Python
oleh mahasiswa Teknik Informatika
