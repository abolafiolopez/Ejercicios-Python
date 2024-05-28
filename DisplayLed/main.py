leds = [
    '1111110',  # 0
    '0110000',  # 1
    '1101101',  # 2
    '1111001',  # 3
    '0110011',  # 4
    '1011011',  # 5
    '1011111',  # 6
    '1110000',  # 7
    '1111111',  # 8
    '1111011',  # 9
]


def imprimir_numeros(numero):
    numero = str(numero)

    lineas = ["" for i in range(5)]
    for n in numero:
        display = [[" ", " ", " "] for i in range(5)]
        led = leds[int(n)]
        if led[0] == "1":
            display[0][0] = display[0][1] = display[0][2] = "#"
        if led[1] == "1":
            display[0][2] = display[1][2] = display[2][2] = "#"
        if led[2] == "1":
            display[2][2] = display[3][2] = display[4][2] = "#"
        if led[3] == "1":
            display[4][0] = display[4][1] = display[4][2] = "#"
        if led[4] == "1":
            display[4][0] = display[3][0] = display[2][0] = "#"
        if led[5] == "1":
            display[2][0] = display[1][0] = display[0][0] = "#"
        if led[6] == "1":
            display[2][0] = display[2][1] = display[2][2] = "#"

        for i in range(5):
            lineas[i] += ''.join(display[i]) + ' '

    for fila in lineas:
        print(' '.join(fila))


imprimir_numeros(900)
