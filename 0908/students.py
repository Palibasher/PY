stud = input("Через пробел укажите сколько раз i-й человек участвовал в чемпионате мира ACM ICPC (>=1 и <=5): ")
stud = list(map(int, stud.split()))
iwant = int(input("Введите, сколько раз студены должны участвовать в чемпионате >=1 и <=5:" ))
r2 = []
for i in stud:
    if i + iwant <= 5:
        r2.append(i)
com = len(r2) // 3
print(com)

# http://codeforces.com/problemset/problem/432/A