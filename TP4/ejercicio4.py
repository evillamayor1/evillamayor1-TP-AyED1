""" Escribir una función que reciba como parámetro un número entero entre 0 y 3999 y 
lo convierta en un número romano, devolviéndolo en una cadena de caracteres. ¿En 
qué cambiaría la función si el rango de valores fuese diferente?"""

#se define la funcion
def convertir_a_romano(numero: int) -> str:
    """
    pre: recibe un número entero entre 0 y 3999
    post: retorna el equivalente del número en formato romano como una cadena
    """
    if not (0 < numero <= 3999):
        raise ValueError("el número debe estar entre 1 y 3999")
    
    #se definen los valores y símbolos romanos
    valores = [
        1000, 900, 500, 400, 
        100, 90, 50, 40, 
        10, 9, 5, 4, 1
    ]
    simbolos = [
        "M", "CM", "D", "CD", 
        "C", "XC", "L", "XL", 
        "X", "IX", "V", "IV", "I"
    ]
    
    romano = "" 
    for valor, simbolo in zip(valores, simbolos):
        while numero >= valor:
            romano += simbolo
            numero -= valor
    return romano

#programa principal
try:
    numero = int(input("ingrese un número entre 1 y 3999: "))
    print(f"el número romano es: {convertir_a_romano(numero)}")
except ValueError as e:
    print(e)
