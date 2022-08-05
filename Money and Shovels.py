r = int(input("Стоимость монеты: "))
R = 10
k = int(input("Стоимость лопаты: "))
z = 0
o = 0
PR2 = 0
SPIS = []
ost_c = k % R
if 1 > k or k > 1000 or 1 > r or r > 10:
    print("НЕМОЖНО!!")
if r == k or ost_c == r or k % R == 0:
    print("1")
else:
    for i in range(1, 10):
        if (i * ost_c) % 10 == 0:
            PR2 = i
            # print(PR2)
            break
    # if (k * 4) % R == 0:
    #     PR2 = 5 #ой тут все четные проверять
    if r > ost_c:
        for i in range(1, 10):
            if (ost_c * i) % R == r:
                # print(i)
                z = i
                break
    elif r < ost_c:
        for O in range(1, 10):
            if (ost_c * O) % R == r:
                o = O
                # print(o)
                break
    if PR2 != 0:
        SPIS.append(PR2)
    if o != 0:
        SPIS.append(o)
    if z != 0:
        SPIS.append(z)
    SPIS = sorted(SPIS)
    print(SPIS[0])


