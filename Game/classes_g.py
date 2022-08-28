from random import randint
class Goblin:
    """Класс для гоблинца"""
    a = randint(0,5)
    d1 = {0 : "враждебно", 2 : "кровожадно", 3 : "агрессивно", 4 : "мягко говоря недружелюбно", 5 : "дружелюбно"}
    d2 = {0: "грозно запыхтел увидев вас.", 2: "стал бить себя кулаком в пах, как только вас заметил.", 3:
        "принялся вращать налитыми кровью глазами, завидев вас издалека.", 4: "принялся приседать, делая вид,"
        "что готов бросить в вас нечистоты.", 5: "улыбнулся и подмигнул вам."}
    d3 = {0: "подумали, а что если он пыхтел, просто из-за того что занимался спортом, когда вы его застали.",
          2: "увидели, что он бил себя кулаком, потому что был возбужден, и хотел заняться с вами любовью.",
          3: "заметили, что глаза у него не были налиты кровью, а он просто\nносил очки красного цвета. Что же вы наделали?",
          4: "обратили внимание, что он хотел бросить в вас не нечистоты, а волшебный порошок.\n Заинтересовавшись вы "
             "понюхали порошок и умерли",
          5: "осознали, что вы нехороший человек"}
    d4 = {0: "", 2: "", 3: "", 4: "", 5: ""}

    def __init__(self, name, sex, hp, atitude=a):
        """Задаем имя, пол, кол-во хп"""
        self.name = name
        self.sex = sex
        self.hp = hp
    def __str__(self):
        return f"Гоблинц по имени - {self.name}"

    def get_name(self):
        """Функция возвращает Имя"""
        return self.name

    def get_sex(self):
        """Функция возвращает Пол"""
        return self.sex

    def get_age(self):
        """Функция возвращает HP"""
        return self.hp

    def fight1(self):
        count = 0
        p = 0
        print(
            f"Вам встретился {self.name}, он настроен {self.d1[self.a]} по отношению к вам,\n"
            f"вы это поняли, глядя как он {self.d2[self.a]}.\n")
        while self.hp > 0 and p != 1:
            p_hit = int(input("Насколько сильно ударить?  Напишите число: \n"
                              "1. Врезать со всей силы\n2. Сильно\n3. Дать пощечину\n"))
            if p_hit == 1:
                p_hit = 10
                self.hp = self.hp - p_hit
                if self.hp > 0:
                    print(f"Вы ударили {self.name}, доставили ему {p_hit} урона и у него осталось {self.hp}")
                else:
                    print("О да!")
            elif p_hit == 2:
                p_hit = 5
                self.hp = self.hp - p_hit
                if self.hp > 0:
                    print(f"Вы ударили {self.name}, доставили ему {p_hit} урона и у него осталось {self.hp}")
                else:
                    print("О да!")
            elif p_hit == 3:
                print("Вы только разозлили гоблинца еще больше")
                count += 1
                if count == 2:
                    print(f"{self.name} разозлился так сильно, что убил вас")
                    p = 1
        if p == 0:
            print(
                f"Вы убили {self.name}, мать вашу! А потом {self.d3[self.a]}")
        else:
            print("Вы умерле жидко пукнув")
