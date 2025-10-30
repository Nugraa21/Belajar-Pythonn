
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
