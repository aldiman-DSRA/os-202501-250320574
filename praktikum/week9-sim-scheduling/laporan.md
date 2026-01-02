
# Laporan Praktikum Minggu [X]
Topik: [Simulasi Algoritma Penjadwalan CPU]

---

## Identitas
- **Nama**  : [aldiman]  
- **NIM**   : [250320574]  
- **Kelas** : [1dsra]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.    
> Membuat program simulasi algoritma penjadwalan FCFS dan/atau SJF.
> Menjalankan program dengan dataset uji yang diberikan atau dibuat sendiri.
> Menyajikan output simulasi dalam bentuk tabel atau grafik.

---

## Dasar Teori

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Menghitung waiting time dan turnaround time.
Mendukung minimal 1 algoritma (FCFS atau SJF non-preemptive).
Menampilkan hasil dalam tabel.
---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- menjelaskan alur program
Program membaca dataset proses (arrival time & burst time).
Proses diurutkan berdasarkan arrival time (FCFS).
CPU mengeksekusi proses secara berurutan.
Program menghitung:
Waiting Time = Start − Arrival
Turnaround Time = Completion − Arrival
Hasil ditampilkan dalam tabel dan dihitung rata-ratanya.
- Perbandingan Simulasi vs Manual
Hasil simulasi sama persis dengan perhitungan manual FCFS.
Ini menunjukkan program berjalan benar dan valid.
-Kelebihan dan Keterbatasan
  Kelebihan:
Perhitungan cepat dan akurat
Mudah diuji dengan berbagai dataset
Mudah dikembangkan ke algoritma lain
  Keterbatasan:
Tidak mencerminkan kondisi sistem nyata sepenuhnya
FCFS kurang efisien karena convoy effect
Tidak cocok untuk sistem interaktif
---

## Kesimpulan
Simulasi penjadwalan FCFS berhasil menghitung waiting time dan turnaround time dengan benar sesuai perhitungan manual. Program membantu memahami alur kerja FCFS, namun memiliki keterbatasan karena kurang efisien dan tidak mencerminkan kondisi sistem nyata sepenuhnya.

---

## Quiz
1. [Pertanyaan 1]  
   **Jawaban:Simulasi diperlukan untuk menguji kebenaran dan kinerja algoritma secara cepat dan akurat, terutama saat jumlah proses banyak, sehingga mengurangi kesalahan perhitungan manual dan memudahkan analisis hasil.
   **  
3. [Pertanyaan 2]  
   **Jawaban:Secara teori hasilnya sama, tetapi pada dataset besar:
Simulasi lebih cepat, konsisten, dan minim kesalahan
Perhitungan manual memakan waktu lama dan rawan kesalahan manusia
**  
5. [Pertanyaan 3]  
   **Jawaban:Algoritma FCFS lebih mudah diimplementasikan karena hanya mengurutkan proses berdasarkan waktu kedatangan tanpa perhitungan tambahan, sedangkan SJF memerlukan pemilihan burst time terpendek sehingga logikanya lebih kompleks.
   **  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
