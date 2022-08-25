from random import randint
def print_mat2(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(f"| {a[i][j]} |", end="")
        print()
r1 = randint(3, 5)
print(r1)
table = [[randint(1, 9) for _ in range(r1)] for a in range(r1)]
table = [[8,1,6],[3,5,7],[4,9,2]]
print_mat2(table)
Rows = []
Cols = []
Diag = []
Diag2 = []
Timer = []
for i, j in enumerate(table):
    Rows.append(sum(j))
    for x, y in enumerate(j):
        Timer.append(table[x][i])
        if len(Timer) >= 3:
            Cols.append(sum(Timer))
            Timer = []
        if x - i == 0:
            Diag.append(table[x][i])
        if x + i == r1 - 1:
            Diag2.append(table[x][i])
for i in range(3):
    if Rows[i] == Cols[i] == sum(Diag) == sum(Diag2):
        print("oh wow")
    else:
        print("oh no")
print(Rows)
print(Cols)
print(sum(Diag))
print(sum(Diag2))