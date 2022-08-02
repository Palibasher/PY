a = input("Введите массу трех толстяков через пробел:")
a = a.split()
a = list(map(int, a))
last = 0
for i in a:
    if i > 752 or i < 100:
        print(i, "неправильный вес толстяка")
        last = 0
        break
    elif last < i:
        last = i
if last != 0:
    print("Победа за толстяком с весом:", last)

