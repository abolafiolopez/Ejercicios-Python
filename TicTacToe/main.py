from random import randrange, choice


def mostrar_tablero(tablero):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    print("+-------" * 3, "+", sep="")
    for col in range(3):
        print("|       " * 3, "|", sep="")
        for fila in range(3):
            print(f"|   {tablero[col][fila]}   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")


def movimiento_usuario(tablero):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    while True:
        movimiento = input("Elige un número del tablero para tu ficha \"O\": ")
        try:
            movimiento = int(movimiento)
            if movimiento >= 1 and int(movimiento) <= 9:
                movimiento -= 1
                col = movimiento // 3
                fila = movimiento % 3
                if not tablero[col][fila] in ["X", "O"]:
                    tablero[col][fila] = "O"
                    break
                else:
                    print("\n¡Casilla ocupada!")

            else:
                print("\n¡Selecciona un número válido!")

        except:
            print(f"\n\"{movimiento}\" no es una selección válida")


def listar_casillas_vacias(tablero):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos.
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    casillas_vacias = []
    for col in range(3):
        for fila in range(3):
            if not tablero[col][fila] in ["X", "O"]:
                casillas_vacias.append((col, fila))

    return casillas_vacias


def comprobar_victoria(tablero, signo):
    # La función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    if signo == "X":
        campeon = "Ordenador"
    elif signo == "O":
        campeon = "Antonio"
    else:
        campeon = None

    cruz1 = True
    cruz2 = True
    for i in range(3):
        if tablero[i][0] == signo and tablero[i][1] == signo and tablero[i][2] == signo:
            return campeon
        if tablero[0][i] == signo and tablero[1][i] == signo and tablero[2][i] == signo:
            return campeon
        if tablero[i][2 - i] != signo:
            cruz1 = False
        if tablero[2 - i][2 - i] != signo:
            cruz2 = False

    if cruz1 or cruz2:
        return campeon


def movimiento_ordenador(tablero):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    casillas_vacias = listar_casillas_vacias(tablero)
    n_vacias = len(casillas_vacias)
    if n_vacias > 0:
        seleccion = randrange(n_vacias)
        col, fila = casillas_vacias[seleccion]
        tablero[col][fila] = "X"


tablero = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
turno_usuario = choice([True, False])

if turno_usuario:
    print("¡Empiezas tú!")
else:
    print("¡Empiezo yo!")

while True:
    mostrar_tablero(tablero)
    if turno_usuario:
        print("\n¡Tu turno!")
        movimiento_usuario(tablero)
        victoria = comprobar_victoria(tablero, signo="O")
    else:
        print("\n¡Mi turno!")
        movimiento_ordenador(tablero)
        victoria = comprobar_victoria(tablero, signo="X")

    if victoria:
        break

    libres = listar_casillas_vacias(tablero)
    if not libres:
        break

    turno_usuario = not turno_usuario

mostrar_tablero(tablero)
if victoria == "Ordenador":
    print("\n¡He ganado!")
elif victoria == "Antonio":
    print("\n¡Has ganado!")
else:
    print("¡Hemos empatado!")
