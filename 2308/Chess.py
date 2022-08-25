L = input("A если победил Антон, Г если победил Витя, через пробел: ")
L = list(map(ord, L.split()))
print(L)
K = [1] * (max(L) + 1)
# print(K)
D = []
for i in range(len(L)):
    if L[i] in D:
        # print(L.index(L[i]))
        K[L[i]] += 1
    else:
        D.append(L[i])
Result = {}
for i in D:
    print(chr(i), K[i])
    Result[chr(i)] = K[i]
print(max(Result))

# http://codeforces.com/problemset/problem/37/A