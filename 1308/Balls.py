f1 = (input("Введите леттеры, 1 леттер - 1 шарик определенного цвета: "))
a1 = int(input("Скокма друзей? "))
f2 = []
max = 0
f1 = list(f1)
for i in f1:
    if ord(i) - 97 < 0 or ord(i) - 97 > 26:
        print("Вы вводите ерунду!")
        break
    else:
        f2.append(ord(i) - 97)
print(f2)
for i in f2:
    if i > max:
        max = i
f3 = [0] * (max + 1)
for i in f2:
    f3[i] += 1
f4 = list(enumerate(f3))
for i in f4:
    if i[1] != 0:
        print(chr(i[0] + 97), i[1])
if sorted(f3)[-1] > a1:
    print("No")
else:
    print("Yea")
