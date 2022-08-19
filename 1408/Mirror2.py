def print_mat2(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            print(a[i][j], end=" ")
        print()

Z = [[5, 9, 2, 6], [6, 2, 4, 3], [1, 2, 8, 7]]
test = print_mat2(Z)
XY = Z[::-1]
print("---------")
test = print_mat2(XY)
