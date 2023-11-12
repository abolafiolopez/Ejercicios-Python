"""
Este es el módulo con los generadores y decorador
"""


def turno_farmacia():
    """
    Generaddor de turnos farmacia
    """
    turno = 1

    while True:

        yield f"F - {turno}"
        turno += 1


def turno_perfumeria():
    """
    Generador de turnos perfumeria
    """

    turno = 1

    while True:
        yield f"P - {turno}"
        turno += 1


def turno_cosmetica():
    """
    Generador de turnos cosmética
    """
    turno = 1

    while True:
        yield f"C - {turno}"
        turno += 1


def decorador_de_turnos(generador):
    """
    Decorador para indicar el turno y área
    """

    def decorador():
        print("\nSu turno es:")
        print(next(generador))
        print("Espere a ser atendido\n")

    return decorador()
