С = input("Строка: ")
CC = []
for i in С:
    if С.index(i) % 3 != 0:
        CC.append(i)
print("".join(map(str,CC)))
