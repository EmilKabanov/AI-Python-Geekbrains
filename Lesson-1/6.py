result = int(input("Ваш результат в первый день (число в километрах): "))
final_result = int(input("Желаемый результат (число в километрах): "))
n = 1
while result < final_result:
    print(f"{n}-й день: {result:.1f}км")
    result = result + (result / 10)
    if result > final_result:
        print(f"Вы достигните результата на {n}-й день")
    n += 1

