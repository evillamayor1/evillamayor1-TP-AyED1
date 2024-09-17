"""Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos), 
donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valo
res de la lista. """

#definir variable
def cuadrados_numeros(n = int):
    #genera una lista con los cuadrados de los numeros
    cuadrados = [i**2 for i in range(1, N + 1)]

    #sustrae los ultimos 10 valores de la lista
    ultimos_10 = cuadrados[-10:]
    return ultimos_10

#definicion del valor N
numero = int(input("ingrese un numero: "))
resultado = cuadrados_numeros(numero)

#imprime los valores de la lista
for i in range(len(resultado)):
    print(resultado[i])