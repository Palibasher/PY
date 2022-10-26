

def logger(func):
    def wrapper(a, b):
        print(f"{func.__name__} началась!")
        result = func(a, b)
        print(f"{func.__name__} кончилась!")
        return result
    return wrapper

@logger
def s_e(a, b):
    return a + b


# our_test = logger(s_e)
# print(our_test(2, 3))
# print((logger(s_e)(2, 2)))
#
# s_e = logger(s_e)

print(s_e(5, 100))