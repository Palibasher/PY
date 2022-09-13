from random import randint
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

class Enemy:
    """Класс для Врага"""
    mood = randint(0, 3)
    enemy_mood = {0: ["Нейтрально", "blank"],
                  1: ["Недружелюбно", "blank"],
                  2: ["Враждебно", "blank"],
                  3: ["Кровожадно", "blank"]}
    def __init__(self, name, str, base_hp, agi, mood = mood, enemy_mood = enemy_mood, class_name = "Общий класс врага", armour = ["Броня", 5, "Такой нет"], weapon = ["Оружие", 0], weapon_pt = 0):
        self.class_name = class_name
        self.name = name #имя врага
        self.str = str # сила
        self.base_hp = base_hp # базовый хп
        self.base_armour = armour[0] # броня монстра
        self.armour_description = armour[2]
        self.defence = armour[1] #защита брони
        self.agi = agi #ловкость
        self.weapon = weapon
        self.weapon_pt = self.weapon[1] #урон оружия
        self.weapon_description = self.weapon[2]
        self.enemy_mood = enemy_mood
        self.mood = mood
        # self.dmg = self.weapon_pt * self.dmg_coefficient #урон
        # self.output_dmg = round(self.dmg * randint(40,120)/100)
    def dmg_coefficient(self):
        return 1 + (self.str / 50)
    def output_dmg(self):
        return self.weapon_pt * self.dmg_coefficient()
    def new_hit(self):
        return round(self.output_dmg() * randint(40,120)/100)
    def get_devparam(self):
        print(f"Класс: {self.class_name}, Имя : {self.name}, сила : {self.str}, броня: {self.base_armour} {self.defence}, оружие - {self.weapon}, урон оружия - {self.weapon_pt}, коэф - {self.dmg_coefficient()}, итоговый урон = {self.new_hit()}\n"
              f"Описание оружия: {self.weapon_description}")
    def get_class_name(self):
        return self.class_name


class Spicked_frog(Enemy):
    """Класс лягушки"""
    def __init__(self):
        super().__init__(name = "Огромная лягушка", class_name="Лягуха", str = 10, base_hp =50, agi = 30, armour = ["Шкура", 5, "Здоровая лягушка и шкура у нее очень плотная"], weapon = ["Лапы", 5, "Лягушачьи лапки: вкусно, но лягушка так просто их не отдаст"])

class Goblin(Enemy):
    """Класс гоблинс"""
    def __init__(self):
        a = randint(0, 8)
        mood = randint(0, 3)
        name_gen = [["Ба", "Та", "Жо", "Бо", "До", "Ту", "Ти", "Ко", "Фо", "Ди", "Фи", "Лу", "Му", "Ду", "Ку", "Ла", "Но", "Ке", "Пе", "Де", "Ун", "Не", "Де", "Ке",],
                    [ "би", "ди", "ни", "ки", "ри", "до", "де", "ке", "се", "не", "фе", "ме", "ми", "ци", "це", "ре", "же", "ле"],
                    [ "усм", "есм", "кус", "пук", "пек", "бек", "ос", "юс", "юм", "бюкмс", "бей", "бак", "бас", "дос", "масмс", "дискис", "жормас", "кесм", "пипм", "писм", "кюкм"]]
        weapons_list = {"Лапы": [5, "Гоблинские лапы с огромными острыми ногтями."],
                        "Камни": [6, "Негодяй собрался бросаться камнями."],
                        "Тупой кинжал": [7, "Ржавый и тупой кинжал."],
                        "Дубинка": [8, "Гоблин играет в бейсбол? Скорее всего нет..."],
                        "Дубинка с шипами": [9, "Выглядит опасно и это точно не для бейсбола."],
                        "Топор мясника": [10, "Средних размеров топор для разделки мяса."],
                        "Плетка": [5, "Что этот гоблин задумал?."],
                        "Копье": [5, "Копье слишком велико для гоблина, вряд ли сможет нанести им много урона."],
                        "Нож": [8, "Хочешь знать, почему я использую нож? Пушки слишком быстры, не успеваешь насладиться, получить истинное удовольствие, а когда я использую нож,\nв этот самый последний момент раскрывается ВСЯ человеческая сущность, и в каком-то смысле я знаю твоих друзей лучше, чем ты."],}
        enemy_mood = {0: ["Нейтрально", "Я могу не только подсказать, но и составить вам компанию!", "И это после того, как вы пытались меня убить?", "Хорошо, забудем разногласия и закопаем топор войны"],
                       1: ["Недружелюбно", "Моя не понимать биолетека..", "Я тебя убивать и делать из твоя черепа горшок!"],
                       2: ["Враждебно", "Сдавайся человечищка, иначе моя твоя убивать", "Вот тебе биолетека, сраный человечишка!!"],
                       3: ["Кровожадно", "О, дружок, моя тебе подскажу подскажу.. смотри, вооо-о-оо-он там!", "О, дружок, моя тебе подскажу подскажу.. смотри, вооо-о-оо-он там!"]}
        name = str(name_gen[0][randint(0,23)]) + str(name_gen[1][randint(0,17)]) + str(name_gen[2][randint(0,20)])
        super().__init__(name = name, class_name="Гоблин", str = 10, base_hp =50, agi = -5, mood = mood, enemy_mood = enemy_mood[mood], armour = ["Стеганная броня", 7, "На гоблине одета курточка, из плотного, но криво прошитого материала, который немножко смягчает тумаки"], weapon = [[*weapons_list.keys()][a], weapons_list[[*weapons_list.keys()][a]][0], weapons_list[[*weapons_list.keys()][a]][1]])
    def __str__(self):
        return f'Этот гоблин - низкорослый, уродливый и {str(self.enemy_mood[0]).lower()} настроен к вам. Землистого цвета кожа, большой, плоский нос, глаза раскосые в форме фисташек.\n'

