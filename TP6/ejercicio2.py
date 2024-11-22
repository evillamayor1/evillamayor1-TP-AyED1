"""Escribir un programa que permita dividir un archivo de texto cualquiera en partes 
que se puedan enviar por correo electronico. El tamaño máximo de las partes se 
ingresa por teclado. Los nombres de los archivos generados deben respetar el 
nombre original con el agregado de un sufijo que indique de qué parte se trata. 
Tener en cuenta que ningun registro puede ser dividido; la particion debe efectuarse después del delimitador del mismo. Mostrar un mensaje de error si el proceso no 
pudiera llevarse a cabo. Recordar que no se permite cargar el archivo completo en 
memoria."""

#se define la funcion
def dividir_archivo(archivo_entrada: str, tamano_maximo: int)-> None:
    """
    pre: archivo_entrada existe y tamano_maximo es un entero mayor a 0
    post: se generan archivos de partes segun el tamaño máximo indicado
    """
    try:
        #se abre el archivo de entrada
        with open(archivo_entrada, "r", encoding="utf-8") as entrada:
            parte_numero = 1
            tamano_actual = 0
            archivo_salida = None

            for linea in entrada:
                if archivo_salida is None or tamano_actual + len(linea.encode("utf-8")) > tamano_maximo:
                    #se cierra el archivo anterior si existe
                    if archivo_salida:
                        archivo_salida.close()
                    
                    #se abre el nuevo archivo de salida
                    nombre_salida = f"{archivo_entrada}_parte{parte_numero}.txt"
                    archivo_salida = open(nombre_salida, "w", encoding="utf-8")
                    parte_numero += 1
                    tamano_actual = 0
                
                #se escribe la linea en el archivo actual
                archivo_salida.write(linea)
                tamano_actual += len(linea.encode("utf-8"))

            #se cierra el ultimo archivo si fue abierto
            if archivo_salida:
                archivo_salida.close()
                
        print("archivo dividido con éxito")
    except FileNotFoundError:
        print(f"el archivo {archivo_entrada} no existe")
    except Exception as e:
        print(f"ocurrio un error inesperado: {e}")

#se piden los datos al usuario y ejecutar
try:
    archivo = input("ingresa el nombre del archivo a dividir: ").strip()
    tamano_maximo = int(input("ingresa el tamaño máximo de cada parte en bytes: ").strip())

    if tamano_maximo <= 0:
        print("el tamaño máximo debe ser mayor a 0")
    else:
        dividir_archivo(archivo, tamano_maximo)
except ValueError:
    print("el tamaño máximo debe ser un numero entero")
