p_m = input("Состояние граждан через пробел: ")
p_m = list(map(int, p_m.split()))
maxi = max(p_m)
diff = 0
for i in p_m:
    diff_k = maxi - i
    diff += diff_k
print(diff)


# http://codeforces.com/problemset/problem/758/A