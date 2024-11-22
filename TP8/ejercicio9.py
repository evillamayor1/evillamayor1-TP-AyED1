"""Escribir un programa que permita ingresar un numero entero N y genere un 
diccionario por comprension con la tabla de multiplicar de N del 1 al 12. Mostrar la 
tabla de multiplicar con el formato apropiado."""

#se define la funcion
def tabla_multiplicar():
    #se ingresa el numero para la tabla de multiplicar
    N = int(input("Ingresa un numero entero N para generar su tabla de multiplicar: "))
    
    #genera el diccionario con la tabla de multiplicar usando comprension de diccionario
    tabla = {i: N * i for i in range(1, 13)}
    
    #se muestra la tabla de multiplicar en formato adecuado
    print(f"\nTabla de multiplicar de {N}:")
    for i in range(1, 13):
        print(f"{N} x {i} = {tabla[i]}")

#se ejecuta la funcion
tabla_multiplicar()
