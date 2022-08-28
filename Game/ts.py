from classes_g import Chest
from classes_g import Player
from random import randint
if __name__ == "__main__":
    player = Player("Гарри", 10, 10)
    chest = Chest(player)
    chest.opening_chest()
    chest.take_items()
    player.show_chr()
    player.get_devparam()
    chest = Chest(player)
    chest.opening_chest()
    chest.take_items()
    player.show_chr()
    player.get_devparam()
# print(weapons.keys())
# print(*weapons.keys())
# print([*weapons.keys()])

# for i in chest.content.keys():
#     print(f"{i} в кол-ве {chest.content[i]}")
#     check_chest = int(input("Хотите узнать подробнее, что это за предмет?\n1. Да\n2. Нет\n"))
#     if check_chest == 1:
#         if i in weapons:
#             print(weapons[i][2])
#         elif i in armors:
#             print(armors[i][2])
#         elif i in amulets:
#             print(amulets[i][2])
#         elif i == "Зелья":
#             print("Волшебное зелье, перед употреблением встряхнуть.")
#         else:
#             print("Волшебный свиток, который запускает во врага элекричеким зарядом. Лучше любых тумаков.")


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