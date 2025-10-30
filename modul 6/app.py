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