"""Escribir una función que reciba como parámetro una cadena de caracteres en la que 
las palabras se encuentran separadas por uno o más espacios. Devolver otra 
cadena con las palabras ordenadas según su longitud, dejando un espacio entre 
cada una. Los signos de puntuación no deben ser tenidos en cuenta al medir la 
longitud de las palabras, pero deberán conservarse en la cadena final.
"""

#se define la funcion
import re

def ordenar_palabras_por_longitud(cadena: str) -> str:
    """
    pre: recibe una cadena de caracteres en la que las palabras están separadas por uno o más espacios
    post: devuelve una cadena con las palabras ordenadas por longitud, separadas por un espacio
    """
    #se separan las palabras de la cadena y limpiar signos de puntuación
    palabras = re.findall(r'\b\w+\b', cadena)
    
    #se ordenan las palabras por su longitud
    palabras_ordenadas = sorted(palabras, key=len)
    
    #se crea una lista de las palabras originales con sus signos
    palabras_con_signos = re.findall(r'\b[^\s]+\b', cadena)
    
    #se construye la cadena final con las palabras ordenadas manteniendo signos
    resultado = []
    for palabra_ordenada in palabras_ordenadas:
        for palabra_original in palabras_con_signos:
            if re.sub(r'\W', '', palabra_original) == palabra_ordenada:
                resultado.append(palabra_original)
                palabras_con_signos.remove(palabra_original)
                break
    
    return ' '.join(resultado)
