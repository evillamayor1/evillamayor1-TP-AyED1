"""Se solicita crear un programa para leer direcciones de correo electronico y verificar 
si representan una direccion valida. Por ejemplo usuario@dominio.com.ar. Para que 
una direccion sea considerada valida el nombre de usuario debe poseer solamente 
caracteres alfanumericos, la direccion contener un solo caracter @, el dominio debe 
tener al menos un caracter y tiene que finalizar con .com o .com.ar. """

#se importa re para comodidad
import re

#se define la funcion
def es_correo_valido(correo: str) -> bool:
    """
    Verifica si una direccion de correo electronico es valida.
    
    Una direccion de correo valida debe cumplir con las siguientes condiciones:
    1. El nombre de usuario debe contener solo caracteres alfanumericos.
    2. El correo debe contener exactamente un caracter '@'.
    3. El dominio debe tener al menos un caracter y debe terminar con '.com' o '.com.ar'.
    """


    #expresion regular para validar el correo electronico
    patron = r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.(com|com\.ar)$'
    
    #se verifica si el correo cumple con el patron
    if re.match(patron, correo, re.IGNORECASE):
        return True
    else:
        return False

def obtener_dominio(correo: str) -> str:
    """
    Extrae el dominio de una direccion de correo electronico.
    """
    #divide la direccion de correo por el caracter '@' y toma la parte despues de '@'
    return correo.split('@')[1].lower()

def main():
    dominios = set() 
    while True:
        correo = input("Introduce una direccion de correo electronico (o presiona Enter para terminar): ")
        
        if correo == "":
            break  

        if es_correo_valido(correo):
            dominio = obtener_dominio(correo)
            dominios.add(dominio)
            print(f"El correo '{correo}' es valido.")
        else:
            print(f"El correo '{correo}' no es valido.")

    #mostrar los dominios unicos y ordenados alfabeticamente
    if dominios:
        print("\nLista de dominios validos:")
        for dominio in sorted(dominios):
            print(dominio)
    else:
        print("No se ingresaron correos validos.")

