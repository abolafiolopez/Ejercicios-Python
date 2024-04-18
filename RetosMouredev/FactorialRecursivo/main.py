"""
 * Escribe una función que calcule y retorne el factorial de un número dado
 * de forma recursiva.
 """


def factorial(n):

    num_factorial = n

    if n == 0:
        return 1
    else:
        for i in range(1, n):
            num_factorial *= n - i

    return num_factorial


def factorial_recursivo(n):

    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n-1)


print(factorial(10))
print(factorial_recursivo(10))
