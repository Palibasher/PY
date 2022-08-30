from classes_g import Chest
from classes_g import Player
from random import randint
from classes_g import Enemy
from classes_g import Goblin
from classes_g import Spicked_frog
if __name__ == "__main__":
    i = 1
    player = Player("Гарри", 10, 10, 10)
    while i != 0:
        chest = Chest(player)
        chest.opening_chest()
        chest.take_items()
        player.show_chr()
        player.get_devparam()
        i = int(input("0 для Стоп\n"))

    # frog = Spicked_frog()
    # frog.get_devparam()
    # frog.new_hit()
    # frog.get_devparam()
    # frog.new_hit()
    # frog.get_devparam()
    # Gobl = Goblin("Бабиус")
    # Gobl.get_devparam()
    # Gobl.new_hit()
    # Gobl.get_devparam()
    # Gobl.new_hit()
    # Gobl.get_devparam()
goblin_weapons = {"Лапы": [5, "Гоблинские лапы с огромными острыми ногтями."]}
print(goblin_weapons["Лапы"][0])
print([*goblin_weapons.keys()][randint(0,0)])
print(goblin_weapons[[*goblin_weapons.keys()][randint(0,0)]][0])


