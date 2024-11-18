"""
12. Resolver el siguiente problema, utilizando funciones:
Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se 
ingresa el número de socio de cinco dígitos hasta ingresar un cero como fin de carga. Se solicita:
a. Informar para cada socio, cuántas veces ingresó al club. Cada socio debe 
aparecer una sola vez en el informe.
b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus 
ingresos. Mostrar los registros de entrada al club antes y después de 
eliminarlo. Informar cuántos ingresos se eliminaron
"""

#se importa la librería de expresiones regulares
import re

#se crea la expresion regular para validar un número de socio
socio_pattern = re.compile(r"^\d{5}$")

#se define la funcion
def registrar_ingresos(none) -> list:
    """
    pre:esta funcion no requiere parametros externos
    post:esta funcion retorna una lista con los números de socio registrados
    """
    ingresos = []
    while True:
        numero_socio = input("ingrese el numero de socio (5 dígitos) o 0 para finalizar: ")
        if numero_socio == "0":
            break
        if not socio_pattern.match(numero_socio):
            print("el numero de socio debe ser un entero de 5 digitos.")
            continue
        ingresos.append(int(numero_socio))
    return ingresos

#se define la funcion para contar los ingresos por socio
def contar_ingresos(ingresos=list) -> None:
    """
    pre: recibe una lista con los números de socios registrados.
    post: imprime un informe con la cantidad de ingresos por cada socio.
    """
    conteo = {}
    for socio in ingresos:
        conteo[socio] = conteo.get(socio, 0) + 1

    print("\nregistro de ingresos por socio:")
    for socio, cantidad in conteo.items():
        print(f"socio {socio}: {cantidad} ingresos")

#se define la funcion para eliminar los ingresos de un socio
def eliminar_socio(ingresos=list) -> list:
    """
    pre: recibe una lista con los numeros de socios registrados
    post: solicita un numero de socio, imprime sus datos y confirma su eliminacion
    """
    print("\nregistros actuales de ingresos:", ingresos)
    while True:
        numero_socio = input("ingrese el numero de socio que se dio de baja (5 digitos): ")
        if not socio_pattern.match(numero_socio):
            print("el numero de socio debe ser un entero de 5 digitos.")
            continue
        numero_socio = int(numero_socio)
        break

    eliminados = ingresos.count(numero_socio)
    ingresos_filtrados = [socio for socio in ingresos if socio != numero_socio]

    print("\nregistros de ingresos despues de la eliminacion:", ingresos_filtrados)
    print(f"se eliminaron {eliminados} ingresos del socio {numero_socio}.")
    return ingresos_filtrados

#se asignan los valores y se llama a las funciones
ingresos = registrar_ingresos()
contar_ingresos(ingresos)
ingresos = eliminar_socio(ingresos)
