"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

#import json
import re

subj = {}
with open('file6.txt', 'r') as lines:
    for line in lines:
        subject, data = line.split(':')
        #print("Предмет:", subject)
        values = data.split()
        #print(values)
        hours = []
        for value in values:
            if any(map(str.isdigit, value)):
                #print('Значение: ', value)
                hours.append(value)
        total_hours = []
        for hour in hours:
            #print('Часов: ', hour)
            hour = re.sub("\D", "", hour)
            #print('Часов - только цифры:', hour)
            total_hours.append(hour)
            total_hours = list(map(int, total_hours))
            sum_hours = sum(total_hours)
        print("Предмет:", subject)
        print('Часов - всего:', sum_hours)
        subj[subject] = sum_hours
    print(f'Общее количество часов по предметам:\n {subj}')