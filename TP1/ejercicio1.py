#ejercicio1

"""Desarrollar una función que reciba tres números enteros positivos y devuelva el 
mayor de los tres, sólo si éste es único (es decir el mayor estricto). Devolver -1 en 
caso de no haber ninguno. No utilizar operadores lógicos (and, or, not). Desarrollar 
también un programa para ingresar los tres valores, invocar a la función y mostrar 
el máximo hallado, o un mensaje informativo si éste no existe"""

#crear la funcion recibiendo 3 numeros enteros
def mayor_abs (n1 = int, n2 = int, n3 = int) -> int:
    """
    Pre: esta funcion recibe 3 numeros enteros

    post: esta funcion retorna un entero

    """

    #definir el mayor entre los 3 numeros
    mayor = max(n1, n2, n3)
    #comprobar cuantas veces aparece el numero mayor
    contador_mayor = 0
    if mayor == n1:
        contador_mayor +=1
    if mayor == n2:
        contador_mayor +=1
    if mayor == n3:
        contador_mayor +=1
    
    #si el numero mayor aparece mas de una vez, no es el mayor absoluto, por lo tanto retorna -1
    if contador_mayor != 1:
        print(-1)
    else:
        print(mayor)

#definir los 3 numeros
n1 = int(input("ingrese un numero:"))
n2 = int(input("ingrese un numero:"))
n3 = int(input("ingrese un numero:"))

#llamada a la funcion
mayor_abs(n1, n2, n3)