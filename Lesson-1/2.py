sec = int(input("Введите время в секундах: "))
hh = str(sec // 3600)
mm = (sec // 60) % 60
ss = sec % 60
if mm < 10:
    mm = '0' + str(mm)
else:
    mm = str(mm)
if ss < 10:
    ss = '0' + str(ss)
else:
    ss = str(ss)
print(f"{hh}:{mm}:{ss}")
