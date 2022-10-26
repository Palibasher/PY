from map import matrix_make_tiles, map_generator3, map_generator2, add_chest_to_map, add_random_to_map
from random import randint
from classes_g import *
from GUI import *

if __name__ == "__main__":
    height = 15
    width = 25
    level_map = matrix_make_tiles(height,width)
    player = Player("Гарри", 100, 100, 100, raw_hp= 50, pos_xx = width, pos_yy = height)


    level_map, path = map_generator3(level_map) # генерация карты из пустого канваса объектов класса тайл
    chest_positions = add_chest_to_map(level_map, path) # генерация сундуков в тайлах, которые соотвествуют пустому проходу
    random_stuff_position = add_random_to_map(level_map, path, chest_positions)
    print(chest_positions)
    print(random_stuff_position)
    # gui_window = G_window(800, 600, "Game", icon="media\gob.png")
    # gui_window.run()
    # gui_window.press_key()
    player_move(player,level_map, chest_positions, random_stuff_position)

