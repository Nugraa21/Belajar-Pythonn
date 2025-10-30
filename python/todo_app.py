import json
import os

# =============================
#  KELAS UTAMA UNTUK TO-DO APP
# =============================
class TodoApp:
    def __init__(self, filename="data.json"):
        self.filename = filename
        self.tasks = []
        self.load_data()

    # -----------------------------
    #  MEMUAT DATA DARI FILE JSON
    # -----------------------------
    def load_data(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    self.tasks = json.load(f)
            except json.JSONDecodeError:
                self.tasks = []
        else:
            self.tasks = []

    # -----------------------------
    #  MENYIMPAN DATA KE FILE JSON
    # -----------------------------
    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    # -----------------------------
    #  MENAMBAHKAN TUGAS BARU
    # -----------------------------
    def add_task(self, title, description):
        task = {
            "title": title,
            "description": description,
            "done": False
        }
        self.tasks.append(task)
        self.save_data()
        print(f"✅ Tugas '{title}' berhasil ditambahkan!")

    # -----------------------------
    #  MENAMPILKAN SEMUA TUGAS
    # -----------------------------
    def show_tasks(self):
        if not self.tasks:
            print("\n📭 Belum ada tugas yang disimpan.\n")
            return

        print("\n📋 Daftar Tugas:")
        for i, task in enumerate(self.tasks, start=1):
            status = "✔️" if task["done"] else "❌"
            print(f"{i}. {task['title']} - {status}\n   Deskripsi: {task['description']}")

    # -----------------------------
    #  MENANDAI TUGAS SELESAI
    # -----------------------------
    def mark_done(self, index):
        try:
            self.tasks[index - 1]["done"] = True
            self.save_data()
            print("🎯 Tugas berhasil ditandai selesai!")
        except IndexError:
            print("⚠️ Nomor tugas tidak valid!")

    # -----------------------------
    #  MENGHAPUS TUGAS
    # -----------------------------
    def delete_task(self, index):
        try:
            deleted = self.tasks.pop(index - 1)
            self.save_data()
            print(f"🗑️ Tugas '{deleted['title']}' berhasil dihapus!")
        except IndexError:
            print("⚠️ Nomor tugas tidak valid!")

    # -----------------------------
    #  MENU UTAMA PROGRAM
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
                try:
                    index = int(input("Masukkan nomor tugas yang selesai: "))
                    self.mark_done(index)
                except ValueError:
                    print("⚠️ Masukkan angka yang valid!")

            elif pilihan == '4':
                self.show_tasks()
                try:
                    index = int(input("Masukkan nomor tugas yang akan dihapus: "))
                    self.delete_task(index)
                except ValueError:
                    print("⚠️ Masukkan angka yang valid!")

            elif pilihan == '5':
                print("👋 Keluar dari aplikasi. Sampai jumpa!")
                break

            else:
                print("⚠️ Pilihan tidak valid! Silakan coba lagi.")


# =============================
#  MAIN PROGRAM
# =============================
if __name__ == "__main__":
    app = TodoApp()
    app.menu()
