nap = input("Кол-во сока в %: ")
nap = list(map(int, nap.split()))
C = 0
for i in nap:
    C += i
print(C/len(nap))
# http://codeforces.com/problemset/problem/200/B