""" Eliminar de una lista de números enteros aquellos valores que se encuentren en 
una segunda lista. Imprimir la lista original, la lista de valores a eliminar y la lista 
resultante. La función debe modificar la lista original sin crear una copia modificada"""

#importo random para generar una lista aleatoria para que sea mas facul de hacer
import random

def eliminar_lista(lista = list, lista_eliminar = list)
    #usando listas por comprension elimina los elementos de la lista de elementos a eliminar
    lista[:] = [i for i in lista if valor not in lista_eliminar]
    return lista

#crea dos listas vacias para la funcion
listaA = []
lista_elim = []

#genera elementos aleatorios y los agrega a las listas
for i in range(10):
    listaA.append(random.randint(1, 15))
for i in range(10):
    lista_elim.append(random.randint(1, 15))

#imprime las listas antes de la modificacion
print("la lista original es:"listaA)
print("la lista de elementos a eliminar es:"lista_elim)

#llama a la funcion y posteriormente imprime la lista ya modificada
lista_final = eliminar_lista(listaA, lista_elim)
print("la lista modificada es:"lista_final)
