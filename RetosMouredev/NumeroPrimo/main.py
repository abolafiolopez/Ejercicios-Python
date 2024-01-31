"""
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""


def comprobar_primo(numero):

    if numero < 2:
        return False

    else:
        for n in range(2, numero):

            if numero % n == 0:
                return False

        return True


def rango_numeros_primos(rango):

    for n in range(rango):
        if comprobar_primo(n):
            print(n)


print(comprobar_primo(23))
rango_numeros_primos(100)
