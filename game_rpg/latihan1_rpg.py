class Hero:
    # Constructor
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")


# -- Main Program --
hero1 = Hero("Layla", 100, 15)
hero2 = Hero("Zilong", 120, 20)

# Analisis 1
hero1.hp = 500
print(hero1.hp)

hero1.info()
hero2.info()
