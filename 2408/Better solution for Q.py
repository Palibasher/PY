def print_mat2(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end="")
        print()
x = int(input("X: ")) - 1
y = int(input("Y: ")) - 1
doska = [[" . " for _ in range(8)] for a in range(8)]
for i, C in enumerate(doska):
    for j, R in enumerate(C):
        print(j, R)
        if i + j == x + y or i - j == x - y:
            doska[i][j] = " * "
        elif i == x or j == y:
            doska[i][j] = " * "
doska[x][y] = " Q "
print()
print_mat2(doska)