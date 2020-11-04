"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"На ноль делить нельзя!")


input_divider = int(input("Введите делимое: "))
input_denominator = int(input("Введите делитель: "))
print(DivisionByNull.divide_by_null(input_divider, input_denominator))
# print(DivisionByNull.divide_by_null(10, 0))
# print(DivisionByNull.divide_by_null(10, 0.1))
