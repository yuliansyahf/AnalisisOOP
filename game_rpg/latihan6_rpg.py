class Hero:
    def __init__(self, nama):
        self.nama = nama

    def serang(self):
        print("Hero menyerang")


class Mage(Hero):
    def serang(self):
        print(f"{self.nama} melempar Fireball!")


class Archer(Hero):
    def serang(self):
        print(f"{self.nama} memanah!")


class Fighter(Hero):
    def serang(self):
        print(f"{self.nama} menebas!")


class Healer(Hero):
    def serang(self):
        print(f"{self.nama} menyembuhkan teman!")


pasukan = [
    Mage("Eudora"),
    Archer("Miya"),
    Fighter("Zilong"),
    Healer("Estes")
]

print("--- PERANG DIMULAI ---")
for p in pasukan:
    p.serang()
