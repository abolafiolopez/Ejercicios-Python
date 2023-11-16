"""
Buscador de números de serie
"""

# Importaciones
import os
from datetime import date
import time
import math
import re

# Variables
ruta = os.getcwd() + "\\Mi_Gran_Directorio"
archivos = []
archivos_codigos = {}
patron = r"N\D{3}-\d{5}"
fecha = f"{date.today().day}/{date.today().month}/{date.today().year}"


# Función para buscar los archivos
def localizar_archivos(ruta):
    """
    Busca los archivos en el directorio y subdirectorios de la ruta
    """
    # Bucle for para buscar los archivos
    for carpeta, subcarpeta, archivo in os.walk(ruta):

        # Bucle para comprobar que es un archivo .txt
        for txt in archivo:
            txt = str(txt).lower()
            if txt.endswith(".txt"):
                archivos.append(carpeta + "\\" + txt)


# Función para buscar los códigos
def buscar_patron(patron, archivos):
    """
    Busca el pantrón en los ficheros
    """
    # Bucle para buscar los códigos y añadirlos al diccionario archivos_codigos
    for archivo in archivos:
        leer_archivo = open(archivo, "r")
        comprobar_archivo = re.search(patron, leer_archivo.read())
        if comprobar_archivo:
            archivos_codigos[os.path.basename(archivo)] = comprobar_archivo.group()
        leer_archivo.close()


# Función para mostrar los archivos y sus códigos
def mostrar_archivos_codigos(archivos_codigos):
    """
    Muestra el nombre del archivo junto a su código
    """
    # Bucle para mostrar los archivos y sus códigos
    for archivo, codigo in archivos_codigos.items():
        print(f"{archivo}\t{codigo}")


# Funcion para iniciar el programa
def inicio():
    """
    Inicia el programa con las funciones
    """
    tiempo_inicio = time.time()
    localizar_archivos(ruta)
    buscar_patron(patron, archivos)
    tiempo_final = time.time()
    print(f"Fecha de búsqueda: {fecha}\n")
    print("Archivo\t\tNR. SERIE")
    print("-------\t\t---------")
    mostrar_archivos_codigos(archivos_codigos)
    print(f"\nNúmeros encontrados: {len(archivos_codigos)}")
    medir_tiempo = math.ceil(tiempo_final - tiempo_inicio)
    print(f"Duración de la búsqueda: {medir_tiempo} segundos")


inicio()
