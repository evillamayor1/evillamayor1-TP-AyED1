"""Desarrollar una función que devuelva una subcadena con los últimos N caracteres 
de una cadena dada. La cadena y el valor de N se pasan como parámetros."""
#se define la funcion
def ultimos_caracteres_rebanadas(cadena: str, n: int) -> str:
    """
    pre: recibe una cadena y el número de caracteres n a extraer desde el final
    post: retorna una subcadena con los últimos n caracteres
    """
    return cadena[-n:] if n <= len(cadena) else cadena
