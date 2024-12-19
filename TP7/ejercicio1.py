"""Escribir una función que devuelva la cantidad de digitos de un numero entero, sin 
utilizar cadenas de caracteres.
"""

#se define la funcion

def contar_digitos(numero: int) -> int:
    """
    Pre: numero es un numero entero (positivo, negativo o cero)

    Post: Se devuelve la cantidad de digitos del numero
    """
    numero = abs(numero)  #se toma el valor absoluto para ignorar el signo
    if numero < 10:
        return 1  #caso base: un solo digito
    else:
        return 1 + contar_digitos(numero // 10)  #recursion con división entera
