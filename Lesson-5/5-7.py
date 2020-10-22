"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json
profit = {}
pr = {}
prof = 0
average_profit = 0
i = 0
with open('file7.txt', 'r') as file:
    for line in file:
        name, firm, income, damages = line.split()
        profit[name] = int(income) - int(damages)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        average_profit = prof / i
        print(f'Средняя прибыль - {average_profit:.2f}')
    else:
        print(f'Прибыль отсутсвует, все работают в убыток')
    pr = {'Средняя прибыль': round(average_profit)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('file7.json', 'w', encoding="utf-8") as write_js:
    json.dump(profit, write_js, ensure_ascii=False)

    js_str = json.dumps(profit, ensure_ascii=False)
    print(f'Создан файл file7.json со следующим содержимым: \n '
    f' {js_str}')