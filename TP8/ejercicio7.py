""" Definir un conjunto con numeros enteros entre 0 y 9. Luego solicitar valores al 
usuario y eliminarlos del conjunto mediante el metodo remove, mostrando el contenido del conjunto luego de cada eliminacion. Finalizar el proceso al ingresar -1. 
Utilizar manejo de excepciones para evitar errores al intentar quitar elementos 
inexistentes.
"""

#se define la funcion
def eliminar_elementos():
    #se define el conjunto con los numeros del 0 al 9
    numeros = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    
    while True:
        try:
            #se olicita un numero al usuario
            valor = int(input("Ingresa un numero para eliminar del conjunto (o -1 para terminar): "))
            
            #si el valor es -1, terminamos el proceso
            if valor == -1:
                break
                
            #se intenta eliminar el valor del conjunto
            numeros.remove(valor)
            
            #se muestra el conjunto despues de la eliminacion
            print("Conjunto despues de la eliminacion:", numeros)
        
        except KeyError:
            #se maneha el error cuando el numero no está en el conjunto
            print(f"El numero {valor} no está en el conjunto.")
        
        except ValueError:
            #se maneja el error si el valor ingresado no es un numero entero
            print("Por favor, ingresa un numero entero válido.")

#se ejecuta la funcion
eliminar_elementos()
