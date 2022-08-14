def print_mat(a):
    for arr in range(len(a)):
        print(a[arr])

def matrix_0(rows, colums):
    a = []
    A = [0] * rows
    for i in range(colums):
        a.append(A)
    return a
TT = int(input())
RR = int(input())
A = matrix_0(TT, RR)
print_mat(A)
