# Создание базового класса Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Метод должен быть реализован в подклассе")

    def eat(self):
        print(f"{self.name} ест")

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, age={self.age})"


# Создание подклассов Bird, Mammal, и Reptile
class Bird(Animal):
    bird_sounds = {
        "курица": "ко-ко-ко",
        "петух": "ку-ка-реку",
        "гусь": "га-га-га",
        "воробей": "чик-чирик"
    }

    def make_sound(self):
        if self.name in self.bird_sounds:
            print(f"{self.name} издает звук {self.bird_sounds[self.name]}")
        else:
            print(f"{self.name} издает пока еще неопределенный в словаре звук")


class Mammal(Animal):
    mammal_sounds = {
        "кот": "мяу",
        "собака": "гав",
        "корова": "му",
        "коза": "меэ"
    }

    def make_sound(self):
        if self.name in self.mammal_sounds:
            print(f"{self.name} издает звук {self.mammal_sounds[self.name]}")
        else:
            print(f"{self.name} издает пока еще неопределенный в словаре звук")


class Reptile(Animal):
    reptile_sounds = {
        "змея": "шшшш",
        "кобра": "шшшшшш"
    }

    def make_sound(self):
        if self.name in self.reptile_sounds:
            print(f"{self.name} издает звук {self.reptile_sounds[self.name]}")
        else:
            print(f"{self.name} издает пока еще неопределенный в словаре звук")


# Полиморфизм с функцией animal_sound
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


# Создание классов для сотрудников

class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def make_function(self):
        raise NotImplementedError("Метод должен быть реализован в подклассе")

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, role={self.role})"


class ZooKeeper(Employee):
    def make_function(self):
        print(f"{self.name} кормит животных.")


class Veterinarian(Employee):
    def make_function(self):
        print(f"{self.name} лечит животных.")


# Полиморфизм с функцией make_function
def employee_function(employees):
    for employee in employees:
        employee.make_function()


# Создание класса Zoo с использованием композиции

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal} добавлен/о в зоопарк.")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee} принят в зоопарк.")

    def __repr__(self):
        return f"Zoo(name={self.name}, animals={self.animals}, employees={self.employees})"


# Пример использования
# Создание зоопарка и добавление животных и сотрудников
zoo = Zoo("Зоопарк №1")
zoo.add_animal(Bird("курица", 1))
zoo.add_animal(Bird("петух", 2))
zoo.add_animal(Bird("гусь", 3))
zoo.add_animal(Bird("воробей", 4))
zoo.add_animal(Bird("пингвин", 5))
zoo.add_animal(Mammal("кот", 1))
zoo.add_animal(Mammal("собака", 2))
zoo.add_animal(Mammal("корова", 3))
zoo.add_animal(Mammal("коза", 4))
zoo.add_animal(Mammal("лошадь", 5))
zoo.add_animal(Reptile("змея", 11))
zoo.add_animal(Reptile("гадюка", 15))
zoo.add_employee(ZooKeeper("Петр", "ZooKeeper"))
zoo.add_employee(Veterinarian("Светлана", "Veterinarian"))

# Вызов звуков животных
animal_sound(zoo.animals)

# Вывод обязанностей сотрудников
employee_function(zoo.employees)
