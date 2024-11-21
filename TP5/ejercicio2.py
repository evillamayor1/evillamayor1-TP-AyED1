""". Realizar una función que reciba como parámetros dos cadenas de caracteres conteniendo números reales, sume ambos valores y devuelva el resultado como un 
número real. Devolver -1 si alguna de las cadenas no contiene un número válido, 
utilizando manejo de excepciones para detectar el error."""

#se define la funcion
def sumar_cadenas(cadena1: str, cadena2: str) -> float:
    """
    pre: recibe dos cadenas que representan numeros reales
    post: devuelve la suma de los dos numeros como numero real o -1 si alguna cadena no es un numero valido
    """
    try:
        #se inteta convertir las cadenas a flotantes
        num1 = float(cadena1)
        num2 = float(cadena2)
        return num1 + num2
    except ValueError:
        #si ocurre un error de valor, se devuelve -1
        return -1

#ejemplo de uso
cadena1 = "12.34"
cadena2 = "56.78"
resultado = sumar_cadenas(cadena1, cadena2)

if resultado == -1:
    print("error: una o ambas cadenas no son numeros validos")
else:
    print(f"el resultado de la suma es: {resultado}")
