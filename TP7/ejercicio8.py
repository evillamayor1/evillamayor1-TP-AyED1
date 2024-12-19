"""Realizar la implementación recursiva del metodo de selección para ordenar una lista 
de numeros enteros Sugerencia: Colocar el elemento mas pequeño en la primera 
posición, y luego ordenar el resto de la lista con una llamada recursiva No usar las 
funciones min() ni max() de Python"""

#se define la funcion

def seleccion_recursiva(lista: list[int], indice: int = 0) -> list[int]:
    """
    Pre: lista es una lista de numeros enteros indice es el indice actual en el que se busca el minimo (inicialmente 0)

    Post: Se devuelve la lista ordenada
    """
    #caso base: si la lista tiene un solo elemento o esta vacia, ya esta ordenada
    if indice == len(lista) - 1:
        return lista
    
    # encontrar el indice del valor minimo en la parte no ordenada
    min_indice = indice
    for i in range(indice + 1, len(lista)):
        if lista[i] < lista[min_indice]:
            min_indice = i
    
    # intercambia el valor minimo encontrado con el valor en la posición actual
    lista[indice], lista[min_indice] = lista[min_indice], lista[indice]
    
    # llamada recursiva para ordenar el resto de la lista
    return seleccion_recursiva(lista, indice + 1)