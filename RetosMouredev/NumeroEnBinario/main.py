"""
Crea un programa se encargue de transformar un número en decimal a binario
sin utilizar funciones propias del lenguaje que lo hagan directamente.
"""


def pedir_numero():
    """
    Pide ingresar un número decimal y lo retorna
    """
    # Validar que sea un número decimal
    while True:
        numero = input("Introduce un número decimal: ")
        try:
            return int(numero)
        except ValueError:
            print(f"\"{numero}\" no es un número decimal\n")


def transformar_binario(numero):
    """
    Transformar un número en binario
    """
    dividendo = numero
    binario = []

    if dividendo == 0:
        return f"El número 0 en binario es 0"

    # Dividir el número mientras sea mayor que 2
    while dividendo > 0:
        binario.append(str(dividendo % 2))
        dividendo = (dividendo // 2)

    # Revertir la cadena y agrupar los números
    binario.reverse()
    numero_binario = "".join(binario)

    return f"El número {numero} en binario es {numero_binario}"


numero = pedir_numero()
print(transformar_binario(numero))
