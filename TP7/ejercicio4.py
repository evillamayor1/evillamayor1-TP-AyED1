"""Desarrollar una función que devuelva el producto de dos numeros enteros por sumas sucesivas"""

#se define la funcion
def producto_por_sumas(a: int, b: int) -> int:
    """
    Pre:
    - a y b son numeros enteros

    Post: se devuelve el producto de a y b calculado mediante sumas sucesivas
    """
    # caso base: si uno de los numeros es 0, el producto es 0
    if b == 0:
        return 0
    
    #si b es positivo, suma a recursivamente
    if b > 0:
        return a + producto_por_sumas(a, b - 1)
    
    #si b es negativo, invierte el signo del producto
    return -producto_por_sumas(a, -b)
