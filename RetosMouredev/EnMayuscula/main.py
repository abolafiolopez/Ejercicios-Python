"""
 * Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
"""

# Función para capitalizar la primera letra de una palabra si no lo está
def letra_en_mayuscula(palabra):

    palabra_mayuscula = ""

    for i, caracter in enumerate(palabra):
        if palabra[i].isalpha() and palabra[i].islower():
            palabra_mayuscula += caracter.upper() + palabra[i + 1:]
            return palabra_mayuscula
        elif palabra[i].isalpha() and palabra[i].isupper():
            palabra_mayuscula += palabra[i:]
            return palabra_mayuscula
        else:
            palabra_mayuscula += caracter


# Función para capitalizar la primera letra de cada palabra de un text
def en_mayuscula(texto):

    palabras = texto.split(" ")

    for i, palabra in enumerate(palabras):
        palabras[i] = letra_en_mayuscula(palabra)

    return " ".join(palabras)


print(en_mayuscula("¡hola! Esto, es una prueba"))
