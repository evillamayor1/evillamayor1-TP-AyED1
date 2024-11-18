"""
Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7 
que no sean múltiplos de 5. A y B se ingresar desde el teclado.
"""

#se define la variable
def lista_multiplos(a = int, b = int) -> list:
    """
    pre:esta funcion recibe dos valores enteros

    post: esta funcion retorna una lista
    """
    #crear la lista por comprensión
    lista = [i for i in range(a, b+1) if i % 7 == 0 and i % 5 != 0]

    print(lista)

#asignacion de valores y llamada a la funcion
a = int(input("ingrese el valor de a:"))
b = int(input("ingrese el valor de b:"))

lista_multiplos(a,b)