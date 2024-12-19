""" Desarrollar una funcion que reciba un numero binario y lo devuelva convertido a 
base decimal. """

#se define la funcion
def binario_a_decimal(binario: int) -> int:
    """
    Pre: binario es un numero entero que representa un valor binario (solo contiene digitos 0 y 1).

    Post: se retorna un numero entero en base decimal equivalente al binario proporcionado.
    """
    if binario == 0:
        return 0  # caso base: un numero binario vacio o cero equivale a 0 en decimal

    # separa el digito más significativo
    digito = binario % 10

    #se realiza la recursion y multiplicar el resultado por 2
    return digito + 2 * binario_a_decimal(binario // 10)