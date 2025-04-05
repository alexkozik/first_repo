class User:
    __next_id = 1
    __users_list = []

    def __init__(self, name):
        if any(user._name == name for user in User.__users_list):
            raise ValueError(f"Пользователь с именем '{name}' уже существует.")
        self._id = User.__next_id
        self._name = name
        self._access = 'user'
        User.__next_id += 1
        User.__users_list.append(self)

    @classmethod
    def get_users(cls):
        return cls.__users_list

    @classmethod
    def find_user_by_name(cls, name):
        for user in cls.__users_list:
            if user._name == name:
                return user
        return None

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

    def __repr__(self):
        return f"User(id={self._id}, name={self._name}, access={self._access})"

class Admin(User):
    def __init__(self, name):
        super().__init__(name)
        self._adm_access = 'admin'

    def __repr__(self):
        return f"Admin(id={self._id}, name={self._name}, access={self._access}, admin_access={self._adm_access})"

    def add_user(self, name):
        user = User(name)
        print(f"Пользователь {user} добавлен.")

    def remove_user(self, name):
        user = self.find_user_by_name(name)
        if user:
            user.destroy()
        else:
            print(f"Пользователь с именем {name} не найден.")

# Пример использования
admin = Admin("Витя")
admin.add_user("Саша")
admin.add_user("Паша")
admin.remove_user("Саша")
admin.remove_user("Костя")

# Вывод всех пользователей
print(User.get_users())
