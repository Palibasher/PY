# """Класс для гоблинца"""
# a = randint(0, 5)
# d1 = {0: "враждебно", 2: "кровожадно", 3: "агрессивно", 4: "мягко говоря недружелюбно", 5: "дружелюбно"}
# d2 = {0: "грозно запыхтел увидев вас.", 2: "стал бить себя кулаком в пах, как только вас заметил.", 3:
#     "принялся вращать налитыми кровью глазами, завидев вас издалека.", 4: "принялся приседать, делая вид,"
#                                                                           "что готов бросить в вас нечистоты.",
#       5: "улыбнулся и подмигнул вам."}
# d3 = {0: "подумали, а что если он пыхтел, просто из-за того что занимался спортом, когда вы его застали.",
#       2: "увидели, что он бил себя кулаком, потому что был возбужден, и хотел заняться с вами любовью.",
#       3: "заметили, что глаза у него не были налиты кровью, а он просто\nносил очки красного цвета. Что же вы наделали?",
#       4: "обратили внимание, что он хотел бросить в вас не нечистоты, а волшебный порошок.\n Заинтересовавшись вы "
#          "понюхали порошок и умерли",
#       5: "осознали, что вы нехороший человек"}
# d4 = {0: "", 2: "", 3: "", 4: "", 5: ""}
#
#
# def __init__(self, name, sex, hp, atitude=a):
#     """Задаем имя, пол, кол-во хп"""
#     self.name = name
#     self.sex = sex
#     self.hp = hp
#
#
# def __str__(self):
#     return f"Гоблинц по имени - {self.name}"
#
#
# def get_name(self):
#     """Функция возвращает Имя"""
#     return self.name
#
#
# def get_sex(self):
#     """Функция возвращает Пол"""
#     return self.sex
#
#
# def get_age(self):
#     """Функция возвращает HP"""
#     return self.hp
#
#
# def fight1(self):
#     count = 0
#     p = 0
#     print(
#         f"Вам встретился {self.name}, он настроен {self.d1[self.a]} по отношению к вам,\n"
#         f"вы это поняли, глядя как он {self.d2[self.a]}.\n")
#     while self.hp > 0 and p != 1:
#         p_hit = int(input("Насколько сильно ударить?  Напишите число: \n"
#                           "1. Врезать со всей силы\n2. Сильно\n3. Дать пощечину\n"))
#         if p_hit == 1:
#             p_hit = 10
#             self.hp = self.hp - p_hit
#             if self.hp > 0:
#                 print(f"Вы ударили {self.name}, доставили ему {p_hit} урона и у него осталось {self.hp}")
#             else:
#                 print("О да!")
#         elif p_hit == 2:
#             p_hit = 5
#             self.hp = self.hp - p_hit
#             if self.hp > 0:
#                 print(f"Вы ударили {self.name}, доставили ему {p_hit} урона и у него осталось {self.hp}")
#             else:
#                 print("О да!")
#         elif p_hit == 3:
#             print("Вы только разозлили гоблинца еще больше")
#             count += 1
#             if count == 2:
#                 print(f"{self.name} разозлился так сильно, что убил вас")
#                 p = 1
#     if p == 0:
#         print(
#             f"Вы убили {self.name}, мать вашу! А потом {self.d3[self.a]}")
#     else:
#         print("Вы умерле жидко пукнув")
#
#
#
# #############функция перезаписи хар-тик
#         def rewrite_player_atr():
#             """Пересчитваем атрибуты, которые могли измениться после надевания предметов"""
#             self.player.health_bonus = self.player.amulet_pt[3]  # бонус от возможного амулета здоровья
#             self.player.dmg_bonus = self.player.amulet_pt[4]  # бонус от возможного амулета берсерка
#             self.player.armor_bonus = self.player.amulet_pt[5]
#             self.player.hp = self.player.raw_hp + self.player.health_bonus  # здоровье
#             self.player.output_dmg = round(self.player.weapon_pt * self.player.dmg_coefficient)  # урон игрока
#             self.player.defence = self.player.armor_pt + self.player.armor_bonus
#             self.player.light_hit = round(self.player.output_dmg * 0.7)
#             self.player.medium_hit = round(self.player.output_dmg * 1.3)
#             self.player.mega_hit = self.player.output_dmg * 2
def i():
    return 3+4
print(i() + 3)