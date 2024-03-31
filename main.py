class User:
    def __init__(self, user_id, name, access_level='user'):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = access_level

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, access_level='admin')
        self.__users = []

    def add_user(self, user):
        self.__users.append(user)
        print(f'Пользователь {user.get_name()} добавлен в систему.')

    def remove_user(self, user_id):
        for user in self.__users:
            if user.get_user_id() == user_id:
                self.__users.remove(user)
                print(f'Пользователь {user.get_name()} удален из системы.')
                return
        print('Пользователь с указанным ID не найден.')

    def list_users(self):
        print('Список пользователей в системе:')
        for user in self.__users:
            print(f'ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}')


user1 = User(1, 'Пушкин Александр')
user2 = User(2, 'Толстой Лев')
user3 = User(3, 'Гоголь Николай')

admin = Admin(0, 'Администратор')

admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)

admin.remove_user(2)

admin.list_users()
