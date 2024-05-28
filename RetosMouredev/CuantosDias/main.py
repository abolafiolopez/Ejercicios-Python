"""
 * Crea una función que calcule y retorne cuántos días hay entre dos cadenas
 * de texto que representen fechas.
 * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 * - La función recibirá dos String y retornará un Int.
 * - La diferencia en días será absoluta (no importa el orden de las fechas).
 * - Si una de las dos cadenas de texto no representa una fecha correcta se
 *   lanzará una excepción.
"""

# Importaciones
import re
from datetime import datetime

"""
Ejercicio realizado sin la librería datetime
"""

# Variables
dias_mes = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30,
            10: 31, 11: 30, 12: 31}


# Función para validar dos fechas
def validar_fecha(fecha1, fecha2):

    patron = r"\d{2}/\d{2}/\d+"

    if re.search(patron, fecha1) and re.search(patron, fecha2):
        fecha1 = [int(n) for n in fecha1.split("/")]
        fecha2 = [int(n) for n in fecha2.split("/")]

        dia1, mes1, anio1 = fecha1
        dia2, mes2, anio2 = fecha2

        if not (1 <= mes1 <= 12 and 1 <= dia1 <= dias_mes[mes1]):
            return False
        if not (1 <= mes2 <= 12 and 1 <= dia2 <= dias_mes[mes2]):
            return False

        return fecha1, fecha2

    else:
        return False


# Función para ordenar las fechas, siendo fecha1 la más baja y fecha2 la más alta
def ordenar_fechas(fecha1, fecha2):
    if fecha1[2] >= fecha2[2]:
        if fecha1[1] >= fecha2[1]:
            if fecha1[0] >= fecha2[0]:
                return fecha2, fecha1
            return fecha2, fecha1
        return fecha2, fecha1
    else:
        return fecha1, fecha2


# Función para comprobar si un año es bisiesto
def comprobar_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


# Función para contar el número de días transcurridos de la fecha corriente
def contar_dias(dia, mes, anio):

    if comprobar_bisiesto(anio):
        dias_mes[2] = 29
    else:
        dias_mes[2] = 28

    return sum(dias_mes[m] for m in range(1, mes)) + dia


# Función para contar la diferencia de dias entre dos fechas ordenadas
def contar_diferencia_dias(fecha1, fecha2):

    dias = 0

    for anio in range(fecha1[2], fecha2[2]):
        if comprobar_bisiesto(anio):
            dias += 366
        else:
            dias += 365

    dias -= contar_dias(fecha1[0], fecha1[1], fecha1[2])
    dias += contar_dias(fecha2[0], fecha2[1], fecha2[2])

    return dias


# Lanzar aplicación
fechas_validadas = validar_fecha("09/03/1995", "28/05/2024")
if fechas_validadas:
    fechas_ordenadas = ordenar_fechas(*fechas_validadas)
    diferencia_dias = contar_diferencia_dias(*fechas_ordenadas)
    print(f"La diferencia de días es de: {diferencia_dias}")
else:
    print("Las fechas no son válidas y no se puede calcular la diferencia de días")


"""
Ejercicio realizado con la librería datetime
"""


# Función para validar las fechas y retornarlas
def validar_fecha(fecha1, fecha2):

    patron = r"\d{2}/\d{2}/\d+"

    if re.search(patron, fecha1) and re.search(patron, fecha2):
        return fecha1, fecha2
    else:
        return False


# Función para retornar las fechas como objetos datetime
def convertir_fechas_validadas(fecha1, fecha2):

    fecha1 = datetime.strptime(fecha1, "%d/%m/%Y")
    fecha2 = datetime.strptime(fecha2, "%d/%m/%Y")

    return fecha1, fecha2


# Función para retornar la diferencia de días entre dos fechas, devuelve el absoluto de días
def contar_diferencia_dias(fecha1, fecha2):

    diferencia = abs(fecha1 - fecha2)

    return diferencia.days


# Lanzar aplicación
fechas_validadas = validar_fecha("09/03/1995", "28/05/2024")
if fechas_validadas:
    fechas_convertidas = convertir_fechas_validadas(*fechas_validadas)
    diferencia_dias = contar_diferencia_dias(*fechas_convertidas)
    print(f"La diferencia de días es de: {diferencia_dias}")
else:
    print("Las fechas no son válidas y no se puede calcular la diferencia de días")
