from classes_g import Chest
from classes_g import Player
from random import randint
from classes_g import Enemy
from classes_g import Goblin
from classes_g import Spicked_frog
from classes_g import fight_with_enemy
if __name__ == "__main__":
    i = 1
    player = Player("Гарри", 10, 10, 10, raw_hp=30)
    chest = Chest(player)
    chest.opening_chest()
    chest.take_items()
    player.show_chr()
    player.get_devparam()

    current_enemy = Goblin()
    current_enemy.get_devparam()
    fight_with_enemy(player, current_enemy)
    # while i != 0:
    #     chest = Chest(player)
    #     chest.opening_chest()
    #     chest.take_items()
    #     player.show_chr()
    #     player.get_devparam()
    #     i = int(input("0 для Стоп\n"))
    #
    # while i != 0:
    #     Gobl = Goblin("Бабиус")
    #     Gobl.get_devparam()
    #     Gobl.new_hit()
    #     i = int(input("0 для Стоп\n"))



