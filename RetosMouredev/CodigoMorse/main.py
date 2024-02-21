"""
Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
- Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
- En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
- El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
 """

import re

# Diccionario del código Morse
codigo_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..- .', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
}

# Expresión regular del abecedario y números
abecedario_numeros = re.compile('[A-Z0-9]')


def traducir_texto(texto):
    """
    Traduce el texto automáticamente de natural a morse y viceversa
    """

    texto = texto.upper()
    texto_natural = bool(re.search(abecedario_numeros, texto))

    # Si el texto es natural
    if texto_natural:
        for letra in texto:

            # Separar palabras con doble espacio
            if letra == " ":
                print(end="  ")
            else:
                # Imprimir letras con espacio
                print(codigo_morse[letra], end=" ")

    # Si no lo es
    else:
        letras_naturales = []
        indice = 0

        # Listar palabras del texto
        texto_morse = [palabra for palabra in texto.split(" ")]

        for letra_morse in texto_morse:
            # Quitar doble espacio y añadir solo uno
            if letra_morse == "" and letra_morse in texto_morse[indice + 1] == "":
                letras_naturales.append(" ")
            else:
                # Añadir la clave correspondiente del diccionario
                for clave, valor in codigo_morse.items():
                    if letra_morse == valor:
                        letras_naturales.append(clave)
            # Aumentar indice para comprobar los dobles espacios
            indice += 1

        # Imprimir las letras naturales
        for letra_natural in letras_naturales:
            print(letra_natural.lower(), end="")


traducir_texto("- .-. .- -.. ..- -.-. .. .-.   - . -..- - ---   -.. .   .--. .-. ..- . -... .-")
print()
traducir_texto("Traducir texto de prueba")
