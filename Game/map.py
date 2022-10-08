from random import randint

class Tile():
    def __init__(self, x, y, wall = "  ", state = 1, situation = 0, was_here = False, digger_was_here = False):
        self.x = x
        self.y = y
        self.state = state
        self.situation = situation
        self.was_here = was_here
        self.digger_was_here = digger_was_here
        self.wall = wall

    def __str__(self):
        return f"{self.wall}"

def matrix_print(matrix):
    for i, j in enumerate(matrix):
        for z, l in enumerate(j):
            print(matrix[i][z], end="")
        print()
# def matrix_print_dig(matrix):
#     for i, j in enumerate(matrix):
#         for z, l in enumerate(j):
#             print(matrix[i][z].digger_was_here, end="")
#         print()

def matrix_make_tiles(height, width, a = 0):
    lvlmap = [[a for i in range(width)] for j in range(height)]
    for i, j in enumerate(lvlmap):
        for z, l in enumerate(j):
            lvlmap[i][z] = Tile(i,z)
    return lvlmap


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









