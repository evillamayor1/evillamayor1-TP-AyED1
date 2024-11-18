"""Escribir una función que reciba una lista de números enteros como parámetro y la 
normalice, es decir que todos sus elementos deben sumar 1.0, respetando las pro
porciones relativas que cada elemento tiene en la lista original. Desarrollar también 
un programa que permita verificar el comportamiento de la función. Por ejemplo, 
normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50]."""

import random

#definir la variable
def normalizar(lista = list) -> list:
    """
    pre:esta funcion recibe una lista

    post: esta funcion retorna una lista
    
    """
    total_lista = sum(lista)
    lista_norm = [i / total_lista for i in lista]
    return lista_norm

lista = []

for i in range(10):
    lista.append(random.randint(1,30))

resultado = normalizar(lista)

