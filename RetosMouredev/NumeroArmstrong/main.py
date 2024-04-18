"""
 * Escribe una función que calcule si un número dado es un número de Armstrong
 * (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información
 * al respecto.
"""


def armstrong(n):

    n_armstrong = 0

    for i in str(n):
        n_armstrong += int(i) ** len(str(n))

    return n == n_armstrong


print(armstrong(370))
