# 1
# Вспомните какие модули вы уже проходили на курсе.
# Создайте файл, в котором вы импортируете встроенные
# в модуль функции под псевдонимами. (3-7 строк импорта).


# from  decimal import Decimal as D
# from random import randint as rnd
# from  math import  sqrt as sq
# from sys import argv as argument
# from sys import builtin_module_names as bmn

# 2
# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа:
# нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных
# границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

from random import randrange
from sys import argv
#
# def guess_the_numb(low_limit: int = 0, upper_limit: int = 100, try_limit: int = 10):
#     user_number = int(input(f'Введите число от {low_limit} до {upper_limit}: '))
#     rand_numb = randrange(low_limit, upper_limit + 1)
#     counter = 1
#     while counter <= try_limit:
#         if user_number == rand_numb:
#             return True
#         elif user_number < rand_numb:
#             user_number = int(input('Ваше число меньше загаданного, попробуйте ещё раз: '))
#         else:
#             user_number = int(input('Ваше число больше загаданного, попробуйте ещё раз: '))
#         counter += 1
#     return False
#
#
# if __name__ == '__main__':
#     print(guess_the_numb())

# 3
# Улучшаем задачу 2.
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры
# используйте генераторное выражение.


# def guess_the_numb(low_limit: int = 0, upper_limit: int = 100, try_limit: int = 10):
#     user_number = int(input(f'Введите число от {low_limit} до {upper_limit}: '))
#     rand_numb = randrange(low_limit, upper_limit + 1)
#     counter = 1
#     while counter <= try_limit:
#         if user_number == rand_numb:
#             return True
#         elif user_number < rand_numb:
#             user_number = int(input('Ваше число меньше загаданного, попробуйте ещё раз: '))
#         else:
#             user_number = int(input('Ваше число больше загаданного, попробуйте ещё раз: '))
#         counter += 1
#     return False
#
#
# if __name__ == '__main__':
#     _, *param = argv
#     print(guess_the_numb(*(int(n)for n in param)))

# 4
# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами
# отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана
# загадка или ноль, если попытки исчерпаны.

# def riddle(secret, answers, qty=3):
#     print(f'Угадай загадку: {secret}')
#     for tries in range(1, qty + 1):
#         answer = input('Введите ответ: ').lower()
#         if answer in answers:
#             return tries
#     return 0


# def storage():
#     puzzles = {'Зимой и летом - одним цветом': ['елка', 'ель', 'сосна'],
#               'Не лает, не кусает, в дом не пускает': ['замок', 'домофон'],
#               'Сидит дет, во сто шуб одет': ['лук', 'луковица']}
#     for key, value in puzzles.items():
#         result = riddle(key, value)
#         print(f'Угадал с {result} попытки' if result > 0 else 'Не угадал')
#
#
# if __name__ == '__main__':
#     storage()

# 5
# Добавьте в модуль с загадками функцию, которая хранит словарь
# списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать
# ей все свои загадки.


