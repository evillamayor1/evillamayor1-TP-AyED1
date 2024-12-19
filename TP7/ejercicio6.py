"""a funcion de Ackermann A(m,n) se define de la siguiente forma:
n+1 si m = 0
A(m-1,1) si n = 0
A(m-1,A(m,n-1)) de otro modo
"""

#se define la funcion

def ackermann(m: int, n: int) -> int:
    """
    Calcula la funcion de Ackermann de manera recursiva

    Pre: m y n son números enteros no negativos (m >= 0, n >= 0)

    Post: se devuelve el resultado de la funcion de Ackermann A(m, n)
    """
    if m == 0:
        return n + 1  # caso base: si m = 0, se devuelve n + 1
    elif n == 0:
        return ackermann(m - 1, 1)  # si n = 0, calcular A(m-1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))  #calculo recursivo para m > 0 y n > 0

def mostrar_cuadro_ackermann(max_m: int, max_n: int):
    """
    Pre:
    - max_m y max_n son enteros positivos que indican los limites superiores para m y n

    Post:
    - Se imprime un cuadro textual con los valores de A(m, n)
    """
    print("Cuadro de valores de la funcion de Ackermann (A(m, n)):\n")
    
    #se imprime el encabezado
    print("m\\n |", end="")
    for n in range(max_n + 1):
        print(f" {n:3}", end="")
    print("\n" + "-" * (6 + (max_n + 1) * 4))

    #se imprimen las filas
    for m in range(max_m + 1):
        print(f"{m:3}  |", end="")
        for n in range(max_n + 1):
            print(f" {ackermann(m, n):3}", end="")
        print()  # salto de linea al final de cada fila