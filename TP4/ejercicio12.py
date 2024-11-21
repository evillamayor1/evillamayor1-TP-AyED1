"""Escribir un programa para crear una lista por comprensión con los naipes de la baraja española. La lista debe contener cadenas de caracteres. Ejemplo: ["1 Oros", "2 
Oros"... ]. Imprimir la lista por pantalla. """

#se define la funcion
def generar_baraja()-> list:
    """
    pre: no recibe parametros
    post: retorna una lista con los naipes de la baraja española
    """
    #palos de la baraja española
    palos = ["Oros", "Copas", "Espadas", "Bastos"]
    #valores de los naipes
    valores = [str(i) for i in range(1, 8)] + ["10", "11", "12"]
    #lista por comprension para generar los naipes
    baraja = [f"{valor} {palo}" for palo in palos for valor in valores]
    return baraja
