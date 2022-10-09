from random import randint
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
enemy_mood = {0: ["Нейтрально", "Я могу не только подсказать, но и составить вам компанию!"],
                       1: ["Недружелюбно", "Моя не понимать биолетека.."],
                       2: ["Враждебно", "Сдавайся человечищка, иначе моя твоя убивать"],
                       3: ["Кровожадно", "О, дружок, я сейчас тебе подскажу.. смотри, вооо-о-оо-он там!"]}
print(enemy_mood[0][1])
weapons = {"Руки": [5, 0, "Руки как руки, тумаков надавать можно."],
           "Тупой кинжал": [7, 60, "Тупой и ржавый кинжал, но им можно больно колоться. А рукояткой можно надавать тумаков"],
           "Дубинка c шипами": [8, 50, "Увесистая такая дубинка из крепкого дерева, годится, что бы раздавать тумаки."],
           "Короткий меч": [9, 38, "Немного ржавый меч, но все же меч."],
           "Топор дровосека": [10, 30, "Можно рубить деревья, а можно конечности врагов. Опасное оружие."],
           "Булава": [11, 25, "Серьезное оружие. Можно надавать очень серьезных тумаков."],
           "Длинный меч": [12, 19, "Длинный острый меч, нешуточное оружие, можно и убить."],
           "Боевой топор": [13, 9, "Топор внушительных размеров, таким можно зарубить быка."],
           "Секира короля гоблинов": [18, 4, "Опасное и редкое оружие, когда-то король гоблинов 'Бабиус Третий', зарубил им собаку, а вообще мог бы и медведя."]
           }
armors = {"Рваная рубаха": [5, 0, "Ваша рубаха, достаточно плохая защита от тумаков."],
          "Стеганная телогрейка": [8, 55, "Хорошая защита от холода, не особо хорошо помогает от тумаков."],
          "Стеганный ватник": [10, 45, "Хорошая защита от логики и здравого смысла, так себе помогает от тумаков."],
          "Кожанка": [15, 37, "Модная курточка из плотной кожи, кое-как помогает от тумаков."],
          "Кольчуга": [20, 30, "Хорошая защита, в том числе и от тумаков."],
          "Пластинчатая броня": [25, 25, "Тяжелая и прочная броня, от тумаков отлично защищает."],
          "Кристаллический доспех": [30, 19, "Броня из сверхпрочного кристалла, тумаки только щекочут."],
          "Броня из шкуры дракона": [35, 9, "Волшебная броня, тумаки не пройдут!."],
          "Броня из шкуры Золотого дракона": [45, 4, "Легендарная броня из шкуры редчайшего дракона, почти полный иммунитет к тумакам."]
          }
amulets = {"Амулет Здоровья":[1, 15, "Увеличивает ваше здоровье", 30, 0, 0],
           "Амулет Защиты":[1, 12, "Защишает от тумаков", 0, 0, 12],
           "Амулет Берсерка":[1, 8, "Добавляет силы вам и вашим ударам, но отнимает здоровье", -20, 0.2, 0],
           "Странный амулет":[1, 4, "Загадочный амулет", 10, 0.1, 5]}
