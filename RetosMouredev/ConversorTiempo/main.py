"""
 * Crea una función que reciba días, horas, minutos y segundos (como enteros)
 * y retorne su resultado en milisegundos.
"""

# Importar la clase timedelta del módulo datetime
from datetime import timedelta


# Función para pedir un número con un texto personalizado
def pedir_numero(texto):

    while True:
        try:
            num = int(input(texto))
            return num
        except:
            print("No has indicado un valor correcto.")


# Función para solicitar los argumentos (día, hora, minutos, segundos) con pedir_numero
def solicitar_argumentos():

    dias = pedir_numero("Dime el día: ")
    horas = pedir_numero("Dime la hora: ")
    minutos = pedir_numero("Dime los minutos: ")
    segundos = pedir_numero("Dime los segundos: ")
    return dias, horas, minutos, segundos


# Función par convertir los argumentos en milisegundos con timedelta
def convertir_tiempo(dias, horas, minutos, segundos):

    tiempo = timedelta(days=dias, hours=horas, minutes=minutos, seconds=segundos)
    return tiempo.total_seconds() * 10**3


# Iniciar app
argumentos = solicitar_argumentos()
a = argumentos
print(f"Has indicado: {a[1]} dias, {a[1]} horas, {a[2]} minutos, {a[3]} segundos.")
milisegundos = convertir_tiempo(*argumentos)
print(f"Son un total de {milisegundos} milisegundos.")
