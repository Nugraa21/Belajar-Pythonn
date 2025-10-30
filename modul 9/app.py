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