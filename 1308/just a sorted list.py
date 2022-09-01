cols = input("Диджиты через пробел: ")
cols = list(map(int, cols.split()))
cols = sorted(cols)
print(cols)

