"""odo programa Python es susceptible de ser interrumpido mediante la pulsación de 
las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. Realizar 
un programa para imprimir los números enteros entre 1 y 100000, y que solicite 
confirmación al usuario antes de detenerse cuando se presione Ctrl-C."""

#se define la funcion

def imprimir_numeros()-> int:
    """
    pre: no recibe parametros
    post: imprime los numeros del 1 al 100000, y solicita confirmacion si se interrumpe con Ctrl-C
    """
    try:
        for numero in range(1, 100001):
            print(numero)
    except KeyboardInterrupt:
        #se captura la excepcion KeyboardInterrupt
        respuesta = input("\nse ha interrumpido el programa, ¿deseas detenerlo? (s/n): ")
        if respuesta.lower() == "s":
            print("programa detenido por el usuario")
        else:
            #si la respuesta es 'no', se continua con el ciclo
            print("continuando con el programa...")
            #se vuelve a iniciar el ciclo
            pass

#se llama a la funcion
imprimir_numeros()
