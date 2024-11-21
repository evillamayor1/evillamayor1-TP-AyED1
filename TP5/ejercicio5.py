""". La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del 
módulo math. Escribir un programa que utilice esta función para calcular la raíz 
cuadrada de un número cualquiera ingresado a través del teclado. El programa 
debe utilizar manejo de excepciones para evitar errores si se ingresa un número 
negativo"""

#se importa match para facilitar el ejercicio
import math

#se define la funcion
def calcular_raiz_cuadrada()-> None:
    """
    pre: no recibe parametros
    post: solicita un numero al usuario y calcula su raiz cuadrada, manejando excepciones
    """
    try:
        numero = float(input("ingrese un numero para calcular su raiz cuadrada: "))
        if numero < 0:
            raise ValueError("no se puede calcular la raiz cuadrada de un numero negativo")
        resultado = math.sqrt(numero)
        print(f"la raiz cuadrada de {numero} es {resultado}")
    except ValueError as e:
        #se captura la excepcion ValueError si el numero es negativo o no valido
        print(f"error: {e}")
    except Exception as e:
        #se captura cualquier otra excepcion
        print(f"error inesperado: {e}")

#se llama a la funcion
calcular_raiz_cuadrada()
