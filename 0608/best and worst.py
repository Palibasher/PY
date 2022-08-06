
sob = (input("Набранные очки, через пррбел: "))
sob = list(map(int, sob.split()))
balance = 0
ohwow = 0
PR = sob[0]
APR = sob[0]
for i in sob:
    if i > PR:
        PR = i
        ohwow += 1
    if i < APR:
        APR = i
        ohwow += 1
print(ohwow)
print(PR, APR)

# http://codeforces.com/problemset/problem/155/A
