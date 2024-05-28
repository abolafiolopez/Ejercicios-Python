class WeekDayError(Exception):
    pass


class Weeker:
    days_week = {"Lun": 1, "Mar": 2, "Mier": 3, "Jue": 4, "Vie": 5, "Sab": 6, "Dom": 7}

    def __init__(self, day):
        try:
            self.__day = self.days_week[day.capitalize()]
        except KeyError:
            raise WeekDayError

    def __str__(self):
        for c, v in self.days_week.items():
            if v == self.__day:
                return c

    def add_days(self, n):
        self.__day += n
        while self.__day > 7:
            self.__day -= 7

    def subtract_days(self, n):
        self.__day -= n
        while self.__day <= 0:
            self.__day += 7

try:
    weekday = Weeker('Lun')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Lunes')
except WeekDayError:
    print("Lo siento, no puedo atender tu solicitud.")


class WeekDayError(Exception):
    pass


class Weeker:
    __names = ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom']

    def __init__(self, day):
        try:
            self.__current = Weeker.__names.index(day)
        except ValueError:
            raise WeekDayError

    def __str__(self):
        return Weeker.__names[self.__current]

    def add_days(self, n):
        self.__current = (self.__current + n) % 7

    def subtract_days(self, n):
        self.__current = (self.__current - n) % 7


try:
    weekday = Weeker('Lun')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Lunes')
except WeekDayError:
    print("Lo siento, no puedo atender tu solicitud.")
