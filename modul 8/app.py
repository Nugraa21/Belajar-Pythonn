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