class Player:
    """Класс для Игрока"""
    def __init__(self, name, raw_str, raw_int, raw_agi, amulet = ["Веревочка",[2, 0, 0, 0, 0, 0]], armor = ["Рваная рубаха", 2], weapon = ["Руки", 5], raw_hp = 100):
        """Задаем имя, пол, кол-во хп"""
        self.a = randint(0, 5) # кубик на будущее
        self.name = name #имя игрока
        self.str = raw_str #сила
        self.int = raw_int #ум
        self.inventar = {"Свитки" : 0, "Зелья" : 0}
        self.agi = raw_agi * 3
        self.armor_pt = armor[1] #защита брони
        self.armor = armor[0] #какая броня
        self.weapon = weapon[0] #какое оружие
        self.weapon_pt = weapon[1] #урон оружия
        self.amulet = amulet[0] # какие амулеты надеты
        self.amulet_pt = [0, 0, 0, 0, 0, 0]
        self.raw_hp = raw_hp
    #Блок функций для пересчета ключевых характеристик
    def health_bonus(self):
        return self.amulet_pt[3]  # бонус от возможного амулета здоровья
    def armour_bonus(self):
        return self.amulet_pt[5]
    def dmg_bonus(self):
        return self.amulet_pt[4] #бонус от возможного амулета берсерка  # бонус от возможного амулета здоровья
    def current_hp(self):
        return self.raw_hp + self.health_bonus()
    def dmg_coefficient(self):
        return 1 + (self.str / 50) + self.dmg_bonus()
    def output_dmg(self):
        return round(self.weapon_pt * self.dmg_coefficient())
    def light_hit(self):
        return round(self.output_dmg() * 0.7)
    def medium_hit(self):
        return round(self.output_dmg() * 1.3)
    def mega_hit(self):
        return self.output_dmg() * 2
    def defence(self):
        return self.armor_pt + self.armour_bonus()


    def get_name(self):
        """Функция возвращает Имя"""
        return self.name
    def show_chr(self):
        """Функция печатает описание"""
        print(f"----------------------------------------------------------------------------------------------------------------------------------\n"
              f"Вас зовут: {self.name}, кол-во ваших очков здоровья: {self.current_hp()}, на вас ваш доспех: {self.armor}, амулет на шее: {self.amulet}\n"
              f"Ваше основное оружие: {self.weapon}, содержимое вашей сумки: Свитки: {self.inventar['Свитки']}, Зелья:{self.inventar['Зелья']}\n"
              f"-----------------------------------------------------------------------------------------------------------------------------------\n")
    def get_devparam(self):
        print(f"Ср.урон - {self.output_dmg()},Коэф.урона - {self.dmg_coefficient()}, урон текущег оружия - {self.weapon_pt}, защита - {self.defence()}\n"
              f"амулет здоровье - {self.health_bonus()}, амулет броня - {self.armour_bonus()}, амулет повржд - {self.dmg_bonus()}, am - {self.amulet}\n"
              f"x - {self.light_hit()}, y - {self.medium_hit()}, z - {self.mega_hit()} {self.amulet_pt}")
    def inventar_use(self):
        """Функция позволяет использовать предмет из инвентаря"""
        if self.inventar["Свитки"] > 0 and self.inventar["Зелья"] > 0:
            print(f"У вас в сумке: cвитки - {self.inventar['Свитки']}, зелья - {self.inventar['Зелья']}, что хотите использовать?")
            c1 = int(input("Введите 1 - для свитка, 2 - для зелья, 3 - если передумали: "))
            if c1 == 1:
                self.inventar["Свитки"] -= 1
                return 1 # нанести 20 урона врагу
            elif c1 == 2:
                self.inventar["Зелья"] -= 1
                print(f"Вы чувстуете себя намного лучше.")
                return 20
            else:
                pass
        elif self.inventar["Свитки"] <= 0 and self.inventar["Зелья"] > 0:
            print(f"У вас в сумке: cвитков нет, зелья - {self.inventar['Зелья']}, хотите выпить зелье?")
            c1 = int(input("Введите 1 - если да, 2 если нет: "))
            if c1 == 1:
                self.inventar["Зелья"] -= 1
                print(f"Вы чувстуете себя намного лучше.")
                return 20
            elif c1 == 2:
                pass
        elif self.inventar["Свитки"] > 0 and self.inventar["Зелья"] <= 0:
            print(f"У вас в сумке: зелий нет, свитки - {self.inventar['Свитки']}, хотите прочитать свиток?")
            c1 = int(input("Введите 1 - если да, 2 если нет: "))
            if c1 == 1:
                self.inventar["Свитки"] -= 1
                print("Как только вы начинаете читать заклинание, ваш голос меняется, слова будто произносят себя сами.\nЧерез мгновение, во врага ударяет заряд электричества, а свиток рассыпатеся в ваших руках")
                return 1 # нанести 10* урона врагу
            elif c1 == 2:
                pass
        else:
            print(f"Извини {self.name}, но сумка пуста, ничего нет..")
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
        if  set([*weapons.keys()]) & set([*self.content.keys()]): #сравниваем содержимое сундука и список оружия
            current_weapon_in_chest = list(set([*weapons.keys()]) & set([*self.content.keys()])) #если есть совпадение, сохраняем переменную
            print(f"Взять {set([*weapons.keys()]) & set([*self.content.keys()])} вместо своего текущего оружия? Сейчас у вас {self.player.weapon}.")
            k = int(input("1. Выглядит лучше моего..\n2. Нет, лучше оставлю свое.\n")) #выбираем поменять ли текущее
            if k == 1: #тут происходит перезаписывание текущего и его хар-ки
                weapon_key = current_weapon_in_chest.pop()
                self.player.weapon_pt = weapons[weapon_key][0]
                self.player.weapon = weapon_key
                print(f"Теперь {self.player.weapon} - ваше основное оружие!")
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
            else:
                pass
        print(self.content)
        if "Свитки" in self.content:
            self.player.inventar['Свитки'] += self.content["Свитки"]
            print(f"Свитки вы убрали в сумку, теперь у вас: cвитки - {self.player.inventar['Свитки']} шт.")
        else:
            pass
        if "Зелья" in self.content:
            self.player.inventar['Зелья'] += self.content["Зелья"]
            print(f"Зелья вы убрали в сумку, теперь у вас: зелья: - {self.player.inventar['Зелья']} шт.")
        else:
            pass



