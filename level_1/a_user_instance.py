"""
Задания:
    1. Создайте экземпляр класса юзера, наполнив любыми данными.
    2. Распечатайте информацию о нем в таком виде: Информация о пользователе: имя, юзернэйм, возраст, телефон.
"""


class User:
    def __init__(self, name: str, username: str, age: int, phone: str):
        self.name = name
        self.username = username
        self.age = age
        self.phone = phone
        


if __name__ == '__main__':
    my_user = User('Jhon', 'Cena', 42, '404')
    print(f'Информация о пользователе: {my_user.name}, {my_user.username}, {my_user.age}, {my_user.phone}')
