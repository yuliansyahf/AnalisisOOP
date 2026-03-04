from abc import ABC, abstractmethod

class GameUnit(ABC):
    @abstractmethod
    def serang(self, target):
        pass

    @abstractmethod
    def info(self):
        pass


class Hero(GameUnit):
    def __init__(self, nama):
        self.nama = nama

    def serang(self, target):
        print(f"Hero {self.nama} menyerang {target}")

    def info(self):
        print(f"Saya Hero {self.nama}")


class Monster(GameUnit):
    def __init__(self, jenis):
        self.jenis = jenis

    def serang(self, target):
        print(f"Monster {self.jenis} menggigit {target}")

    def info(self):
        print(f"Saya Monster {self.jenis}")


h = Hero("Alucard")
m = Monster("Serigala")

h.info()
m.info()
