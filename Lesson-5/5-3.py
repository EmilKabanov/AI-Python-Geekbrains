"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

summa = 0
count = 0
persons = []
with open("file3.txt", "r") as file_obj:
    content = file_obj.readlines()
    for line in content:
        line = line.replace("\n", "")
        tokens = line.split(' - ')
        summa += int(tokens[1])
        count += 1
        if int(tokens[1]) < 20000:
            persons.append(tokens[0])
        result = summa / count
    print(f"Средняя зарплата: {round(result, 2)}")
    print(f"Меньше 20 000 получают: {persons}")