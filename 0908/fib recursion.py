def fib():
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b
s = fib()
for i in range(20):
    print(i, next(s))

