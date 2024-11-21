""". Desarrollar un programa que permita realizar reservas en una sala de cine de N 
filas con M butacas por cada fila. Desarrollar las siguientes funciones y utilizarlas 
en un mismo programa:
mostrar_butacas: Mostrara por pantalla el estado de cada una de las butacas 
del cine. Esta funcion debera ser invocada antes de que se realice la reserva, y 
se volvera a invocar luego de la misma con los estados actualizados.
reservar: Debera recibir una matriz y la butaca seleccionada, y actualizara la 
sala en caso de estar disponible dicha butaca. La funcion devolvera True/False 
si logro o no reservar la butaca.
cargar_sala: Recibira una matriz como parametro y la cargara con valores 
aleatorios para simular una sala con butacas ya reservadas.
butacas_libres: Recibira como parametro la matriz y retornara cuantas butacas desocupadas hay en la sala.
butacas_contiguas: Buscara la secuencia mas larga de butacas libres contiguas en una misma fila y devolvera las coordenadas de inicio de la misma. """
 
import random

#se define la funcion para mostrar el estado de las butacas
def mostrar_butacas(sala: list) -> None:
    """
    pre: recibe una matriz que representa la sala
    post: imprime por pantalla el estado de cada butaca (0: libre, 1: reservada)
    """
    print("\nestado de la sala:")
    for fila in sala:
        print(" ".join(map(str, fila)))

#se define la funcion para reservar una butaca
def reservar(sala: list, fila: int, butaca: int) -> bool:
    """
    pre: recibe la matriz de la sala, el numero de fila y el numero de butaca
    post: retorna True si se logro reservar la butaca, False si ya estaba ocupada
    """
    if sala[fila][butaca] == 0:
        sala[fila][butaca] = 1
        return True
    else:
        return False

#se define la funcion para cargar la sala con valores aleatorios
def cargar_sala(sala: list) -> None:
    """
    pre: recibe la matriz de la sala
    post: actualiza la sala con valores aleatorios (0: libre, 1: reservada)
    """
    for i in range(len(sala)):
        for j in range(len(sala[0])):
            sala[i][j] = random.choice([0, 1])

#se define la funcion para contar las butacas libres
def butacas_libres(sala: list) -> int:
    """
    pre: recibe la matriz de la sala
    post: retorna la cantidad de butacas libres en la sala
    """
    return sum(fila.count(0) for fila in sala)

#se define la funcion para encontrar la secuencia mas larga de butacas libres contiguas
def butacas_contiguas(sala: list) -> tuple:
    """
    pre: recibe la matriz de la sala
    post: retorna una tupla con las coordenadas (fila, inicio, longitud) de la secuencia mas larga de butacas libres
    """
    mejor_fila, mejor_inicio, mejor_longitud = -1, -1, 0
    for i, fila in enumerate(sala):
        inicio, longitud = -1, 0
        for j, butaca in enumerate(fila):
            if butaca == 0:
                if longitud == 0:
                    inicio = j
                longitud += 1
            else:
                if longitud > mejor_longitud:
                    mejor_fila, mejor_inicio, mejor_longitud = i, inicio, longitud
                longitud = 0
        #verificar si la secuencia mas larga esta al final de la fila
        if longitud > mejor_longitud:
            mejor_fila, mejor_inicio, mejor_longitud = i, inicio, longitud
    return mejor_fila, mejor_inicio, mejor_longitud

#se solicita al usuario las dimensiones de la sala
n = int(input("ingrese el nmero de filas de la sala: "))
m = int(input("ingrese el nmero de butacas por fila: "))

#se inicializa la matriz de la sala
sala = [[0 for _ in range(m)] for _ in range(n)]

#se cargan las butacas con valores aleatorios
cargar_sala(sala)

#se muestra el estado inicial de las butacas
mostrar_butacas(sala)

#se cuenta y muestra la cantidad de butacas libres
print(f"\nla sala tiene {butacas_libres(sala)} butacas libres")

#se solicita al usuario reservar una butaca
fila = int(input("\ningrese el nmero de fila para la reserva: "))
butaca = int(input("ingrese el nmero de butaca para la reserva: "))

if reservar(sala, fila, butaca):
    print("\nreserva exitosa")
else:
    print("\nla butaca ya esta reservada")

#se muestra el estado actualizado de las butacas
mostrar_butacas(sala)

#se encuentra y muestra la secuencia mas larga de butacas libres contiguas
fila, inicio, longitud = butacas_contiguas(sala)
if fila != -1:
    print(f"\nla secuencia mas larga de butacas libres contiguas esta en la fila {fila}, comienza en la butaca {inicio} y tiene longitud {longitud}")
else:
    print("\nno hay secuencias de butacas libres contiguas")
