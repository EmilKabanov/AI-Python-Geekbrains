"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

my_list = []
while True:
    line = input("Введите что-нибудь: ")
    if line == '':
        print(my_list)
        break
    else:
        newline = line + '\n'
        my_list.append(newline)

    with open("file1.txt", "w") as file_obj:
        file_obj.writelines(my_list)

# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

#  my_list = ['Hello\n', 'Chao\n', 'Hola\n', 'Hola123\n']
# with open("test_2.txt", 'w+') as file_obj:
#     file_obj.writelines(my_list)
# lines = 0
# letters = 0

with open("file1.txt") as file_obj:
    content = file_obj.readlines()
    lines = len(content)
    n = 1
    print("\nЗадание 2")
    for line in content:
        letters = len(line) - 1
        print(f"Символов в строке {n}: {letters}")
        n += 1

    print(f"Всего строк в файле: {lines}")

