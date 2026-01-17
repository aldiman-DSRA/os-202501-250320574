
# Laporan Praktikum Minggu [X]
Topik: [Sinkronisasi Proses dan Masalah Deadlock]

---

## Identitas
- **Nama**  : [aldiman]  
- **NIM**   : [250320574]  
- **Kelas** : [1dsra]

---

## Tujuan
>Mengidentifikasi empat kondisi penyebab deadlock (mutual exclusion, hold and wait, no preemption, circular wait).
>Menjelaskan mekanisme sinkronisasi menggunakan semaphore atau monitor.
>menganalisis dan memberikan solusi untuk kasus deadlock



---

## Dasar Teori
1.deadlock adalah kondisi ketika dua atau lebih proses saling menunggu sumber daya sehingga tidak ada proses yang dapat melanjutkan eksekusi 
2.deadlock terjadi apabila empat kondisi coffman terpenuhi secara bersamaan
mutual exculion, hold and wait, no preemption, dan circular wait
3.sinkronisasi proses digunakan untuk mengatur akses ke sumber daya bersama
agar tidak terjadi konflik

---

## Langkah Praktikum
langkah langkah simulasi dining philosophers
1.menyiapkan python
2.memasukan kode kedalam python 
kode pseudocode (versi deadlock) simmulasi dining philosophers
while true:
    think()
    pick_left_fork()
    pick_right_fork()
    eat()
    put_left_fork()
    put_right_fork()
    
3.mengamati proses eksekusi 
  -perhatikan output awal (semua filsuf berhasil pada kondisi thinking
  -setiap filsuf berhasil mengambil garpu kiri
  -semua filsuf mencoba mengambil garpu kanan
4.mengedentifikasi deadlock
-program berhenti menmpilkan output
-tidak ada filsuf yang masuk ke kondisi eating
-cpu masih aktif,tetapi proses tidak berkembang
kondisi ini menunjukan deadlock telah terjadi
5.hasil pada terminal
  <img width="764" height="925" alt="image" src="https://github.com/user-attachments/assets/a67d5af4-5335-471b-b990-232a26d86491" />

langkah langkah versi fixed (deadlock free)
1.mentiapkan python
2.memasukan kode pada python
semaphore room = 4
semaphore fork[5] = {1,1,1,1,1}

while true:
    think()
    wait(room)
    wait(fork[left])
    wait(fork[right])
    eat()
    signal(fork[left])
    signal(fork[right])
    signal(room)
3.mengamati proses eksekusi
-program tidak berhenti
-filsuf beragntian masuk ke kondsisi eating
-tidak ada kondisi freeze sepeti eksekusi eksperimen 1
4.hasil pada terminal
<img width="1920" height="1080" alt="Screenshot 2026-01-17 161724" src="https://github.com/user-attachments/assets/52c9485e-e7b0-4486-a612-7f25095a8dc3" />

analsis deadlock
| Syarat Deadlock  | Status   | Alasan                                |
| ---------------- | -------- | ------------------------------------- |
| Mutual Exclusion | Ada      | Garpu tetap eksklusif                 |
| Hold and Wait    | Ada      | Filsuf memegang garpu                 |
| No Preemption    | Ada      | Garpu tidak direbut                   |
| Circular Wait    | Hilang   | Dibatasi semaphore / urutan asimetris |







## Kode / Perintah
kode pseudocode (versi deadlock) simmulasi dining philosophers
while true:
    think()
    pick_left_fork()
    pick_right_fork()
    eat()
    put_left_fork()
    put_right_fork()
  <img width="764" height="925" alt="image" src="https://github.com/user-attachments/assets/a67d5af4-5335-471b-b990-232a26d86491" />

  

  

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. [Pertanyaan 1]  
   **Jawaban:**  
2. [Pertanyaan 2]  
   **Jawaban:**  
3. [Pertanyaan 3]  
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
