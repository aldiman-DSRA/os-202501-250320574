
# Laporan Praktikum Minggu [X]
Topik: [manajemen proses dan user linux"]

---

## Identitas
- **Nama**  : [aldiman]  
- **NIM**   : [250320574]  
- **Kelas** : [1dsra]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
> Mahasiswa mampu menjelaskan
> konsep proses dan user dalam sistem opersilinux
> menampilkan daftar proses yang sedang berjalan dan statusnya
> menggunakan perintah untuk membuat dan mengelola user
> menhentikan atau mengontrol proses tertentu menggunakan pid
> menjelaskan kaitan antara menejemen user dan kemanan sistem

---

## Dasar Teori
manejemen pengguna
menejemen proses


---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.
   membuka linux wsl
   jalan kode sesuai 
3. Perintah yang dijalankan.  
4. File dan kode yang dibuat.  
5. Commit message yang digunakan.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
id
groups 
sudo adduser praktikan
sudo passwd praktikan
ps aux | head -10
top -n 1
(PID: ID unik setiap proses (digunakan untuk menghentikan program).
USER: Nama pengguna yang menjalankan proses tersebut.
%CPU: Persentase beban kerja proses pada prosesor.
%MEM: Persentase penggunaan RAM oleh proses tersebut.
COMMAND: Nama aplikasi atau perintah yang sedang berjalan.)
sleep 1000 &
ps aux | grep sleep
kill <PID>
pstree -p | head -20
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Proses adalah Program yang Dieksekusi: Setiap perintah atau aplikasi yang dijalankan dalam sistem Linux didefinisikan sebagai sebuah proses.
Manajemen Proses Sangat Penting: Kemampuan untuk memantau dan mengontrol proses sangat penting untuk administrasi sistem yang efektif, termasuk mendiagnosis masalah kinerja dan memastikan keamanan.
Identifikasi dan Kepemilikan: Setiap proses memiliki PID (Process ID) unik dan dimiliki oleh USER tertentu (seperti root atau pengguna biasa). Hal ini menegaskan bahwa proses dengan hak akses terbatas tidak dapat mengakses sumber daya yang tidak diizinkan, sehingga meningkatkan keamanan sistem.
---

## Quiz
1. [Pertanyaan 1]  
   **Jawaban:Systemd (atau pendahulunya, init) adalah proses pertama yang dijalankan saat sistem Linux melakukan booting, biasanya dengan PID 1. Fungsi utamanya adalah menginisialisasi dan mengelola semua proses dan layanan lain yang diperlukan agar sistem dapat beroperasi dengan benar.**  
2. [Pertanyaan 2]  
   **Jawaban:kill: Perintah ini digunakan untuk menghentikan proses tertentu dengan mengirimkan sinyal ke Process ID (PID) yang spesifik. Sintaks dasarnya adalah kill <PID>.
killall: Perintah ini menghentikan semua proses yang sedang berjalan yang cocok dengan nama proses yang diberikan. Ini berguna untuk menghentikan beberapa instance dari aplikasi yang sama sekaligus. 
**  
3. [Pertanyaan 3]  
   **Jawaban:Root adalah super user dengan kontrol penuh atas sistem untuk tugas administrasi (instalasi, konfigurasi,)**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
