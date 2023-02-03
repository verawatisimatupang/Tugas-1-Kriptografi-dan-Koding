# Tugas-1-Kriptografi-dan-Koding
<br />

<a name="readme-top"></a>
<!-- TABLE OF CONTENTS -->
Daftar Isi
  <ol>
    <li><a href="#anggota-kelompok">Anggota Kelompok</a></li>
    <li><a href="#pertanyaan">Pertanyaan</a></li>
    <li><a href="#spesifikasi">Spesifikasi</a></li>
    <li><a href="#cara-menjalankan-aplikasi">Cara Menjalankan Aplikasi</a></li>
  </ol>

<!-- Anggota Kelompok -->
## Anggota Kelompok
1. 18220002 - Verawati Esteria S. Simatupang
2. 18220010 - Agnes Tamara

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Pertanyaan -->
## Pertanyaan
Buatlah sebuah program berbasis web atau program desktop (pilih salah satu) dalam 
Bahasa C/C++/Java/Python/Ruby/Golang/dll (pilih salah satu) dengan antarmuka (GUI)
yang mengimplementasikan:<br />
a) Vigenere Cipher standard (26 huruf alfabet)<br />
b) Extended Vigenere Cipher (256 karakter ASCII)<br />
c) Playfair Cipher (26 huruf alfabet)<br />
d) One-time pad (26 huruf alfabet)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Spesifikasi -->
## Spesifikasi
1. Program dapat menerima pesan berupa file sembarang (file text maupun file biner) atau pesan yang diketikkan dari papan-ketik. 
2. Program dapat mengenkripsi plainteks. Khusus untuk Vigenere Cipher dengan 26 huruf alfabet, Playfair Cipher dengan 26 huruf alfabet, dan One-time pad dengan 26 huruf alfabet, program hanya mengenkripsi karakter alfabet saja. Angka, spasi, dan tanda baca lainnya diabaikan dan dibuang saat cipherteks ditampilkan atau disimpan.
3. Untuk One-time pad, kunci dibaca dari file teks yang berisi huruf-huruf yang dibangkitkan secara acak. Jumlah huruf di dalam file kunci sebaiknya banyak (misalnya puluhan ribu huruf). Huruf-huruf kunci yang digunakan adalah sepanjang karakter di dalam pesan, sisa huruf yang tidak terpakai dibiarkan begitu saja.
4. Program dapat mendekripsi cipherteks menjadi plainteks semula.
5. Untuk pesan berupa text, program dapat menampilkan plainteks dan cipherteks di layar. Cipherteks dapat ditampilkan dalam dua cara: (a) tanpa spasi, (b) kelompok 5-huruf.
6. Program dapat menyimpan cipherteks ke dalam file. 
7. Kunci dimasukkan oleh pengguna. Panjang kunci bebas.
8. Untuk enkripsi plainteks sembarang file (khusus untuk extended Vigenere Cipher), setiap file diperlakukan sebagai file of bytes. Program membaca setiap  byte di dalam file (termasuk byte-byte header file) dan mengenkripsinya. Hanya saja file yang sudah terenkripsi tidak bisa dibuka oleh program aplikasinya karena header file ikut terenkripsi. Namun dengan mendekripsinya kembali maka file tersbut dapat dibuka oleh aplikasinya.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Cara Menjalankan Aplikasi -->
### Cara Menjalankan Aplikasi
1. Dijalankan melalui file Main.py atau run di cmd yaitu
```sh
  python Main.py
  ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

