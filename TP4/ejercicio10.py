""" Desarrollar una función para reemplazar todas las apariciones de una palabra por 
otra en una cadena de caracteres y devolver la cadena obtenida y un entero con la 
cantidad de reemplazos realizados. Tener en cuenta que sólo deben reemplazarse 
palabras completas, y no fragmentos de palabras. Escribir también un programa 
para verificar el comportamiento de la función. """

#se importa re para facilitar el ejercicio
import re

#se define la funcion

def reemplazar_palabra(cadena: str, palabra_buscar: str, palabra_reemplazar: str) -> tuple[str, int]:
    """
    pre: recibe una cadena, una palabra a buscar y una palabra para reemplazar
    post: devuelve la cadena con las palabras reemplazadas y la cantidad de reemplazos realizados
    """
    # construir un patrón para reemplazar solo palabras completas
    patron = rf'\b{re.escape(palabra_buscar)}\b'
    
    # realizar los reemplazos y contar cuántos se hicieron
    nueva_cadena, cantidad_reemplazos = re.subn(patron, palabra_reemplazar, cadena)
    
    return nueva_cadena, cantidad_reemplazos
