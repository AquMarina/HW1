# 1
# Создайте функцию-замыкание, которая запрашивает два целых числа:
# от 1 до 100 для загадывания,
# от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.

from random import randint


# def num_riddles(num=randint(1, 100), count=10):
#     def num_endeavors():
#         for i in range(count):
#             user_input_num = int(input('Введите число от 1 до 100: '))
#             print(f"Оставшееся количество попыток - {count - i}")
#             if user_input_num == num:
#                 return f'Поздравляю число угаданно - {num}, за сколько попыток {i}'
#             elif user_input_num > num:
#                 print('Искомое число меньше!')
#             elif user_input_num < num:
#                 print('Искомое число больше!')
#         return 'Закончились попытки'
#     return num_endeavors
#
#
# if __name__ == '__main__':
#     func_num_game = num_riddles(23, 5)
#     print(func_num_game())
#     print()
#     print(func_num_game())
#     print()
#     func_game_2 = num_riddles(42, 7)
#     print(func_game_2())
#     print()
#     print(func_game_2())

# 2
# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами из диапазонов.

from random import randint
from typing import Callable


# def num_control(func: Callable):
#     NUMBER_MIN = 1
#     NUMBER_MAX = 100
#     COUNT_MIN = 1
#     COUNT_MAX = 10
#
#     def wrapper(num, count, *args, **kwargs):
#         if num < NUMBER_MIN or num > NUMBER_MAX:
#             num = randint(NUMBER_MIN, NUMBER_MAX)
#             print(f'{num= }')
#         if count < COUNT_MIN or count > COUNT_MAX:
#             count = randint(COUNT_MIN, COUNT_MAX)
#             print(f'{count= }')
#         return func(num, count, *args, **kwargs)
#
#     return wrapper


# @num_control
# def num_endeavors(num, count):
#     for i in range(count):
#         user_input_num = int(input('Введите число от 1 до 100: '))
#         print(f"Оставшееся количество попыток - {count - i}")
#         if user_input_num == num:
#             return f'Поздравляю число угаданно - {num}, за сколько попыток {i}'
#         elif user_input_num > num:
#             print('Искомое число меньше!')
#         elif user_input_num < num:
#             print('Искомое число больше!')
#     return 'Закончились попытки'
#
#
# if __name__ == '__main__':
#     print(num_endeavors(500, 5))

# 3
