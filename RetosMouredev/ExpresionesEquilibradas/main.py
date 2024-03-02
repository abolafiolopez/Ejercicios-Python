"""
Crea un programa que comprueba si los paréntesis, llaves y corchetes
de una expresión están equilibrados.
- Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
- Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
- Expresión balanceada: { [ a * ( c + d ) ] - 5 }
- Expresión no balanceada: { a * ( c + d ) ] - 5 }
"""

expresion_balanceada = "{ [ a * ( c + d ) ] - 5 }"
expresion_no_balanceada = "{ a * ( c + d ) ] - 5 }"


# Función 1 para comprobar si la expresión está o no balanceada
def expresion_equilibrada_1(expresion):

    delimitadores = {"{": "}", "[": "]", "(": ")"}
    d_apertura = []
    d_cierre = []

    # Obtener delimitadores de apertura
    for caracter in expresion:
        if caracter in delimitadores.keys():
            d_apertura.append(caracter)

    # Obtener delimitadores de cierre
    for caracter in expresion:
        if caracter in delimitadores.values():
            d_cierre.insert(0, caracter)

    # Comparar delimitadores de apertura y cierre, o si no hay delimitadores en la expresión
    for apertura, cierre in zip(d_apertura, d_cierre):
        if delimitadores[apertura] != cierre or delimitadores == []:
            return False

    return True


print("*** Resultados con la función 1 ***")
print("Expresión balanceada:", expresion_equilibrada_1(expresion_balanceada))
print("Expresión no balanceada:", expresion_equilibrada_1(expresion_no_balanceada))


# Función 2 para comprobar si la expresión está o no balanceada (corregida)
def expresion_equilibrada_2(expresion):

    delimitadores = {"{": "}", "[": "]", "(": ")"}
    d_apertura = []

    # Obtener delimitadores de la expresión
    for caracter in expresion:
        # Comprobar si se encuentra en los limitadores de apertura
        if caracter in delimitadores:
            d_apertura.append(caracter)
        # Comprobar si se encuentra en los limitadores de cierre
        elif caracter in delimitadores.values():
            # Comprobar los delimitadores de apertura con los de cierre, o no hay
            if not d_apertura or delimitadores[d_apertura.pop()] != caracter:
                return False

    return True


print("*** Resultados con la función 2 ***")
print("Expresión balanceada:", expresion_equilibrada_2(expresion_balanceada))
print("Expresión no balanceada:", expresion_equilibrada_2(expresion_no_balanceada))
