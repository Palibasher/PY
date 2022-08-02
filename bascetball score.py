c, p = 0, 0
z = 1
L = [int(input("Колличество очков первой комманды в четверти №{} ".format(z+a))) for a in range(4)]
V = [int(input("Колличество очков второй комманды в четверти №{} ".format(z+a))) for a in range(4)]
for i in L:
    c += i
for n in V:
    p += n
if p > c:
    print("Вторая комманда победила со счетом", p, ":", c)
elif c > p:
    print("Первая комманда победила со счетом", c, ":", p)
else:
    print("Ничья")