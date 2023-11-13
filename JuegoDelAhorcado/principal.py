"""
Juego del ahorcado
"""

from random import choice

palabras = ["Acertijo", "Python", "Ordenador", "Servidor", "Programación"]
palabra_secreta = choice(palabras).lower()
letras_acertadas = []
letras_falladas = []
vidas = 6


# Función para ocultar la palabra
def ocultar_palabra(palabra_secreta,letras_acertadas):
    """
    Oculta la palabra secreta según las letras acertadas
    """

    palabra_oculta = []

    # Bucle para ocultar la palabra
    for letra in palabra_secreta:

        if letra in letras_acertadas:
            palabra_oculta.append(letra)
        else:
            palabra_oculta.append("_")

    return " ".join(palabra_oculta)


# Función para pedir una letra
def pedir_letra():
    """
    Bucle para incdicar la letra
    """

    # Bucle para pedir la letra
    while True:
        letra = input("Por favor, dime una letra: ").lower()

        if not letra.isalpha() or len(letra) > 1:
            print(f"{letra} no es una letra válida\n")
        else:
            return letra


# Función para chequear la letra
def chequear_letra(letra_validada):
    """
    Chequea la letra con la letra validada
    """

    if (letra_validada in letras_acertadas) or (letra_validada in letras_falladas):
        print(f"Tu letra \"{letra_validada}\" ya está dicha\n")
    elif letra_validada in palabra_secreta:
        print(f"Enorabuena, tu letra {letra_validada} está en la palabra secreta \n")
        letras_acertadas.append(letra_validada)
    else:
        print(f"Tu letra {letra_validada} no se encuentra en la palabra secreta. Pierdes una vida!")
        letras_falladas.append(letra_validada)
        return False


# Función para comprobar la palbra
def comprobar_palabra(letras_acertadas,palabra_secreta):
    """
    Comprueba la palabra palabra secreta con las letras acertadas
    """

    palabra_secreta = list(set(palabra_secreta))
    palabra_secreta.sort()
    letras_acertadas.sort()

    if letras_acertadas == palabra_secreta:
        return True

print("Bienvenido al juego del ahorcado")
print("Mucha suerte! Comenzamos!\n")

# Bucle para iniciar la apliación
while vidas > 0:

    print(f"Tienes {vidas} vidas para averiguar la palabra secreta: " + ocultar_palabra(palabra_secreta,letras_acertadas) + "\n")
    print(f"Las letras acertadas son: {letras_acertadas}")
    print(f"Las letras falladas son: {letras_falladas}")

    letra_validada = pedir_letra()
    letra_chequeada = chequear_letra(letra_validada)

    if letra_chequeada == False:
        vidas -= 1
    palabra_resuelta = comprobar_palabra(letras_acertadas,palabra_secreta)
    if palabra_resuelta == True:
        print(f"Enorabuena, has acertado la palabra secrteta que era \"{palabra_secreta}\"")
        break

if vidas == 0:
    print(f"Lo siento, esta vez no ha podidio ser, la palabra era \"{palabra_secreta}\". Inténtalo de nuevo")