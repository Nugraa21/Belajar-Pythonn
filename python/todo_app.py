import json

deleted = self.tasks.pop(index - 1)
self.save_data()
print(f"🗑️ Tugas '{deleted['title']}' berhasil dihapus!")
except IndexError:
print("⚠️ Nomor tugas tidak valid!")


# -----------------------------
# MENU UTAMA PROGRAM
# -----------------------------
def menu(self):
while True:
print("""
==============================
📘 MENU TO-DO LIST
==============================
1. Tambah Tugas
2. Lihat Tugas
3. Tandai Selesai
4. Hapus Tugas
5. Keluar
==============================
""")


pilihan = input("Pilih menu (1-5): ")


if pilihan == '1':
title = input("Judul tugas: ")
desc = input("Deskripsi: ")
self.add_task(title, desc)


elif pilihan == '2':
self.show_tasks()


elif pilihan == '3':
self.show_tasks()
index = int(input("Masukkan nomor tugas yang selesai: "))
self.mark_done(index)


elif pilihan == '4':
self.show_tasks()
index = int(input("Masukkan nomor tugas yang akan dihapus: "))
self.delete_task(index)


elif pilihan == '5':
print("👋 Keluar dari aplikasi. Sampai jumpa!")
break


else:
print("⚠️ Pilihan tidak valid! Silakan coba lagi.")


# =============================
# MAIN PROGRAM
# =============================
if __name__ == "__main__":
app = TodoApp()
app.menu()