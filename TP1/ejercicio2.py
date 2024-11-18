"""Desarrollar una función que reciba tres números enteros positivos correspondientes 
al día, mes, año de una fecha y verifique si corresponden a una fecha válida. Debe 
tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos. 
Devolver True o False según la fecha sea correcta o no. Realizar también un 
programa para verificar el comportamiento de la función."""
#se define la variable
def verificar_fecha(dia = int, mes = int, anio = int) -> bool:
    """
    Pre: esta funcion recibe 3 numeros enteros

    post: esta funcion retorna un valor booleano

    """
    #se crea una lista de la cantidad de dias en el mes cuando no es viciesto
    cantidad_dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    #si es viciesto, el mes de febrero pasa a tener 29 dias
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        cantidad_dias[1] = 29
    
    #se comprieba que las fechas son validas, de ser alguna invalida, retorna False
    if mes > 12 or mes <1:
        return False
    if dia < 1 or dia > cantidad_dias[mes -1]:
        return False
    if anio < 1:
        return False
    else:
        return True

#se definen los valores
dia = int(input("ingrese el dia:"))
mes = int(input("ingrese el mes:"))
anio = int(input("ingrese el anio:"))

#se llama a la funcion
verificar_fecha(dia, mes, anio)