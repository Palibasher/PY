class Cat:
    """Класс для кошек"""
    def __init__(self, name, sex, age):
        """Задаем имя, пол, возраст"""
        self.name = name
        self.sex = sex
        self.age = age
    def __str__(self):
        return f"{self.name}"

    def Get_name(self):
        """Функция возвращает Имя"""
        return self.name

    def Get_sex(self):
        """Функция возвращает Пол"""
        return self.sex

    def Get_age(self):
        """Функция возвращает Возраст"""
        return self.age
