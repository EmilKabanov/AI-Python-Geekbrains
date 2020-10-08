num = int(input("Введите целое положительное число: "))
result = num % 10
num = num // 10
while num > 0:
    if num % 10 > result:
        result = num % 10
    num = num // 10
print(result)
