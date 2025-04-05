# Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа
# и могут добавлять или удалять пользователя из системы.
#
# Требования:
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе:
# ID, имя и уровень доступа ('user' для обычных сотрудников).
# 2.Класс Admin: Этот класс должен наследоваться от класса User.
# Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
# Класс должен также содержать методы add_user и remove_user, которые позволяют добавлять и удалять пользователей
# из списка (представь, что это просто список экземпляров User).
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи.
# Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

class User:
    __next_id = 1
    __users_list = []

    def __init__(self, name):
        # Проверка на существование пользователя с таким именем
        if any(user._name == name for user in User.__users_list):
            raise ValueError(f"Пользователь с именем '{name}' уже существует.")
        self._id = User.__next_id
        self._name = name
        self._access = 'user'
        User.__next_id += 1
        User.__users_list.append(self)

    # переопределение метода возвращающего объект
    # без этого обЬекты возвращаются в таком виде     <__main__.User object at 0x7f82a0202f70>
    def __repr__(self):
        return f"User (id={self._id}, name={self._name}, access={self._access})"

    @classmethod
    def get_users(cls):
        return cls.__users_list

    @classmethod
    def find_user_by_name(cls, name):
        for user in cls.__users_list:
            if user._name == name:
                return user
        return None  # или выбросить исключение, если объект не найден

    def destroy(self):
        if self in User.__users_list:
            User.__users_list.remove(self)
            print(f"Пользователь {self._name} удален.")

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_access(self):
        return self._access


class Admin(User):
    def __init__(self, name):
        super().__init__(name)
        self._access = 'admin'

    def __repr__(self):
        return f"Admin(id={self._id}, name={self._name}, access={self._access})"

    def add_user(self, name):
        user = User(name)
        print(f"Пользовватель {user} добавлен")

    def remove_user(self, name):
        user = self.find_user_by_name(name)
        if user:
            user.destroy()
            # print(f"Пользователь с именем {user.} удален")
        else:
            print(f"Пользователь с именем {name} не найден.")


# Вывод всех созданных пользователей
def print_all_users():
    # print(User.get_users())
    all_users = User.get_users()
    for user in all_users:
        print(f'id: {user.get_id()}, name: {user.get_name()}, access: {user.get_access()} ')


# пример использования

admin = Admin("Витя")
admin.add_user("Саша")
admin.add_user("Паша")

print("Все созданные пользователи:")
print_all_users()

admin.remove_user("Саша")
admin.remove_user("Костя")

print("Все пользователи после удаления Саши:")
print_all_users()

admin.add_user("Костя")

print("Все пользователи после добавления Кости:")
print_all_users()
