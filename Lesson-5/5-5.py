"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

def my_sum():
    try:
        with open('file5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()
            summary = (sum(map(int, my_numb)))
            print(f"Числа записаны в файл file5.txt. Сумма числе в файле = {summary}")
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильное число. Ошибка ввода-вывода')
my_sum()