sum = 0
er = 0
z = 1 #задаем счетчик для вывода номера посетителя
col = int(input("Сколько билетов хотите приобрести? "))
L = [int(input("Введите возраст посетителя №{} и нажмите Enter: ".format(z+i))) for i in range(col)]
z = 1 #перезаписываем счетчик для посетителя
for i in L:
    if i < 0 or i > 110:
        print("№{}. Этот человек еще не родился, либо слишком старый".format(z))
        er += 1
        z += 1
    elif 0 <= i < 18:
        print("№{}. До 18 вход свободный".format(z))
        z += 1
    elif 18 <= i < 25:
        print("№{}. От 18 до 25 лет - 990 руб".format(z))
        z += 1
        sum += 990
    elif 25 <= i <= 110:
        print("№{}. От 25 лет — полная стоимость - 1390 руб".format(z))
        z += 1
        sum += 1390
if (len(L) - er) > 3: #считаем сумму валидных регистраций, вычитая из общего кол-ва сумму ошибочных посететилей
    sum = sum * 0.9 #применяем скидку для 4 и более зарегистрированных
    print("Поздравляем, вы получаете скидку 10%!. Cумма к оплате: ", int(sum))
else:
    print("Сумма к оплате: ", int(sum))