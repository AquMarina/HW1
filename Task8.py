# 1
# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

# import json
# from pathlib import Path
# from pprint import pprint
#
#
# def file_to_json(file: Path):
#     data = {}
#     with open(file, 'r', encoding="utf-8") as f_read:
#         for line in f_read:
#             name, number = line.split(' - ')
#             data[name.capitalize()] = number
#         pprint(data)
#     with open(file.stem + '.json', 'w', encoding='utf-8') as f_write:
#         json.dump(data, f_write, ensure_ascii=False, indent=2)
#
#
# if __name__=="__main__":
#     file_to_json(Path('file_new.txt'))

# 2
# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.

# import json
# from pathlib import Path
#
#
# def set_users(file: Path) -> None:
#     unique_id = set()
#     if not file.is_file():
#         data = {str(level): {} for level in range(1, 8)}
#     else:
#         with open(file, 'r', encoding='utf-8') as f_r:
#             data = json.load(f_r)
#             for dict_id in data.values():
#                 unique_id.update(dict_id)
#             print(unique_id)
#     print(data)
#
#     while True:
#         user_name = input('Введите имя: ')
#
#         if not user_name:
#             break
#         user_id = input('Введите id: ')
#         user_level = input('Введите уровень: ')
#
#         if user_id not in unique_id and user_level in data:
#             data[user_level][user_id] = user_name
#             unique_id.add(user_id)
#             with open(file, 'w', encoding='utf-8') as f_w:
#                 json.dump(data, f_w, ensure_ascii=False, indent=2)
#         else:
#             print('Неправильный ввод!')
#
#
# if __name__ == '__main__':
#     set_users(Path('users.json'))


# 3
# Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
# import csv
# import json
# from pathlib import Path
#
#
# def json_to_csv(file):
#     with open(file, 'r', encoding="utf-8") as f_reader:
#         data = json.load(f_reader)
#
#     rows = []
#     for level, dict_id in data.items():
#         for id, name in dict_id.items():
#             rows.append({"level": level, "id": id, "name": name})
#     with open(f"{file.stem}.csv", "w", newline="", encoding="utf-8") as f_writer:
#         csv_write = csv.DictWriter(f_writer, fieldnames=["level", "id", "name"], dialect="excel-tab")
#         csv_write.writeheader()
#         csv_write.writerows(rows)
#
#
# if __name__ == '__main__':
#     json_to_csv(Path('users.json'))