def print_mat(a):
    for arr in range(len(a)):
        print(a[arr])
def print_mat2(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end="")
        print()
y = int(input("Y: ")) - 1
x = int(input("X: ")) - 1
doska = [" . " for a8 in range(72)]
a = []
A = []
stand = 8
for _ in doska:
    if stand > 0:
        a.append(_)
        stand -= 1
    else:
        A.append(a)
        stand = 8
        a = []
A[x].pop(y)
A[x].insert(y, " @ ")
k = []
for i in A[x]:
    if i == ' . ':
        k.append(" * ")
    else:
        k.append(" @ ")
A.pop(x)
A.insert(x, k)
for i in range(len(A)):
    if i != x:
        A[i].pop(y)
        A[i].insert(y, " * ")
for i in range(len(A)):
    for j in range(len(A[i])):
        if i + j == x + y or i - j == x - y:
            A[i][j] = " * "
A[x][y] = " @ "

print_mat2(A)
