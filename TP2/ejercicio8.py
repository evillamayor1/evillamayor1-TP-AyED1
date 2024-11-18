"""
 Utilizar la técnica de listas por comprensión para construir una lista con todos los 
números impares comprendidos entre 100 y 200.
"""

#se define la variable a usar
def impares() -> list:
    """
    pre: esta funcion no recibe nada

    post: esta funcion retorna una lista 
    """
    impares = [i for i in range(100, 201) if i % 2 != 0]
    return impares

#asignacion de valores y llamada a la funcion
lista_impares = impares()

print(lista_impares)
