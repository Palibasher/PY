def print_mat(a):
    for arr in a:
        print(arr)

C = int(input("Кол-во строк: "))
R = int(input("Кол-во столбов: "))
A = [ [0]*R for i in range(C) ]
for i in range(R):
    for j in range(C):
        T = input("Вводите дигит: ")
        A[j][i] = T
print_mat(A)
for c in range(C-1, -1, -1):
    for r in range(R):
        print(A[c][r], end=" ")
    print()
# https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=8&id_topic=120&id_problem=745