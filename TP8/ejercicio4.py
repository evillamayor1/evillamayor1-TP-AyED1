""" Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas 
son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). La función devuelve True 
o False. Escribir también un programa para verificar su comportamiento. Considerar 
el uso de conjuntos para resolver este ejercicio"""

#se define la funcion
def encajan_fichas(ficha1 = tuple, ficha2= tuple)-> bool:
    """
    pre: recibe dos tuplas, cada una representando una ficha de dominó
    post: devuelve True si las fichas encajan (comparten un número), False si no
    """
    #se combierten las tuplas a conjuntos para comprobar si comparten algún número
    set_ficha1 = set(ficha1)
    set_ficha2 = set(ficha2)
    
    #se verifica si hay algún número común entre los dos conjuntos
    return not set_ficha1.isdisjoint(set_ficha2)

#programa principal

#se ingresan las dos fichas de dominó
ficha1 = tuple(map(int, input("Ingresa la primera ficha (dos números separados por espacio): ").split()))
ficha2 = tuple(map(int, input("Ingresa la segunda ficha (dos números separados por espacio): ").split()))

 #se verifica si las fichas encajan
if encajan_fichas(ficha1, ficha2):
    print("Las fichas encajan.")
else:
    print("Las fichas no encajan.")
