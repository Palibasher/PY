podk = input("4 цвета: ")
podk = list(map(int, podk.split()))
p2 = []
for i in podk:
    if i not in p2:
        p2.append(i)
print((len(podk)) - len(p2))

# http://codeforces.com/problemset/problem/228/A