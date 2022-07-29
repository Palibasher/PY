# Дописать функцию print_ladder так,
# чтобы она для числа n печатала лесенку следующего типа:
# n = 3
# *
# **
# ***

# n = 4
# *
# **
# ***
# ****


def print_ladder(n):
    while n > 1:
        for i in range(n):
            print("*" * (i + 1))
            n = n - 1

print_ladder(66)