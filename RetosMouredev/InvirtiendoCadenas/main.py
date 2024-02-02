"""
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""


def invertir_texto():

    texto = input("Ingrese el texto a invertir: ")
    indice = -1
    texto_invertido = ""

    for letra in texto:
        texto_invertido += texto[indice]
        indice -= 1

    print(texto_invertido)


invertir_texto()
