"""
 Escribe un programa que imprima los 50 primeros números de la sucesión
 de Fibonacci empezando en 0.
 La serie Fibonacci se compone por una sucesión de números en
 la que el siguiente siempre es la suma de los dos anteriores.
 0, 1, 1, 2, 3, 5, 8, 13...
 """

# Método 1
numeros = []
i = 0
n = 0

while i <= 50:

    try:
        n = (numeros[i] + numeros[i + 1])
        numeros.append(n)
        i += 1

    except IndexError:
        numeros.append(n)
        n += 1

print(numeros)


# Método 2
n1 = 0
n2 = 1

for i in range(50):

    print(n1)

    n_fibonacci = n1 + n2

    n1 = n2
    n2 = n_fibonacci
