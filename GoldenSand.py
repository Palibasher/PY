a = input("Введите три числа, по цене трех видов песка, и три числа, по объему трех емкостей, через пробел:")
a = a.split()
a = list(map(int, a))
a1 = [a[0], a[1], a[2]]
a2 = [a[3], a[4], a[5]]
pes = sorted(a1)
kor = sorted(a2)
nice = pes[0]*kor[0] + pes[1]*kor[1] + pes[2]*kor[2]
print(nice)


