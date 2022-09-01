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
    def __init__(self, name, str, base_hp, agi, class_name = "Общий класс врага", armour = ["Броня", 5], weapon = ["Оружие", 0], weapon_pt = 0):
        self.class_name = class_name
        self.name = name #имя врага
        self.str = str # сила
        self.base_hp = base_hp # базовый хп
        self.base_armour = armour[0] # броня монстра
        self.defence = armour[1] #защита брони
        self.agi = agi #ловкость
        self.weapon = weapon
        self.weapon_pt = self.weapon[1] #урон оружия
        self.weapon_description = self.weapon[2]
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



class Spicked_frog(Enemy):
    """Класс лягушки"""
    def __init__(self):
        super().__init__(name = "Огромная лягушка", class_name="Лягуха", str = 10, base_hp =50, agi = 30, armour = ["Шкура", 5], weapon = ["Лапы", 5, "Лягушачьи лапки: вкусно, но лягушка так просто их не отдаст"])

class Goblin(Enemy):
    """Класс гоблинс"""
    def __init__(self, name):
        weapons_list = {"Лапы": [5, "Гоблинские лапы с огромными острыми ногтями."],
                        "Камни": [6, "Негодяй собрался бросаться камнями."],
                        "Тупой кинжал": [7, "Ржавый и тупой кинжал."],
                        "Дубинка": [8, "Гоблин играет в бейсбол? Скорее всего нет..."],
                        "Дубинка с шипами": [9, "Выглядит опасно и это точно не для бейсбола."],
                        "Топор мясника": [10, "Средних размеров топор для разделки мяса."],
                        "Плетка": [5, "Что этот гоблин задумал?."],
                        "Копье": [5, "Копье слишком велико для гоблина, вряд ли сможет нанести им много урона."],
                        "Нож": [8, "Хочешь знать, почему я использую нож? Пушки слишком быстры, не успеваешь насладиться, получить истинное удовольствие, а когда я использую нож,\nв этот самый последний момент раскрывается ВСЯ человеческая сущность, и в каком-то смысле я знаю твоих друзей лучше, чем ты."],}
        a = randint(0, 8)
        super().__init__(name, class_name="Гоблин", str = 10, base_hp =50, agi = -5, armour = ["Стеганная броня", 7], weapon = [[*weapons_list.keys()][a], weapons_list[[*weapons_list.keys()][a]][0], weapons_list[[*weapons_list.keys()][a]][1]])


class Player:
    """Класс для Игрока"""
    def __init__(self, name, raw_str, raw_int, raw_agi, luck = 0 , amulet = ["Веревочка",[2, 0, 0, 0, 0, 0]], armor = ["Рваная рубаха", 2], weapon = ["Руки", 5], raw_hp = 100):
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
    player = player
    enemy = enemy
    player_hp = player.current_hp()
    accumulative_dmg = 0
    while enemy.base_hp > 0 and player_hp > 0:
        print(f"Враг = {enemy.name}, здоровье врага - {enemy.base_hp}\n")
        make_hit = int(input("Желаете ударить врага?\n 1 - Да. \n 2 - Нет.\n"))
        if make_hit == 1:
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
                    else:
                        enemy.base_hp -= final_damage
                        print(f"Вы ударили {enemy.name} на {final_damage} урона, у него осталось {enemy.base_hp} жизни")
                        if enemy.base_hp <= 0:
                            print(f"Вы убили {enemy.name}")
                if check_for_luck < 20 + enemy.agi:
                    if randint(1,2) == 1:
                        print(f"{enemy.name} смог заблокировать ваш удар!")
                    else:
                        print(f"{enemy.name} смог увернуться от вашего удара!")
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
                            break
                    else:
                        enemy.base_hp -= final_damage
                        print(f"Вы ударили {enemy.name} на {final_damage} урона, у него осталось {enemy.base_hp} жизни")
                        if enemy.base_hp <= 0:
                            print(f"Вы убили {enemy.name}")
                            break
                if check_for_luck < 50 + enemy.agi:
                    if randint(1, 2) == 1:
                        print(f"{enemy.name} смог заблокировать ваш удар!")
                    else:
                        print(f"{enemy.name} смог увернуться от вашего удара!")
            if what_hit == 3: # сильный удар
                check_for_luck = randint(1, 100)
                if check_for_luck >= 25 + enemy.agi: # шанс попасть 25
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
                                break
                        else: # выполняем простой крит
                            enemy.base_hp -= final_damage
                            print(f"Вы нанесли мощный удар {enemy.name} на {final_damage} урона, у него осталось {enemy.base_hp} жизни")
                            if enemy.base_hp <= 0:
                                print(f"Вы убили {enemy.name}")
                                break
                        if enemy.base_hp <= 0:
                            print(f"Вы убили {enemy.name}")
                            break
                    else: # выполняем сильный удар
                        enemy.base_hp -= final_damage
                        print(f"Вы ударили {enemy.name} на {final_damage} урона, у него осталось {enemy.base_hp} жизни")
                        if enemy.base_hp <= 0:
                            print(f"Вы убили {enemy.name}")
                            break
                if check_for_luck < 25 + enemy.agi:
                    if randint(1, 2) == 1:
                        print(f"{enemy.name} смог заблокировать ваш удар!")
                    else:
                        print(f"{enemy.name} смог увернуться от вашего удара!")


        #     if enemy.base_hp > 0:
        #         enemy_hit = enemy.new_hit()
        #         player_hp -= enemy_hit
        #         accumulative_dmg += enemy_hit #Важно!! Не запутаться с уроном после применения всех коэффициэнтов
        #         print(f"{enemy.name} ударил вас, нанес {enemy_hit} урона, у вас осталось {player_hp}")
        #         if player_hp < 0:
        #             print("Похоже вы убиты")
        #         pass
        #     elif enemy.base_hp <= 0:
        #         print(f"{enemy.name} убит!")
        #         break
        # else:
        #     enemy_hit = enemy.new_hit()
        #     player_hp -= enemy_hit
        #     accumulative_dmg += enemy_hit
        #     print(f"{enemy.name} ударил вас, нанес {enemy_hit} урона, у вас осталось {player_hp}")
        #     if player_hp < 0:
        #         print("Похоже вы убиты")


