
# Laporan Praktikum Minggu [X]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : [aldiman]  
- **NIM**   : [250320574]  
- **Kelas** : [1dsra]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
> Menginstal perangkat lunak virtualisasi (VirtualBox/VMware).
> Membuat dan menjalankan sistem operasi guest di dalam VM.
> Mengatur konfigurasi resource VM (CPU, RAM, storage).
> Menjelaskan mekanisme proteksi OS melalui virtualisasi.


---

## Dasar Teori
1.	Virtualisasi memungkinkan satu komputer menjalankan sistem operasi lain secara virtual tanpa mengganggu sistem utama.
2.	Manajemen resource (CPU dan RAM) pada VM memengaruhi performa sistem operasi guest.
3.	Isolasi sistem membuat OS guest terpisah dari host, sehingga lebih aman (sandboxing).

---

## Langkah Praktikum
1.<img width="827" height="612" alt="image" src="https://github.com/user-attachments/assets/952dbc05-a986-473b-a32e-a08563a5c279" />
2.<img width="827" height="603" alt="image" src="https://github.com/user-attachments/assets/755e748b-da52-457c-8a91-a18ae6de1868" />
3.<img width="827" height="570" alt="image" src="https://github.com/user-attachments/assets/9b187775-de1a-4946-a4ed-2c8f85432fd1" />
4.<img width="827" height="537" alt="image" src="https://github.com/user-attachments/assets/c35c1314-f91c-432c-8d64-914816a57cf0" />
5.<img width="827" height="523" alt="image" src="https://github.com/user-attachments/assets/9bf53e67-1f23-49b6-ac26-94d9504f0d9e" />
6.<img width="827" height="522" alt="image" src="https://github.com/user-attachments/assets/c046687a-6323-49df-8728-48672f2dc915" />

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

Perubahan alokasi CPU dan RAM pada virtual machine berpengaruh langsung terhadap performa sistem operasi guest. Saat resource ditingkatkan, sistem berjalan lebih responsif dan waktu proses menjadi lebih cepat. Virtual machine juga menyediakan isolasi antara host dan guest, sehingga aktivitas atau kesalahan pada guest tidak berdampak langsung pada sistem host. Hal ini menunjukkan bahwa virtualisasi berfungsi sebagai sandbox yang meningkatkan keamanan dan stabilitas sistem.

---

## Kesimpulan

1.	Virtual machine memungkinkan menjalankan sistem operasi guest secara terisolasi tanpa mengganggu sistem host.
2.	Alokasi CPU dan RAM berpengaruh terhadap performa sistem operasi guest.
3.	Virtualisasi meningkatkan keamanan sistem melalui isolasi (sandboxing).

---

## Quiz
1. [Pertanyaan 1]  
   **
   Host OS adalah sistem operasi utama yang berjalan langsung di komputer fisik, sedangkan guest OS adalah sistem operasi yang berjalan di dalam mesin virtual.
   :**  
3. [Pertanyaan 2]  
   **
   Hypervisor berfungsi mengelola dan membagi resource hardware (CPU, RAM, storage) agar dapat digunakan oleh mesin virtual secara terisolasi.
   :**  
5. [Pertanyaan 3]  
   **
   Karena guest OS terisolasi dari host, maka kesalahan atau serangan pada guest tidak langsung memengaruhi sistem host (sandboxing).
   :**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
