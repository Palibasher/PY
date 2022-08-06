
sob = (input("События через пробел: "))
sob = list(map(int, sob.split()))
balance = 0
shit = 0
for i in sob:
    if i > 0:
        balance = balance + i
    elif i < 0:
        balance = balance + i
        if balance < 0:
            shit -= i
            balance = 0


print(shit)

# http://codeforces.com/problemset/problem/155/A