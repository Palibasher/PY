import tkinter
from classes_g import *


class G_window():
    """Класс окно интерфейс"""
    def __init__(self, width, height, title, resizable = (False , False), icon = None):
        self.root = tkinter.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconphoto(False, tkinter.PhotoImage(file = icon))
        self.root.bind("<Key>", self.press_key)
    def run(self):
        self.root.mainloop()

    def press_key(self, event):
        print(event.keysym)
        if event.keysym == "Up":
            self.root.create_child_w(100,100,"Ha")
        elif event.keysym == "Down":
            pass
        elif event.keysym == "Left":
            pass
        elif event.keysym == "Right":
            pass






if __name__ == "__main__":
    w1 = G_window(800, 600, "Game", icon = "media\gob.png")

    w1.create_child_w(100,100,"hd")
    w1.run()


##скорее через игрока нужно обращаться к окну и получаот от окна ретурн, а на основе ответа делать мув


def gui_player_move_handler(player, window):
    def wrapper(lvlmap):
        move = player.make_move(lvlmap)
        if move == 1:
            pass
    return wrapper
