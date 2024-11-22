""". Escribir una función buscarclave() que reciba como parámetros un diccionario y un 
valor, y devuelva una lista de claves que apunten ("mapeen") a ese valor en el diccionario. Comprobar el comportamiento de la función mediante un programa apropiado"""

#se define la funciom
def buscarclave(diccionario, valor)-> list:
    """
    Recibe un diccionario y un valor, y devuelve una lista de claves
    que mapean a ese valor en el diccionario.
    """
    claves = [clave for clave, val in diccionario.items() if val == valor]
    return claves

def programa():
    #se crea un diccionario de ejemplo
    diccionario = {
        "a": 10,
        "b": 20,
        "c": 10,
        "d": 30,
        "e": 20
    }
    
    #se solicita un valor al usuario para buscar las claves
    valor_buscado = int(input("Ingrese un valor para buscar las claves: "))
    
    #se llama a la función buscarclave
    claves_encontradas = buscarclave(diccionario, valor_buscado)
    
    #se muestran los resultados
    if claves_encontradas:
        print(f"Las claves que mapean al valor {valor_buscado} son: {claves_encontradas}")
    else:
        print(f"No se encontraron claves que mapeen al valor {valor_buscado}.")

#se ejecuta el programa
programa()
