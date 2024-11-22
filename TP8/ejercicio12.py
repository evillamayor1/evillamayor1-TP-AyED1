""". Una librería almacena su lista de precios en un diccionario. Diseñar un programa 
para crearlo, incrementar los precios de los cuadernos en un 15%, imprimir un 
listado con todos los elementos de la lista de precios e indicar cual es el ítem mas 
costoso que venden en el comercio."""

#se define la funcion

def incrementar_precios(precios, producto, porcentaje):
    #se verifica si el producto existe en el diccionario
    if producto in precios:
        #se incrementa el precio en el porcentaje dado
        precios[producto] *= (1 + porcentaje / 100)
    else:
        print(f"El producto {producto} no se encuentra en el listado.")

def obtener_mas_costoso(precios):
    #se encuentra el producto con el precio mas alto
    mas_costoso = max(precios, key=precios.get)
    return mas_costoso, precios[mas_costoso]

def programa():
    #se crea el diccionario con los precios de los productos
    precios = {
        "cuaderno": 50,
        "lapiz": 10,
        "goma": 5,
        "boligrafo": 20,
        "regla": 15,
        "escalera": 30,
        "carpeta": 25
    }

    #se incrementan los precios de los cuadernos en un 15%
    incrementar_precios(precios, "cuaderno", 15)

    #se imprimen la lista de precios
    print("Lista de precios actualizada:")
    for producto, precio in precios.items():
        print(f"{producto}: ${precio:.2f}")

    #se indica el ítem mas costoso
    mas_costoso, precio_mas_costoso = obtener_mas_costoso(precios)
    print(f"\nEl producto mas costoso es {mas_costoso} con un precio de ${precio_mas_costoso:.2f}")

#se ejecuta el programa
programa()
