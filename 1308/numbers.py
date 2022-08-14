f1 = (input("Диджиты через пробел: "))
max = 0
co = 0
f1 = list(map(int, f1.split()))
for i in f1:
    if i > max:
        max = i
f2 = [0] * (max + 1)
for i in f1:
    f2[i] += 1
f3 = list(enumerate(f2))
for i in f3:
    if i[1] != 0:
        print(i[0], i[1])

