a = input()
a = int(a)
if a > 1440:
    b = a // 1440
    A = a - 1440 * b
    HH = A // 60
    MM = A % 60
    print(HH, ':', MM)
if a < 1440:
    HH = a // 60
    MM = a % 60
    print(HH, ':', MM)