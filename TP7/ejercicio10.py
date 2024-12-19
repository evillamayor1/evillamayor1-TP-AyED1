"""ir una función que sume todos los elementos de una matriz de M x N y devuelva el resultado. No usar la función sum()."""


#se define la funcion

def sumar_matriz(matriz: list[list[int]], fila: int = 0, columna: int = 0) -> int:
    """

    Pre:
     matriz es una lista de listas de enteros (M x N)
     fila y columna son los índices actuales que se están sumando

    Post:
     Devuelve la suma de todos los elementos de la matriz
    """
    # caso base: si se ha recorrido todas las filas y columnas, finaliza
    if fila == len(matriz):
        return 0
    
    # caso base: si se ha recorrido toda la fila actual, pasamos a la siguiente fila
    if columna == len(matriz[fila]):
        return sumar_matriz(matriz, fila + 1, 0)
    
    #se suma el elemento actual y llamar recursivamente para la siguiente columna
    return matriz[fila][columna] + sumar_matriz(matriz, fila, columna + 1)