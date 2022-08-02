z = int(input())
M = [[i*j for j in range(1, z)] for i in range(1, z)]
for n in range(z):
    while n <= z:
        print(M[n])
        n += 1