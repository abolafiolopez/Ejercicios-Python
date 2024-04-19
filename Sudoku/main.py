def sudoku(lista):

    patron = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    lista = [[n for n in str(fila)] for fila in lista]

    # Comprobar filas
    for fila in lista:
        if sorted(fila) != patron:
            return False

    # Comrpbar columnas
    for i in range(9):
        col = ""
        for fila in lista:
            col += fila[i]
        if sorted(col) != patron:
            return False

    # Comprobar cuadrados
    cuadrado = []
    for c in range(0, 7, 3):
        for f in range(0, 7, 3):
            for fila in lista[f:f + 3]:
                cuadrado += fila[c:c + 3]
            if sorted(cuadrado) != patron:
                return False
            else:
                cuadrado = []

    return True


lista = [
    295743861,
    431865927,
    876192543,
    387459216,
    612387495,
    549216738,
    763524189,
    928671354,
    154938672,
]
print(sudoku(lista))

lista = [
    195743862,
    431865927,
    876192543,
    387459216,
    612387495,
    549216738,
    763524189,
    928671354,
    254938671,
]
print(sudoku(lista))
