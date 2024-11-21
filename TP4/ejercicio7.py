"""Escribir una función para eliminar una subcadena de una cadena de caracteres, a 
partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resultante. Escribir también un programa para verificar el comportamiento de la misma. 
Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
"""

#funcion con rebanadas
def eliminar_subcadena_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    pre: recibe una cadena, la posicion inicial (base 0) y la cantidad de caracteres a eliminar
    post: retorna la cadena resultante eliminando la subcadena especificada
    """
    return cadena[:posicion] + cadena[posicion + cantidad:]

#funcion sin rebanadas
def eliminar_subcadena_sin_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    pre: recibe una cadena, la posicion inicial (base 0) y la cantidad de caracteres a eliminar
    post: retorna la cadena resultante eliminando la subcadena especificada sin usar rebanadas
    """
    resultado = ""
    for i in range(len(cadena)):
        if i < posicion or i >= posicion + cantidad:
            resultado += cadena[i]
    return resultado
