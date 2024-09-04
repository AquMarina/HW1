# 1
# Напишите программу, которая рисует прямоугольную рамку с помощью
# символьной графики. Для вертикальных линий используйте символ
# вертикального штриха (|), а для горизонтальных — дефис (-). Пусть ширину и
# высоту рамки определяет пользователь.

width = int(input("Введите ширину рамки: "))
height = int(input("Введите высоту рамки: "))
for line in range(height + 1):
    for col in range(width + 1):
        if col == width or col == 0:
            print('|', end='')
        elif line == height or line == 0:
            print('-', end='')
        else:
            print(' ', end='')
    print()


# 2
# Треугольник
# Треугольник существует только тогда, когда сумма любых двух его сторон
# больше третьей. Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если
# хотя бы в одном случае отрезок окажется больше суммы двух других, то
# треугольника с такими сторонами не существует. Отдельно сообщить является
# ли треугольник разносторонним, равнобедренным или равносторонним.
a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))
#
if a < b+c or b < a+c or c < a+b:
    if a == b or a == c or b == c:
        print('Треугольник равнобедренный!')
    elif a == b == c:
        print('Треугольник равносторонний!')
    else:
        print('Треугольник разносторонний!')
else:
    print('Треугольника с такими сторонами не существует!')

# 3
# Напишите программу, которая считает количество простых чисел в заданной
# последовательности и выводит ответ на экран.
# Простое число делится только на себя и на единицу. Последовательность
# задаётся при помощи вызова ввода (input) на каждой итерации цикла. Одна
# итерация — одно число.
count = 0
num1 = int(input('Введите количество чисел в последовательности: '))
for i in range(num1):
    num2 = int(input('Введите число: '))
    if num2 > 1:
        for divider in range(2, num2):
            if num2 % divider == 0:
                break
        else:
            count += 1
print('Количество простых чисел:', count)

# 4
# Яма
# Представьте, что вы разрабатываете компьютерную игру с текстовой графикой.
# Вам поручили создать генератор ландшафта. Напишите программу, которая
# получает на вход число N и выводит на экран числа в виде ямы.

depth = int(input('Введите глубину ямы: '))
for line in range(depth):
    for left_number in range(depth, depth - line - 1, -1):
        print(left_number, end="")
    point_count = 2 * (depth - line - 1)
    print("." * point_count, end="")
    for right_number in range(depth - line, depth + 1):
        print(right_number, end="")
    print()

# 5
# Игра «Компьютер угадывает число»
# Мальчик загадывает число между 1 и 100 (включительно). Компьютер может
# спросить у мальчика: «Твоё число равно, меньше или больше, чем число N?»,
# где N — число, которое хочет проверить компьютер. Мальчик отвечает одним из
# трёх чисел: 1 — равно, 2 — больше, 3 — меньше.
# Напишите программу, которая с помощью цепочки таких вопросов и ответов
# мальчика угадывает число.
# Дополнительно: сделайте так, чтобы можно было гарантированно угадать
# число за семь попыток.

left, right = 0, 101
count = 0
while True:
  n = (left + right) // 2
  print('Твоё число равно, больше или меньше', n, '?')
  num = int(input('1 — равно, 2 — больше, 3 — меньше: '))
  count += 1
  if num == 1:
    print('Угадали число! Количество попыток:', count)
    break
  elif num == 2:
    left = n
  else:
    right = n
