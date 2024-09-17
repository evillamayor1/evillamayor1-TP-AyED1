""" a. Generar una lista de N números aleatorios del 1 al 100. El valor de N se ingresa 
a través del teclado.
 b. Recibir una lista como parámetro y devolver True si la misma contiene algún 
elemento repetido. La función no debe modificar la lista.
 c. Recibir una lista como parámetro y devolver una nueva lista con los elementos 
únicos de la lista original, sin importar el orden. 
Combinar estas tres funciones en un mismo programa"""

import random

#definir funcion 
def generar_lista(n = int):
    #genera una lista por comprension con la longitud deseada
    lista = [random.randint(1, 100) for i in range(n)]
    return lista

#definir funcion
def elemento_repetido(lista = list):
    #itera sobre la lista buscando elementos repetidos, retorna true si encuentra alguno
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False

#definir variable 
def elementos_unicos(lista = list):
    #crea una lista de elementos unicos y comprueba si estos existen en la lista
    unicos = []
    for elemento in lista:
        if elemento not in unicos:
            unicos.append(elemento)
    return unicos
