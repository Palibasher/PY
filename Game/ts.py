from classes_g import Chest
from random import randint
weapons = {"Руки": [8, 0, "Руки как руки, тумаков надавать можно"],
           "Тупой кинжал": [12, 55, "Тупой, но колоться пойдет"],
           "Дубинка шипами": [13, 50, "Увесистая такая дубинка из крепкого дерева, тумаков надавать в самый раз"],
           "Короткий меч": [14, 31, "Немного ржавый меч, но все же меч"],
           "Топор дровосека": [14, 30, "Можно рубить деревья, а можно конечности врагов, ну и тумаков надавать"],
           "Булава": [15, 25, "Серьезное оружие. Можно надавать очень серьезных тумаков"],
           "Длинный меч": [16, 19, "Длинный острый меч, шутки кончились"],
           "Боевой топор": [17, 9, "Топор внушительных размеров, таким можно зарубить быка"],
           "Секира короля гоблинов": [18, 4, "Опасное и редкое оружие, когда-то король гоблинов 'Бабиус Третий', зарубил им собаку"]
           }

chest = Chest()
chest.opening_chest()
print(chest.content)
chest = Chest()
chest.opening_chest()
print(chest.content)
chest = Chest()
chest.opening_chest()
print(chest.content)
chest = Chest()
chest.opening_chest()
print(chest.content)

# for i in chest.content.keys():
#     print(i[0])

# z = {}
# ran_wp = randint(1, 100)
#
# for i in weapons.keys():
#     if weapons[i][1] >= ran_wp:
#         print(f"{i}, число - {ran_wp}")
#         z = {}
#         z[i] = 1
# print(z)
# print(ran_wp)