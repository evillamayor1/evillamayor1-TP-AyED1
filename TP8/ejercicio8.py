""". Generar e imprimir un diccionario donde las claves sean números enteros entre 1 y 
20 (ambos incluidos) y los valores asociados sean el cuadrado de las claves."""

#se define la funcion
def generar_diccionario()-> None:
    #se genera el diccionario con claves entre 1 y 20 y valores como el cuadrado de las claves
    diccionario = {clave: clave**2 for clave in range(1, 21)}
    
    #se imprime el diccionario generado
    print(diccionario)

#se ejecuta la funcion
generar_diccionario()
