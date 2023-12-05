"""
Web scraping de la página toscrape.com
para obtener los títulos de los libros con 4 o 5 estrellas
más baratos de 20 Libras
"""

# Importaciones
import bs4
import requests
import re

# Variables
url_base = 'http://books.toscrape.com/catalogue/page-{}.html'
lista_titulos = []
lista_precios = []
patron_precio = r'\d{2}.\d{2}'

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

            # Chequear precio
            precios = libro.select('.price_color')[0]

            # Bucle para encontrar el precio y guardarlo en la lista
            for p in precios:
                buscar_precio = re.search(patron_precio, p)
                precio_libro = buscar_precio.group()

                # Guardar precio si es menor a £20
                if float(precio_libro) < 20:
                    lista_precios.append(precio_libro)

                    # Guardar título en la lista
                    titulo_libro = libro.select('a')[1]['title']
                    lista_titulos.append(titulo_libro)

# Bucle para imprimir cada título de la lista y su precio
for titulo, precio in zip(lista_titulos, lista_precios):
    print(f'{titulo}: £{precio}')
