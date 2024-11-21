"""Las siguientes matrices responden distintos patrones de relleno. Desarrollar funciones que generen cada una de ellas sin intervencion humana y escribir un programa 
que las invoque e imprima por pantalla. El tamaño de las matrices debe establecerse como N x N, donde N se ingresa a traves del teclado.
"""

# se define la funcion para generar la matriz a
def generar_matriz_a(n: int) -> list:
    # pre: recibe el tamaño n de la matriz
    # post: retorna la matriz con ceros excepto la diagonal principal con numeros de 1 a n
    return [[i + 1 if i == j else 0 for j in range(n)] for i in range(n)]

# se define la funcion para generar la matriz b
def generar_matriz_b(n: int) -> list:
    # pre: recibe el tamaño n de la matriz
    # post: retorna la matriz con ceros excepto la diagonal secundaria con potencias de 3
    return [[3 ** (n - i - 1) if j == n - i - 1 else 0 for j in range(n)] for i in range(n)]

# se define la funcion para generar la matriz c
def generar_matriz_c(n: int) -> list:
    # pre: recibe el tamaño n de la matriz
    # post: retorna la matriz con ceros excepto la diagonal principal y secundaria con valores alternados
    return [[4 if i == j else 2 if j == n - i - 1 else 0 for j in range(n)] for i in range(n)]

# se define la funcion para generar la matriz d
def generar_matriz_d(n: int) -> list:
    # pre: recibe el tamaño n de la matriz
    # post: retorna la matriz donde cada fila tiene el mismo valor descendente
    return [[n - i for _ in range(n)] for i in range(n)]

# se define la funcion para generar la matriz e
def generar_matriz_e(n: int) -> list:
    # pre: recibe el tamaño n de la matriz
    # post: retorna la matriz con valores crecientes por fila de izquierda a derecha
    return [[i + j for j in range(n)] for i in range(n)]

# se define la funcion para generar la matriz f
def generar_matriz_f(n: int) -> list:
    # pre: recibe el tamaño n de la matriz
    # post: retorna la matriz con ceros excepto las diagonales y el centro
    return [[1 if i == j or j == n - i - 1 else 0 for j in range(n)] for i in range(n)]

# se define la funcion para generar la matriz g
def generar_matriz_g(n: int) -> list:
    # pre: recibe el tamaño n de la matriz
    # post: retorna la matriz con numeros consecutivos por filas
    return [[i * n + j + 1 for j in range(n)] for i in range(n)]

# se define la funcion para generar la matriz h
def generar_matriz_h(n: int) -> list:
    # pre: recibe el tamaño n de la matriz
    # post: retorna la matriz con numeros consecutivos por columnas
    return [[j * n + i + 1 for j in range(n)] for i in range(n)]

# se define la funcion para generar la matriz i
def generar_matriz_i(n: int) -> list:
    # pre: recibe el tamaño n de la matriz
    # post: retorna la matriz con valores iguales en cada fila
    return [[n + j for j in range(n)] for _ in range(n)]

# se define la funcion para imprimir una matriz
def imprimir_matriz(matriz: list) -> None:
    # pre: recibe una matriz
    # post: imprime la matriz fila por fila
    for fila in matriz:
        print(" ".join(map(str, fila)))

# se solicita al usuario el tamaño de la matriz
n = int(input("ingrese el tamaño de la matriz (N x N): "))

# se generan y se imprimen todas las matrices
print("\nmatriz a:")
imprimir_matriz(generar_matriz_a(n))

print("\nmatriz b:")
imprimir_matriz(generar_matriz_b(n))

print("\nmatriz c:")
imprimir_matriz(generar_matriz_c(n))

print("\nmatriz d:")
imprimir_matriz(generar_matriz_d(n))

print("\nmatriz e:")
imprimir_matriz(generar_matriz_e(n))

print("\nmatriz f:")
imprimir_matriz(generar_matriz_f(n))

print("\nmatriz g:")
imprimir_matriz(generar_matriz_g(n))

print("\nmatriz h:")
imprimir_matriz(generar_matriz_h(n))

print("\nmatriz i:")
imprimir_matriz(generar_matriz_i(n))
