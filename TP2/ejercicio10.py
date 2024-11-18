""" Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con los 
elementos de la primera que sean impares. El proceso deberá realizarse utilizando 
la función filter(). Imprimir las dos listas por pantalla. 
"""
#se exporta la libreria necesaria
import random

#se define la funcion
def lista_impares() -> list:
    """
    pre:esta funcion no requiere parametros

    post: esta funcion retorna listas
    """
    #se genera la lista con números al azar
    lista_azar = [random.randint(1, 100) for i in range(20)]

    #se crea la nueva lista con los elementos impares
    lista_nueva = list(filter(lambda x: x % 2 != 0, lista_azar))

    #se retornan las listas
    print("la lista original es:", lista_azar, "y la lista con impares es:", lista_nueva)

lista_impares()