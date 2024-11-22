"""Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras 
repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar las palabras 
ordenadas según su longitud. Los signos de puntuación no deben afectar el 
proceso."""

#se define la funcion
def procesar_frase()-> tuple:
    frase = ''.join(caracter for caracter in palabra if caracter.isalnum())
    #se divide la frase en palabras
    palabras = frase.split()
    
    #se limpia cada palabra de puntuación
    palabras_limpias = [limpiar_puntuacion(palabra) for palabra in palabras]
    
    #se eliminan las palabras repetidas usando un conjunto
    palabras_unicas = set(palabras_limpias)
    
    #se ordenan las palabras por longitud
    palabras_ordenadas = sorted(palabras_unicas, key=len)
    
    return palabras_ordenadas

#programa principal

frase = input("Ingresa una frase: ")
    
# procesamos la frase y mostramos las palabras ordenadas
palabras_ordenadas = procesar_frase(frase)
    
print("Palabras ordenadas por longitud:")
for palabra in palabras_ordenadas:
    print(palabra)
