"""Un hotel necesita un programa para gestionar la operación de sus habitaciones. El hotel 
cuenta con 10 pisos y 6 habitaciones por piso. Por cada huésped o grupo familiar que se aloja en el mismo se registra la siguiente información:
· DNI del cliente (número entero)
· Apellido y Nombre
· Fecha de ingreso (DDMMAAAA)
· Fecha de egreso (DDMMAAAA)
· Cantidad de ocupantes
Se solicita desarrollar un programa para realizar las siguientes tareas:
· Registrar el ingreso de huéspedes al hotel, hasta que se ingrese un número de DNI -1. 
Esta información deberá grabarse en un archivo CSV donde cada registro incluirá todos 
los campos indicados más arriba. Tener en cuenta que los números de DNI no pueden 
repetirse y que la fecha de salida debe ser mayor a la de entrada.
· Finalizado el ingreso de huéspedes se solicita"""

#se importan las librerias necesarias
import csv
from datetime import datetime

#se define la funcion
def registrar_huespedes(archivo_csv: str):
    """
    pre: se tiene un archivo csv para registrar los datos de los huespedes
    post: se graba un archivo csv con los datos validados de los huespedes
    """
    try:
        registros = []
        dnis = set() 

        while True:
            #se solicita el dni
            dni = input("ingresa el dni del huesped (-1 para finalizar): ").strip()
            if dni == "-1":
                break

            if not dni.isdigit():
                print("error: el dni debe ser un numero entero valido")
                continue

            dni = int(dni)
            if dni in dnis:
                print("error: el dni ya esta registrado")
                continue

            #se solicitan los otros datos
            nombre = input("ingresa el apellido y nombre del huesped: ").strip()
            fecha_ingreso = input("ingresa la fecha de ingreso (DDMMAAAA): ").strip()
            fecha_egreso = input("ingresa la fecha de egreso (DDMMAAAA): ").strip()
            ocupantes = input("ingresa la cantidad de ocupantes: ").strip()

            #validaciones
            try:
                fecha_ingreso_dt = datetime.strptime(fecha_ingreso, "%d%m%Y")
                fecha_egreso_dt = datetime.strptime(fecha_egreso, "%d%m%Y")
            except ValueError:
                print("error: las fechas deben estar en formato DDMMAAAA")
                continue

            if fecha_egreso_dt <= fecha_ingreso_dt:
                print("error: la fecha de egreso debe ser mayor que la fecha de ingreso")
                continue

            if not ocupantes.isdigit() or int(ocupantes) <= 0:
                print("error: la cantidad de ocupantes debe ser un numero entero mayor a 0")
                continue

            #se agrega el registro
            registros.append([
                dni, nombre, fecha_ingreso, fecha_egreso, int(ocupantes)
            ])
            dnis.add(dni)
            print("huesped registrado correctamente")

        #se graban los registros en el archivo csv
        with open(archivo_csv, "w", newline="", encoding="utf-8") as archivo:
            escritor_csv = csv.writer(archivo)
            escritor_csv.writerow(["dni", "nombre", "fecha_ingreso", "fecha_egreso", "ocupantes"])
            escritor_csv.writerows(registros)

        print(f"los datos han sido registrados en {archivo_csv}")

    except Exception as e:
        print(f"error inesperado: {e}")

#flujo principal
try:
    archivo_destino = input("ingresa el nombre del archivo csv para guardar los datos: ").strip()
    registrar_huespedes(archivo_destino)
except Exception as e:
    print(f"error inesperado: {e}")
