"""
Crea un programa que se encargue de calcular el aspect ratio de una
imagen a partir de una url.
- Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.
"""

from PIL import Image
from io import BytesIO
import requests


def calcular_ratio_imagen(url):
    """
    Calcula el ratio de una imagen a partir de una url con la imagen.
    """

    # Descargar y abrir la imagen en memoria
    url_imagen = requests.get(url)
    imagen = Image.open(BytesIO(url_imagen.content))

    # Dimensiones del objeto
    ancho, alto = imagen.size

    # Calcular ratio
    ratio_imagen = ancho / alto

    return ratio_imagen


ratio = calcular_ratio_imagen('https://detallesorballo.com/wp-content/uploads/2020/09/imagen-de-prueba-320x240-1.jpg')
print(f"El ratio de la imagen es {ratio}")
