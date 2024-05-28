def read_int(prompt, minimo, maximo):
    while True:
        try:
            num = int(input(prompt))
            assert minimo <= num <= maximo
            break
        except ValueError:
            print("Error: entrada incorrecta")
        except AssertionError:
            print(f"Error: el número no está dentro del rango permitido {minimo} - "
                  f"{maximo}")
        except:
            print("Algo salió mal")

    return num


v = read_int("Ingresa un número entre -10 a 10: ", -10, 10)

print("El número es:", v)
