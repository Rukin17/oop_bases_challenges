"""
У нас есть класс TextProcessor, который содержит в себе методы для работы с текстом.

Задания:
    1. Создайте класс AdvancedTextProcessor, который будет наследником TextProcessor.
    2. Переопределите метод summarize у класса AdvancedTextProcessor таким образом, чтобы он возвращал еще и количество слов в тексте.
       Например: Total text length: 67, total number of words in the text: 10
    3. Создайте экземпляры каждого из двух классов и у каждого экземпляра вызовите все возможные методы.
"""


class TextProcessor:
    def __init__(self, text):
        self.text = text

    def to_upper(self):
        return self.text.upper()

    def summarize(self):
        return f'Total text length: {len(self.text)}'


class AdvancedTextProcessor(TextProcessor):
    def summarize(self):
        count = 0
        for _ in self.text.split():
            count += 1

        return f'{super().summarize()}, total number of words in the text: {count}'


if __name__ == '__main__':
    my_text_1 = TextProcessor('Mein herz brennt')
    print(my_text_1.to_upper())
    print(my_text_1.summarize())
    print()
    my_text = AdvancedTextProcessor('А у вас, молоко убежало!')
    print(my_text.summarize())
