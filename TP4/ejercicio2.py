"""Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la 
misma tiene 80 columnas.
"""
#se define la funcion
def centrar_cadena(cadena: str) -> str:
    """
    pre: recibe una cadena de caracteres
    post: retorna la cadena centrada para una pantalla de 80 columnas
    """
    columnas = 80
    espacios = (columnas - len(cadena)) // 2 
    return ' ' * espacios + cadena

# programa principal
cadena = input("ingrese una cadena de caracteres: ")
cadena_centrada = centrar_cadena(cadena)
print(cadena_centrada)
