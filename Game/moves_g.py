def fight1(enemy):
    count = 0
    p = 0
    print(f"Вам встретился {enemy}, он настроен кровожадно по отношению к вам,\nвы это поняли, глядя как он злобно вращает налитыми кровью глазами.\n")
    while enemy.hp > 0 and p != 1:
        p_hit = input("Насколько сильно ударить?  Напишите: Ебануть со всей силы, сильно или дать пощечину:\n")
        p_hit = p_hit.lower()
        if p_hit == "ебануть со всей силы":
            p_hit = 10
            enemy.hp = enemy.hp - p_hit
            if enemy.hp > 0:
                print(f"Вы ударили {enemy.name}, доставили ему {p_hit} урона и у него осталось {enemy.hp}")
            else:
                print("О да!")
        elif p_hit == "сильно":
            p_hit = 5
            enemy.hp = enemy.hp - p_hit
            if enemy.hp > 0:
                print(f"Вы ударили {enemy.name}, доставили ему {p_hit} урона и у него осталось {enemy.hp}")
            else:
                print("О да!")
        elif p_hit == "дать пощечину":
            print("Вы только разозлили гоблинца еще больше")
            count += 1
            if count == 2:
                print(f"{enemy.name} разозлился так сильно, что убил вас")
                p = 1
    if p == 0:
        print(
            f"Вы убили {enemy.name}, мать вашу! А потом заметили, что глаза у него не были налиты кровью, а он просто\nносил очки красного цвета. Что же вы наделали?")
    else:
        print("Вы умерле жидко пукнув")