def fight_with_enemy(player, enemy):
    made_attack = 0
    player_hp = player.current_hp()
    player_defence = player.defence()
    def inner_player_hp_checker():
        if 0 < player_hp < 10:
            print("Критический уровень здоровья!")
            return 1
        elif player_hp > 10:
            return 1
        else:
            print("Вы умерли, земля вам пухом...")
            return 0
    def inner_enemy_hit():
        hit = enemy.new_hit()
        check_for_luck_enemy = randint(1, 100)
        if check_for_luck_enemy > 30 + player.agi: #шанс попасть
            if randint(0, 9) == 9:
                hit += hit
                hit = round(hit - (hit * (player_defence / 100)))
                print(f"{enemy.name} сделал обманный вапад и нанес вам можный удар в голову, на {hit} повреждений!")
                return hit
            hit = round(hit - (hit * (player_defence / 100)))
            print(f"{enemy.name} яростно вращая глазами, смог ударить вас на {hit} повреждений.")
            return hit
        elif check_for_luck_enemy <= 30 + player.agi: #шанс промазать
            if randint(0,1) == 1:
                print(f"{enemy.name} замахнулся, и попытался оглушить вас, но вы мастерски заблокировали удар!")
                return 0
            else:
                print(f"{enemy.name} набросился, но вы ловко увернулись из-под удара!")
                return 0
    while enemy.base_hp > 0 and player_hp > 0:
        print(f"......................................................................................................\n"
              f"Остаток очков здоровья врага - {enemy.base_hp}")
        make_hit = int(input(f"Остаток ваших очков здоровья {player_hp}.\nЖелаете ударить врага?\n 1 - Да. \n 2 - Нет.\n"))
        if make_hit == 1:
            made_attack += 1
            what_hit = int(input("Как будем убивать?\n"
                                 "1. Попытаться ударить по конечностям.\n"
                                 "2. Попытаться нанести удар в туловище\n"
                                 "3. Попытаться врезать по голове\n"))
            if what_hit == 1:  #вариант слабый удар
                check_for_luck = randint(1,100)
                if check_for_luck >= 20 + enemy.agi:
                    damage = player.light_hit()
                    final_damage = round((damage - (damage * (enemy.defence / 100))) * (randint(50, 150)/100))
                    if randint(1,5) == 4:
                        final_damage = final_damage * 3
                        enemy.base_hp -= final_damage
                        print(f"Вы почувствовали прилив ярости и нанесли сокрушительный удар {enemy.name} на {final_damage} урона, у него осталось {enemy.base_hp} жизни")
                        if enemy.base_hp <= 0:
                            print(f"Вы убили {enemy.name}")
                            return 1
                        else:
                            player_hp = player_hp - inner_enemy_hit()
                            if inner_player_hp_checker() == 0:
                                return 0
                    else:
                        enemy.base_hp -= final_damage
                        print(f"Вы ударили {enemy.name} на {final_damage} урона, у него осталось {enemy.base_hp} жизни")
                        if enemy.base_hp <= 0:
                            print(f"Вы убили {enemy.name}")
                            return player_hp
                        else:
                            player_hp = player_hp - inner_enemy_hit()
                            if inner_player_hp_checker() == 0:
                                return 0
                if check_for_luck < 20 + enemy.agi:
                    if randint(1,2) == 1:
                        print(f"{enemy.name} смог заблокировать ваш удар!")
                        player_hp = player_hp - inner_enemy_hit()
                        if inner_player_hp_checker() == 0:
                            return 0
                    else:
                        print(f"{enemy.name} смог увернуться от вашего удара!")
                        player_hp = player_hp - inner_enemy_hit()
                        if inner_player_hp_checker() == 0:
                            return 0
            if what_hit == 2: #вариант средний удар
                check_for_luck = randint(1, 100)
                if check_for_luck >= 50 + enemy.agi:
                    damage = player.medium_hit()
                    final_damage = round((damage - (damage * (enemy.defence / 100))) * (randint(50, 150) / 100))
                    if randint(1,6) == 6:
                        final_damage = final_damage * 3
                        enemy.base_hp -= final_damage
                        print(f"Вы почувствовали прилив ярости и нанесли сокрушительный удар {enemy.name} на {final_damage} урона, у него осталось {enemy.base_hp} жизни")
                        if enemy.base_hp <= 0:
                            print(f"Вы убили {enemy.name}")
                            return player_hp
                        else:
                            player_hp = player_hp - inner_enemy_hit()
                            if inner_player_hp_checker() == 0:
                                return 0
                    else:
                        enemy.base_hp -= final_damage
                        print(f"Вы ударили {enemy.name} на {final_damage} урона, у него осталось {enemy.base_hp} жизни")
                        if enemy.base_hp <= 0:
                            print(f"Вы убили {enemy.name}")
                            return player_hp
                        else:
                            player_hp = player_hp - inner_enemy_hit()
                            if inner_player_hp_checker() == 0:
                                return 0
                if check_for_luck < 50 + enemy.agi:
                    if randint(1, 2) == 1:
                        print(f"{enemy.name} смог заблокировать ваш удар!")
                        player_hp = player_hp - inner_enemy_hit()
                        if inner_player_hp_checker() == 0:
                            return 0
                    else:
                        print(f"{enemy.name} смог увернуться от вашего удара!")
                        player_hp = player_hp - inner_enemy_hit()
                        if inner_player_hp_checker() == 0:
                            return 0
            if what_hit == 3: # сильный удар
                check_for_luck = randint(1, 100)
                if check_for_luck <= 25 + enemy.agi: # шанс попасть 25
                    damage = player.mega_hit()
                    final_damage = round((damage - (damage * (enemy.defence / 100))) * (randint(50, 150) / 100))
                    if randint(1, 5) == 5: # проверка на крит
                        final_damage = final_damage * 2
                        if randint(1, 3) == 3: # мегакрит
                            final_damage = final_damage * 2
                            enemy.base_hp -= final_damage
                            print(f"Вы почувствовали прилив ярости и нанесли сокрушительный удар {enemy.name} на {final_damage} урона, у него осталось {enemy.base_hp} жизни")
                            if enemy.base_hp <= 0:
                                print(f"Вы убили {enemy.name}")
                                return player_hp
                            else:
                                player_hp = player_hp - inner_enemy_hit()
                                if inner_player_hp_checker() == 0:
                                    return 0
                        else: # выполняем простой крит
                            enemy.base_hp -= final_damage
                            print(f"Вы нанесли мощный удар {enemy.name} на {final_damage} урона, у него осталось {enemy.base_hp} жизни")
                            if enemy.base_hp <= 0:
                                print(f"Вы убили {enemy.name}")
                                return player_hp
                            else:
                                player_hp = player_hp - inner_enemy_hit()
                                if inner_player_hp_checker() == 0:
                                    return 0
                        if enemy.base_hp <= 0:
                            print(f"Вы убили {enemy.name}")
                            return player_hp
                    elif what_hit == 3: # выполняем сильный удар
                        enemy.base_hp -= final_damage
                        print(f"Вы ударили {enemy.name} на {final_damage} урона, у него осталось {enemy.base_hp} жизни")
                        if enemy.base_hp <= 0:
                            print(f"Вы убили {enemy.name}")
                            return player_hp
                        else:
                            player_hp = player_hp - inner_enemy_hit()
                            if inner_player_hp_checker() == 0:
                                return 0
                if check_for_luck > 25 + enemy.agi:
                    if randint(1, 2) == 1:
                        print(f"{enemy.name} смог заблокировать ваш удар!")
                        player_hp = player_hp - inner_enemy_hit()
                        if inner_player_hp_checker() == 0:
                            return 0
                    else:
                        print(f"{enemy.name} смог увернуться от вашего удара!")
                        player_hp = player_hp - inner_enemy_hit()
                        if inner_player_hp_checker() == 0:
                            return 0
        else:
            action = int(input(f"Что будем делать?\n"
                               f"1. Выпить зелье или прочитать свиток.\n"
                               f"2. Попытаться убежать.\n"
                               f"3. Попытаться вступить в переговоры.\n"
                               f"4. Внимательно осмотреть врага\n"
                               f"5. Я передумал, хочу сражаться!\n"))
            if action == 1: #пьем зелье #читаем свиток
                use_item = player.inventar_use()
                if use_item == 20:
                    player_hp += 20
                    player_hp = player_hp - inner_enemy_hit()
                    if inner_player_hp_checker() == 0:
                        return 0
                elif use_item == 1:
                    enemy.base_hp -= round(10 * (player.int / 10))
                    if enemy.base_hp <= 0:
                        print(f"Вы убили {enemy.name}")
                        return player_hp
                    else:
                        print(f"{enemy.name} корчится от боли, ошарашенно вращая глазами\n")
                        pass
            elif action == 2: #побег
                pass
            elif action == 3: #переговоры
                action = int(input(f"Что сказать?\n"
                                   f"1. Извините, Вы не подскажете, как пройти в библиотеку?\n"
                                   f"2. Слушай, друг... Не хотелось бы тебя убивать. А ты хочешь помирать?\n"
                                   f"3. Эй ты, чертов {enemy.get_class_name()}, либо сдавайся, либо я выпущу твои кишки.\n"))
                if action == 1: #библиотека #1,2
                    if made_attack == 0: #не было насилия
                        if enemy.mood == 0:#нейтрально
                            print(enemy.enemy_mood[1])
                            action = int(input(f"Что сказать?\n"
                                               f"1. Я не ошибся, когда увидел интелект в ваших глазах!\n"
                                               f"2. Хм... нет, я передумал.\n"))
                            if action == 1:
                                return "friendship"
                            if action == 2:
                                pass
                        if enemy.mood == 1:#недруг
                            print(enemy.enemy_mood[1])
                        if enemy.mood == 2:#враг
                            print(enemy.enemy_mood[1])
                        if enemy.mood == 3:#кровожадный
                            print(enemy.enemy_mood[2])
                            action = int(input(f"Что выбрать?\n"
                                               f"1. Посмотреть куда указывает {enemy.name}!\n"
                                               f"2. Хм... нет, я передумал.\n"))
                            if action == 1:
                                player_hp = player_hp - 500
                                print("Вы почувствовали мощный удар в затылок, затем свет погас..")
                                if inner_player_hp_checker() == 0:
                                    return 0
                            if action == 2:
                                pass
                    if made_attack > 0: #было насилие
                        if enemy.mood == 0: #нейтрально
                            print(enemy.enemy_mood[2])
                            action = int(input(f"Что сказать?\n"
                                               f"1. Я приношу вам глубочайшие извинения {enemy.name}!\n"
                                               f"2. Хм... ну как хочешь.\n"))
                            if action == 1:
                                print(enemy.enemy_mood[3])
                                return "friendship"
                            if action == 2:
                                pass
                        if enemy.mood == 1: #недруг
                            print(enemy.enemy_mood[2])
                            player_hp = player_hp - inner_enemy_hit()
                            if inner_player_hp_checker() == 0:
                                return 0
                        if enemy.mood == 2: #враг
                            print(enemy.enemy_mood[2])
                            player_hp = player_hp - inner_enemy_hit()
                            if inner_player_hp_checker() == 0:
                                return 0
                        if enemy.mood == 3: #кровожадный
                            print(enemy.enemy_mood[2])
                            action = int(input(f"Что выбрать?\n"
                                               f"1. Посмотреть куда указывает {enemy.name}!\n"
                                               f"2. Хм... нет, я передумал.\n"))
                            if action == 1:
                                player_hp = player_hp - 500
                                print("Вы почувствовали мощный удар в затылок, затем свет погас..")
                                if inner_player_hp_checker() == 0:
                                    return 0
                            if action == 2:
                                pass
                if action == 2: #мягкое предложение помириться
                    pass
                if action == 3: #жесткое предложение помириться
                    pass
            elif action == 5: #взад
                pass
            elif action == 4: #информация о враге
                action = int(input(f"Что рассмотреть поподробнее?\n"
                                   f"1. Оружие.\n"
                                   f"2. Броня.\n"
                                   f"3. Общая информация о {enemy.name}.\n"
                                   f"4. Назад\n"))
                if action == 1: #информация о оружии
                    print(f"{enemy.weapon[0]},\n{enemy.weapon[2]}")
                elif action == 2: #информация о броне
                    print(f"{enemy.base_armour},\n{enemy.armour_description}")
                elif action == 3: #информация в целом
                    print(enemy)
                elif action == 4:
                    pass



