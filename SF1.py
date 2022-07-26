a = int(input("a"))
b = int(input("b"))
c = int(input("c"))
if a < 45 and b > 45 and c > 45:
    print("true")
elif a > 45 and b < 45 and c > 45:
    print("true")
elif a > 45 and b > 45 and c < 45:
    print("true")
else:
    print("false")