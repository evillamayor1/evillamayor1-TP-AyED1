""". Crear una función contarvocales(), que reciba una palabra y cuente cuántas vocales 
contiene, identificando la cantidad de cada una. Devolver un diccionario con los 
resultados. Luego desarrollar un programa para leer una frase e invocar a la 
función por cada palabra que contenga la misma. Imprimir las palabras y la 
cantidad de vocales hallada."""

#se define la funcion
def contarvocales(palabra = str)-> dict:
    #diccionario para contar las vocales
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    #se comvierte la palabra a minusculas para no diferenciar mayusculas de minusculas
    palabra = palabra.lower()
    
    #se recorre la palabra y se cuentan las vocales
    for letra in palabra:
        if letra in vocales:
            vocales[letra] += 1
    
    #se retorna el diccionario con la cantidad de vocales de cada tipo
    return vocales

def programa():
    #se lee una frase desde el teclado
    frase = input("Introduce una frase: ")
    
    #se separa la frase en palabras
    palabras = frase.split()
    
    #se procesa cada palabra
    for palabra in palabras:
        #se llama a la funcion
        resultado = contarvocales(palabra)
        
        #se muestra el resultado
        print(f"Palabra: {palabra} -> {resultado}")

#se ejecuta el programa
programa()
