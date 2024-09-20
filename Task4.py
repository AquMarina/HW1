# def user_input(text):
#     words = sorted(text.split())
#     max_length = len(max(words, key=len))
#     # print(words)
#     # print(max(words))
#     # print(max(words, key=len))
#     # print(max_length)
#     for i, word in enumerate(words, start=1):
#         print(f"{i}. {word:>{max_length}}")
#
# global_text = input('Введите текст: ')
# user_input(global_text)

# 2
# def unique_unicode(text: str) -> list[int]:
#     set_letters = sorted(set(text), reverse=True)
#     return list(map(ord, set_letters))
#
#
# texts = input('Введите текст: ')
# print(*unique_unicode(texts))

# 3
# def user_input_str(text: str) -> dict[str, int]:
#     start, stop = sorted(map(int, text.split()))
#     my_dict = {}
#
#     for key in range(start, stop +1):
#         my_dict[chr(key)] = key
#     return my_dict
#
#
# num1 = input('Введите строку: ')
# print(user_input_str(num1))

# 4
# def bubble_sort(list_1: list[int]):
#     for i in range(1, len(list_1)):
#         is_sorted = True
#         for j in range(len(list_1) -i):
#             if list_1[j] > list_1[j+1]:
#                 list_1[j], list_1[j+1] = list_1[j+1], list_1[i]
#                 is_sorted = False
#         if is_sorted:
#             return
#
#
# new_list = [1, 5, 8, 56, 23, 1, 6]
# print(new_list)
#
# bubble_sort(new_list)
# print(new_list)



