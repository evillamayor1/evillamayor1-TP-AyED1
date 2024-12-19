""" Escribir una funcion que devuelva la suma de los N primeros numeros naturales"""

#se define l funcion
def suma_numeros_naturales(n: int) -> int:
    """
    Pre: n es un entero no negativo (n >= 0)

    Post: se devuelve un entero que representa la suma de los numeros naturales desde 1 hasta N
    """
    if n == 0:
        return 0  #caso base: la suma de los primeros 0 numeros es 0
    else:
        return n + suma_numeros_naturales(n - 1)  #recursion sumando n

