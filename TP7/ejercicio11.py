"""Desarrollar una función que devuelva el minimo elemento de una matriz de M x N"""


#se define la funcion

def minimo_matriz(matriz: list[list[int]], fila: int = 0, columna: int = 0, minimo: int = float('inf')) -> int:
    """
    Pre:
    matriz es una lista de listas de enteros (M x N).
    fila y columna son los indices actuales de la matriz.
    minimo es el valor minimo encontrado hasta el momento, inicializado a infinito.

    Post: Devuelve el minimo valor de la matriz.
    """
    # caso base: si se ha recorrido toda la matriz, devuelve el minimo
    if fila == len(matriz):
        return minimo
    
    # caso base: si se ha recorrido toda la columna de la fila actual, pasa a la siguiente fila
    if columna == len(matriz[fila]):
        return minimo_matriz(matriz, fila + 1, 0, minimo)
    
    # actualiza el minimo si encontro un valor menor
    nuevo_minimo = min(minimo, matriz[fila][columna])
    
    #llamada recursiva para el siguiente elemento en la columna
    return minimo_matriz(matriz, fila, columna + 1, nuevo_minimo)
