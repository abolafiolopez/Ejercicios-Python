"""
Web scraping de la página unplash para sacar las imágenes
"""

import bs4
import requests

resultado = requests.get('https://escueladirecta.com/courses')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

imagenes = sopa.select('.course-box-image')[0]['src']

imagen_curso_1 = requests.get(imagenes)
'''print(imagen_curso_1)
print(imagen_curso_1.content)'''

imagen = open('imagen_curso1.jpg', 'wb')
imagen.write(imagen_curso_1.content)
imagen.close()