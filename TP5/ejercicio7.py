"""7. Escribir un programa que juegue con el usuario a adivinar un numero. El programa 
debe generar un numero al azar entre 1 y 500 y el usuario debe adivinarlo. Para 
eso, cada vez que se introduce un valor se muestra un mensaje indicando si el numero que tiene que adivinar es mayor o menor que el ingresado. Cuando consiga 
adivinarlo, se debe imprimir en pantalla la cantidad de intentos que le tomó hallar 
el numero. Si el usuario introduce algo que no sea un numero se mostrará un 
mensaje en pantalla y se lo contará como un intento más."""

#se importa random para facilidad
import random

#se define la funcion
def adivinar_numero():
    """
    pre: no recibe parametros
    post: el programa genera un numero aleatorio y el usuario intenta adivinarlo, contando los intentos
    """
    numero_aleatorio = random.randint(1, 500)
    intentos = 0
    
    while True:
        try:
            #se pide al usuario que ingrese un numero
            guess = int(input("ingrese un numero entre 1 y 500: "))
            intentos += 1

            if guess < numero_aleatorio:
                print("el numero es mayor")
            elif guess > numero_aleatorio:
                print("el numero es menor")
            else:
                print(f"¡correcto! el numero era {numero_aleatorio}")
                print(f"te tomó {intentos} intentos")
                break
        except ValueError:
            #si el usuario no ingresa un numero, cuenta como intento
            print("ingresaste un valor no numérico, cuenta como un intento adicional")
            intentos += 1

#se ejecuta la funcion
adivinar_numero()
