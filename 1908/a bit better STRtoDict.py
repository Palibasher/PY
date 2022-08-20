Pepe = ["a", 1, 3, "b", 44, 3, "d", 3, 4, 8, "ks", 3, 0, 7, -66, "k", -20]
D = {}
Pl = []
Timer = -1
for zn in Pepe:
    Timer += 1
    Stop = len(Pepe) - 1
    if Timer == Stop:
        Pl.append(zn)
        D[K] = Pl
        break
    if type(zn) == str:
        K = zn
    if type(zn) == int:
        Pl.append(zn)
        if type(Pepe[Timer + 1]) == str:
            D[K] = Pl
            Pl = []
print(D)
