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