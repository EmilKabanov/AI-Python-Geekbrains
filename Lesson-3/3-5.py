"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""

def my_sum():
    res = 0
    while True:
        numbers = input('Введите несколько чисел через пробел или q чтобы выйте: ').split()
        for i in numbers:
            try:
                if i == 'q':
                    print(f'Итоговая сумма: {res}')
                    return
                else:
                    res += int(i)
            except ValueError:
                print('Вы должны ввести число или q')
        print(f'Текущая сумма: {res}')

my_sum()