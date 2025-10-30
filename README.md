# 📘 Modul Belajar Python Lengkap (Level 1–10)

Selamat datang di **Modul Belajar Python by Ludang Prasetyo Nugroho** 🐍

Modul ini disusun untuk membantu kamu memahami bahasa pemrograman **Python** dari **dasar hingga mahir**.  
Setiap level berisi **penjelasan teori**, **contoh kode**, dan **komentar yang lengkap** agar mudah dipahami.

---

## 🧭 Daftar Isi

1. [Level 1 — Pengenalan Python](#-level-1--pengenalan-python)
2. [Level 2 — Variabel dan Tipe Data](#-level-2--variabel-dan-tipe-data)
3. [Level 3 — Operator dan Ekspresi](#-level-3--operator-dan-ekspresi)
4. [Level 4 — Percabangan (If, Elif, Else)](#-level-4--percabangan-if-elif-else)
5. [Level 5 — Perulangan (For dan While)](#-level-5--perulangan-for-dan-while)
6. [Level 6 — Struktur Data (List, Tuple, Dictionary)](#-level-6--struktur-data-list-tuple-dictionary)
7. [Level 7 — Fungsi (Function)](#-level-7--fungsi-function)
8. [Level 8 — File Handling (Baca & Tulis File)](#-level-8--file-handling-baca--tulis-file)
9. [Level 9 — PBO / OOP (Pemrograman Berorientasi Objek)](#-level-9--pbo--oop-pemrograman-berorientasi-objek)
10. [Level 10 — Mini Project: To-Do List Sederhana](#-level-10--mini-project-to-do-list-sederhana)

---

## 🧩 Level 1 — Pengenalan Python

### 🎯 Tujuan:
- Memahami apa itu Python.
- Menjalankan program pertama (Hello World).

### 📖 Penjelasan:
Python adalah bahasa pemrograman **interpreted**, artinya dijalankan baris demi baris tanpa proses kompilasi.  
Cocok untuk pemula karena sintaksnya sederhana dan mudah dibaca.

### 💻 Contoh Program:

```python
# ===============================================
# PROGRAM 1: Pengenalan Dasar Python
# ===============================================
# Baris ini adalah komentar. Komentar tidak dieksekusi oleh program.
# Gunakan tanda '#' untuk menulis komentar tunggal.

# Fungsi print() digunakan untuk menampilkan teks ke layar.
print("Halo, Dunia!")

# Kamu juga bisa menampilkan angka atau operasi matematika langsung.
print(2 + 3)
print("Hasil penjumlahan 2 + 3 adalah", 2 + 3)

# Kesalahan umum pemula: lupa tanda kutip atau tanda kurung.
# print(Halo Dunia) ❌  → Salah karena tidak pakai tanda kutip.
```

---

## 🧮 Level 2 — Variabel dan Tipe Data

### 🎯 Tujuan:
- Mengenal variabel, tipe data, dan cara penggunaannya.

### 📖 Penjelasan:
Variabel digunakan untuk menyimpan data di memori.  
Kamu bisa menyimpan teks (string), angka (integer/float), atau logika (boolean).

### 💻 Contoh Program:

```python
# ===============================================
# PROGRAM 2: Variabel dan Tipe Data
# ===============================================

# Membuat variabel
nama = "Ludang"
umur = 20
suhu_tubuh = 36.7
is_aktif = True

# Menampilkan tipe data masing-masing variabel
print(type(nama))      # <class 'str'>
print(type(umur))      # <class 'int'>
print(type(suhu_tubuh))# <class 'float'>
print(type(is_aktif))  # <class 'bool'>

# Menampilkan nilai dengan format string
print(f"Halo, nama saya {nama}, umur {umur} tahun, suhu tubuh {suhu_tubuh}°C")
```

---

## 🧠 Level 3 — Operator dan Ekspresi

### 🎯 Tujuan:
- Mengenal operator matematika, logika, dan perbandingan.

### 💻 Contoh Program:

```python
# ===============================================
# PROGRAM 3: Operator dan Ekspresi
# ===============================================

# Operator aritmatika
x = 10
y = 3
print("Penjumlahan:", x + y)
print("Pengurangan:", x - y)
print("Perkalian:", x * y)
print("Pembagian:", x / y)
print("Sisa bagi:", x % y)

# Operator perbandingan
print("Apakah x lebih besar dari y?", x > y)
print("Apakah x sama dengan y?", x == y)

# Operator logika
print("Hasil logika:", x > 5 and y < 5)
print("Hasil logika:", x > 5 or y > 10)
```

---

## 🔄 Level 4 — Percabangan (If, Elif, Else)

### 🎯 Tujuan:
- Membuat keputusan dalam program berdasarkan kondisi tertentu.

### 💻 Contoh Program:

```python
# ===============================================
# PROGRAM 4: Percabangan
# ===============================================

nilai = int(input("Masukkan nilai kamu: "))

if nilai >= 90:
    print("Nilai kamu A, luar biasa!")
elif nilai >= 75:
    print("Nilai kamu B, bagus!")
elif nilai >= 60:
    print("Nilai kamu C, tingkatkan lagi!")
else:
    print("Nilai kamu D, harus belajar lebih giat!")
```

---

## 🔁 Level 5 — Perulangan (For dan While)

### 🎯 Tujuan:
- Mengulang perintah secara otomatis.

### 💻 Contoh Program:

```python
# ===============================================
# PROGRAM 5: Perulangan For dan While
# ===============================================

# Contoh perulangan for
for i in range(1, 6):
    print(f"Perulangan ke-{i}")

# Contoh perulangan while
angka = 0
while angka < 5:
    print("Angka sekarang:", angka)
    angka += 1  # Menambah nilai agar tidak infinite loop
```

---

## 📦 Level 6 — Struktur Data (List, Tuple, Dictionary)

### 🎯 Tujuan:
- Mengelola data dalam bentuk koleksi.

### 💻 Contoh Program:

```python
# ===============================================
# PROGRAM 6: Struktur Data
# ===============================================

# List (bisa diubah)
buah = ["apel", "jeruk", "pisang"]
print("Daftar buah:", buah)

# Menambah dan menghapus elemen list
buah.append("mangga")
buah.remove("jeruk")
print("Setelah diubah:", buah)

# Tuple (tidak bisa diubah)
warna = ("merah", "hijau", "biru")
print("Warna ke-2:", warna[1])

# Dictionary (data dengan pasangan kunci-nilai)
siswa = {"nama": "Nindy", "umur": 21, "kelas": "Informatika"}
print("Nama siswa:", siswa["nama"])
```

---

## ⚙️ Level 7 — Fungsi (Function)

### 🎯 Tujuan:
- Membuat fungsi agar kode lebih terstruktur.

### 💻 Contoh Program:

```python
# ===============================================
# PROGRAM 7: Fungsi
# ===============================================

# Fungsi untuk menghitung luas persegi
def hitung_luas_persegi(sisi):
    # sisi * sisi menghitung luas berdasarkan rumus matematika
    luas = sisi * sisi
    return luas

# Memanggil fungsi
total = hitung_luas_persegi(5)
print("Luas persegi adalah:", total)
```

---

## 📚 Level 8 — File Handling (Baca & Tulis File)

### 🎯 Tujuan:
- Menulis dan membaca data ke file teks.

### 💻 Contoh Program:

```python
# ===============================================
# PROGRAM 8: File Handling
# ===============================================

# Menulis file
with open("data.txt", "w") as file:
    file.write("Halo, ini adalah data yang disimpan di file!")

# Membaca file
with open("data.txt", "r") as file:
    isi = file.read()
    print("Isi file:", isi)
```

---

## 🧩 Level 9 — PBO / OOP (Pemrograman Berorientasi Objek)

### 🎯 Tujuan:
- Memahami konsep class dan object.

### 💻 Contoh Program:

```python
# ===============================================
# PROGRAM 9: OOP Dasar
# ===============================================

class Hewan:
    # Konstruktor (fungsi yang dijalankan saat objek dibuat)
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def bersuara(self):
        print(f"{self.nama} adalah seekor {self.jenis} yang sedang bersuara.")

# Membuat objek
kucing = Hewan("Miko", "Kucing")
kucing.bersuara()
```

---

## 🚀 Level 10 — Mini Project: To-Do List Sederhana

### 🎯 Tujuan:
- Menggabungkan konsep variabel, list, percabangan, dan fungsi.

### 💻 Contoh Program:

```python
# ===============================================
# MINI PROJECT: To-Do List Sederhana
# ===============================================

# List untuk menyimpan tugas
tugas = []

# Fungsi untuk menampilkan semua tugas
def tampilkan_tugas():
    print("\nDaftar Tugas:")
    if not tugas:
        print("(Kosong)")
    else:
        for i, t in enumerate(tugas):
            print(f"{i+1}. {t}")

# Fungsi untuk menambah tugas
def tambah_tugas():
    t = input("Masukkan tugas baru: ")
    tugas.append(t)
    print("Tugas berhasil ditambahkan!")

# Fungsi untuk menghapus tugas
def hapus_tugas():
    tampilkan_tugas()
    try:
        index = int(input("Hapus tugas nomor: ")) - 1
        if 0 <= index < len(tugas):
            tugas.pop(index)
            print("Tugas berhasil dihapus!")
        else:
            print("Nomor tidak valid!")
    except ValueError:
        print("Masukkan angka yang benar!")

# Program utama
while True:
    print("\n=== MENU TO-DO LIST ===")
    print("1. Lihat Tugas")
    print("2. Tambah Tugas")
    print("3. Hapus Tugas")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tampilkan_tugas()
    elif pilihan == "2":
        tambah_tugas()
    elif pilihan == "3":
        hapus_tugas()
    elif pilihan == "4":
        print("Terima kasih telah menggunakan To-Do List!")
        break
    else:
        print("Pilihan tidak valid!")
```

---

## 🏁 Penutup
Selamat! Kamu telah menyelesaikan **10 Level Belajar Python** 🎉

Langkah selanjutnya:
- Coba buat project pribadi seperti kalkulator, game tebak angka, atau sistem login.
- Pelajari library populer seperti `tkinter`, `pandas`, `flask`, dan `pygame`.

> Dibuat dengan ❤️ oleh **Ludang Prasetyo Nugroho** — modul ini 100% gratis untuk belajar dan latihan.