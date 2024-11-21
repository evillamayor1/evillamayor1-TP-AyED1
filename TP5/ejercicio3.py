"""Desarrollar una función que devuelva una cadena de caracteres con el nombre del 
mes cuyo número se recibe como parámetro. Los nombres de los meses deberán 
obtenerse de una lista de cadenas de caracteres inicializada dentro de la función. 
Devolver una cadena vacía si el número de mes es inválido. La detección de meses 
inválidos deberá realizarse a través de excepciones."""

#se define la funcion
def obtener_mes(numero_mes: int) -> str:
    """
    pre: recibe un numero de mes entre 1 y 12
    post: devuelve el nombre del mes correspondiente o una cadena vacia si el numero es invalido
    """
    meses = [
        "enero", "febrero", "marzo", "abril", "mayo", "junio", 
        "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
    ]
    
    try:
        #se verifica si el numero de mes esta dentro del rango valido
        return meses[numero_mes - 1]
    except IndexError:
        #si el numero esta fuera del rango, se devuelve cadena vacia
        return ""

#ejemplo de uso
numero_mes = 5
mes = obtener_mes(numero_mes)

if mes:
    print(f"el mes correspondiente al numero {numero_mes} es {mes}")
else:
    print(f"numero de mes invalido: {numero_mes}")
