"""
Web scraping de la página toscrape.com
para obtener los títulos de los libros con 4 o 5 estrellas
"""

# Importaciones
import bs4
import requests

# Variables
url_base = 'http://books.toscrape.com/catalogue/page-{}.html'
lista_titulos = []

# Bucle para iterar páginas
for i in range(1, 51):

    # Crear sopa de cada página
    url_pagina = url_base.format(i)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # Seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    # Bucle para iterar libros
    for libro in libros:

        # Chequear 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:

            # Guardar título en la lista
            titulo_libro = libro.select('a')[1]['title']
            lista_titulos.append(titulo_libro)

# Bucle para imprimir cada título de la lista
for titulo in lista_titulos:
    print(titulo)




