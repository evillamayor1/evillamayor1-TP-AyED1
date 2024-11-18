"""Una persona desea llevar el control de los gastos realizados al viajar en el subte
rráneo dentro de un mes. Sabiendo que dicho medio de transporte utiliza un es
quema de tarifas decrecientes (detalladas en la tabla de abajo) se solicita desarro
llar una función que reciba como parámetro la cantidad de viajes realizados en un 
determinado mes y devuelva el total gastado en viajes. Realizar también un pro
grama para verificar el comportamiento de la función"""

#de 1 a 20: 650, 21 a 30: 20%, 31 a 40: 40%, mas de 40: 60%

#se define la variable
def tarifa(viajes):
    """
    Pre: esta funcion recibe un unico valor entero

    post: esta funcion retorna un valor entero

    """
    total = 0
    tarifa_base = 650
    
    #se salculan los primeros 20 viajes
    if viajes <= 20:
        total = tarifa_base * viajes
    else:
        total += tarifa_base * 20
        #se salculan los siguientes 10 viajes con 20% de descuento
        if viajes <= 30:
            total += (viajes - 20) * (tarifa_base * 0.80)
        else:
            total += 10 * (tarifa_base * 0.80)
            #se calculan los siguientes 10 viajes con 40% de descuento
            if viajes <= 40:
                total += (viajes - 30) * (tarifa_base * 0.60)
            else:
                total += 10 * (tarifa_base * 0.60)
                #se calculan los viajes adicionales con 60% de descuento
                total += (viajes - 40) * (tarifa_base * 0.40)

    return total

#se cargan la cantidad de viajes y se llama a la funcion
cant_viajes = int(input("Ingrese la cantidad de viajes: "))
total = tarifa(cant_viajes)
