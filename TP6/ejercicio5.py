""" Se dispone de tres formatos diferentes de archivos de texto en los que se almacenan datos de empleados, detallados más abajo. Desarrollar un programa para cada 
uno de los formatos suministrados, que permitan leer cada uno de los archivos y 
grabar los datos obtenidos en otro archivo de texto con formato CSV.
Archivo 1: Los campos tienen longitud fija con un espacio de separación 
entre ellos.
(Regla) 1 2 3 4 5 6 
012345678901234567890123456789012345678901234567890123456789012
Pérez Juan 20080211 Corrientes 348 
González Ana M 20080115 Juan de Garay 1111 3er piso dto A
Archivo 2: Todos los campos de este archivo están precedidos por un 
número de dos dígitos que indica la longitud del campo a leer.
10Pérez Juan082008021114Corrientes 348
14González Ana M082008011533Juan de Garay 1111 3er piso dto A
NOTAS:
· Los espacios que se encuentren al final de las cadenas en el formato 1 deberán 
ser eliminados.
· El formato 2 debe generalizarse para que soporte registros con cualquier cantidad de campos"""

#se importa csv
import csv

#se define la funcion del formato1
def convertir_formato1_a_csv(archivo_entrada: str, archivo_salida: str):
    """
    pre: archivo_entrada tiene datos de empleados en formato de longitud fija
    post: se graba un archivo CSV con los datos procesados
    """
    try:
        with open(archivo_entrada, "r", encoding="utf-8") as entrada, \
             open(archivo_salida, "w", newline="", encoding="utf-8") as salida:
            csv_writer = csv.writer(salida)
            csv_writer.writerow(["apellido", "nombre", "fecha_ingreso", "direccion"])

            for linea in entrada:
                #se procesan los campos de la línea eliminando espacios al final
                campos = [
                    linea[0:10].strip(),  #apellido
                    linea[10:20].strip(),  #nombre
                    linea[20:28].strip(),  #fecha_ingreso
                    linea[28:].strip()  #direccion
                ]
                csv_writer.writerow(campos)
        print(f"archivo csv generado en {archivo_salida}")
    except FileNotFoundError:
        print(f"el archivo {archivo_entrada} no existe")
    except Exception as e:
        print(f"ocurrió un error: {e}")

#flujo principal
try:
    entrada = input("ingresa el nombre del archivo de formato 1: ").strip()
    salida = input("ingresa el nombre del archivo csv de salida: ").strip()
    convertir_formato1_a_csv(entrada, salida)
except Exception as e:
    print(f"error inesperado: {e}")


#se define la funcion para el formato 2
def convertir_formato2_a_csv(archivo_entrada: str, archivo_salida: str):
    """
    pre: archivo_entrada tiene datos de empleados en formato con longitudes dinámicas
    post: se graba un archivo CSV con los datos procesados
    """
    try:
        with open(archivo_entrada, "r", encoding="utf-8") as entrada, \
             open(archivo_salida, "w", newline="", encoding="utf-8") as salida:
            csv_writer = csv.writer(salida)
            csv_writer.writerow(["campo1", "campo2", "campo3", "campo4"]) 

            for linea in entrada:
                campos = []
                i = 0
                while i < len(linea):
                    #se lee la longitud del campo
                    longitud = int(linea[i:i+2])
                    i += 2
                    #se extrae el campo de longitud especificada
                    campo = linea[i:i+longitud]
                    i += longitud
                    campos.append(campo.strip())
                csv_writer.writerow(campos)
        print(f"archivo csv generado en {archivo_salida}")
    except FileNotFoundError:
        print(f"el archivo {archivo_entrada} no existe")
    except Exception as e:
        print(f"ocurrió un error: {e}")

# flujo principal
try:
    entrada = input("ingresa el nombre del archivo de formato 2: ").strip()
    salida = input("ingresa el nombre del archivo csv de salida: ").strip()
    convertir_formato2_a_csv(entrada, salida)
except Exception as e:
    print(f"error inesperado: {e}")
