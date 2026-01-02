
# Laporan Praktikum Minggu [X]
Topik: [Penjadwalan CPU – FCFS dan SJF]

---

## Identitas
- **Nama**  : [aldiman]  
- **NIM**   : [250320574]  
- **Kelas** : [1dsra]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.   
> Tujuan utamanya adalah memahami bagaimana sistem operasi menentukan urutan eksekusi proses, serta bagaimana waiting time dan turnaround time memengaruhi performa sistem.


---

## Dasar Teori
waiting time dan turnaround time untuk algoritma FCFS dan SJF.
performa FCFS dan SJF berdasarkan hasil analisis.
kelebihan dan kekurangan masing-masing algoritma.

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
Algoritma	Avg Waiting Time	Avg Turnaround Time	Kelebihan	Kekurangan
FCFS	8.75	14.75	Sederhana dan mudah diterapkan	Tidak efisien untuk proses panjang
SJF	6.25	12.25	Optimal untuk job pendek	Menyebabkan starvation pada job panjang


---

## Kesimpulan
SJF lebih efisien dibanding FCFS (WT & TAT lebih kecil)
Namun SJF berisiko starvation, terutama jika banyak job pendek datang terus-menerus
FCFS lebih adil, tetapi kurang optimal secara performa
---

## Quiz
1. [Pertanyaan 1]  
   **Jawaban:perbedaan utaman antara fcfs dan sjf
aspek=dasar penjadwalan,preemptive,efisiensi,rata rata waiting time,resiko starvation
fcfs=urutanwaktu kedatangan,tidak,kurang efisien,lebih besar,tidak ada
sjf=burst time terpendek,bisa(non-preemptive/preemptive,lebih efisien,lebih kecil,ada
   **  
3. [Pertanyaan 2]  
   **Jawaban:Karena proses dengan burst time paling pendek dieksekusi lebih dulu, maka:
Proses pendek tidak menunggu lama
Proses panjang memang menunggu, tetapi tidak menambah waktu tunggu total secara signifikan**  
4. [Pertanyaan 3]  
   **Jawaban:
-Starvation=
Proses dengan burst time panjang bisa tidak pernah dieksekusi,
Terjadi jika proses pendek terus berdatangan

-Sulit memprediksi burst time=
Sistem interaktif tidak tahu pasti lama eksekusi user process,
Estimasi bisa tidak akurat

-Respons buruk untuk user tertentu=
User dengan proses panjang merasa sistem tidak responsif,
Tidak cocok untuk sistem yang butuh respon cepat & adil**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
