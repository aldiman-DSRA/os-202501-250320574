
# Laporan Praktikum Minggu [X]
Topik: [LAPORAN DALAM BENTUK IMRAD]

---

## Identitas
- **Nama**  : [aldiman]  
- **NIM**   : [250320574]  
- **Kelas** : [1dsra]

---

## Tujuan
> menyusun laporan praktikum dengan struktur ilmiahc(pendahuluan-metode-hasil-pembahasan-kesimpulan
> menyajikan hasil uji kedalam bentuk tabel dan grafik yang jelas
> menuliskan analsis hasil dengan argumentasi yang logis
> menyusun sitasi dan daftar pustaka dengan format ynag logis
> 
---
## PENDAHULUAN
LATAR BELAKANG
Sistem operasi memiliki peran penting dalam mengatur dan mengelola sumber daya komputer, salah satunya adalah Central Processing Unit (CPU). CPU hanya dapat mengeksekusi satu proses pada satu waktu, sehingga diperlukan mekanisme penjadwalan (CPU Scheduling) untuk menentukan urutan proses yang akan dijalankan. Penjadwalan yang baik dapat meningkatkan efisiensi penggunaan CPU serta mengurangi waktu tunggu proses.

Beberapa algoritma penjadwalan CPU yang umum digunakan adalah First Come First Serve (FCFS) dan Shortest Job First (SJF). Algoritma FCFS menjalankan proses berdasarkan urutan kedatangan, sedangkan SJF memilih proses dengan waktu eksekusi paling singkat. Masing-masing algoritma memiliki kelebihan dan kekurangan dalam hal efisiensi, waktu tunggu, dan keadilan proses.

Oleh karena itu, diperlukan sebuah pengujian dan analisis terhadap algoritma FCFS dan SJF untuk memahami cara kerjanya serta membandingkan performa keduanya. Pada praktikum ini, simulasi penjadwalan dilakukan menggunakan bahasa pemrograman Python untuk memperoleh hasil yang lebih terstruktur dan mudah dianalisis.

RUMUSAN MASALAH
1.	Bagaimana cara kerja algoritma penjadwalan CPU FCFS dan SJF?
2.	Bagaimana perbedaan urutan eksekusi proses pada algoritma FCFS dan SJF?
3.	Algoritma manakah yang menghasilkan waktu tunggu (waiting time) dan turnaround time yang lebih efisien?

TUJUAN
1.	Memahami konsep dasar penjadwalan CPU pada sistem operasi.
2.	Mengimplementasikan algoritma FCFS dan SJF menggunakan bahasa pemrograman Python.
3.	Menganalisis dan membandingkan hasil penjadwalan FCFS dan SJF berdasarkan waiting time dan turnaround time.
4.	Mengetahui kelebihan dan kekurangan masing-masing algoritma penjadwalan.

## METODE
LINGKUAN UJI

A. Lingkungan Uji (Testing Environment)

   Eksperimen dilakukan menggunakan lingkungan komputasi sebagai berikut
   
    1.	Sistem Operasi: Windows 11
    2.	Bahasa Pemrograman: Python 3.x
    3.	Editor/IDE: Visual Studio Code
    
B. Langkah Eksperimen

   Langkah-langkah yang dilakukan dalam eksperimen ini adalah:
1.	Menentukan dataset proses yang terdiri dari Process ID, Arrival Time, dan Burst Time.
2.	Mengimplementasikan algoritma First Come First Serve (FCFS) dalam Python.
3.	Mengimplementasikan algoritma Shortest Job First (SJF) Non-Preemptive dalam Python.
4.	Menjalankan simulasi penjadwalan menggunakan dataset yang sama untuk kedua algoritma.
5.	Mencatat hasil eksekusi berupa waktu mulai (start time), waktu selesai (finish time), waiting time, dan turnaround time.
6.	Membandingkan hasil FCFS dan SJF berdasarkan nilai rata-rata waktu tunggu dan turnaround time.
7.	Menganalisis efisiensi masing-masing algoritma berdasarkan hasil simulasi.

C. Parameter dan Dataset (Parameters & Dataset)

Parameter yang digunakan dalam eksperimen meliputi:

1.Arrival Time (AT): Waktu kedatangan proses ke antrian ready.

2.Burst Time (BT): Lama waktu eksekusi proses oleh CPU.

3.Start Time (ST): Waktu proses mulai dieksekusi.

4.Finish Time (FT): Waktu proses selesai dieksekusi.

Dataset proses yang digunakan ditunjukkan pada Tabel berikut:
| Proses | Arrival Time | Burst Time |
| ------ | ------------ | ---------- |
| P1     | 0            | 12         |
| P2     | 1            | 2          |
| P3     | 2            | 1          |
| P4     | 3            | 3          |

Dataset ini dipilih untuk menunjukkan perbedaan perilaku algoritma ketika terdapat proses dengan burst time panjang yang datang lebih awal dan proses dengan burst time pendek yang datang belakangan.

D. CARA PENGUKURAN

Pengukuran kinerja algoritma dilakukan menggunakan metrik berikut:
1. Waiting time (WT)
   
   Waktu tunggu sebelum eksekusi oleh cpu
   Wt=start time – arrival time
   
3. Turnaround time (tat)
   Total waktu yang dibutuhkan proses sejak datang hingga selesai dieksekusi
   Tat =finish time -  arrival time
   
5. Rata rata waiting time 
   Digunakan sebagai indikator efisiensi algoritma penjadwalan
   Average wt =(∑WT)/(JUMLAH PROSES)
   
7. Rata rata turnaround time
   Digunakan untuk menilai kecepatan penyelesaian keseluruh proses

## HASIL
INTERPRETASI HASIL

TABEL HASIL UJI PENJADWALAN

A. Hasil Algoritma Fcfs (First Come First Serve)

| Proses | Arrival Time | Burst Time | Start Time | Finish Time | Waiting Time | Turnaround Time |
| ------ | ------------ | ---------- | ---------- | ----------- | ------------ | --------------- |
| P1     | 0            | 12         | 0          | 12          | 0            | 12              |
| P2     | 1            | 2          | 12         | 14          | 11           | 13              |
| P3     | 2            | 1          | 14         | 15          | 12           | 13              |
| P4     | 3            | 3          | 15         | 18          | 12           | 15              |

Rata-rata Waiting Time FCFS = 8,75
Rata-rata Turnaround Time FCFS = 13,25

B.	Hasil Algoritma SJF Non-Preemptive

| Proses | Arrival Time | Burst Time | Start Time | Finish Time | Waiting Time | Turnaround Time |
| ------ | ------------ | ---------- | ---------- | ----------- | ------------ | --------------- |
| P1     | 0            | 12         | 0          | 12          | 0            | 12              |
| P3     | 2            | 1          | 12         | 13          | 10           | 11              |
| P2     | 1            | 2          | 13         | 15          | 12           | 14              |
| P4     | 3            | 3          | 15         | 18          | 12           | 15              |

Rata-rata Waiting Time SJF = 8,50
Rata-rata Turnaround Time SJF = 13,00

RINGKASAN TEMUAN

Berdasarkan hasil pengujian yang telah dilakukan, diperoleh beberapa temuan utama sebagai berikut:

1.Algoritma SJF Non-Preemptive menghasilkan rata-rata waiting time yang lebih kecil dibandingkan FCFS.

2.Perbedaan kinerja tidak terlalu signifikan karena proses dengan burst time panjang (P1) datang lebih awal dan harus dieksekusi terlebih dahulu.

3.FCFS cenderung menyebabkan waktu tunggu yang lebih besar untuk proses yang datang belakangan.

4.SJF lebih efisien dalam mengatur waktu CPU, namun tetap berpotensi menyebabkan starvation pada proses dengan burst time besar.

## PEMBAHASAN

A.	Interpretasi Hasil

Berdasarkan tabel hasil pengujian, algoritma SJF Non-Preemptive menunjukkan kinerja yang lebih baik dibandingkan algoritma FCFS dalam meminimalkan waktu tunggu dan waktu penyelesaian proses. Hal ini terlihat dari nilai rata-rata waiting time SJF (8,50) yang lebih kecil dibandingkan FCFS (8,75), serta rata-rata turnaround time SJF (13,00) yang juga lebih rendah dibandingkan FCFS (13,25).

Perbedaan nilai yang tidak terlalu signifikan disebabkan oleh adanya proses dengan burst time yang sangat panjang (P1) dan datang lebih awal. Pada kedua algoritma, proses tersebut harus dieksekusi terlebih dahulu sehingga membatasi peluang algoritma SJF untuk mengoptimalkan waktu tunggu proses lainnya.

B.	Keterbatasan Eksperimen

Eksperimen ini memiliki beberapa keterbatasan, antara lain:

1.	Jumlah proses yang diuji relatif sedikit, sehingga variasi hasil belum terlalu luas.
2.	Algoritma SJF yang digunakan adalah versi Non-Preemptive, sehingga proses yang sedang berjalan tidak dapat dihentikan meskipun terdapat proses dengan burst time lebih pendek.
3.	Burst time dianggap sudah diketahui secara pasti, sedangkan pada sistem nyata burst time sering kali hanya dapat diperkirakan.
4.	Hasil hanya dianalisis menggunakan tabel tanpa visualisasi grafik, sehingga pola eksekusi proses tidak terlihat secara visual.

C.	Perbandingan dengan Teori / Ekspektasi

Secara teori, algoritma Shortest Job First (SJF) dikenal sebagai algoritma yang optimal dalam meminimalkan rata-rata waiting time. Hasil eksperimen ini sesuai dengan teori, di mana SJF tetap menghasilkan rata-rata waktu tunggu yang lebih kecil dibandingkan FCFS.

Namun, teori SJF biasanya menunjukkan perbedaan yang cukup signifikan ketika proses berdurasi pendek tersedia lebih awal. Pada dataset yang digunakan, proses dengan burst time pendek datang setelah proses panjang dimulai, sehingga keunggulan SJF tidak terlihat secara maksimal. Hal ini menunjukkan bahwa pola kedatangan proses sangat memengaruhi efektivitas algoritma SJF.

## KESIMPULAN
Kesimpulan
1.	Algoritma SJF Non-Preemptive menghasilkan rata-rata waiting time dan turnaround time yang lebih kecil dibandingkan FCFS berdasarkan hasil pengujian tabel.
2.	Perbedaan kinerja antara FCFS dan SJF tidak terlalu signifikan karena adanya proses dengan burst time panjang yang datang lebih awal.
3.	Algoritma FCFS mudah diimplementasikan, namun kurang efisien dalam mengoptimalkan waktu tunggu proses.
4.	Pemilihan algoritma penjadwalan harus disesuaikan dengan karakteristik proses dan kebutuhan sistem.

## DAFTAR PUSTAKA
1.	Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). Operating System Concepts (10th ed.). Hoboken, NJ: John Wiley & Sons.
2.	Tanenbaum, A. S., & Bos, H. (2015). Modern Operating Systems (4th ed.). Boston: Pearson Education.
3.	GeeksforGeeks. (2023). CPU Scheduling in Operating Systems.
https://www.geeksforgeeks.org/cpu-scheduling-in-operating-systems/

## Quiz
1. [Pertanyaan 1]  
   **IMRAD membuat laporan lebih ilmiah karena strukturnya jelas, sistematis, dan memudahkan evaluasi setiap bagian.
   :**  
3. [Pertanyaan 2]  
   **Hasil menyajikan data apa adanya, sedangkan Pembahasan menjelaskan dan menafsirkan data tersebut.:**  
4. [Pertanyaan 3]  
   **Sitasi dan daftar pustaka penting untuk menunjukkan dasar teori, menghindari plagiarisme, dan meningkatkan kredibilitas laporan.:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
