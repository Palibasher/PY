class client:
    """Класс клиента в Доме питомца"""
    def __init__(self, fname, lname, city, balance):
        self.fname = fname
        self.lname = lname
        self.city = city
        self.balance = balance
    def __str__(self):
        """Функция выводит информацию по принту"""
        return f"{self.lname} {self.fname}. {self.city}. Баланс: {self.balance}"
    def getinfo1(self):
        Info1 = [self.lname, self.fname, self.city]
        return Info1