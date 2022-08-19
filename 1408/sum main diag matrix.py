def print_mat2(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            print(a[i][j], end=" ")
        print()

Z = [[6, 2, 0, 4, 3], [5, 4, 0, 7, 1], [1, 7, 0, 3, 0], [3, 7, 6, 5, 0], [0, 3, 1, 0, 0]]
test = print_mat2(Z)
print(----)

def summ_main_diag(a):
    summ = 0
    for i in range(len(a)):
        summ += Z[i][i]
    return summ
test = summ_main_diag(Z)
print(test)