jokes = {"Пустой флакон из под зелья":[10, 65, "Кто то выпил, а грязный флакон бросил, вряд ли пригодится."],
           "Обертку от конфеты":[10, 55, "Жаль саму конфету кто-то уже облагородил"],
           "Банановая кожура":[5, 45, "Обычная кожура, высохла. Откуда она черт возьми в сундуке?"],
           "Пуговица":[35, 35, "Бесполезный хлам!"],
           "Записка от незнакомца":[25, 25, "Привет тебе друг! Я советую тебе поворачивать назад и идти домой, иначе получишь тумаков. С любовью, Пипкист!"],
           "Записка от неизвестного":[15, 10, "Когда мне было 15 лет, и я ходил срать батя всё время как-бы невзначай крутился возле толчка,\n"
                                             "и всё спрашивал, что ты там затих, почему тебя не слышно? первый раз я не ответил, так он начал ломиться в дверь,\n"
                                             "и орать, что ты там молчишь, что с тобой? начал материться, и говорить, что вообще дверь с петель снимет,\n"
                                             "алсо, батя ругался, если я сру и не смываю, причём не просто вконце срания, а непосредственно после \n"
                                             "вылезания какашки, мотивировал это тем, что воняет, и сам потом мне говорил: вот я какну и смываю, и ты так делай! \n"
                                             "однажды я срать сел, и слышу, батя где-то у двери встал в отдалении, ну я жопу вытер, и на пол накарачики присел,\n"
                                             "а там щель очень широкая снизу у двери, ну я в щель и смотрю, а там батя на карачиках сидит и в щель смотрит, и мне говорит:\n"
                                             "ты чё? ебанутый? чё ты там делаешь? батя кстати всё время какие-то травы пьёт, чтобы срать часто, срёт по 5 раз в день,\n"
                                             "а потом говорит, что жопу жжёт, и ещё пердит он. пиздец короче! реальная история. я не тролль"]
         }

#простая фунция передвижения игрока по плоскому полю
def make_move(self, lvlmap):
    if self.pos_x == 0 and self.pos_y == 0:  # верхний левый угол, начало
        where_to_go = int(input("Куда двинуться?\n"
                                "1. Восток\n"
                                "2. Юг\n"))
        if where_to_go == 1:
            self.pos_x += 1
        elif where_to_go == 2:
            self.pos_y += 1
    elif self.pos_x == self.pos_xx and self.pos_y == self.pos_yy:  # нижний правый угол
        where_to_go = int(input("Куда двинуться?\n"
                                "1. Север\n"
                                "2. Запад\n"))
        if where_to_go == 1:
            self.pos_y -= 1  # Север
        elif where_to_go == 2:
            self.pos_x -= 1  # Запад
    elif self.pos_x == 0 and self.pos_y == self.pos_yy:  # нижний левый угол
        where_to_go = int(input("Куда двинуться?\n"
                                "1. Север\n"
                                "2. Восток\n"))
        if where_to_go == 2:
            self.pos_x += 1  # Восток
        elif where_to_go == 1:
            self.pos_y -= 1  # Север
    elif self.pos_x == self.pos_xx and self.pos_y == 0:  # верхний правый угол
        where_to_go = int(input("Куда двинуться?\n"
                                "1. Юг\n"
                                "2. Запад\n"))
        if where_to_go == 1:
            self.pos_y += 1  # Юг
        elif where_to_go == 2:
            self.pos_x -= 1  # Запад
    elif self.pos_x == 0:  # левая сторона
        where_to_go = int(input("Куда двинуться?\n"
                                "1. Восток\n"
                                "2. Юг\n"
                                "3. Север\n"))
        if where_to_go == 1:
            self.pos_x += 1
        elif where_to_go == 2:
            self.pos_y += 1
        elif where_to_go == 3:
            self.pos_y -= 1
    elif self.pos_y == 0:  # верхняя сторона
        where_to_go = int(input("Куда двинуться?\n"
                                "1. Восток\n"
                                "2. Юг\n"
                                "3. Запад\n"))
        if where_to_go == 1:
            self.pos_x += 1  # Восток
        elif where_to_go == 2:
            self.pos_y += 1  # Юг
        elif where_to_go == 3:
            self.pos_x -= 1  # Запад
    elif self.pos_x == self.pos_xx:  # правая сторона
        where_to_go = int(input("Куда двинуться?\n"
                                "1. Юг\n"
                                "2. Север\n"
                                "3. Запад\n"))
        if where_to_go == 1:
            self.pos_y += 1  # Юг
        elif where_to_go == 2:
            self.pos_y -= 1  # Север
        elif where_to_go == 3:
            self.pos_x -= 1  # Запад
    elif self.pos_y == self.pos_yy:  # нижняя сторона
        where_to_go = int(input("Куда двинуться?\n"
                                "1. Восток\n"
                                "2. Север\n"
                                "3. Запад\n"))
        if where_to_go == 1:
            self.pos_x += 1  # Восток
        elif where_to_go == 2:
            self.pos_y -= 1  # Север
        elif where_to_go == 3:
            self.pos_x -= 1  # Запад
    else:  # не угол и не периметр
        where_to_go = int(input("Куда двинуться?\n"
                                "1. Восток\n"
                                "2. Юг\n"
                                "3. Север\n"
                                "4. Запад\n"))
        if where_to_go == 1:
            self.pos_x += 1  # Восток
        elif where_to_go == 2:
            self.pos_y += 1  # Юг
        elif where_to_go == 3:
            self.pos_y -= 1  # Север
        elif where_to_go == 4:
            self.pos_x -= 1  # Запад
