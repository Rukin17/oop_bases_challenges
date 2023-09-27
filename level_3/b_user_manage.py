"""
У нас есть класс UserManager, который содержит в себе спискок юзернэймов пользователей и может расширять этот список.

Задания:
    1. Создайте класс AdminManager, который будет наследником UserManager.
       У него должен быть свой уникальный метод ban_username, который по переданному в него юзернэйму будет удалять
       юзернэйм из списка. Если такого юзернэйма в списке нет - должно печататься сообщение: "Такого пользователя не существует."
    2. Создайте класс SuperAdminManager, который будет наследником AdminManager.
       У него должен быть свой уникальный метод ban_all_users, который будет удалять все юзернэймы из списка.
    3. Создайте экземпляры каждого из трех классов и у каждого экземпляра вызовите все возможные методы.
"""


class UserManager:
    def __init__(self):
        self.usernames = []

    def add_user(self, username: str):
        self.usernames.append(username)

    def get_users(self):
        return self.usernames


class AdminManager(UserManager):
    def ban_username(self, name: str):
        if name not in self.get_users():
            print('Такого пользователя не существует')
        else:
            self.get_users().remove(name)


class SuperAdminManager(AdminManager):
    def ban_all_users(self):
        self.usernames = []



if __name__ == '__main__':
    users = UserManager()
    users.add_user('Jay')
    users.add_user('Dexter')
    users.add_user('Mike')
    users.add_user('Silvername')
    print(users.get_users())

    ban_user = AdminManager()
    ban_user.add_user('Mike')
    ban_user.add_user('Silvername')
    ban_user.ban_username('Mike')
    ban_user.ban_username('Jay')
    print(ban_user.get_users())

    
    all_ban = SuperAdminManager()
    all_ban.add_user('Jay')
    all_ban.add_user('Dexter')
    all_ban.add_user('Mike')
    all_ban.ban_username('Tomatos')
    print(all_ban.get_users())

    all_ban.ban_all_users()
    print(all_ban.get_users())

