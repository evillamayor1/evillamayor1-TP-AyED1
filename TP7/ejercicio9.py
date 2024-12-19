"""Realizar una función recursiva para imprimir una matriz de M x N con el formato 
apropiado
"""

#se define la funcion
def imprimir_matriz(matriz: list[list[int]], fila: int = 0) -> None:
    """
    Pre: matriz es una lista de listas de enteros (M x N) 
    fila es el índice de la fila actual que se está imprimiendo

    Post: Imprime la matriz en el formato adecuado, con cada fila en una nueva línea
    """
    # caso base: si se han impreso todas las filas, finaliza
    if fila == len(matriz):
        return
    
    #se imprime la fila actual
    print(" ".join(map(str, matriz[fila])))
    
    # llamada recursiva para imprimir la siguiente fila
    imprimir_matriz(matriz, fila + 1)
