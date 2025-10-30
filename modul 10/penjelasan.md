
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