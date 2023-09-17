"""
У любого продукта есть такие свойства: название, описание, цена, вес

Задания:
    1. Создайте класс продукта.
    2. Создайте экземпляр этого продукта и наполинте своими данными.
    3. Распечатайте о нем иформацию в таком виде: Информация о продукте: название, описание, цена, вес
"""


class Product:
    def __init__(self, name: str, description: str, price: int, weight: str) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.weight = weight

    def get_product_info(self) -> str:
        return f'Информация о продукте: {self.name}, {self.description}, {self.price}, {self.weight}'
        


if __name__ == '__main__':
    my_product = Product('ПрАтеин', 'С высоким содержанием белка', 4500, '5кг')
    print(my_product.get_product_info())
