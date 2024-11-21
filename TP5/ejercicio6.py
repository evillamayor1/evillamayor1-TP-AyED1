"""6. El método index permite buscar un elemento dentro de una lista, devolviendo la 
posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se 
produce una excepción de tipo ValueError. Desarrollar un programa que cargue 
una lista con numeros enteros ingresados a través del teclado (terminando con -1) 
y permita que el usuario ingrese el valor de algunos elementos para visualizar la 
posición que ocupan, utilizando el método index. Si el numero no pertenece a la 
lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el 
proceso al tercer error detectado. No utilizar el operador in durante la busqueda."""

#se define la funcion
def buscar_elemento()-> None:
    """
    pre: no recibe parametros
    post: permite ingresar una lista de numeros y buscar sus posiciones, manejando excepciones
    """
    lista_numeros = []
    #se carga la lista con numeros hasta que se ingrese -1
    while True:
        try:
            numero = int(input("ingrese un numero (-1 para terminar): "))
            if numero == -1:
                break
            lista_numeros.append(numero)
        except ValueError:
            print("error: debe ingresar un numero entero")

    errores = 0
    #permite que el usuario busque numeros hasta el tercer error
    while errores < 3:
        try:
            buscar = int(input("ingrese el numero a buscar: "))
            posicion = lista_numeros.index(buscar)
            print(f"el numero {buscar} se encuentra en la posición {posicion}")
        except ValueError:
            errores += 1
            print("error: el numero no se encuentra en la lista")
        
        if errores == 3:
            print("se alcanzaron 3 errores, el programa se detiene")

#se ejecuta la funcion
buscar_elemento()
