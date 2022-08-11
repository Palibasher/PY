f1 = input("Ввести компрессию: ")
f1 = [int(a) for a in str(f1)]
stt = []
ftt = []
f1 = list(enumerate(f1))

for i in f1:
    if i[0] % 2 == 0:
        stt.append(i[1])
    else:
        ftt.append(i[1])
RES = list(zip(stt,ftt))
print(RES)
man = ""
add = ""
for i in RES:
    add = str(i[1]) * int(i[0])
    man = man + add
print(man)

# https://leetcode.com/problems/decompress-run-length-encoded-list/