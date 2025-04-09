import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        damage = random.randint(10, self.attack_power)
        other.health -= damage
        print(f"{self.name} атакует {other.name}, нанося {damage} единиц урона. У {other.name} осталось {other.health} здоровья.")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player_name, computer_name):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        round_number = 1
        while self.player.is_alive() and self.computer.is_alive():
            print(f"\nРаунд {round_number}:")
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"{self.computer.name} повержен! {self.player.name} побеждает!")
                break
            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.player.name} повержен! {self.computer.name} побеждает!")
                break
            round_number += 1

# Пример использования
game = Game("Игрок", "Компьютер")
game.start()