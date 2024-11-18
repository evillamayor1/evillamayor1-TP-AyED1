"""Intercalar los elementos de una lista entre los elementos de otra. La intercalación 
deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará 
una lista nueva sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3] 
y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7]. Las listas pueden 
tener distintas longitudes."""

#se define la variable a usar
def intercalar(lista1 = list, lista2 = list) -> list: 
    """
    pre: esta funcion recibe una lista

    post: esta funcion retorna una lista
    
    """
    #se calcula la longitud minima que va tener que usarse en el bucle
    longitud = min(len(lista1), len(lista2))
    #se usa un buble for para agregar los elementos de la lista 2 a la 1
    for i in range(longitud):
        lista1[2*i+1:2*i+1] = [lista2[i]]

    #si la lista es mas larga solo se agregan los elementos restantes
    if len(lista2) > len(lista1):
        lista1[len(lista1):] = lista2[len(lista1)//2:]
    return lista1

lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]
lista_final = intercalar(lista1, lista2)

print(lista_final)