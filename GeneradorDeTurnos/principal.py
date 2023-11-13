import turnos
from os import system

# Areas de la Farmacia
areas = {"Farmacia": turnos.turno_farmacia(), "Perfumeria": turnos.turno_perfumeria(), "Cosmética":turnos.turno_cosmetica()}
numero_areas = len(areas)


def listar_areas():
    """
    Función para crear el desplegable con las áreas
    """
    indice = 1
    for area in areas.keys():
        print(f"[{indice}] - {area}")
        indice += 1


def elegir_area():
    """
    Función para elegir el área
    """
    # Bucle para iniciar la elección
    while True:
        listar_areas()
        # Intenta comprobar si el valor insertado es un número
        try:
            eleccion = int(input("\nElige el número del áera que deseas: "))
            # Comprueba si el numero se encuentra en el rango de áreas disponibles
            if eleccion in range(1, numero_areas + 1):
                return list(areas)[eleccion - 1]
            else:
                print("No has seleccionado un número correcto\n")
        # En caso de no ser un número devuelve que no es correcto
        except ValueError:
            print("No has seleccionado un número correcto\n")


def otro_turno():
    """
    Función para preguntar si quiere otro turno o no
    """
    # Bucle para preguntar si quiere otro turno
    while True:
        print("\nQuieres sacar otro turno?\n[S] - Sí\n[N] - No")
        # Validar otro turno
        try:
            otro_turno = input("\nElige una opción: ").lower()
            ["s", "n"].index(otro_turno)
        except ValueError:
            print("No has elegido una opción correcta")
        else:
            return otro_turno


# Función para iniciar la aplicación
def inicio():
    """
    Función para iniciar el programa
    """
    # Bucle para iniciar la función
    while True:
        system("cls")
        print("Bienvenid@ a Farmacia Lizanus")
        print("Estas son nuestras áreas\n")
        area_elegida = elegir_area()
        turnos.decorador_de_turnos(areas[area_elegida])
        continuar_finalizar = otro_turno()
        # Validar si continua o no
        if continuar_finalizar == "s":
            continue
        else:
            print("Gracias por usar nuestro programa. Un saludo!")
            break


inicio()
