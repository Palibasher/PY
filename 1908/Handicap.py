Pepe = ["a", 1, 3, "b", 44, 3, "d", 3, 4, 8, "ks", 3, 0, "k", -20]
D = {}
Pl = []
Timer = 0
Pepe1 = Pepe
Pepe1.append("STOP")
for zn in Pepe1:
    if type(zn) == str:
        if Pl == []:
            D[zn] = Pl
            Timer = zn
        if Pl != []:
            D[Timer] = Pl
            Pl = []
            Timer = zn
    elif type(zn) == int:
        Pl.append(zn)
print(D)