def make_path_in_out(lvlmap):
    max_y, max_x = len(lvlmap), len((lvlmap[0]))
    next_step = (0, 0)
    end_point = (max_x - 1, max_y - 1)
    path = []
    def go_up(next_step):
        next_step = (next_step[0], next_step[1] - 1)  # верх
        return next_step
    def go_down(next_step):
        next_step = (next_step[0], next_step[1] + 1)  # низ
        return next_step
    def go_right(next_step):
        next_step = (next_step[0] + 1, next_step[1])  # право
        return next_step
    def go_left(next_step):
        next_step = (next_step[0] - 1, next_step[1]) #лево
        return next_step
    def up_down_left_right(next_step):
        if randint(0, 1) == 0: #право лево либо верх низ
            if randint(0, 1) == 0: #право лево
                next_step = go_right(next_step) #право
            else:
                next_step = go_left(next_step) #право лево
        else:
            if randint(0, 1) == 0: #верх низ
                next_step = go_down(next_step)
            else:
                next_step = go_up(next_step) #верх
        return next_step
    while next_step != end_point:
        if next_step in path:
            next_step = (0, 0)
            path = []
        else:
            if 0 < next_step[0] < end_point[0] and 0 < next_step[1] < end_point[1]: #тело матрицы
                path.append(next_step)
                next_step = up_down_left_right(next_step)
            elif next_step[0] == 0 and next_step[1] == 0:  # верхний левый угол
                path.append(next_step)
                if randint(0, 1) == 1:
                    next_step = go_down(next_step)
                else:
                    next_step = go_right(next_step)
            elif next_step[0] == end_point[0] and next_step[1] == 0:  # верхний правый угол
                path.append(next_step)
                if randint(0, 1) == 1:
                    next_step = go_down(next_step)
                else:
                    next_step = go_left(next_step)
            elif next_step[0] == 0 and next_step[1] == end_point[1]:  # нижний левый угол
                path.append(next_step)
                if randint(0, 1) == 1:
                    next_step = go_up(next_step)
                else:
                    next_step = go_right(next_step)
            elif 0 < next_step[0] < end_point[0] and next_step[1] == 0:  # верхняя граница без углов
                path.append(next_step)
                a = randint(0, 2)
                if a == 0:
                    next_step = go_left(next_step)
                elif a == 1:
                    next_step = go_right(next_step)
                else:
                    next_step = go_down(next_step)
            elif 0 < next_step[0] < end_point[0] and next_step[1] == end_point[1]:  # нижняя граница без углов
                path.append(next_step)
                a = randint(0, 2)
                if a == 0:
                    next_step = go_left(next_step)
                elif a == 1:
                    next_step = go_right(next_step)
                else:
                    next_step = go_up(next_step)
            elif next_step[0] == end_point[0] and 0 < next_step[1] < end_point[1]:  # правая граница без углов
                path.append(next_step)
                a = randint(0, 2)
                if a == 0:
                    next_step = go_left(next_step)
                elif a == 1:
                    next_step = go_down(next_step)
                else:
                    next_step = go_up(next_step)
            elif next_step[0] == 0 and 0 < next_step[1] < end_point[1]:  # левая граница без углов
                path.append(next_step)
                a = randint(0, 2)
                if a == 0:
                    next_step = go_right(next_step)
                elif a == 1:
                    next_step = go_down(next_step)
                else:
                    next_step = go_up(next_step)
    path.append(next_step)
    return path