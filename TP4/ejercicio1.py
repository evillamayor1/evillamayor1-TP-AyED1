""". Desarrollar una función que determine si una cadena de caracteres es capicúa, sin 
utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita 
verificar su funcionamiento."""

def es_capicua(cadena):
    """
    pre: recibe una cadena de caracteres
    post: retorna True si la cadena es capicua, False en caso contrario
    """
    #se recorr la cadena desde ambos extremos hacia el centro
    inicio = 0
    fin = len(cadena) - 1

    while inicio < fin:
        #se comparan los caracteres en los extremos
        if cadena[inicio] != cadena[fin]:
            return False
        #se avanza hacia el centro
        inicio += 1
        fin -= 1

    return True

# programa principal para verificar el funcionamiento
while True:
    print("\nverificar si una cadena es capicua")
    cadena = input("ingrese una cadena (o 'salir' para finalizar): ").strip()

    if cadena.lower() == "salir":
        print("saliendo del programa")
        break

    if es_capicua(cadena):
        print("la cadena es capicua")
    else:
        print("la cadena no es capicua")
