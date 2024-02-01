"""
Crea una única función (importante que sólo sea una) que sea capaz
de calcular y retornar el área de un polígono.
La función recibirá por parámetro sólo UN polígono a la vez.
Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
Imprime el cálculo del área de un polígono de cada tipo.
"""


class Poligono:

    def area(self):
        pass

    def __str__(self):
        return type(self).__name__


class Triangulo(Poligono):

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2


class Cuadrado(Poligono):

    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado


class Rectangulo(Poligono):

    def __init__(self, altura, anchura):
        self.altura = altura
        self.anchura = anchura

    def area(self):
        return self.altura * self.anchura


def calcular_area(poligono):
    print(f"El aréa del {poligono} es {poligono.area()}")


calcular_area(Triangulo(10, 4))
calcular_area(Cuadrado(6))
calcular_area(Rectangulo(10, 4))
