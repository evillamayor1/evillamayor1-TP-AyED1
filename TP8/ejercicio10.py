""". Desarrollar una funcion eliminarclaves() que reciba como parámetros un diccionario 
y una lista de claves. La funcion debe eliminar del diccionario todas las claves 
contenidas en la lista, devolviendo el diccionario modificado y un número entero 
que represente la cantidad de claves eliminadas. Desarrollar también un programa 
para verificar su comportamiento."""

#se define la variable
def eliminarclaves(diccionario = dict, claves_a_eliminar = list)-> dict:
    #se inicia un contador para las claves eliminadas
    cantidad_eliminadas = 0
    
    #se itera sobre las claves que sera eliminar
    for clave in claves_a_eliminar:
        #si la clave está en el diccionario, se elimina
        if clave in diccionario:
            del diccionario[clave]
            cantidad_eliminadas += 1  #se aumenta el contador
    
    #se retorna el diccionario modificado y el número de claves eliminadas
    return diccionario, cantidad_eliminadas

#programa para verificar el comportamiento de la funcion
def programa():
    #se crea un diccionario de ejemplo
    diccionario = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5
    }
    
    #lista de claves a eliminar
    claves_a_eliminar = ["b", "d", "z"]  #la clave "z" no existe
    
    #se le llama a la funcion
    diccionario_modificado, claves_eliminadas = eliminarclaves(diccionario, claves_a_eliminar)
    
    #se muestran los resultados
    print("Diccionario modificado:", diccionario_modificado)
    print("Cantidad de claves eliminadas:", claves_eliminadas)

#se ejecuta el programa
programa()
