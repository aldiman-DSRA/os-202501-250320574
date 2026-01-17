
# Laporan Praktikum Minggu [X]
Topik: [manajemen file dan permission di linux]

---

## Identitas
- **Nama**  : []  
- **NIM**   : [NIM Mahasiswa]  
- **Kelas** : [Kelas]

---

## Tujuan
> Mahasiswa mampu menggunakan perintah dasar Linux untuk mengelola file dan direktori, memahami konsep permission dan ownership, serta mendokumentasikan hasil praktikum dalam bentuk laporan dan repositori Git.

---

## Dasar Teori
-Sistem file Linux menggunakan struktur hierarki berbentuk pohon (tree).
-Setiap file dan direktori memiliki permission (izin akses) dan ownership (kepemilikan).
-Permission terdiri dari read (r), write (w), dan execute (x).
-Perintah chmod digunakan untuk mengubah permission file.
-Perintah chown digunakan untuk mengubah pemilik dan grup file.

---

## Langkah Praktikum
a.	Menyiapkan environment Linux (Ubuntu/WSL) dan direktori kerja praktikum.
b.	Menjalankan perintah navigasi sistem file (pwd, ls, cd).
c.	Membaca isi file sistem menggunakan cat.
d.	Membuat file dan mengubah permission serta ownership.
e.	Mengambil screenshot hasil eksekusi.
f.	Melakukan commit dan push ke repositori Git.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
pwd
cd/tmp
ls -a

cat/etc/passwd | head -n 5

echo "Hello <aldiman><250320574>" > percobaan.txt
ls -l percobaan.txt
chmod 600 percobaan.txt
ls -l percobaan.txt
sudo chown root percobaan.txt
ls -l percobaan.txt

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
1.	Manajemen file dan permission merupakan aspek penting dalam keamanan Linux.
2.	Perintah chmod dan chown memungkinkan kontrol akses yang fleksibel.
3.	Dokumentasi praktikum membantu pemahaman dan pelacakan hasil kerja.

---

## Quiz
1. [Pertanyaan 1]  
   **mengubah hak akses (permission) file atau direktori:**  
2. [Pertanyaan 2]  
   **owner memiliki rwx, group memilki r-x dan others hanya memilki r:**  
3. [Pertanyaan 3]  
   **chmod mengatur hak akses ,sedangkan chown mengatur kepimilikan file:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
