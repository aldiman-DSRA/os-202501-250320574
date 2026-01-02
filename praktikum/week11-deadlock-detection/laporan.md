
# Laporan Praktikum Minggu [X]
Topik: [Simulasi dan Deteksi Deadlock]

---

## Identitas
- **Nama**  : [aldiman]  
- **NIM**   : [250320574]  
- **Kelas** : [1dsra]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.   
> Membuat program sederhana untuk mendeteksi deadlock.
> Menjalankan simulasi deteksi deadlock dengan dataset uji.
> Menyajikan hasil analisis deadlock dalam bentuk tabel.
> Memberikan interpretasi hasil uji secara logis dan sistematis.

---

## Dasar Teori
mempelajari mekanisme deteksi deadlock dalam sistem operasi.
mendeteksi deadlock yang telah terjadi menggunakan pendekatan algoritmik.
membuat program simulasi sederhana deteksi deadlock. 

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah

```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
| Proses | Allocation | Request |
| ------ | ---------- | ------- |
| P1     | R1         | R2      |
| P2     | R2         | R3      |
| P3     | R3         | R1      |

Sistem dalam kondisi DEADLOCK
Proses yang terlibat deadlock: P1, P2, P3

Validasi Manual / Logis
Analisis manual menunjukkan:
P1 menunggu R2 yang dipegang P2
P2 menunggu R3 yang dipegang P3
P3 menunggu R1 yang dipegang P1

Terjadi siklus tunggu:
P1 → P2 → P3 → P1

Mengapa Deadlock Terjadi?
Deadlock terjadi karena setiap proses:
Memegang satu resource
Menunggu resource lain yang sedang dipegang proses lain
Tidak ada proses yang dapat melanjutkan eksekusi

Kaitan dengan Teori Deadlock (Empat Kondisi)
Deadlock terjadi karena keempat kondisi deadlock terpenuhi:

Mutual Exclusion
Resource hanya bisa digunakan satu proses dalam satu waktu.
Hold and Wait
Proses memegang resource sambil menunggu resource lain.
No Preemption
Resource tidak bisa diambil paksa dari proses lain.
Circular Wait
Terjadi siklus menunggu antar proses (P1 → P2 → P3 → P1).
---

## Kesimpulan
sistem terbukti berada dalam kondisi deadlock karena terjadi siklus saling menunggu antar proses. Hasil deteksi program sesuai dengan analisis manual, dan deadlock terjadi karena keempat kondisi deadlock (mutual exclusion, hold and wait, no preemption, dan circular wait) terpenuhi.
---

## Quiz
1. [Pertanyaan 1]  
   **Jawaban:
Deadlock Prevention
Mencegah deadlock dengan menghilangkan salah satu dari empat kondisi deadlock (misalnya melarang hold and wait).
Deadlock Avoidance
Menghindari deadlock dengan mengevaluasi setiap permintaan resource agar sistem tetap dalam kondisi aman (contoh: algoritma Banker).
Deadlock Detection
Membiarkan deadlock terjadi, lalu mendeteksi dan menangani deadlock setelah terjadi.**  
2. [Pertanyaan 2]  
   **Jawaban:
Deteksi deadlock diperlukan karena:
Tidak semua sistem dapat menerapkan prevention atau avoidance
Lebih fleksibel untuk sistem dengan kebutuhan resource dinamis
Overhead lebih rendah dibanding avoidance pada sistem besar
**  
3. [Pertanyaan 3]  
   **Jawaban:
Kelebihan:
Implementasi relatif sederhana
Tidak membatasi penggunaan resource
Cocok untuk sistem dengan beban dinamis

Kekurangan:
Deadlock dibiarkan terjadi terlebih dahulu
Memerlukan mekanisme pemulihan (recovery)
Dapat mengganggu kinerja saat deadlock muncul
**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
