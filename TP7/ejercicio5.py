"""Realizar una función que devuelva el resto de dos numeros enteros, utilizando restas sucesivas"""

#se define la funcion

def resto_por_restas(dividendo: int, divisor: int) -> int:
    """
    Pre:
    divisor debe ser un numero distinto de 0
    dividendo y divisor son numeros enteros

    Post: se devuelve el resto de dividir dividendo entre divisor
    """
    if divisor == 0:
        raise ValueError("El divisor no puede ser 0")
    
    #manejo de casos para numeros negativos
    if dividendo < 0:
        return -resto_por_restas(-dividendo, divisor)
    if divisor < 0:
        return resto_por_restas(dividendo, -divisor)
    
    #caso base: si el dividendo es menor que el divisor, el resto sera el dividendo
    if dividendo < divisor:
        return dividendo
    
    #paso recursivo: resta el divisor del dividendo y continuar
    return resto_por_restas(dividendo - divisor, divisor)