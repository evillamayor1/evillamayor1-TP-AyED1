""" Desarrollar un programa para rellenar una matriz de N x N con números enteros al 
azar comprendidos en el intervalo [0,N2
), de tal forma que ningún número se repita. Imprimir la matriz por pantalla"""

#se importa la libreria random
import random

#crea la funcion para la matriz random
def llenar_matriz_aleatoria(n: int) -> list:
    """
    pre: recibe el tamaño de la matriz n (entero positivo)
    post: retorna una matriz de tamaño n x n con números enteros aleatorios sin repeticiones
    """
    #genera una lista de números únicos dentro del rango [0, N^2)
    numeros = random.sample(range(n**2), n**2)

    #se llena la matriz con los números aleatorios generados
    matriz = []
    for i in range(n):
        fila = numeros[i * n:(i + 1) * n]
        matriz.append(fila)

    return matriz

#crea una funcion para imprimir toda la matriz
def imprimir_matriz(matriz: list) -> None:
    """
    pre: recibe una matriz
    post: imprime la matriz por pantalla
    """
    for fila in matriz:
        print(fila)

#se ejecuta el programa
n = int(input("Ingrese el tamaño de la matriz (n x n): "))
matriz = llenar_matriz_aleatoria(n)

print("\nMatriz generada:")
imprimir_matriz(matriz)
