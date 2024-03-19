"""
Crea una función que reciba dos cadenas como parámetro (str1, str2)
e imprima otras dos cadenas como salida (out1, out2).
- out1 contendrá todos los caracteres presentes en la str1 pero NO
estén presentes en str2.
- out2 contendrá todos los caracteres presentes en la str2 pero NO
estén presentes en str1.
"""


def salidas(cadena_1, cadena_2):

    unicos_1 = []
    unicos_2 = []

    for c in cadena_1.lower():
        if c not in cadena_2 and c not in unicos_1:
            unicos_1.append(c)

    for c in cadena_2.lower():
        if c not in cadena_1 and c not in unicos_2:
            unicos_2.append(c)

    return unicos_1, unicos_2


cadena_1 = "Esto es una prueba"
cadena_2 = "De caracteres diferentes"

print(salidas(cadena_1, cadena_2))
