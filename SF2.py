# Дано натуральное восьмизначное число. Выясните, является ли оно палиндромом
# (читается одинаково слева направо и справа налево)

a = input("Введите восьмизначное число:")
if len(a) != 8:
    print ("Это не восьмизначное")
else:
    if a[0:4:] == a[-1:-5:-1]:
        print("allright!")
    else:
         print("noo good")

kaspa:qrywfx0ysverysyhhfs5m66hc0uruw8jfht2ffnndhqmmku9gdcrzgzrfkl4q