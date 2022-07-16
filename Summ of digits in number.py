a = input()
dl = (len(a))
A = int(a)
dl = int(dl)
TT = 0
while dl >= 0:
    Z = (A // 10**dl)%10
    dl = dl - 1
    print(Z)
    TT = Z + TT
print(TT)