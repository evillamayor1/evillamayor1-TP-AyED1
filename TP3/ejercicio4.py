"""Una fabrica de bicicletas guarda en una matriz la cantidad de unidades producidas 
en cada una de sus plantas durante una semana. De este modo, cada columna representa el día de la semana y cada fila a una de sus fabricas
Se solicita:
a. Crear una matriz con datos generados al azar para N fabricas durante una 
semana, considerando que la capacidad máxima de fabricación es de 150 
unidades por día y puede suceder que en ciertos días no se fabrique ninguna. 
b. Mostrar la cantidad total de bicicletas fabricadas por cada fabrica. 
c. Cuál es la fabrica que más produjo en un solo día (detallar día y fabrica).
d. Cuál es el día más productivo, considerando todas las fabricas combinadas.
e. Crear una lista por comprensión que contenga la menor cantidad fabricada 
por cada fabrica."""

#se importa la libreria random
import random

#se define la funcion
def generar_matriz_bicicletas(n_fabricas: int, dias: int) -> list:
    """
    pre: recibe el numero de fabricas y dias
    post: retorna una matriz con la cantidad de bicicletas producidas por cada fabrica durante la semana
    """
    matriz = []
    for _ in range(n_fabricas):
        fila = [random.randint(0, 150) for _ in range(dias)]
        matriz.append(fila)
    return matriz

#se define la funcion
def mostrar_total_fabricado(matriz: list) -> None:
    """
    pre: recibe una matriz con las producciones diarias
    post: imprime la cantidad total de bicicletas fabricadas por cada fabrica
    """
    for i, fila in enumerate(matriz):
        total = sum(fila)
        print(f"fabrica {i+1}: {total} bicicletas")

#se define la funcion
def fabrica_mas_productiva(matriz: list) -> None:
    """
    pre: recibe una matriz con las producciones diarias
    post: imprime la fabrica que más produjo en un solo día, detallando el día y la cantidad
    """
    max_bicicletas = 0
    dia_max = -1
    fabrica_max = -1

    for i, fila in enumerate(matriz):
        for j, cantidad in enumerate(fila):
            if cantidad > max_bicicletas:
                max_bicicletas = cantidad
                fabrica_max = i + 1
                dia_max = j + 1

    print(f"la fabrica {fabrica_max} produjo más en el daa {dia_max} con {max_bicicletas} bicicletas")

#se define la funcion
def dia_mas_productivo(matriz: list) -> None:
    """
    pre: recibe una matriz con las producciones diarias
    post: imprime el día más productivo considerando todas las fabricas
    """
    total_dia = [sum(matriz[i][j] for i in range(len(matriz))) for j in range(len(matriz[0]))]
    dia_max = total_dia.index(max(total_dia)) + 1
    print(f"el día más productivo fue el día {dia_max} con {max(total_dia)} bicicletas")

#se define la funcion
def menor_produccion_por_fabrica(matriz: list) -> list:
    """
    pre: recibe una matriz con las producciones diarias
    post: retorna una lista con la menor cantidad de bicicletas fabricadas por cada fabrica
    """
    menores = [min(fila) for fila in matriz]
    print(f"menor producción por fabrica: {menores}")
    return menores

#se ejecuta del programa
n_fabricas = int(input("ingrese el numero de fabricas: "))
dias = 7  # ya que se considera una semana de 7 días

matriz = generar_matriz_bicicletas(n_fabricas, dias)
mostrar_total_fabricado(matriz)
fabrica_mas_productiva(matriz)
dia_mas_productivo(matriz)
menor_produccion_por_fabrica(matriz)
