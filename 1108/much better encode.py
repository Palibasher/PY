f1 = input("Ввести компрессию: ")
f1 = [int(a) for a in str(f1)]
f2 = []
for i in range(len(f1) - 1):
    if i % 2 == 0:
        print(f1[i], f1[i + 1])
        for z in range(f1[i]):
            f2.append(f1[i + 1])
print(f2)