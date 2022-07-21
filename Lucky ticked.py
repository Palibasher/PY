a = input("Введите номер билета:")
if len(a) != 6:
    print ("Неправильный номер")
else:
    a = list(map(int, a))
    x = a[0] + a[1] + a[2]
    y = a[3] + a[4] + a[5]
    if x == y:
        print("Вам невероятно повезло!")
    else:
        print("Good luck next time")