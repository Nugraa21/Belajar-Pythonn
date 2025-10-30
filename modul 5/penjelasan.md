
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
