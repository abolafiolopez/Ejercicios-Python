"""
Escribe una función que reciba un texto y retorne verdadero o
falso (Boolean) según sean o no palíndromos.
Un Palíndromo es una palabra o expresión que es igual si se lee
de izquierda a derecha que de derecha a izquierda.
NO se tienen en cuenta los espacios, signos de puntuación y tildes.
Ejemplo: Ana lleva al oso la avellana.
"""

import re
import unicodedata


def eliminar_signos(cadena):
    """
    Elimina los signos de puntuación del texto ingresado
    """

    # Normalizar texto NFD
    texto_nfd = unicodedata.normalize('NFD', cadena)

    # Reemplazar carácter especial por una cadena vacía
    texto_limpio = re.sub("[^a-zA-Z0-9]", "", texto_nfd)
    print(texto_limpio)
    return texto_limpio.lower()


def es_palindromo(cadena_limpia):
    """
    Verifica si la cadena o texto es un palindromo
    """

    i = -1

    # Comprobar cada letra con su reversa
    for c in cadena_limpia:
        if c == cadena_limpia[i]:
            i -= 1
        else:
            return False

    return True


cadena = input("Ingrese un texto: ")
cadena_limpia = eliminar_signos(cadena)
print(es_palindromo(cadena_limpia))
