from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return "наносит удар мечом"

class Bow(Weapon):
    def attack(self):
        return "наносит удар из лука"

class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"Герой выбирает {weapon.__class__.__name__.lower()}.")

    def fight(self, monster):
        if self.weapon is None:
            print("Герой не выбрал оружие!")
            return

        print(f"Герой {self.weapon.attack()}.")
        monster.take_damage()

class Monster:
    def __init__(self):
        self.alive = True

    def take_damage(self):
        self.alive = False
        print("Монстр побежден!")

def main():
    fighter = Fighter("Герой")
    monster = Monster()

    # Боец выбирает меч
    fighter.change_weapon(Sword())
    fighter.fight(monster)

    # Создаем нового монстра для следующего боя
    monster = Monster()

    # Боец выбирает лук
    fighter.change_weapon(Bow())
    fighter.fight(monster)

if __name__ == "__main__":
    main()
