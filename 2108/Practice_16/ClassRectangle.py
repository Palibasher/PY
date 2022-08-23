class Rectangle:
    """Классы прямоугольников, с соответствующими характеристиками"""
    def __init__(self, x, y, wight, height):
        """Задаем шикину и длину, а так же координаты х, у"""
        self.wight = wight
        self.height = height
        self.x = x
        self.y = y
        self.Area = self.wight * self.height

    def __str__(self):
        """Функция выводит информацию по принту"""
        return f"Ширина - {self.wight}, длина - {self.height}, координаты x,y = {self.x}, {self.y}, {self.Area}"

    def GetWight(self):
        """Функция возвращает ширину"""
        return self.wight

    def GetHeight(self):
        """Функция возвращает длину"""
        return self.height

    def GetArea(self):
        """Функция возвращает площадь"""
        Area = self.wight * self.height
        return Area
