
# Laporan Praktikum Minggu [X]
Topik: [Manajemen Memori – Page Replacement (FIFO & LRU)]

---

## Identitas
- **Nama**  : [aldiman]  
- **NIM**   : [250320574]  
- **Kelas** : [1dsra]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.    
> Mengimplementasikan algoritma page replacement FIFO dalam program.
> Mengimplementasikan algoritma page replacement LRU dalam program.
> Menjalankan simulasi page replacement dengan dataset tertentu.
> Membandingkan performa FIFO dan LRU berdasarkan jumlah page fault.

---

## Dasar Teori
- mempelajari manajemen memori virtual, khususnya mekanisme page replacement.
- memahami bagaimana sistem operasi mengganti halaman (page) di memori utama ketika terjadi page fault, serta membandingkan performa algoritma FIFO (First-In First-Out) dan LRU (Least Recently Used).
---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
algoritma fifo
jumlah page fault=10
keterangan=Mengganti halaman yang masuk paling awal tanpa memperhatikan frekuensi penggunaan sehingga page fault lebih banyak

algoritma lru
jumlah page fault=9
keterangan=Mengganti halaman yang paling lama tidak digunakan sehingga lebih efisien dan menghasilkan page fault lebih sedikit

mengapa jumlah page fault bisa berbeda beda
FIFO mengganti halaman yang paling lama masuk tanpa melihat apakah halaman tersebut sering digunakan.
LRU mengganti halaman yang paling lama tidak digunakan, sehingga lebih sesuai dengan pola akses program.

Analisis algoritma mana yang lebih efisien dan alasannya.
LRU lebih efisien dibanding FIFO karena:
> Menghasilkan page fault lebih sedikit
> Lebih adaptif terhadap lokalitas referensi
> Kinerja lebih stabil pada berbagai pola akses

---

## Kesimpulan
Berdasarkan praktik simulasi penggantian halaman, algoritma LRU terbukti lebih efisien dibanding FIFO karena menghasilkan jumlah page fault lebih sedikit. Perbedaan ini terjadi karena LRU mempertimbangkan riwayat penggunaan halaman, sedangkan FIFO hanya berdasarkan urutan masuk tanpa melihat pola akses.

---

## Quiz
1. [Pertanyaan 1]  
   **Jawaban:
FIFO (First In First Out) mengganti halaman yang paling lama masuk ke memori tanpa melihat apakah halaman tersebut sering digunakan.
LRU (Least Recently Used) mengganti halaman yang paling lama tidak digunakan, berdasarkan riwayat akses.
**  
3. [Pertanyaan 2]  
   **Jawaban:
FIFO dapat mengalami Belady’s Anomaly karena penambahan jumlah frame tidak selalu menurunkan page fault. Hal ini terjadi karena FIFO tidak mempertimbangkan pola penggunaan halaman, sehingga halaman yang masih sering digunakan bisa tetap diganti.
   **  
5. [Pertanyaan 3]  
   **Jawaban:
LRU lebih baik karena memanfaatkan lokalitas referensi, yaitu halaman yang baru digunakan cenderung akan digunakan kembali, sehingga jumlah page fault biasanya lebih sedikit dibanding FIFO.
   **  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
