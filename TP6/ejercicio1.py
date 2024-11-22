""" Escribir un programa que lea un archivo de texto conteniendo un conjunto de apellidos y nombres en formato "Apellido, Nombre" y guarde en el archivo 
ARMENIA.TXT los registros de aquellas personas cuyo apellido termina con la cadena "IAN", en el archivo ITALIA.TXT los terminados en "INI" y en ESPAÑA.TXT los 
terminados en "EZ". Descartar el resto. Ejemplo:
Arslanian, Gustavo –> ARMENIA.TXT
Rossini, Giuseppe –> ITALIA.TXT
Pérez, Juan –> ESPAÑA.TXT
Smith, John –> descartar
El archivo puede ser creado mediante el Block de Notas o el cualquier otro editor"""

#se define la funcion
def procesar_archivo_apellidos(archivo_entrada: str):
    """
    pre: archivo_entrada contiene nombres en formato "Apellido, Nombre"
    post: se crean tres archivos con los registros clasificados según el apellido
    """
    try:
        #se abre el archivo de entrada
        with open(archivo_entrada, "r", encoding="utf-8") as entrada:
            #se abren archivos de salida
            with open("ARMENIA.TXT", "w", encoding="utf-8") as armenia, \
                 open("ITALIA.TXT", "w", encoding="utf-8") as italia, \
                 open("ESPAÑA.TXT", "w", encoding="utf-8") as espana:

                for linea in entrada:
                    linea = linea.strip() #se eliminan espacios en blanco
                    if not linea: #se saltan lineas vacias
                        continue

                    apellido, nombre = map(str.strip, linea.split(","))
                    
                    #se verifican sufijos sufijos y escribir en el archivo correspondiente
                    if apellido.upper().endswith("IAN"):
                        armenia.write(linea + "\n")
                    elif apellido.upper().endswith("INI"):
                        italia.write(linea + "\n")
                    elif apellido.upper().endswith("EZ"):
                        espana.write(linea + "\n")
    except FileNotFoundError:
        print(f"el archivo {archivo_entrada} no existe")
    except Exception as e:
        print(f"ocurrió un error inesperado: {e}")

#se ejecuta la función
archivo = "nombres.txt"
procesar_archivo_apellidos(archivo)
