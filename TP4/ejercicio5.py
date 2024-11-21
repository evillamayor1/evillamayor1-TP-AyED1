""" Escribir una función filtrar_palabras() que reciba una cadena de caracteres conteniendo una frase y un entero N, y devuelva otra cadena con las palabras que tengan N o más caracteres de la cadena original. Escribir también un programa para 
verificar el comportamiento de la misma. Hacer tres versiones de la función, para 
cada uno de los siguientes casos:
a. Utilizando sólo ciclos normales
b. Utilizando listas por comprensión
c. Utilizando la función filter"""

#se define la funcion
def filtrar_palabras_ciclos(frase: str, n: int) -> str:
    """
    pre: recibe una frase y un entero n
    post: retorna una cadena con las palabras que tienen n o más caracteres
    """
    #se divide la frase en palabras
    palabras = frase.split()
    resultado = []
    #se verifica si la longitud de la palabra es mayor o igual a n
    for palabra in palabras:
        if len(palabra) >= n:  
            resultado.append(palabra)
    #se unen las palabras filtradas en una cadena
    return " ".join(resultado) 
