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