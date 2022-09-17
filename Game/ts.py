from map import *
from random import randint
from classes_g import *
if __name__ == "__main__":
    height = 10
    width = 5
    level_map = matrix_make_tiles(height,width)
    player = Player("Гарри", 10, 10, 10, raw_hp=30, pos_xx = width, pos_yy = height)
    # chest = Chest(player)
    # chest.open_and_take()
    # player.show_chr()
    # player.get_devparam()
    # current_enemy = Goblin()
    # current_enemy.get_devparam()
    # fight_with_enemy(player, current_enemy)
    path = make_path_in_out(level_map)
    print(path)
    matrix_1 = [[" " for i in range(height)] for j in range(width)]
    for i, j in enumerate(matrix_1):
        for z, l in enumerate(j):
            hello = (i, z)
            if hello in path:
                matrix_1[i][z] = "#"
            else:
                matrix_1[i][z] = f"_"
    for arr in range(len(matrix_1)):
        print(matrix_1[arr])


    # player_move(player, level_map)






