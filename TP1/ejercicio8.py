""". La siguiente función permite averiguar el día de la semana para una fecha determi
nada. La fecha se suministra en forma de tres parámetros enteros y la función de
vuelve 0 para domingo, 1 para lunes, 2 para martes, etc. Escribir un programa para 
imprimir por pantalla el calendario de un mes completo, correspondiente a un mes 
y anio cualquiera basándose en la función suministrada. Considerar que la semana 
comienza en domingo.
def diadelasemana(dia,mes,anio):
    if mes <3:
        mes = mes +10
        anio = anio -1
    else:
        mes = mes-2
    siglo = anio // 100
    anio2 = anio % 100
    diasem = (((26*mes-2)//10)+dia+anio2+(anio2//4)+(siglo//4)-(2*siglo))%7

"""
#conserva la variable original para usarla
def diadelasemana(dia: int, mes: int, anio: int) -> int:
    if mes < 3:
        mes += 10
        anio -= 1
    else:
        mes -= 2
    siglo = anio // 100
    anio2 = anio % 100
    diasem = (((26 * mes - 2) // 10) + dia + anio2 + (anio2 // 4) + (siglo // 4) - (2 * siglo)) % 7
    return diasem
#se define la variable principal
def imprimir_calendario(mes: int, anio: int) -> None:
    """
    pre: esta variable recibe dos valores enteros

    post: esta variable retorna un calendario
    """
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dias_semana = ["Dom", "Lun", "Mar", "Mié", "Jue", "Vie", "Sáb"]

    #se ajustan las fechas en caso de ser anio viciesto
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        dias_mes[1] = 29

    print(f"Calendario para {mes}/{anio}\n")
    
    #se imprimen los dias de la semana
    for dia in dias_semana:
        print(dia, end=" ")
    print()

    #se calcula el primer dia del mes
    primer_dia = diadelasemana(1, mes, anio)
    
    #se imprimen espacios en blanco hasta el primer dia del mes
    for _ in range(primer_dia):
        print("    ", end="")

    #se imprime todos los dias del mes
    for dia in range(1, dias_mes[mes - 1] + 1):
        print(f"{dia:2}", end="  ")
        if (primer_dia + dia) % 7 == 0:
            print()

#asignacion de variables y llamada a la funcion
mes = 10
anio = 2024
imprimir_calendario(mes, anio)
