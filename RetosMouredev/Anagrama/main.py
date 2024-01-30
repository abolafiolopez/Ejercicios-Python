"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
"""


# Función del anagrama
def anagrama(string_1, string_2):

    lista_palabra_1 = [letra for letra in string_1]
    lista_palabra_2 = [letra for letra in string_2]

    if sorted(string_1) != sorted(string_2):

        return False

    else:

        for z in zip(lista_palabra_1, lista_palabra_2):

            if z[0] == z[1]:
                return False

        return True


palabra_1 = "lacteo"
palabra_2 = "coleta"

print(anagrama(palabra_1, palabra_2))
