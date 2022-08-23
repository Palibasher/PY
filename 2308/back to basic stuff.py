L = input("Введите высоту башен: ")
L = list(map(int, L.split()))
K = [1] * (max(L) + 1)
print(K)
D = []
for i in range(len(L)):
    if L[i] in D:
        # print(L.index(L[i]))
        K[L[i]] += 1
    else:
        D.append(L[i])
for i in D:
    print(i, K[i])
print(len(D))
print(f"Самая высокая башня будет {max(K)} блоков высотой, всего башенок будет {len(D)}")

# http://codeforces.com/problemset/problem/37/A