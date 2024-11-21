"""Desarrollar una función que extraiga una subcadena de una cadena de caracteres, 
indicando la posición y la cantidad de caracteres deseada. Devolver la subcadena 
como valor de retorno. Escribir también un programa para verificar el comportamiento de la misma. Ejemplo, dada la cadena "El número de teléfono es 4356-
7890" extraer la subcadena que comienza en la posición 25 y tiene 9 caracteres, 
resultando la subcadena "4356-7890". Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas"""
#variable con rebanadas
def extraer_subcadena_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    pre: recibe una cadena, la posicion inicial (base 0) y la cantidad de caracteres
    post: retorna la subcadena extraida utilizando rebanadas
    """
    return cadena[posicion:posicion + cantidad]

#variable sin rebanadas
def extraer_subcadena_sin_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    pre: recibe una cadena, la posicion inicial (base 0) y la cantidad de caracteres
    post: retorna la subcadena extraida sin usar rebanadas
    """
    subcadena = ""
    for i in range(posicion, posicion + cantidad):
        if i < len(cadena): 
            subcadena += cadena[i]
    return subcadena

