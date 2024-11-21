""" Desarrollar una función para ingresar a través del teclado un número natural. La 
función rechazará cualquier ingreso inválido de datos utilizando excepciones y 
mostrará la razón exacta del error. Controlar que se ingrese un número, que ese 
número sea entero y que sea mayor que 0, mostrando un mensaje con la razón 
exacta del error en caso necesario. Devolver el valor ingresado cuando éste sea 
correcto. Escribir también un programa que permita probar el correcto funcionamiento de la misma.
"""

#se define la funcion
def ingresar_numero()-> int:
    """
    pre: solicita al usuario un numero natural
    post: devuelve el numero si es valido, en caso de error muestra el mensaje de error
    """
    while True:
        try:
            #se pide el numero al usuario
            numero = input("ingrese un numero natural mayor que 0: ")

            #se verifica si el valor es un numero entero
            if not numero.isdigit():
                raise ValueError("debe ingresar un numero entero")

            numero = int(numero)

            #se verifica que el numero sea mayor que 0
            if numero <= 0:
                raise ValueError("el numero debe ser mayor que 0")

            #si todo es correcto, retorna el numero el numero
            return numero

        except ValueError as e:
            #si ocurre un error, se muestra el mensaje correspondiente
            print(f"error: {e}")

