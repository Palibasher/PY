a = []
b = 5
for i in range(b):
    a.append(list(map(int, input().split())))

for colums in range(b):
    for rows in range(b):
        print(a[rows][colums], end=" ")
    print()

