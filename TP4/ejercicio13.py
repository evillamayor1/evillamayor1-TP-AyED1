"""uchas aplicaciones financieras requieren que los números sean expresados también en letras. Por ejemplo, el número 2153 puede escribirse como "dos mil ciento 
cincuenta y tres". Escribir un programa que utilice una función para convertir un 
número entero entre 0 y 1 billón (1.000.000.000.000) a letras. ¿En qué cambiaría 
la función si también aceptara números negativos? ¿Y números con decimales?
"""
#se define la variable

def convertir_a_letras(num = int)-> None:
    """
    Convierte un número entero entre 0 y 1 billón a letras.
    """
    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", 
                "diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", 
                "dieciocho", "diecinueve"]
    decenas = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", 
               "ochenta", "noventa"]
    centenas = ["", "cien", "doscientos", "trescientos", "cuatrocientos", "quinientos", 
                "seiscientos", "setecientos", "ochocientos", "novecientos"]
    
    def subcadena(num = int)-> str:
        """Convierte números entre 0 y 999"""
        if num == 0:
            return ""
        elif num < 20:
            return unidades[num]
        elif num < 100:
            if num % 10 == 0:
                return decenas[num // 10]
            else:
                return f"{decenas[num // 10]} y {unidades[num % 10]}"
        else:
            if num == 100:
                return "cien"
            else:
                return f"{centenas[num // 100]} {subcadena(num % 100)}"

    #se divide el numero en secciones
    if num == 0:
        return "cero"
    
    partes = []
    billon = 10**12
    millones = 10**6
    miles = 10**3
    
    if num >= billon:
        partes.append(f"{subcadena(num // billon)} billón")
        num %= billon
    if num >= millones:
        partes.append(f"{subcadena(num // millones)} millón")
        num %= millones
    if num >= miles:
        partes.append(f"{subcadena(num // miles)} mil")
        num %= miles
    if num > 0:
        partes.append(subcadena(num))
    
    return " ".join(partes)

#programa de prueba
numero = int(input("introduce un numero entre 0 y 1 billón: "))
print(f"el numero {numero} en letras es: {convertir_a_letras(numero)}")
