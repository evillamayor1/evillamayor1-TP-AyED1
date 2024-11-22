""" Desarrollar un programa que utilice una función que reciba como parámetro una 
cadena de caracteres conteniendo una dirección de correo electrónico y devuelva 
una tupla con las distintas partes que componen dicha dirección. Ejemplo: 
alguien@uade.edu.ar -> (alguien, uade, edu, ar). La función debe detectar 
formatos de fecha inválidos y devolver una tupla vacía.
"""

#se define la funcion
def descomponer_email(email= str)-> tuple:
    """
    pre: se recibe una cadena con una dirección de correo electrónico
    post: devuelve una tupla con las partes del correo, o una tupla vacía si el formato es inválido
    """
    try:
        #se verifica que el correo contenga exactamente un '@'
        if email.count('@') != 1:
            return ()

        # Dividir el correo en usuario y dominio
        usuario, dominio = email.split('@')
        
        #se verifica que el dominio contenga al menos un punto
        if '.' not in dominio:
            return ()

        #se divide el dominio en subdominios
        partes = dominio.split('.')
        
        #se verifica que haya al menos dos partes (dominio y extensión)
        if len(partes) < 2:
            return ()

        #retorna la tupla con las partes del correo
        return (usuario,) + tuple(partes)
    
    except Exception:
        #si ocurre cualquier excepción, devolver una tupla vacía
        return ()

#programa principal para ingresar los datos e invocar la función
email = input("ingresa una dirección de correo electrónico: ")
resultado = descomponer_email(email)
    
if resultado:
    print(f"partes del correo: {resultado}")
else:
    print("formato de correo inválido")
