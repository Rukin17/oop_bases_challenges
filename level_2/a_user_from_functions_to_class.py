""""
У нас есть функции для работы с пользователем, но хочется работать с ним через класс.

Задания:
    1. Создайте класс User и перенесите всю логику работы с пользователем туда.
"""

def generate_short_user_description(username: str, user_id: int, name: str):
    return f'User with id {user_id} has {username} username and {name} name'


class User:
    def __init__(self, user_id: int, username: str, name: str) -> None:
        self.user_id = user_id
        self.username = username
        self.name = name

    def make_username_capitalized(self):
        return self.username.capitalize()
    
    def make_username_capitalized(self):
        return self.username.capitalize()