class Player:
    """Класс для Игрока"""
    def __init__(self, name, raw_str, raw_int, luck = 0 , amulet = ["Веревочка",[2, 0, 0, 0, 0, 0]], armor = ["Рваная рубаха", 2], weapon = ["Руки", 5], raw_hp = 30):
        """Задаем имя, пол, кол-во хп"""
        self.a = randint(0, 5) # кубик на будущее
        self.name = name #имя игрока
        self.str = raw_str #сила
        self.int = raw_int #ум
        self.inventar = {"Свитки" : 0, "Зелья" : 0}
        self.armor_pt = armor[1] #защита брони
        self.armor = armor[0] #какая броня
        self.weapon = weapon[0] #какое оружие
        self.weapon_pt = weapon[1] #урон оружия
        self.amulet = amulet[0] # какие амулеты надеты
        self.amulet_pt = [0, 0, 0, 0, 0, 0]
        self.health_bonus = self.amulet_pt[3] #бонус от возможного амулета здоровья
        self.dmg_bonus = self.amulet_pt[4] #бонус от возможного амулета берсерка
        self.armor_bonus = self.amulet_pt[5]
        self.raw_hp = raw_hp
        self.hp = raw_hp + self.health_bonus #здоровье
        self.dmg_coefficient = 1 + (self.str / 10) + self.dmg_bonus # прикидка для будущей формулы
        self.output_dmg = self.weapon_pt * self.dmg_coefficient #урон игрока
        self.defence = self.armor_pt + self.armor_bonus
    def get_name(self):
        """Функция возвращает Имя"""
        return self.name
    def show_chr(self):
        """Функция печатает описание"""
        print(f"----------------------------------------------------------------------------------------------------------------------------------\n"
              f"Вас зовут: {self.name}, кол-во ваших очков здоровья: {self.hp}, на вас ваш доспех: {self.armor}, амулет на шее: {self.amulet}\n"
              f"Ваше основное оружие: {self.weapon}, содержимое вашей сумки: Свитки: {self.inventar['Свитки']}, Зелья:{self.inventar['Зелья']}\n"
              f"-----------------------------------------------------------------------------------------------------------------------------------\n")
    def get_devparam(self):
        print(f"Dmg output - {self.output_dmg},coef - {self.dmg_coefficient}, wp_dmg - {self.weapon_pt}, def - {self.defence}\n"
              f"amulet hp - {self.health_bonus}, amuletar - {self.armor_bonus}, amuletdmg - {self.dmg_bonus}, am - {self.amulet}")
    def inventar_use(self):
        """Функция позволяет использовать предмет из инвентаря"""
        if {self.inventar["Свитки"]} != 0 and self.inventar["Зелья"] != 0:
            print(f"У вас в сумке: cвитки - {self.inventar['Свитки']}, зелья - {self.inventar['Зелья']}, что хотите использовать?")
            c1 = int(input("Введите 1 - для свитка, 2 - для зелья, 3 - если передумали: "))
            if c1 == 1:
                self.inventar["Свитки"] -= 1
                return 1 # нанести 20 урона врагу
            elif c1 == 2:
                self.hp += 20 # вылечить 20 хп
                self.inventar["Зелья"] -= 1
                print(f"Вы подлечились, и теперь у вас {self.hp} здоровья")
            else:
                pass
        elif {self.inventar["Свитки"]} == 0 and self.inventar["Зелья"] != 0:
            print(f"У вас в сумке: cвитков нет, зелья - {self.inventar['Зелья']}, хотите выпить зелье?")
            c1 = int(input("Введите 1 - если да, 2 если нет: "))
            if c1 == 1:
                self.hp += 20 # вылечить 20 хп
                self.inventar["Зелья"] -= 1
                print(f"Вы подлечились, и теперь у вас {self.hp} здоровья")
            elif c1 == 2:
                pass
        elif {self.inventar["Свитки"]} != 0 and self.inventar["Зелья"] == 0:
            print(f"У вас в сумке: зелий нет, свитки - {self.inventar['Свитки']}, хотите прочитать свиток?")
            c1 = int(input("Введите 1 - если да, 2 если нет: "))
            if c1 == 1:
                self.inventar["Свитки"] -= 1
                return 1 # нанести 20 урона врагу
            elif c1 == 2:
                pass
        else:
            print(f"Извини {self.name}, но сумка пуста, ничего нет, совсем ничего")
    def add_scroll(self, scr = 1):
        move_1 = int(input("На стене, в щелке между камнями, вы заметили какую то рваную бумажку. Взять?\n1. Да\n2. Кто-то бычок засунул... нет.\n"))
        if move_1 == 1:
            self.inventar["Свитки"] += scr
            print(f"Никакой не бычок, а настоящий магический свиток, теперь у вас их {self.inventar['Зелья']}")
        elif move_1 == 2:
            print("Вы обошли стороной странную бумажку")
            pass
    def add_potion(self, pot = 1):
        move_1 = int(input("Вы заметили в грязи бутылочку с зельем. Взять?\n1. Да\n2. Мусор какой то... нет.\n"))
        if move_1 == 1:
            self.inventar["Зелья"] += pot
            print(f"Это и в прямь оказалась бутылочка с зельем здоровья, теперь у вас их {self.inventar['Зелья']}")
        elif move_1 == 2:
            print("Вы осорожно обошли подозрительный флакон и пошли дальше")
            pass
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
amulets = {"Амулет Здоровья":[1, 15, "Увеличивает ваше здоровье", 10, 0, 0],
           "Амулет Защиты":[1, 12, "Защишает от тумаков", 0, 0, 10],
           "Амулет Берсерка":[1, 8, "Добавляет силы вам и вашим ударам", 0, 0.2, 0],
           "Странный амулет":[1, 4, "Загадочный амулет", 5, 0.1, 5]}
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

