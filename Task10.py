# 1
# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.
# class Circumference:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def perimeter(self):
#         return 2 * 3,14 * self.radius
#
#     def area(self):
#         return  3,14 * self.radius ** 2
#
#
# circle = Circumference(25)
#
# print(f'{circle.radius = }')
# print(f'{circle.perimeter() = }')
# print(f'{circle.area() = }')

# 2
# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.

# class Rectangle:
#     def __init__(self, length, width=None):
#         self.length = length
#         if width == None:
#             self.width = length
#         else:
#             self.width = width
#
#     def perimeter(self):
#         return 2 * (self.length * self.width)
#
#     def area(self):
#         return self.length * self.width

# 3
# Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.

# class Person:
#     person_list = []
#
#     def __init__(self, name, surname, age, city):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.city = city
#         Person.person_list.append({
#             'name': self.name,
#             'surname': self.surname,
#             'age': self.age,
#             'city': self.city
#         })

    # def birthday(self):
    #     self.age += 1
    #
    # def full_name(self):
    #     return f'{self.name} {self.surname}'

#     def get_age(self):
#         return self.age
#
#     def get_city(self):
#         return self.city
#
#
# if __name__ == '__main__':
#     p1 = Person('Андрей', 'Черушин', 28, 'Курган')
#     print(p1.person_list)
#     print(p1.get_age())
#     print(p1.full_name())
#     p1.birthday()
#     print(p1.person_list)


# 4
# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# шестизначный идентификационный номер
# уровень доступа вычисляемый как остаток от деления суммы цифр id на семь

# class Person:
#     person_list = []
#
#     def __init__(self, name, surname, age, city):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.city = city
#         Person.person_list.append({
#             'name': self.name,
#             'surname': self.surname,
#             'age': self.age,
#             'city': self.city
#         })

    # def birthday(self):
    #     self.age += 1
    #
    # def full_name(self):
    #     return f'{self.name} {self.surname}'
    #
    # def get_age(self):
    #     return self.age
    #
    # def get_city(self):
    #     return self.city


# class Worker(Person):
#     def __init__(self, id_worker, name, surname, age, city):
#         super().__init__(name, surname, age, city)
#         if 100_000 <= id_worker <= 999_999:
#             self.id_worker = id_worker
#         else:
#             self.id_worker = 100_000
#         self.guard = self.id_worker % 7

#     def get_level_guard(self):
#         return self.guard
#
#
# if __name__ == '__main__':
#     p1 = Worker(0, 'Андрей', 'Черушин', 28, 'Курган')
#     print(p1.guard)
#     print(p1.get_level_guard())
#     print(p1.name)

# 5
# Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

# class Bird:
#     def __init__(self, name, age, weight, wing_span, beak_size):
#         self.name = name
#         self.age = age
#         self.weight = weight
#         self.wing_span = wing_span
#         self.beak_size = beak_size
#
#     def specific_bird(self):
#         return f'Особенности: {self.beak_size}, {self.wing_span}'


# class Mammal:
#     def __init__(self, name, age, weight, fangs, size):
#         self.name = name
#         self.age = age
#         self.weight = weight
#         self.fangs = fangs
#         self.size = size
#
#     def specific_mammal(self):
#         return f'Особенности: {self.size}, {self.fangs}'


# class Fish:
#     def __init__(self, name, age, weight, underwater, habitat):
#         self.name = name
#         self.age = age
#         self.weight = weight
#         self.underwater = underwater
#         self.habitat = habitat
#
#     def specific_fish(self):
#         return f'Особенности: {self.habitat}, {self.underwater}'
#
#
# if __name__ == '__main__':
    # p1 = Bird('Soika', '1r', '0,1kg', '0,5cm', '0,1cm')
    # p2 = Mammal('Leon', 'S-r', '7r', 'smol', 'True')
    # p3 = Fish('losos', '1r', '25cm', '50-70m', 'rive')
    #
    # print(p1.specific_bird())
    # print(p2.specific_mammal())
    # print(p3.specific_fish())

# 6
# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.

class Animal:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight


class Bird:
    def __init__(self, name, age, weight, wing_span, beak_size):
        super().__init__(name, age, weight)
        self.wing_span = wing_span
        self.beak_size = beak_size

    def specific_bird(self):
        return f'Особенности: {self.beak_size}, {self.wing_span}'


class Mammal:
    def __init__(self, name, age, weight, fangs, size):
        super().__init__(name, age, weight)
        self.fangs = fangs
        self.size = size

    def specific_mammal(self):
        return f'Особенности: {self.size}, {self.fangs}'


class Fish:
    def __init__(self, name, age, weight, underwater, habitat):
        super().__init__(name, age, weight)
        self.underwater = underwater
        self.habitat = habitat

    def specific_fish(self):
        return f'Особенности: {self.habitat}, {self.underwater}'


if __name__ == '__main__':
    p1 = Bird('Soika', '1r', '0,1kg', '0,5cm', '0,1cm')
    p2 = Mammal('Leon', 'S-r', '7r', 'smol', 'True')
    p3 = Fish('losos', '1r', '25cm', '50-70m', 'rive')

    print(p1.specific_bird())
    print(p2.specific_mammal())
    print(p3.specific_fish())