# def rec_sum(n):
#    if n == 1:  # терминальный случай
#        return 1
#    return n + rec_sum(n - 1)  # рекурсивный вызов
k = input()

def c(k, r = ""):
    if len(k) < 1:
        return r
    r += k[-1]
    k = k[0:len(k) - 1:]
    return c(k,r)
print(c(k))
