z = int(input())
X = int(input())
count = 0
M = [[i*j for j in range(1, z+1)] for i in range(1, z+1)]
for index, row in enumerate(M):
    print(row)
    if X in row:
        count += 1
print(count)



