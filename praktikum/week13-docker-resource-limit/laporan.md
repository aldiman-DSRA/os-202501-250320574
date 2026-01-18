
# Laporan Praktikum Minggu [X]
Topik: [Docker – Resource Limit (CPU & Memori)]

---

## Identitas
- **Nama**  : [aldiman]  
- **NIM**   : [250320574]  
- **Kelas** : [1dsra]

---

## Tujuan  
> Menulis Dockerfile sederhana untuk sebuah aplikasi/skrip.
> Membangun image dan menjalankan container.
> Menjalankan container dengan pembatasan CPU dan memori.
> Mengamati dan menjelaskan perbedaan eksekusi container dengan dan tanpa limit resource.


---

## Dasar Teori
> Docker dan Container
Docker memungkinkan aplikasi dijalankan di dalam container, yaitu lingkungan terisolasi yang berisi aplikasi dan dependensinya sehingga dapat berjalan konsisten di berbagai sistem.

> Docker Image dan Dockerfile
Docker image adalah template untuk membuat container, sedangkan Dockerfile berisi instruksi untuk membangun image secara otomatis dan terstruktur.

> Manajemen Resource
Docker dapat membatasi penggunaan sumber daya seperti CPU dan memori agar container tidak mengganggu proses lain pada sistem.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.
   > membuat program python
   > membuat dockerfile  
2. Perintah yang dijalankan.
   >  Membangun Docker image
docker build -t resource-test .
   > Menjalankan container tanpa pembatasan resource
docker run --rm resource-test
   > Menjalankan container dengan pembatasan CPU
docker run --rm --cpus="0.5" resource-test
   > Menjalankan container dengan pembatasan memori
docker run --rm --memory="64m" resource-test
   > Melihat daftar image Docker
docker images
3. File dan kode yang dibuat.
4. Commit message yang digunakan.

---

## Kode / Perintah
docker build -t resource-test .
docker run --rm resource-test
docker run --rm --cpus="0.5" resource-test
docker run --rm --memory="64m" resource-test
docker images
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis

Analisis
Hasil percobaan menunjukkan bahwa Docker mampu menjalankan aplikasi uji dengan baik serta membatasi penggunaan sumber daya sesuai pengaturan. Tanpa pembatasan, aplikasi memanfaatkan CPU secara maksimal sehingga berjalan lebih cepat. Dengan pembatasan CPU, kinerja aplikasi menjadi lebih lambat karena alokasi CPU dibatasi. Pada pembatasan memori, container tidak dapat menggunakan memori melebihi batas yang ditentukan dan proses dihentikan saat batas tercapai. Hal ini membuktikan bahwa Docker efektif dalam mengelola dan mengontrol penggunaan resource.

---

## Kesimpulan
1.	Docker berhasil digunakan untuk menjalankan aplikasi uji di dalam container secara terisolasi dan konsisten.

2.	Pembatasan resource seperti CPU dan memori berpengaruh langsung terhadap kinerja aplikasi, di mana pembatasan CPU memperlambat proses dan pembatasan memori membatasi alokasi memori.

3.	Docker efektif dalam mengelola penggunaan sumber daya sistem sehingga mencegah satu aplikasi menggunakan resource secara berlebihan.

---

## Quiz
1. [Pertanyaan 1]  
   **Pembatasan CPU dan memori diperlukan agar satu container tidak menggunakan seluruh sumber daya sistem. Dengan adanya limit, kinerja sistem tetap stabil dan aplikasi lain yang berjalan tidak terganggu.:**  
2. [Pertanyaan 2]  
   **Virtual Machine (VM) memiliki isolasi resource yang lebih kuat karena menggunakan sistem operasi sendiri, sedangkan container berbagi kernel dengan host. Container lebih ringan dan efisien, namun tingkat isolasinya sedikit lebih rendah dibandingkan VM.:**  
3. [Pertanyaan 3]  
   **Jika aplikasi menggunakan memori melebihi batas yang ditentukan, proses dapat dihentikan secara paksa atau mengalami error. Hal ini menyebabkan aplikasi berhenti berjalan, namun membantu mencegah kehabisan memori pada sistem secara keseluruhan.:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