class Chest():
    """Класс сундук"""
    def __init__(self, player):
        self.player = player
        self.content = {}
        self.ran_wp = randint(1, 100)
        self.ran_ar = randint(1, 100)
        self.ran_am = randint(1, 100)
        self.ran_jk = randint(1, 100)
    def opening_chest(self):
        """Логика дропа из сундука"""
        print("Вы открываете сундук и внутри находите:")
        weapon_drop = {}
        armor_drop = {}
        amulet_drop = {}
        jokes_drop = {}
        if randint(1, 2) == 1: #добавляем в сундук зелья, чем больше, тем меньше шанс
            if randint(1, 2) == 1:
                self.content["Зелья"] = 1
            elif randint(1, 3) == 2:
                self.content["Зелья"] = 2
            elif randint(1, 8) == 5:
                self.content["Зелья"] = 3
        else:
            pass
        if randint(1, 2) == 1: #добавляем в сундук свитки, чем больше, тем меньше шанс
            if randint(1, 2) == 1:
                self.content["Свитки"] = 1
            elif randint(1, 4) == 2:
                self.content["Свитки"] = 2
            elif randint(1, 10) == 5:
                self.content["Свитки"] = 3
        for i in weapons.keys(): #добавляем в оружие, чем круче, тем меньше шанс
            if weapons[i][1] >= self.ran_wp:
                weapon_drop = {}
                weapon_drop[i] = 1
        if len(list(weapon_drop)) != 0:
            container = list(weapon_drop)
            self.content[container[0]] = 1
        for i in armors.keys(): #добавляем в броню, чем круче, тем меньше шанс
            if armors[i][1] >= self.ran_ar:
                armor_drop = {}
                armor_drop[i] = 1
        if len(list(armor_drop)) != 0:
            container = list(armor_drop)
            self.content[container[0]] = 1
        for i in amulets.keys(): #добавляем амулет
            if amulets[i][1] >= self.ran_am:
                amulet_drop = {}
                amulet_drop[i] = 1
        if len(list(amulet_drop)) != 0:
            container = list(amulet_drop)
            self.content[container[0]] = 1
        for i in jokes.keys(): #добавляем lol
            if jokes[i][1] >= self.ran_jk:
                jokes_drop = {}
                jokes_drop[i] = 1
        if len(list(jokes_drop)) != 0:
            container = list(jokes_drop)
            self.content[container[0]] = 1
        chek_container = list(self.content)
        if len(chek_container) == 0:
            self.content["Эх, не повезло, сундук оказался пустой"] = None
        for i in self.content.keys(): #выводим предметы
            print(f"{i} в кол-ве {self.content[i]} шт.")
            check_chest = int(input("Хотите узнать подробнее, что это за предмет?\n1. Да\n2. Нет\n"))
            if check_chest == 1:
                if i in weapons:
                    print(weapons[i][2])
                elif i in armors:
                    print(armors[i][2])
                elif i in amulets:
                    print(amulets[i][2])
                elif i in jokes:
                    print(jokes[i][2])
                elif i == "Зелья":
                    print("Волшебное зелье, перед употреблением встряхнуть.")
                elif i == "Свитки":
                    print("Волшебный свиток, который запускает во врага элекричеким зарядом. Лучше любых тумаков.")
                else:
                    print("Нет предмета, друг, если не считать предметом пустоту, но это филосовский вопрос.")
        print("В итоге вы нашли:", *self.content, sep=" || ")
    def take_items(self):
        def rewrite_player_atr():
            """Пересчитваем атрибуты, которые могли измениться после надевания предметов"""
            self.player.health_bonus = self.player.amulet_pt[3]  # бонус от возможного амулета здоровья
            self.player.dmg_bonus = self.player.amulet_pt[4]  # бонус от возможного амулета берсерка
            self.player.armor_bonus = self.player.amulet_pt[5]
            self.player.hp = self.player.raw_hp + self.player.health_bonus  # здоровье
            self.player.dmg_coefficient = 1 + (
                        self.player.str / 50) + self.player.dmg_bonus  # прикидка для будущей формулы
            self.player.output_dmg = round(self.player.weapon_pt * self.player.dmg_coefficient)  # урон игрока
            self.player.defence = self.player.armor_pt + self.player.armor_bonus
        if  set([*weapons.keys()]) & set([*self.content.keys()]): #сравниваем содержимое сундука и список оружия
            current_weapon_in_chest = list(set([*weapons.keys()]) & set([*self.content.keys()])) #если есть совпадение, сохраняем переменную
            print(f"Взять {set([*weapons.keys()]) & set([*self.content.keys()])} вместо своего текущего оружия? Сейчас у вас {self.player.weapon}.")
            k = int(input("1. Выглядит лучше моего..\n2. Нет, лучше оставлю свое.\n")) #выбираем поменять ли текущее
            if k == 1: #тут происходит перезаписывание текущего и его хар-ки
                weapon_key = current_weapon_in_chest.pop()
                self.player.weapon_pt = weapons[weapon_key][0]
                self.player.weapon = weapon_key
                print(f"Теперь {self.player.weapon} - ваше основное оружие!")
                ## Пересчет дамага, здоровья и пр.. для Player
                rewrite_player_atr()
            else:
                pass
        if  set([*armors.keys()]) & set([*self.content.keys()]): #все то же для брони
            current_armor_in_chest = list(set([*armors.keys()]) & set([*self.content.keys()]))
            print(f"Взять {set([*armors.keys()]) & set([*self.content.keys()])} вместо своей брони? Сейчас у вас {self.player.armor}.")
            k = int(input("1. Выглядит лучше моей..\n2. Нет, лучше оставлю свою.\n"))
            if k == 1:
                armor_key = current_armor_in_chest.pop()
                self.player.armor_pt = armors[armor_key][0]
                self.player.armor = armor_key
                print(f"Теперь {self.player.armor} - ваша основная броня!")
                ## Пересчет для Player
                rewrite_player_atr()
            else:
                pass
        if  set([*amulets.keys()]) & set([*self.content.keys()]): #все то же для амулета
            current_amulet_in_chest = list(set([*amulets.keys()]) & set([*self.content.keys()]))
            print(f"Надеть {set([*amulets.keys()]) & set([*self.content.keys()])} вместо текущего, сейчас у вас {self.player.amulet}.")
            k = int(input("1. Надеть..\n2. Нет, лучше оставлю свой.\n"))
            if k == 1:
                amulet_key = current_amulet_in_chest.pop()
                self.player.amulet_pt = amulets[amulet_key]
                self.player.amulet = amulet_key
                print(f"Теперь {self.player.amulet} висит у вас на шее!")
                ## Пересчет для Player
                rewrite_player_atr()
            else:
                pass
        print(self.content)
        if "Свитки" in self.content:
            self.player.inventar['Свитки'] += self.content["Свитки"]
            print(f"Свитки вы убрали в сумку, теперь у вас: cвитки - {self.player.inventar['Свитки']} шт.")
            rewrite_player_atr()
        else:
            pass
        if "Зелья" in self.content:
            self.player.inventar['Зелья'] += self.content["Зелья"]
            print(f"Зелья вы убрали в сумку, теперь у вас: зелья: - {self.player.inventar['Зелья']} шт.")
            rewrite_player_atr()
        else:
            pass






