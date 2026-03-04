class Hero:
    def __init__(self, nama, hp_awal):
        self.nama = nama
        self.__hp = hp_awal

    def get_hp(self):
        return self.__hp

    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
            self.__hp = 0
        elif nilai_baru > 1000:
            self.__hp = 1000
        else:
            self.__hp = nilai_baru

    def diserang(self, damage):
        self.set_hp(self.get_hp() - damage)
        print(f"{self.nama} HP tersisa {self.get_hp()}")


# -- Uji Coba --
hero1 = Hero("Layla", 100)
hero1.set_hp(-50)
print(hero1.get_hp())

# Analisis 4
print(f"Mencoba akses paksa: {hero1._Hero__hp}")
