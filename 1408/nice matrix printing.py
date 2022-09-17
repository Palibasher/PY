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

def matrix_print_names(matrix):
    name_matrix = matrix
    for i, j in enumerate(matrix):
        name_i = str(i)
        for z, l in enumerate(j):
            name_j = str(z)
            name_matrix[i][z] = name_i + name_j
    return name_matrix