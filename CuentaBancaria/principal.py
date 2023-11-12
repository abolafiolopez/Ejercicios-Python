from os import system
class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, saldo):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo


    def __str__(self):
        return f"Hola {self.nombre} {self.apellido} su número de cuenta es {self.numero_cuenta} y su saldo es de {round(self.saldo,2)}€"


    def depositar(self, deposito):

        print(f"El deposito de {deposito}€ se ha efectuado correctamente")

        self.saldo += deposito


    def retirar(self, retiro):

        if retiro > self.saldo:
            print(f"El retiro de {retiro}€ es mayor que tu saldo disponible: {self.saldo}€")
        else:
            print(f"El retiro de {retiro}€ se ha efectuado correctamente")
            self.saldo -= retiro


def elegir_opcion():

    print("[1].Depositar dinero")
    print("[2].Retirar dinero")
    print("[3].Salir")

    while True:

        opcion = input("Elige una opción | 1, 2 o 3: ")

        try:
            opcion = int(opcion)

            if opcion in range(1, 4):
                break
            else:
                print(f"\"{opcion}\" no es una opción válida")

        except ValueError:
            print(f"\"{opcion}\" no es una opción válida")

    return opcion


def hacer_deposito():

    while True:
        deposito = input("Cuánto deseas depositar?: ")
        try:
            deposito = float(deposito)
            break
        except ValueError:
            print(f"\"{deposito}\" no es un valor correcto")

    return round(deposito, 2)


def hacer_retiro():

    while True:

        retiro = input("Cuánto deseas retirar?: ")

        try:
            retiro = float(retiro)
            break
        except ValueError:
            print(f"\"{retiro}\" No es un valor válido!")

    return round(retiro, 2)


def crear_cliente():

    nombre = input("Por favor, dime tu nombre: ")
    apellido = input("Por favor, dime tu apellido: ")
    numero_cuenta = input("Cuál es su número de cuenta?: ")

    while True:

        saldo = input("De cuánto sería su saldo disponible?: ")

        try:
            saldo = float(saldo)
            break
        except ValueError:
            print(f"\"{saldo}\" no es un saldo correcto")

    cliente_creado = Cliente(nombre,apellido, numero_cuenta, saldo)

    return cliente_creado


def inicio():

    cliente_creado = crear_cliente()
    system("cls")

    while True:

        print("*********************")
        print("Bienvenido a su banco")
        print("*********************")
        print(f"\n{cliente_creado}\n")

        opcion = elegir_opcion()

        if opcion == 1:
            deposito = hacer_deposito()
            cliente_creado.depositar(deposito)

        elif opcion == 2:
            retiro = hacer_retiro()
            cliente_creado.retirar(retiro)
        else:
            break

    print("Gracias por operar en banco Abolafio's Bank")


inicio()

# cliente1 = Cliente("Antonio", "Abolafio", "zxcv1234", 1000)
# print(cliente1)
# cliente1.depositar()
# cliente1.retirar()