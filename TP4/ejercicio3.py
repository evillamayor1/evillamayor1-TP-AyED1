"""os números de claves de dos cajas fuertes están intercalados dentro de un número 
entero llamado "clave maestra", cuya longitud no se conoce. Realizar un programa 
para obtener ambas claves, donde la primera se construye con los dígitos ubicados 
en posiciones impares de la clave maestra y la segunda con los dígitos ubicados en 
posiciones pares. Los dígitos se numeran desde la izquierda. Ejemplo: Si clave 
maestra fuera 18293, la clave 1 sería 123 y la clave 2 sería 89."""

#se define la funciom
def obtener_claves(clave_maestra: int) -> tuple[str, str]:
    """
    pre: recibe un número entero como clave maestra
    post: retorna dos cadenas: clave 1 (dígitos en posiciones impares) y clave 2 (dígitos en posiciones pares)
    """
    clave_str = str(clave_maestra)
    clave_1 = ""  # dígitos en posiciones impares
    clave_2 = ""  # dígitos en posiciones pares

    for i, digito in enumerate(clave_str):
        if (i + 1) % 2 != 0:  # posición impar
            clave_1 += digito
        else:  # posición par
            clave_2 += digito

    return clave_1, clave_2

# programa principal
clave_maestra = int(input("ingrese la clave maestra: "))
clave_1, clave_2 = obtener_claves(clave_maestra)

print(f"clave 1 (posiciones impares): {clave_1}")
print(f"clave 2 (posiciones pares): {clave_2}")
