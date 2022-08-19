def print_mat2(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            print(a[i][j], end=" ")
        print()

Z = [[6, 2, 0, 4, 3], [5, 4, 0, 7, 1], [1, 7, 0, 3, 0], [3, 7, 6, 5, 0], [3, 7, 6, 5, 0], [1, 1, 1, 1, 1]]
test = print_mat2(Z)
print("----")

def summ_for_rows_and_cols(a):
    Rowlen = len(a[0])
    Collen = len(a)
    summ = 0
    rsumm = []
    for i in range(Collen):
        for j in range(Rowlen):
            summ += a[i][j]
        rsumm.append(summ)
        summ = 0
    for i in range(Rowlen):
        for j in range(Collen):
            summ += a[j][i]
        rsumm.append(summ)
        summ = 0

    return rsumm
test = summ_for_rows_and_cols(Z)
print(test)