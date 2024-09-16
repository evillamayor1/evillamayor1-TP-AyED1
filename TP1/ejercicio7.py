""" Escribir una función diasiguiente(dia, mes año) que reciba como parámetro una 
fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros 
correspondientes el día siguiente al dado. Utilizando esta función sin modificaciones 
ni agregados, desarrollar programas que permitan:
 a. Sumar N días a una fecha.
 b. Calcular la cantidad de días existentes entre dos fechas cualesquiera."""

 #se define la funcion 
 def dia_sig(dia = int, mes = int, anio = int):
    #se agrega un dia
    dia +=1

    #se actualizan el mes y anio de ser necesario
    if dia > 30:
        dia = 1
        mes += 1
    if mes > 12:
        mes = 1
        anio+= 1
    
    #se devuelven las fechas actualizadas
    return dia, mes, anio





