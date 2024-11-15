# Домашнее задание по теме "Создание функций на лету"

# 1 - lambda функция
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x,y: list(x) == list(y), first, second)))


# 2 - Замыкание

def get_advanced_writer(file_name):

    def write_everything(*data_set):
        file = open(file_name, 'w', encoding="utf-8")
        for i in range(len(data_set)):
            file.write(f'{data_set[i]}\n')
        file.close()
        return

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# 3 - Метод __call__

from random import choice


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


# Ваш класс здесь
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())