
# Laporan Praktikum Minggu [X]
Topik: [Penjadwalan CPU – Round Robin (RR) dan Priority Scheduling]

---

## Identitas
- **Nama**  : [aldiman]  
- **NIM**   : [250320574]  
- **Kelas** : [1dsra]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
>waiting time dan turnaround time pada algoritma RR dan Priority.
>Membandingkan performa algoritma RR dan Priority.
>Menjelaskan pengaruh time quantum dan prioritas terhadap keadilan eksekusi proses.
>Menarik kesimpulan mengenai efisiensi dan keadilan kedua algoritma.

---

## Dasar Teori
1. Penjadwalan CPU (CPU Scheduling)
Penjadwalan CPU adalah mekanisme sistem operasi untuk menentukan urutan eksekusi proses yang berada dalam keadaan ready agar penggunaan CPU menjadi efisien dan adil.

2. Round Robin (RR) Scheduling
Round Robin adalah algoritma penjadwalan preemptive yang memberikan CPU ke setiap proses secara bergiliran dengan time quantum tertentu.

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
- 1. Analisis Round Robin (RR)
Berdasarkan pengujian beberapa nilai time quantum, terlihat bahwa nilai quantum sangat memengaruhi kinerja algoritma Round Robin.
Quantum kecil (q = 2)
Sistem menjadi sangat responsif, namun terjadi context switching yang sering sehingga average waiting time dan turnaround time meningkat.
Quantum sedang (q = 3)
Memberikan keseimbangan terbaik antara responsivitas dan efisiensi.
Nilai average waiting time = 8.5 dan average turnaround time = 14 menunjukkan performa yang optimal dibandingkan quantum lain.
Quantum besar (q = 5)
Overhead menurun, namun perilaku sistem mendekati FCFS sehingga responsivitas menurun, walaupun waktu rata-rata lebih kecil.

2. Analisis Priority Scheduling
Pada algoritma Priority Scheduling, proses dengan prioritas lebih tinggi dieksekusi terlebih dahulu sehingga:
Average waiting time (6) dan average turnaround time (11.5) lebih kecil dibandingkan RR
Algoritma ini lebih efisien untuk proses penting
Namun, terdapat kelemahan utama yaitu:
Starvation, di mana proses berprioritas rendah dapat menunggu terlalu lama
Tingkat keadilan lebih rendah dibandingkan RR
---

## Kesimpulan
Berdasarkan hasil pengujian dan analisis penjadwalan CPU, dapat disimpulkan bahwa algoritma Round Robin dan Priority Scheduling memiliki karakteristik yang berbeda. Round Robin dengan time quantum optimal (q = 3) mampu memberikan keseimbangan antara responsivitas dan keadilan dengan average waiting time sebesar 8,5 dan average turnaround time sebesar 14. Namun, performa algoritma ini sangat bergantung pada pemilihan nilai time quantum.
---

## Quiz
1. [Pertanyaan 1]  
   **Jawaban:Perbedaan utama terletak pada dasar penentuan urutan eksekusi proses:
Round Robin (RR) menjadwalkan proses secara bergiliran dengan jatah waktu (time quantum) yang sama untuk setiap proses, sehingga menekankan keadilan dan responsivitas.
Priority Scheduling menjadwalkan proses berdasarkan tingkat prioritas, sehingga proses dengan prioritas lebih tinggi akan dieksekusi terlebih dahulu dan menekankan efisiensi untuk proses penting.**  
2. [Pertanyaan 2]  
   **Jawaban:Ukuran time quantum sangat memengaruhi kinerja Round Robin:

Time quantum terlalu kecil
➝ Context switching sering terjadi
➝ Overhead tinggi
➝ Waiting time dan turnaround time meningkat

Time quantum terlalu besar
➝ Perilaku sistem mendekati FCFS
➝ Responsivitas menurun
➝ Proses lain menunggu lebih lama

Time quantum optimal
➝ Keseimbangan antara efisiensi dan responsivitas
➝ Performa sistem menjadi lebih baik**  
3. [Pertanyaan 3]  
   **Jawaban:Starvation terjadi karena:

Proses berprioritas tinggi terus-menerus mendapatkan CPU
Proses berprioritas rendah terus tertunda
Akibatnya, proses prioritas rendah bisa menunggu sangat lama atau tidak pernah dieksekusi**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
