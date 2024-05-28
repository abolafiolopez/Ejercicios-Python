def obtener_rango():

    while True:
        rango = input("Indica un rango del 1 al 25 para encriptar: ")
        try:
            rango = int(rango)
            if 1 <= rango <= 25:
                return rango
            else:
                print("El número que has ingresado no es válido")
        except ValueError:
            print(f"\"{rango}\" no es válido")


def encriptar_cadena(cadena, rango):

    cadena_encriptada = ""

    for letra in cadena:
        if not letra.isalpha():
            cadena_encriptada += letra
        else:
            if letra.isupper():
                letra = (ord(letra) + rango)
                if letra > ord('Z'):
                    ch_encriptado = chr((letra - ord('Z')) + (ord('A') - 1))
                else:
                    ch_encriptado = chr(letra)
                cadena_encriptada += ch_encriptado
            else:
                letra = (ord(letra) + rango)
                if letra > ord('z'):
                    ch_encriptado = chr((letra - ord('z')) + (ord('a') - 1))
                else:
                    ch_encriptado = chr(letra)
                cadena_encriptada += ch_encriptado
    return cadena_encriptada


cadena = input("Ingresa una cadena de texto para encriptar: ")
rango = obtener_rango()
cadena_encriptada = encriptar_cadena(cadena, rango)
print(cadena_encriptada)
