# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

goods = int(input("Сколько товаров вы хотите добавить? "))
n = 1
my_dict = []
my_list = []
my_analys = {}
while n <= goods:
    print("Товар", n)
    my_dict = dict({'название': input("Введите название товара "), 'цена': input("Введите цену "),
                    'количество': input('Введите количество '), 'eд': input("Введите единицу измерения ")})
    my_list.append((n, my_dict))
    n += 1
print(my_list)
for good in my_list:
    for key, value in good[1].items():
        if key in my_analys:
            my_analys[key].append(value)
        else:
            my_analys[key] = [value]
print(my_analys);


