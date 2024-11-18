""". Escribir una función que reciba una lista como parámetro y devuelva True si la lista 
está ordenada en forma ascendente o False en caso contrario. Por ejemplo, 
ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar 
además un programa para verificar el comportamiento de la función."""

#definir la funcion:
def esta_ordenado(lista)-> bool:
    """
    pre: esta funcion recibe una lista

    post: esta funcion retorna un valor booleano
    
    """
    #comprueba que el valor siguiente a i sea mayor a este, de ser caso contrario, la lista no esta orenada
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True


#solicita al usuario 10 valores que se agregaran a la lista 
lista = []
for i in range(10):
    numero = int(input("ingrese un numero"))
    lista.append(numero)

#usa la lista como parametro para la funcion y devuelve una respuesta 
resultado = esta_ordenado(lista)
if resultado == True:
    print("la lista esta ordenada")
else:
    print("la lista no esta ordenada")