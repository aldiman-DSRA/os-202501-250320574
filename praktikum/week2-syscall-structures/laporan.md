
# Laporan Praktikum Minggu [2]
Topik: [struktur system kernel]

---

## Identitas
- **Nama**  : [Aldiman]  
- **NIM**   : [250320574]  
- **Kelas** : [1DSRA]

---

## Tujuan
Tujuan praktikum minggu ini.    
> Menjelaskan konsep dan fungsi system call dalam sistem operasi
> mengidentifikasi jenis jenis system call dan fungsinya
> mengamati alur perpindahan mode user ke kernel saat sytem call terjadi
> menggunakan perintah linux untuk menampilkan dan menganalisis system call

---

## Dasar Teori
1.Inti sistem operasi 
Kernel adalah bagian inti dari sistem operasi yang selalu berada di dalam memori utama (kernel-space) sejak komputer dinyalakan hingga dimatikan
2.Jembatan perangkat lunak-perangkat keras
Fungsi uatamanya adalah sebagai perantara (jembatan) antara aplikasi (yang berjalan di user-space) dan perangkat keras fisik
3.Manajemen sumber daya 
Kernel bertanggung jawab penuh atas pengelolaan sumber daya sistem yang vital
•	Manajemen proses
Membuat,menjadwalkan ulang, dan menghentikan proses,serta mengalokasikan waktu CPU
•	Manajemen memori
Mengalokasikan ruang memori ke berbagai proses dan melindungi ruang memori satu proses dari proses lainya
•	Manajemen perangkat I/O
Mengelola komunikasi dengan perangkat keras seperti disk, keyboard, dan jaringan melalui device drivers


---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
strace ls
strace -e trace=open,read,write,close cat /etc/passwd
dmesg | tail -n 10
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
Kesimpulan dari praktik struktur system kernel secara umum adalah untuk menciptakan keseimbangan antara efisiensi, stabilitas, keamanan, dan fleksibilitas.

---

## Quiz
1. [Apa fungsi utama system call dalam sistem operasi?]  
   **Sebagai jembatan antara aplikasi tingkat pengguna dan kernel sistem operasi untuk meminta layanan-layanan yang disediakan oleh OS:**  
2. [Sebutkan 4 kategori system call yang umum digunakan.]  
   **Kontrol proses (process control)
Contoh: fork(), exit(), wait().
Manajemen berkas (file management)
Contoh: open(), read(), write(), close().
Manajemen perangkat (device management)
Contoh: ioctl(), read(), write().
Pemeliharaan informasi (information maintenance)
Contoh: getpid(), alarm(), sleep()
:**  
3. [Mengapa system call tidak bisa dipanggil langsung oleh user program?]  
   **Pemisahan Hak Akses: Program pengguna berjalan dalam user mode dengan hak akses terbatas, sementara system call membutuhkan kernel mode (hak akses penuh).
Keamanan dan Proteksi: Akses langsung dapat membuka celah keamanan dan memungkinkan program berbahaya merusak sistem atau data.
Kontrol dan Validasi: OS perlu memvalidasi dan mengontrol setiap permintaan akses ke sumber daya penting (memori, perangkat keras) untuk mencegah kerusakan sistem (crash).
:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
