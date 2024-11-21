""" . Un hotel necesita un programa para gestionar la operacion de sus habitaciones. El 
hotel cuenta con 10 pisos y 6 habitaciones por piso. Por cada huesped o grupo 
familiar que se aloja en el mismo se registra la siguiente informacion:
· DNI del cliente (numero entero)
· Apellido y Nombre
· Fecha de ingreso (DDMMAAAA)
· Fecha de egreso (DDMMAAAA)
· Cantidad de ocupantes
Se solicita desarrollar un programa que utilice arreglos para realizar las siguientes 
tareas:
a. Registrar el ingreso de huespedes al hotel, hasta que se ingrese un numero de 
DNI igual a -1. Tener en cuenta que los numeros de DNI no pueden repetirse y 
que la fecha de salida debe ser mayor a la de entrada. El piso y habitacion son 
asignados arbitrariamente, y no puede asignarse una habitacion ya otorgada. 
b. Finalizado el ingreso de huespedes se solicita:
1. Mostrar el piso con mayor cantidad de habitaciones ocupadas.
2. Mostrar cuantas habitaciones vacias hay en todo el hotel.
3. Mostrar el piso con mayor cantidad de personas.
4. Mostrar cual sera la proxima habitacion en desocuparse. La fecha actual se 
ingresa por teclado. Mostrar todas las que correspondan.
5. Mostrar un listado de todos los huespedes registrados en el hotel, ordenado 
por apellido."""

#constantes para la estructura del hotel
PISOS = 10
HABITACIONES = 6

#se define la matriz del hotel
hotel = [[None for _ in range(HABITACIONES)] for _ in range(PISOS)]

#funcion para registrar huespedes
def registrar_huesped(hotel = list, dni = int, nombre = str, fecha_ingreso = int, fecha_egreso = int, ocupantes = int)-> bool:
    """
    pre: recibe el hotel y los datos del huesped
    post: asigna arbitrariamente una habitacion libre y registra los datos del huesped, retorna True si tuvo exito
    """
    for piso in range(PISOS):
        for habitacion in range(HABITACIONES):
            if hotel[piso][habitacion] is None:  
                hotel[piso][habitacion] = {
                    "dni": dni,
                    "nombre": nombre,
                    "fecha_ingreso": fecha_ingreso,
                    "fecha_egreso": fecha_egreso,
                    "ocupantes": ocupantes
                }
                return True
    return False 

#funcion para encontrar el piso con mas habitaciones ocupadas
def piso_mas_ocupado(hotel = list)-> None:
    """
    pre: recibe el hotel
    post: retorna el piso con mayor cantidad de habitaciones ocupadas
    """
    ocupados_por_piso = [sum(1 for habitacion in piso if habitacion) for piso in hotel]
    return ocupados_por_piso.index(max(ocupados_por_piso)) + 1

#funcion para contar habitaciones vacias
def habitaciones_vacias(hotel = list)-> None:
    """
    pre: recibe el hotel
    post: retorna la cantidad total de habitaciones vacias en el hotel
    """
    return sum(1 for piso in hotel for habitacion in piso if habitacion is None)

#funcion para encontrar el piso con mas personas
def piso_con_mas_personas(hotel = list)-> None:
    """
    pre: recibe el hotel
    post: retorna el piso con mayor cantidad total de ocupantes
    """
    personas_por_piso = [sum(habitacion["ocupantes"] for habitacion in piso if habitacion) for piso in hotel]
    return personas_por_piso.index(max(personas_por_piso)) + 1

#funcion para encontrar la proxima habitacion en desocuparse
def proxima_desocupacion(hotel = list, fecha_actual = int)-> list:
    """
    pre: recibe el hotel y la fecha actual
    post: retorna una lista con las habitaciones que se desocuparan primero (si la fecha de egreso es menor o igual a la actual)
    """
    proximas = []
    for piso, habitaciones in enumerate(hotel):
        for habitacion, datos in enumerate(habitaciones):
            if datos and datos["fecha_egreso"] <= fecha_actual:
                proximas.append({"piso": piso + 1, "habitacion": habitacion + 1, **datos})
    return proximas

#funcion para mostrar el listado de huespedes ordenado por apellido
def listar_huespedes(hotel = list)-> list:
    """
    pre: recibe el hotel
    post: retorna una lista de todos los huespedes ordenada por apellido
    """
    huespedes = [habitacion for piso in hotel for habitacion in piso if habitacion]
    return sorted(huespedes, key=lambda x: x["nombre"].split()[0].lower())

#programa principal
while True:
    print("\n1. registrar nuevo huesped")
    print("2. mostrar piso con mayor cantidad de habitaciones ocupadas")
    print("3. mostrar cuantas habitaciones vacias hay en todo el hotel")
    print("4. mostrar el piso con mayor cantidad de personas")
    print("5. mostrar la proxima habitacion en desocuparse")
    print("6. mostrar listado de huespedes ordenado por apellido")
    print("7. salir")
    opcion = input("ingrese una opcion: ")

    if opcion == "1":
        while True:
            dni = int(input("ingrese el dni del cliente (-1 para terminar): "))
            if dni == -1:
                break
            nombre = input("ingrese el apellido y nombre del cliente: ")
            fecha_ingreso = input("ingrese la fecha de ingreso (DDMMAAAA): ")
            fecha_egreso = input("ingrese la fecha de egreso (DDMMAAAA): ")
            if fecha_egreso <= fecha_ingreso:
                print("la fecha de egreso debe ser mayor a la de ingreso")
                continue
            ocupantes = int(input("ingrese la cantidad de ocupantes: "))

            if not registrar_huesped(hotel, dni, nombre, fecha_ingreso, fecha_egreso, ocupantes):
                print("no hay habitaciones disponibles")
                break

    elif opcion == "2":
        print(f"el piso con mayor cantidad de habitaciones ocupadas es el {piso_mas_ocupado(hotel)}")

    elif opcion == "3":
        print(f"el numero total de habitaciones vacias es {habitaciones_vacias(hotel)}")

    elif opcion == "4":
        print(f"el piso con mayor cantidad de personas es el {piso_con_mas_personas(hotel)}")

    elif opcion == "5":
        fecha_actual = input("ingrese la fecha actual (DDMMAAAA): ")
        proximas = proxima_desocupacion(hotel, fecha_actual)
        if proximas:
            print("\nhabitaciones proximas a desocuparse:")
            for habitacion in proximas:
                print(f"piso: {habitacion['piso']}, habitacion: {habitacion['habitacion']}, fecha de egreso: {habitacion['fecha_egreso']}")
        else:
            print("no hay habitaciones proximas a desocuparse")

    elif opcion == "6":
        listado = listar_huespedes(hotel)
        if listado:
            print("\nlistado de huespedes:")
            for huesped in listado:
                print(f"nombre: {huesped['nombre']}, dni: {huesped['dni']}, piso: {hotel.index(huesped) // 6 + 1}")
        else:
            print("no hay huespedes registrados")

    elif opcion == "7":
        print("saliendo del programa")
        break

    else:
        print("opcion invalida, intente nuevamente")
