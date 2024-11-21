"""
1. Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento, imprimiendo la matriz luego de invocar a cada función:
a. Cargar números enteros en una matriz de N x N, ingresando los datos desde 
teclado. 
b. Ordenar en forma ascendente cada una de las filas de la matriz.
c. Intercambiar dos filas, cuyos números se reciben como parámetro.
d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
e. Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
f. Calcular el promedio de los elementos de una fila, cuyo número se recibe como 
parámetro.
g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo número se recibe como parámetro.
h. Determinar si la matriz es simétrica con respecto a su diagonal principal.
i. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
j. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo 
una lista con los números de las mismas.
NOTA: El valor de N debe leerse por teclado. Las funciones deben servir cualquiera 
sea el valor ingresado.
"""

# se define la función para cargar números en una matriz
def cargar_matriz(n: int) -> list:
    """
    pre: recibe el tamaño de la matriz n (entero positivo)
    post: retorna una matriz de tamaño n x n con valores ingresados desde teclado
    """
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            valor = int(input(f"ingrese el valor para la posición ({i+1},{j+1}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

# se define la función para ordenar filas de la matriz
def ordenar_filas(matriz: list) -> list:
    """
    pre: recibe una matriz de tamaño n x n
    post: retorna la matriz con las filas ordenadas en forma ascendente
    """
    for fila in matriz:
        fila.sort()
    return matriz

# se define la función para intercambiar dos filas
def intercambiar_filas(matriz: list, fila1: int, fila2: int) -> list:
    """
    pre: recibe una matriz y dos índices de fila
    post: retorna la matriz con las filas intercambiadas
    """
    matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]
    return matriz

# se define la función para intercambiar dos columnas
def intercambiar_columnas(matriz: list, col1: int, col2: int) -> list:
    """
    pre: recibe una matriz y dos índices de columna
    post: retorna la matriz con las columnas intercambiadas
    """
    for fila in matriz:
        fila[col1], fila[col2] = fila[col2], fila[col1]
    return matriz

# se define la función para transponer la matriz
def transponer_matriz(matriz: list) -> list:
    """
    pre: recibe una matriz de tamaño n x n
    post: retorna la matriz traspuesta sobre sí misma
    """
    n = len(matriz)
    for i in range(n):
        for j in range(i + 1, n):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]
    return matriz

# se define la función para calcular el promedio de una fila
def promedio_fila(matriz: list, fila: int) -> float:
    """
    pre: recibe una matriz y el índice de una fila
    post: retorna el promedio de los elementos de la fila indicada
    """
    return sum(matriz[fila]) / len(matriz[fila])

# se define la función para calcular el porcentaje de impares en una columna
def porcentaje_impares_columna(matriz: list, columna: int) -> float:
    """
    pre: recibe una matriz y el índice de una columna
    post: retorna el porcentaje de elementos impares en la columna indicada
    """
    impares = sum(1 for fila in matriz if fila[columna] % 2 != 0)
    return (impares / len(matriz)) * 100

# se define la función para verificar simetría con respecto a la diagonal principal
def es_simetrica_principal(matriz: list) -> bool:
    """
    pre: recibe una matriz de tamaño n x n
    post: retorna True si la matriz es simétrica respecto a la diagonal principal
    """
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

# se define la función para verificar simetría con respecto a la diagonal secundaria
def es_simetrica_secundaria(matriz: list) -> bool:
    """
    pre: recibe una matriz de tamaño n x n
    post: retorna True si la matriz es simétrica respecto a la diagonal secundaria
    """
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[n - 1 - i][n - 1 - j]:
                return False
    return True

# se define la función para encontrar columnas capicúa
def columnas_capicua(matriz: list) -> list:
    """
    pre: recibe una matriz de tamaño n x n
    post: retorna una lista con los números de las columnas capicúa
    """
    n = len(matriz)
    columnas = []
    for col in range(n):
        columna = [matriz[i][col] for i in range(n)]
        if columna == columna[::-1]:
            columnas.append(col)
    return columnas

# ejecución del programa
n = int(input("ingrese el tamaño de la matriz (n x n): "))
matriz = cargar_matriz(n)

print("\nmatriz inicial:")
for fila in matriz:
    print(fila)

matriz = ordenar_filas(matriz)
print("\nmatriz con filas ordenadas:")
for fila in matriz:
    print(fila)

fila1, fila2 = map(int, input("ingrese dos filas a intercambiar (separadas por un espacio): ").split())
matriz = intercambiar_filas(matriz, fila1, fila2)
print("\nmatriz con filas intercambiadas:")
for fila in matriz:
    print(fila)

col1, col2 = map(int, input("ingrese dos columnas a intercambiar (separadas por un espacio): ").split())
matriz = intercambiar_columnas(matriz, col1, col2)
print("\nmatriz con columnas intercambiadas:")
for fila in matriz:
    print(fila)

matriz = transponer_matriz(matriz)
print("\nmatriz traspuesta:")
for fila in matriz:
    print(fila)

fila = int(input("ingrese el número de fila para calcular el promedio: "))
print(f"\npromedio de la fila {fila}: {promedio_fila(matriz, fila):.2f}")

columna = int(input("ingrese el número de columna para calcular el porcentaje de impares: "))
print(f"\nporcentaje de impares en la columna {columna}: {porcentaje_impares_columna(matriz, columna):.2f}%")

print(f"\nla matriz es simétrica respecto a la diagonal principal: {es_simetrica_principal(matriz)}")
print(f"la matriz es simétrica respecto a la diagonal secundaria: {es_simetrica_secundaria(matriz)}")

print(f"\ncolumnas capicúa: {columnas_capicua(matriz)}")
