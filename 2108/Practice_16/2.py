from Classclient import client


R23231 = client("Василий", "Гаркуша", "Каспийск", 133)
R23232 = client("Борис", "Секундеев", "Ростов", 233)
R23233 = client("Вадим", "Кошка", "Берендеев", 123)
R23234 = client("Валентина", "Тересова", "Лондон", 23333)
SP = [R23231, R23232, R23233, R23234]

for i in SP:
    print(*i.getinfo1())