"""
Ejercicio simulando una cuenta bancaria
"""

from os import system

# Clase Persona
class Persona:

    def __init__(self, nombre, apellido):
        """
        Atribudos de instancia
        """
        self.nombre = nombre
        self.apellido = apellido


# Clase Cliente que hereda de Persona
class Cliente(Persona):

    saldo = 0

    def __init__(self, nombre, apellido, numero_cuenta):
        """
        Atributos de instancia, beben de Persona
        """
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta


    def __str__(self):
        """
        Método especial para imprimir en pantalla
        """
        return f"Hola {self.nombre} {self.apellido} su número de cuenta es {self.numero_cuenta} y su saldo es de {round(self.saldo,2)}€"


    # Función para depositar
    def depositar(self, deposito):

        print(f"El deposito de {deposito}€ se ha efectuado correctamente")

        self.saldo += deposito


    # Función para retirar
    def retirar(self, retiro):

        if retiro > self.saldo:
            print(f"El retiro de {retiro}€ es mayor que tu saldo disponible: {self.saldo}€")
        else:
            print(f"El retiro de {retiro}€ se ha efectuado correctamente")
            self.saldo -= retiro


# Función para elegir una opción
def elegir_opcion():

    print("[1].Depositar dinero")
    print("[2].Retirar dinero")
    print("[3].Salir")

    # Bucle para elegir una opción
    while True:

        opcion = input("Elige una opción | 1, 2 o 3: ")

        # Validar opción
        try:
            opcion = int(opcion)

            if opcion in range(1, 4):
                break
            else:
                print(f"\"{opcion}\" no es una opción válida")

        except ValueError:
            print(f"\"{opcion}\" no es una opción válida")

    return opcion


# Función para hacer los depósitos
def hacer_deposito():

    # Bucle para indicar el depísto
    while True:
        deposito = input("Cuánto deseas depositar?: ")

        # Validar depósito
        try:
            deposito = float(deposito)
            break
        except ValueError:
            print(f"\"{deposito}\" no es un valor correcto")

    return round(deposito, 2)


# Función para hacer los retiros
def hacer_retiro():

    # Bucle para indicar el retiro
    while True:

        retiro = input("Cuánto deseas retirar?: ")

        # Validar retiro
        try:
            retiro = float(retiro)
            break
        except ValueError:
            print(f"\"{retiro}\" No es un valor válido!")

    return round(retiro, 2)


# Función para crear el cliente
def crear_cliente():

    nombre = input("Por favor, dime tu nombre: ")
    apellido = input("Por favor, dime tu apellido: ")
    numero_cuenta = input("Cuál es su número de cuenta?: ")

    cliente_creado = Cliente(nombre,apellido, numero_cuenta)

    return cliente_creado


# Función para iniciar la aplicación
def inicio():

    cliente_creado = crear_cliente()
    system("cls")

    # Bucle para iniciar la aplicación
    while True:

        print("*********************")
        print("Bienvenido a su banco")
        print("*********************")
        print(f"\n{cliente_creado}\n")

        opcion = elegir_opcion()

        # Validar opción
        if opcion == 1:
            deposito = hacer_deposito()
            cliente_creado.depositar(deposito)

        elif opcion == 2:
            retiro = hacer_retiro()
            cliente_creado.retirar(retiro)
        else:
            break

    print("Gracias por operar en nuestro banco")


inicio()
