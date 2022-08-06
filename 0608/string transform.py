text = input("Text: ")
ltext = text.lower()
exep = ["a", "o", "y", "e", "u", "i"]
n2 = []
for i in ltext:
    if i not in exep:
        n2.append(".")
        n2.append(i)
print("".join(n2))

# http://codeforces.com/problemset/problem/118/A