viruchka = int(input("Укажите размер вашей выручки: "))
izderjki = int(input("Укажите размер издержек: "))
if viruchka > izderjki:
    print("Фирма прибыльна")
    pribil = viruchka - izderjki
    print('Прибыль: ', pribil)
    rentabelnost = (pribil / viruchka) * 100
    print(f"Рентабельность: {rentabelnost:.0f}%")
    sotrudnikov = int(input("Сколько у вас сотрудников: "))
    pribil_sotrudnika = pribil / sotrudnikov
    print(f"Прибыль на сотрудника: {pribil_sotrudnika:.2f}")
elif viruchka < izderjki:
    print("Фирма убыточна")
else:
    print("Фирма работает в ноль")
