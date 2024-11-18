""" Desarrollar cada una de las siguientes funciones y escribir un programa que per
mita verificar su funcionamiento imprimiendo la lista luego de invocar a cada fun
ción:
 a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elemen
tos también será un número al azar de dos dígitos.
 b. Calcular y devolver el producto de todos los elementos de la lista anterior.
 c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar 
se ingresa desde el teclado y la función lo recibe como parámetro. No utilizar 
listas auxiliares.
 d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas 
auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50]"""

#importar random
import random 

#definir funcion
def listaA()-> list:
    #se genera la longitud y una lista vacia
    longitud = random.randint(10, 20)
    lista = []

    #se general los numeros de manera aleatoria y se agregan a la lista creada anteriormente
    for i in range(longitud):
        lista.append(random.randint(100, 999))
    return lista

#asignacion y llamada de funcion
lista = listaA()
print(lista)

#definir funcion
def total_lista(lista= list)-> int:
    #crear una variable contador y sumar los elementos con una iteracion
    total = 0
    for i in range(len(lista)):
        total += i
    return total

#asignacion y llamada de funcion
total = total_lista(lista)
print(total)

#definir variable
def eliminar_valores(n = int, lista = list):
    #itera sobre la lista asignada e itara sobre ella, en caso de coincidir es eliminada
    for i in range(len(lista)):
        if i == n:
            lista.remove(i)
    return lista

#asignacion y llamada a la variable
valor = int(input("ingrese el valor a eliminar: "))
lista_sin_valores = eliminar_valores(valor, lista)

#definir variable
def es_capi(lista = list):
    #voltea la lista con metido de slicing y compara si la version volteada es igual a la original
    lista_capi = lista[::-1]
    if lista_capi == lista:
        return "es capicua"
    else:
        return "no es capicua"

#asignar valores y llamar la funcion
listaB = [1,5,9,10,9,5,1]
capi = es_capi (listaB)
print(capi)

