from map import *
from random import randint
from classes_g import *
if __name__ == "__main__":
    height = 15
    width = 25
    level_map = matrix_make_tiles(height,width)
    player = Player("Гарри", 10, 10, 10, raw_hp=30, pos_xx = width, pos_yy = height)
    # chest = Chest(player)
    # chest.open_and_take()
    # player.show_chr()
    # player.get_devparam()
    # current_enemy = Goblin()
    # current_enemy.get_devparam()
    # fight_with_enemy(player, current_enemy)
    # path = make_path_in_out(level_map)
    # path2 = make_path_in_out(level_map)
    # path.extend(path2)
    # print(path)

    level_map, path = map_generator3(level_map)
    print(f"результат {path}")
    # matrix_print(level_map)
    for i, j in enumerate(level_map):
        for z, l in enumerate(j):
            if level_map[i][z].digger_was_here == True:
                level_map[i][z].wall = "ˍ ˍ"
            else:
                level_map[i][z].wall = "▓▓▓"

    # for i, j in enumerate(level_map):
    #     for z, l in enumerate(j):
    #         print(level_map[i][z], end="")
    #     print()
    # for i, j in enumerate(level_map):
    #     for z, l in enumerate(j):
    #         print(level_map[i][z].digger_was_here, end="")
    #     print()
    player_move(player,level_map)




