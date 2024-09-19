# f = open('text_data.txt', 'a', encoding='utf-8')
# f.write('\nОкончание файла\n')
# f.close()

# f = open('bin_data', 'wb', buffering=64)
# f.write(b'x' * 1200)
# f.close()

# f = open('data.txt', 'wb')
# f.write('Привет, '.encode('utf-8') + 'мир!'.encode('cp1251'))
# f.close()
#
# f = open('data.txt', 'r', encoding='utf-8')
# print(list(f))
# f.close()
#
# f = open('data.txt', 'r', encoding='utf-8', errors='replace')
# print(list(f))
# f.close()

# Сэндвич
# s = input()
# print(s[::2] + s[1::2][::-1])

# with (
#         open('text_data.txt', 'r+', encoding='utf-8') as f1,
#         open('bin_data', 'rb') as f2,
#         open('data.txt', 'r', encoding='utf-8', errors='backslashreplace') as f3
# ):
#     print(list(f1))
#     print(list(f2))
#     print(list(f3))

# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     print(list(f))

# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     res = f.read()
#     print(f'Читаем первый раз\n{res}')
#     res = f.read()
#     print(f'Читаем второй раз\n{res}')

# SIZE = 100
# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     while res := f.read(SIZE):
#         print(res)

# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         print(line, end='')

# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         print(line[:-1])
#         print(line.replace('\n', ''))
# last = before = 0
# text = ['kdhbkbdbjkjd kdjnjbdkjn, lkdf.',
#         'kdjgkjbkdjnj kjdfvkjbnj',
#         'kdjbkjdbkdjgb skjbkjs.']
# size = 64
# with open('new_data.txt', 'r+', encoding='utf-8') as f:
    # for line in text:
    #     res = f.write(f'{line}\n')
    #     print(f'{res = }\n{len(line) = }')
    # f.writelines('\n'.join(text))
    # for line in text:
    #     # print(line, file=f)
    #     print(line, end='***\n##', file=f)
    # print(f.tell())
    # for line in text:
    #     f.write(f'{line}\n')
    #     print(f.tell())
    # print(f.tell())
    # while line := f.readline():
    #     last, before = f.tell(), last
    #     print(f'{last = }, {before = }')
    # print(f'{last = }, {before = }')
    # print(f'{f.seek(before, 0) = }')
    # f.write('\n'.join(text))
    # print(f.seek(before, 0))
    # print(f.truncate(size))

import os
from pathlib import Path
# print(os.getcwd())
# print(Path.cwd())
# os.chdir('../..')
# print(os.getcwd())
# print(Path.cwd())
#
# os.mkdir('dir/other_dir/new_os_dir')
# Path('some_dir/dir/new_path_dir').mkdir(parents=True)

# 1
# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
#
# Минимальное число - -1000, максимальное - +1000.
# Количество строк и имя файла передаются как аргументы функции.
from random import randint, uniform, choice

# MIN_NUM = -1000
# MAX_NUM = 1000


# def addition_num(name, inlines):
#
#     with open(name, 'a', encoding='utf-8') as f:
#         for _ in range(inlines):
#             f.write(f'{randint(MIN_NUM, MAX_NUM)} | {uniform(MIN_NUM, MAX_NUM)}\n')
#
#
# lines = int(input('Введите количество строк: '))
# file_name = input('Введите имя файла: ')
#
# if __name__ == '__main__':
#     addition_num(file_name, lines)

# 2
# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# Полученные имена сохраните в файл.

from pathlib import Path

# VOWELS = 'eyuioa'
# CONSONANTS = 'HFKDeHGJ'
# MIN_LEN = 4
# MAX_LEN = 7


# def generate_names(filename: str | Path, names_count):
#     with open(filename, 'a', encoding='utf-8') as f:
#         for _ in range(names_count):
#             name = ''
#             cur_letter = choice((-1, 1))
#             for _ in range(randint(MIN_LEN, MAX_LEN)):
#                 if cur_letter == -1:
#                     name += choice(VOWELS)
#                 else:
#                     name += choice(CONSONANTS)
#                 cur_letter *= -1
#             f.write(name.capitalize() + '\n')


# if __name__ == '__main__':
#     generate_names(Path('name.txt'), 10)

# def generate_names(filename: str | Path, names_count: int):
#     with open(filename, 'a', encoding='utf8') as f:
#         for _ in range(names_count):
#             cur_letter = choice((-1, 1))
#             name = ''.join(
#                 choice(VOWELS) if (cur_letter:=cur_letter*(-1)) == -1 else choice(CONSONANTS) for _ in range(randint(MIN_LEN, MAX_LEN))
#             )
#             f.write(name.capitalize() + '\n')

# 3
# Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# При достижении конца более короткого файла,
# возвращайтесь в его начало.