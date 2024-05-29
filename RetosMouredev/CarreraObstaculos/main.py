"""
 * Crea una función que evalúe si un/a atleta ha superado correctamente una
 * carrera de obstáculos.
 * - La función recibirá dos parámetros:
 *      - Un array que sólo puede contener String con las palabras
 *        "run" o "jump"
 *      - Un String que represente la pista y sólo puede contener "_" (suelo)
 *        o "|" (valla)
 * - La función imprimirá cómo ha finalizado la carrera:
 *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
 *        será correcto y no variará el símbolo de esa parte de la pista.
 *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
 *      - Si hace "run" en "|" (valla), se variará la pista por "/".
 * - La función retornará un Boolean que indique si ha superado la carrera.
 * Para ello tiene que realizar la opción correcta en cada tramo de la pista.
"""

# Variables
pista = "___|__|"
acciones = ["correr", "correr", "correr", "saltar", "correr", "correr", "saltar"]


# Función para correr, retorna "/" si no es correcto
def correr(suelo="_"):
    return suelo if suelo == "_" else "/"


# Función para saltar, retorna "X" si no es correcto
def saltar(valla="|"):
    return valla if valla == "|" else "X"


# Función para superar la carrrera de obstáculos
def carrera_obstaculos(pista, acciones):

    pista_finalizada = ""

    try:
        for elemento, accion in zip(pista, acciones):
            if elemento not in "_|":
                raise ValueError(f"El elemento no de la pista no es válido: '{elemento}'")
            if accion not in ["correr", "saltar"]:
                raise ValueError(f"La acción no es válida: '{accion}'")

            if accion == "correr":
                pista_finalizada += correr(elemento)
            elif accion == "saltar":
                pista_finalizada += saltar(elemento)

        print(f"Pista finalizada: {pista_finalizada}")
        return pista_finalizada == pista
    except ValueError as e:
        print(f"Ha habido un error durante la carrera. {e}")


# Lanzar aplicación
carrera = carrera_obstaculos(pista, acciones)
if carrera:
    print("Se ha superado con éxito la carrera de obstáculos.")
else:
    print("No se ha podido superar la carrera de obstáculos.")
    print(f"La pista es: {pista}")
