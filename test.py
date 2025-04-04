class Car:
    def __init__(self, make, model):
        self.public_make = make  # Открытый атрибут
        self._protected_model = model  # Защищенный атрибут
        self.__private_year = 2022  # Приватный атрибут

    def public_method(self):
        return f"Это открытый метод. Машина: {self.public_make} {self._protected_model}."

    def _protected_method(self):
        return "Это защищенный метод."

    def __private_method(self):
        return "Это приватный метод."


class ElectricCar(Car):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size

    def get_details(self):
        # Можно обратиться к открытому и защиценному атрибуту, но не к приватному
        details = f"{self.public_make} {self._protected_model}, battery size: {self.battery_size} kWh."
        # Нельзя напряную обратиться к __ private_method и __ private_year
        return details


# Создание экземпляра ElectricCar
tesla = ElectricCar(make='Tesla', model='Model S', battery_size=100)

# Доступ к открытому атрибуту и методу:
print(tesla.public_make)
print(tesla.public_method())

# Доступ к защищённому атрибуту (не рекомендуется, но возможно):
print(tesla._protected_model)
print(tesla._protected_method())

# # Доступ к приватному атрибуту:
# print(tesla.__private_year)

# Доступ к приватному атрибуту через mangling:
# При такой записи получается, что через объект класса мы заходим в определенный класс и берем у него определенный атрибут.
# Это не совсем правильно, немного нарушает законы инкапсуляции и не принято в среде программистов.
print(tesla._Car__private_year)
