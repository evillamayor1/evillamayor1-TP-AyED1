""" Desarrollar las siguientes funciones utilizando tuplas para representar fechas y horarios, y luego escribir un programa que las vincule:
a. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha 
válida.
b. Sumar N días a una fecha.
c. Ingresar un horario desde teclado, verificando que sea correcto.
d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al 
segundo se considerará que el primero corresponde al día anterior. En ningún 
caso la diferencia en horas puede superar las 24 horas.
"""

#impotan las librerias requeridas
from datetime import datetime, timedelta

#se define la funcion
def ingresar_fecha() -> tuple:
    """
    pre: no se reciben parámetros
    post: se devuelve una tupla con fecha válida (dia, mes, anio)
    """
    while True:
        try:
            fecha = input("ingresa una fecha en formato dd/mm/aaaa: ")
            dia, mes, anio = map(int, fecha.split('/'))
            # validar si la fecha es válida al intentar crear un objeto datetime
            datetime(anio, mes, dia)
            return (dia, mes, anio)
        except ValueError:
            print("fecha invalida. intenta de nuevo")

def sumar_dias(fecha= int, dias=int)-> tuple:
    """
    pre: se recibe una tupla con fecha (dia, mes, anio) y un entero con los dias a sumar
    post: se devuelve una nueva tupla con la fecha resultante (dia, mes, anio)
    """
    dia, mes, anio = fecha
    fecha_base = datetime(anio, mes, dia)
    nueva_fecha = fecha_base + timedelta(days=dias)
    return (nueva_fecha.day, nueva_fecha.month, nueva_fecha.year)

def ingresar_horario()-> tuple:
    """
    pre: no se reciben parámetros
    post: se devuelve una tupla con un horario válido (hora, minuto, segundo)
    """
    while True:
        try:
            horario = input("ingresa un horario en formato hh:mm:ss: ")
            hora, minuto, segundo = map(int, horario.split(':'))
            # validar si el horario es válido
            if 0 <= hora < 24 and 0 <= minuto < 60 and 0 <= segundo < 60:
                return (hora, minuto, segundo)
            else:
                print("horario invalido. intenta de nuevo")
        except ValueError:
            print("formato incorrecto. intenta de nuevo")

def diferencia_horarios(horario1, horario2)->tuple:
    """
    pre: se reciben dos tuplas con horarios válidos (hora, minuto, segundo)
    post: se devuelve la diferencia en horas, minutos y segundos como una tupla
    """
    h1 = timedelta(hours=horario1[0], minutes=horario1[1], seconds=horario1[2])
    h2 = timedelta(hours=horario2[0], minutes=horario2[1], seconds=horario2[2])

    #se ajusta si el primer horario es mayor que el segundo
    if h1 > h2:
        h2 += timedelta(days=1)

    diferencia = h2 - h1
    horas, resto = divmod(diferencia.seconds, 3600)
    minutos, segundos = divmod(resto, 60)
    return (horas, minutos, segundos)

#flujo principal
if __name__ == "__main__":
    print("a. ingresar una fecha válida")
    fecha = ingresar_fecha()
    print(f"fecha ingresada: {fecha}")

    print("\nb. sumar n días a una fecha")
    dias = int(input("ingresa el número de días a sumar: "))
    nueva_fecha = sumar_dias(fecha, dias)
    print(f"nueva fecha: {nueva_fecha}")

    print("\nc. ingresar un horario válido")
    horario1 = ingresar_horario()
    print(f"primer horario ingresado: {horario1}")

    horario2 = ingresar_horario()
    print(f"segundo horario ingresado: {horario2}")

    print("\nd. calcular la diferencia entre dos horarios")
    diferencia = diferencia_horarios(horario1, horario2)
    print(f"diferencia: {diferencia[0]} horas, {diferencia[1]} minutos, {diferencia[2]} segundos")
