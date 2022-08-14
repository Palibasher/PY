Z = [[3,4,3,3],[7,1,1,1], [-3,-4,9,0]]
def print_mat(a):
    for arr in range(len(a)):
        print(a[arr])
def print_mat_rever(a):
    for arr in range(len(a)):
        print(list(reversed(a[arr])))
print_mat(Z)
print_mat_rever(Z)
