Z = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
Z2 = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# def print_mat(a):
#     for arr in range(len(a)):
#         print(a[arr])
# def print_mat_rever(a):
#     for arr in range(len(a)):
#         print(list(reversed(a[arr])))
# print_mat(Z)
def print_mat2(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            print(a[i][j], end=" ")
        print()
test = print_mat2(Z)
def find0(a):
    y, x = None, None
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == 1:
                y, x = i, j
    return y, x
T = find0(Z)
T2 = find0(Z2)
print(T, T2)
print(abs(T[0] - T2[0]) + (abs(T[1] - T2[1])))


