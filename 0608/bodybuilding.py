r = int(input("Повторы: "))
e = input("Подходы: ")
e = list(map(int, e.split()))
for i in range(len(e)):
    e[i] = r * e[i]
c = (e[::3])
b = (e[1::3])
w = (e[2::3])
def sum(n):
    b = 0
    for i in n:
        b += i
    return b
c, b, w = sum(c), sum(b), sum(w)
SP = [c, b, w]
IND = SP.index(max(SP))
if IND == 2:
    print("back")
elif IND == 1:
    print("biceps")
elif IND == 0:
    print("chest")

# http://codeforces.com/problemset/problem/255/A