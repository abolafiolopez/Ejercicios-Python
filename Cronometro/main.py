def dos_digitos(digito):
    digito = str(digito)
    if len(digito) == 1:
        digito = "0" + digito

    return digito

print(dos_digitos(24))
class Timer:
    def __init__(self, horas=0, minutos=0, segundos=0):
        self.__horas = horas
        self.__minutos = minutos
        self.__segundos = segundos

    def __str__(self):
        return (f"{dos_digitos(self.__horas)}:"
                f"{dos_digitos(self.__minutos)}:"
                f"{dos_digitos(self.__segundos)}")

    def next_second(self):
        self.__segundos += 1
        if self.__segundos == 60:
            self.__minutos += 1
            self.__segundos = 0
            if self.__minutos == 60:
                self.__horas += 1
                self.__minutos = 0
                if self.__horas == 24:
                    self.__horas = 0
                    self.__minutos = 0
                    self.__segundos = 0

    def prev_second(self):
        self.__segundos -= 1
        if self.__segundos == -1:
            self.__minutos -=1
            self.__segundos = 59
            if self.__minutos == -1:
                self.__horas -= 1
                self.__minutos = 59
                if self.__horas == -1:
                    self.__horas = 23
                    self.__minutos = 59
                    self.__segundos = 59


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
timer.prev_second()
print(timer)
timer.prev_second()
print(timer)
timer.next_second()
print(timer)
timer.next_second()
print(timer)
timer.next_second()
print(timer)
timer.next_second()
print(timer)
