"""Escribir una función que reciba como parámetro una tupla conteniendo una fecha 
(día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada 
en formato extendido. La función debe contemplarse que el año se ingrese en dos 
dígitos, los que serán interpretados según un año de corte definido dentro del 
programa. Cualquier año mayor que éste se considerará del siglo pasado. Por 
ejemplo, si el año de corte fuera 30, la función devuelve "12 de Octubre de 2030" 
para (12,10,30). Pero si la tupla fuera (25, 12, 31) devolverá "25 de Diciembre de 
1931". Si el año se ingresa en cuatro dígitos el año de corte no será tenido en 
cuenta. Escribir también un programa para ingresar los datos, invocar a la función y 
mostrar el resultado."""

#se define la funcion
def fecha_extendida(fecha = int)-> str:
    """
    pre: se recibe una tupla con fecha (dia, mes, anio)
    post: se devuelve una cadena con la fecha en formato extendido
    """
    #se define el año de corte (por ejemplo, 30)
    anio_corte = 30
    
    dia, mes, anio = fecha

    #si el año tiene dos dígitos, se evalúa con el año de corte
    if anio < 100:
        if anio > anio_corte:
            anio += 2000
        else:
            anio += 1900
    
    #lista con los nombres de los meses
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    #se compone la fecha en formato extendido
    fecha_extendida = f"{dia} de {meses[mes-1]} de {anio}"

    return fecha_extendida

#se ingresan los datos de la fecha
dia = int(input("ingresa el día: "))
mes = int(input("ingresa el mes (1-12): "))
anio = int(input("ingresa el año (dos dígitos o cuatro dígitos): "))

#se llama a la función para obtener la fecha extendida
fecha = (dia, mes, anio)
resultado = fecha_extendida(fecha)
    
 #se muestra el resultado
print(f"fecha extendida: {resultado}")
