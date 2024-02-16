"""
Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final
de todas ellas.
- Los signos de puntuación no forman parte de la palabra.
- Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
- No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
"""

# Importaciones
import re


def eliminar_signos():
    """
    Elimina los signos de puntuación del texto ingresado
    """
    # Ingresar el texto
    texto = input("Ingrese un texto: ")

    # Reemplazar carácter especial por una cadena vacía
    texto_limpio = re.sub("[^a-zA-Z0-9]", " ", texto).strip()
    return texto_limpio.lower()


def contar_palabras_y_repeticiones(texto_limpio):
    """
    Obtiene las palabras y repeticiones a partir del texto limpio
    """
    palabras_y_repeticiones = {}

    # Listar palabras del texto sin espacios
    palabras = texto_limpio.split(" ")

    # Agregar las palabras y repeticiones al diccionario
    for palabra in palabras:
        if palabra in palabras_y_repeticiones:
            palabras_y_repeticiones[palabra] += 1
        else:
            palabras_y_repeticiones[palabra] = 1

    # Contar palabras repetidas
    for key, value in palabras_y_repeticiones.items():
        if value == 1:
            print(f"La palabra {key} se repite {value} vez")
        elif value >= 2:
            print(f"La palabra {key} se repite {value} veces")


contar_palabras_y_repeticiones(eliminar_signos())
