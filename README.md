# 📘 Modul Belajar Python Super Lengkap (Level 1–10 + Tambahan)

Selamat datang di **Modul Super Lengkap Belajar Python by Ludang Prasetyo Nugroho** 🐍

Modul ini disusun agar kamu bisa belajar Python dari **nol sampai mahir**, dengan **penjelasan mendalam, komentar di setiap kode, dan latihan tambahan di setiap level.**

---

## 🧭 Daftar Isi

1. [Level 1 — Pengenalan Python & Instalasi](#-level-1--pengenalan-python--instalasi)
2. [Level 2 — Variabel, Input, dan Tipe Data](#-level-2--variabel-input-dan-tipe-data)
3. [Level 3 — Operator dan Ekspresi](#-level-3--operator-dan-ekspresi)
4. [Level 4 — Percabangan (If, Elif, Else)](#-level-4--percabangan-if-elif-else)
5. [Level 5 — Perulangan (For dan While)](#-level-5--perulangan-for-dan-while)
6. [Level 6 — Struktur Data (List, Tuple, Dictionary, Set)](#-level-6--struktur-data-list-tuple-dictionary-set)
7. [Level 7 — Fungsi dan Scope Variabel](#-level-7--fungsi-dan-scope-variabel)
8. [Level 8 — File Handling & Exception Handling](#-level-8--file-handling--exception-handling)
9. [Level 9 — OOP (Class, Object, Inheritance, Polymorphism)](#-level-9--oop-class-object-inheritance-polymorphism)
10. [Level 10 — Mini Project: To-Do List Sederhana](#-level-10--mini-project-to-do-list-sederhana)
11. [Bonus — Modul Lanjutan: Library Populer](#-bonus--modul-lanjutan-library-populer)
12. [Latihan & Challenge Tiap Level](#-latihan--challenge-tiap-level)

---

## 🧩 Level 1 — Pengenalan Python & Instalasi

### 🎯 Tujuan:
- Mengenal Python, cara instalasi, dan menjalankan kode.

### 📖 Penjelasan:
Python adalah bahasa pemrograman tingkat tinggi yang **mudah dibaca, fleksibel, dan powerful**. Digunakan dalam berbagai bidang seperti:
- Web development (Flask, Django)
- Data Science (Pandas, NumPy)
- Machine Learning (TensorFlow, Scikit-learn)
- IoT, Automasi, dan Game.

### 🛠️ Instalasi:
1. Unduh Python di [https://python.org/downloads](https://python.org/downloads)
2. Centang opsi **“Add Python to PATH”** saat instalasi.
3. Cek instalasi di terminal:
   ```bash
   python --version
   ```

### 💻 Contoh Program Pertama:

```python
# ==============================================
# PROGRAM 1: Hello World Python Pertamaku
# ==============================================

# Fungsi print() digunakan untuk menampilkan teks ke layar.
# Komentar di Python diawali dengan tanda pagar (#)
print("Halo, Dunia!")
print("Selamat datang di belajar Python bersama Ludang!")

# Kamu juga bisa menampilkan hasil operasi matematika:
print("2 + 3 =", 2 + 3)
```

---

## 🧮 Level 2 — Variabel, Input, dan Tipe Data

### 🎯 Tujuan:
- Mengenal variabel, input dari pengguna, dan tipe data dasar.

```python
# ==============================================
# PROGRAM 2: Variabel dan Input
# ==============================================

# Variabel digunakan untuk menyimpan data sementara di memori.
# Tidak perlu deklarasi tipe data secara eksplisit.

nama = input("Masukkan nama kamu: ")
umur = int(input("Masukkan umur kamu: "))  # diubah ke integer
suhu_tubuh = float(input("Masukkan suhu tubuh kamu: "))
is_aktif = True  # contoh boolean

print(f"\nHalo {nama}! Umurmu {umur} tahun dan suhu tubuhmu {suhu_tubuh}°C.")
```

### 📚 Penjelasan Tambahan:
- `int()` digunakan untuk mengubah input menjadi angka bulat.
- `float()` untuk angka desimal.
- `bool()` untuk nilai logika (True/False).

---

## 🧠 Level 3 — Operator dan Ekspresi

### 🎯 Tujuan:
- Memahami operator matematika, logika, dan perbandingan.

```python
# ==============================================
# PROGRAM 3: Operator Dasar
# ==============================================

a, b = 10, 3  # menyimpan dua nilai sekaligus

# Operator Aritmatika
print(a + b, a - b, a * b, a / b, a % b, a ** b)

# Operator Perbandingan
print(a == b, a != b, a > b, a < b)

# Operator Logika
print(a > 5 and b < 5)  # True jika dua kondisi benar
print(a > 5 or b > 10)  # True jika salah satu benar
```

### 💡 Catatan Penting:
Operator sangat sering digunakan untuk membuat ekspresi logika dan kontrol alur program.

---

## 🔄 Level 4 — Percabangan (If, Elif, Else)

### 🎯 Tujuan:
- Membuat keputusan berdasarkan kondisi.

```python
# ==============================================
# PROGRAM 4: If-Else Python
# ==============================================

nilai = int(input("Masukkan nilai kamu: "))

if nilai >= 90:
    print("A — Sangat Baik!")
elif nilai >= 75:
    print("B — Bagus!")
elif nilai >= 60:
    print("C — Cukup!")
else:
    print("D — Kurang!")
```

### ⚡ Latihan:
Buat program penentu **kelulusan** berdasarkan nilai rata-rata 3 mata pelajaran.

---

## 🔁 Level 5 — Perulangan (For dan While)

### 🎯 Tujuan:
- Mengulang proses menggunakan `for` dan `while`.

```python
# ==============================================
# PROGRAM 5: Looping Dasar
# ==============================================

# Looping menggunakan for
for i in range(1, 6):
    print(f"Perulangan ke-{i}")

# Looping menggunakan while
angka = 0
while angka < 5:
    print("Angka sekarang:", angka)
    angka += 1
```

### 🧩 Catatan:
- `range(n)` membuat urutan angka dari 0 sampai n-1.
- Pastikan ada kondisi berhenti di `while` agar tidak infinite loop.

---

## 📦 Level 6 — Struktur Data (List, Tuple, Dictionary, Set)

### 🎯 Tujuan:
- Mengenal berbagai jenis struktur data di Python.

```python
# ==============================================
# PROGRAM 6: Struktur Data Lengkap
# ==============================================

# List: data yang bisa diubah
buah = ["apel", "pisang", "mangga"]
buah.append("jeruk")
print(buah)

# Tuple: data yang tidak bisa diubah
warna = ("merah", "hijau", "biru")
print(warna[1])

# Dictionary: pasangan key-value
mahasiswa = {"nama": "Nindy", "umur": 21, "jurusan": "Informatika"}
print(mahasiswa["nama"])

# Set: data unik tanpa urutan
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # Union
print(a & b)  # Intersection
```

---

## ⚙️ Level 7 — Fungsi dan Scope Variabel

### 🎯 Tujuan:
- Membuat fungsi dengan parameter dan nilai balik (return).

```python
# ==============================================
# PROGRAM 7: Fungsi dan Scope
# ==============================================

def hitung_luas_persegi(sisi):
    """Menghitung luas persegi dari panjang sisi"""
    return sisi * sisi

# Fungsi dengan parameter default
def sapa(nama="Pengunjung"):
    print(f"Halo, {nama}! Selamat belajar Python.")

print(hitung_luas_persegi(5))
sapa()
sapa("Ludang")
```

---

## 📂 Level 8 — File Handling & Exception Handling

### 🎯 Tujuan:
- Membaca dan menulis file, serta menangani error.

```python
# ==============================================
# PROGRAM 8: File dan Exception Handling
# ==============================================

try:
    # Menulis ke file
    with open("data.txt", "w") as f:
        f.write("Halo, ini data Python!")

    # Membaca isi file
    with open("data.txt", "r") as f:
        print(f.read())

except FileNotFoundError:
    print("File tidak ditemukan!")
except Exception as e:
    print("Terjadi kesalahan:", e)
```

---

## 🧩 Level 9 — OOP (Class, Object, Inheritance, Polymorphism)

### 🎯 Tujuan:
- Mengenal dasar OOP dan penerapan inheritance.

```python
# ==============================================
# PROGRAM 9: Object Oriented Programming
# ==============================================

class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def bersuara(self):
        print(f"{self.nama} mengeluarkan suara umum.")

# Inheritance (Pewarisan)
class Kucing(Hewan):
    def bersuara(self):
        print(f"{self.nama} mengeong: Meong!")

class Anjing(Hewan):
    def bersuara(self):
        print(f"{self.nama} menggonggong: Guk Guk!")

# Polymorphism
hewan_list = [Kucing("Miko"), Anjing("Doggo")]
for h in hewan_list:
    h.bersuara()
```

---

## 🚀 Level 10 — Mini Project: To-Do List Sederhana

### 🎯 Tujuan:
- Menggabungkan seluruh konsep Python.

```python
# ==============================================
# MINI PROJECT: To-Do List
# ==============================================

tugas = []

def tampilkan_tugas():
    if not tugas:
        print("Belum ada tugas.")
    else:
        for i, t in enumerate(tugas):
            print(f"{i+1}. {t}")

def tambah_tugas():
    t = input("Masukkan tugas baru: ")
    tugas.append(t)

def hapus_tugas():
    tampilkan_tugas()
    try:
        idx = int(input("Nomor tugas yang dihapus: ")) - 1
        if 0 <= idx < len(tugas):
            tugas.pop(idx)
    except ValueError:
        print("Masukkan angka yang valid!")

while True:
    print("\n1. Tampilkan Tugas\n2. Tambah Tugas\n3. Hapus Tugas\n4. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "1": tampilkan_tugas()
    elif pilih == "2": tambah_tugas()
    elif pilih == "3": hapus_tugas()
    elif pilih == "4": break
    else: print("Pilihan tidak valid!")
```

---

## 🎁 Bonus — Modul Lanjutan: Library Populer

- **NumPy** → Pengolahan array dan matematika ilmiah.
- **Pandas** → Analisis dan manajemen data.
- **Matplotlib** → Visualisasi grafik.
- **Flask** → Web Framework ringan.
- **Tkinter** → GUI desktop sederhana.
- **MQTT / paho-mqtt** → Komunikasi IoT.

---

## 🧠 Latihan & Challenge Tiap Level

- Level 1: Buat program menampilkan biodata kamu.
- Level 2: Hitung BMI (Berat / Tinggi²).
- Level 3: Kalkulator sederhana.
- Level 4: Penentu bilangan genap/ganjil.
- Level 5: Program hitung mundur.
- Level 6: Data nilai siswa (list of dict).
- Level 7: Fungsi konversi suhu.
- Level 8: Simpan hasil kalkulator ke file.
- Level 9: Buat class `Mahasiswa` dengan atribut dan method.
- Level 10: Tambah fitur simpan & load tugas ke file JSON.

---

> Dibuat dengan ❤️ oleh **Ludang Prasetyo Nugroho** — versi ini cocok untuk belajar mandiri, dosen, atau pelatihan profesional.
