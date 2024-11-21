""". Escribir un programa que cuente cuantas veces se encuentra una subcadena dentro 
de otra cadena, sin diferenciar mayusculas y minusculas. Tener en cuenta que los 
caracteres de la subcadena no necesariamente deben estar en forma consecutiva 
dentro de la cadena, pero si respetando el orden de los mismos. Ejemplo:
Cadena:
Platero es pequeño, peludo, suave; tan blando por fuera, que se diria todo de algodon, que no lleva 
huesos. Solo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro.
Sub-cadena: UADE
Cantidad encontrada: 4 (Las coincidencias estan resaltadas en la cadena siguiente)
Platero es pequeño, peludo, suave; tan blando por fuera, que se diria todo de algodon, que no lleva 
huesos. Solo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro."""

#se define la funcion 
def contar_subcadena(cadena: str, subcadena: str) -> int:
    """
    pre: recibe una cadena principal y una subcadena
    post: retorna la cantidad de veces que la subcadena aparece respetando el orden de los caracteres
    """
    #se combierten ambas cadenas a minusculas para no diferenciar mayusculas y minusculas
    cadena = cadena.lower()
    subcadena = subcadena.lower()

    def buscar(cadena, subcadena, idx):
        # caso base: subcadena vacia, una coincidencia encontrada
        if not subcadena:
            return 1
        # caso base: cadena vacia pero subcadena no, no hay coincidencias
        if not cadena:
            return 0
        # caso recursivo: si el primer caracter coincide, avanzar en ambas cadenas
        if cadena[0] == subcadena[0]:
            return buscar(cadena[1:], subcadena[1:], idx + 1) + buscar(cadena[1:], subcadena, idx + 1)
        # caso recursivo: si no coincide, avanzar solo en la cadena principal
        return buscar(cadena[1:], subcadena, idx + 1)

    return buscar(cadena, subcadena, 0)


#programa principal
def main():
    cadena = ("Platero es pequeño, peludo, suave; tan blando por fuera, que se diria todo de algodon, "
              "que no lleva huesos. Solo los espejos de azabache de sus ojos son duros cual dos "
              "escarabajos de cristal negro.")
    subcadena = "UADE"
    
    cantidad = contar_subcadena(cadena, subcadena)
    
    print(f"cadena:\n{cadena}")
    print(f"\nsubcadena: {subcadena}")
    print(f"\ncantidad encontrada: {cantidad}")

