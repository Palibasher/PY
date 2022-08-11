f1 = input("Введите число 1: ")
f1 = [int(a) for a in str(f1)]
f2 = input("Введите число 2: ")
f2 = [int(a) for a in str(f2)]
f3 = list(zip(f1, f2))
fr = []
for i in f3:
    if i[0] + i[1] == 1:
        fr.append(1)
    else:
        fr.append(0)
fr = [str(a) for a in fr]
print("".join(fr))

# http://codeforces.com/problemset/problem/61/A