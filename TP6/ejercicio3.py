"""Una institución deportiva necesita clasificar a sus atletas para inscribirlos en los 
próximos Juegos Panamericanos. Para eso encargó la realización de un programa 
que incluya las siguientes funciones:
GrabarRangoAlturas(): Graba en un archivo las alturas de los atletas de distintas 
disciplinas, los que se ingresan desde el teclado. Cada dato se debe grabar en una 
línea distinta. Ejemplo:
<Deporte 1>
<altura del atleta 1>
<altura del atleta 2>
< . . . >
<Deporte 2>
<altura del atleta 1>
<altura del atleta 2>
< . . . >
GrabarPromedio(): Graba en un archivo los promedios de las alturas de los atletas, leyendo los datos del archivo generado en el paso anterior. La disciplina y el 
promedio deben grabarse en líneas diferentes. Ejemplo:
<Deporte 1>
<Promedio de alturas deporte 1>
<Deporte 2>
<Promedio de alturas deporte 2>
< . . . >
"""

#se define la funcion
def grabar_rango_alturas(archivo_alturas: str):
    """
    pre: archivo_alturas es un nombre válido de archivo
    post: se graban las alturas de los atletas organizadas por disciplinas
    """
    try:
        with open(archivo_alturas, "w", encoding="utf-8") as archivo:
            while True:
                deporte = input("ingresa el nombre del deporte (o vacío para terminar): ").strip()
                if not deporte:
                    break
                
                archivo.write(f"{deporte}\n")
                print(f"ingresa las alturas para {deporte}. escribe 'fin' para terminar:")
                
                while True:
                    altura = input("altura del atleta: ").strip()
                    if altura.lower() == "fin":
                        break
                    if altura.replace(".", "", 1).isdigit():
                        archivo.write(f"{altura}\n")
                    else:
                        print("ingresa una altura válida")
    except Exception as e:
        print(f"ocurrió un error al grabar las alturas: {e}")

def grabar_promedio(archivo_alturas: str, archivo_promedios: str):
    """
    pre: archivo_alturas contiene datos válidos organizados por disciplinas y alturas
    post: se graban los promedios de alturas por disciplina en archivo_promedios
    """
    try:
        with open(archivo_alturas, "r", encoding="utf-8") as entrada, \
             open(archivo_promedios, "w", encoding="utf-8") as salida:
            deporte = None
            alturas = []

            for linea in entrada:
                linea = linea.strip()
                if not linea.replace(".", "", 1).isdigit():  #se asume que es el nombre de un deporte
                    if deporte and alturas:
                        promedio = sum(alturas) / len(alturas)
                        salida.write(f"{deporte}\n{promedio:.2f}\n")
                    deporte = linea
                    alturas = []
                else:
                    alturas.append(float(linea))
            
            if deporte and alturas:  #se procesa la ultima disciplina
                promedio = sum(alturas) / len(alturas)
                salida.write(f"{deporte}\n{promedio:.2f}\n")
    except FileNotFoundError:
        print(f"el archivo {archivo_alturas} no existe")
    except Exception as e:
        print(f"ocurrió un error al calcular promedios: {e}")

#se define la funcion
def mostrar_mas_altos(archivo_promedios: str):
    """
    pre: archivo_promedios contiene promedios válidos por disciplina
    post: se muestran disciplinas cuyos atletas superan la estatura promedio general
    """
    try:
        total_alturas = 0
        total_disciplinas = 0
        promedios = []

        with open(archivo_promedios, "r", encoding="utf-8") as archivo:
            deporte = None
            for linea in archivo:
                linea = linea.strip()
                if not linea.replace(".", "", 1).isdigit():  #nombre del deporte
                    deporte = linea
                else:
                    promedio = float(linea)
                    promedios.append((deporte, promedio))
                    total_alturas += promedio
                    total_disciplinas += 1
        
        if total_disciplinas == 0:
            print("no hay datos suficientes para calcular")
            return

        promedio_general = total_alturas / total_disciplinas
        print(f"promedio general: {promedio_general:.2f}")
        print("disciplinas con promedio superior al general:")
        for deporte, promedio in promedios:
            if promedio > promedio_general:
                print(f"{deporte}: {promedio:.2f}")
    except FileNotFoundError:
        print(f"el archivo {archivo_promedios} no existe")
    except Exception as e:
        print(f"ocurrió un error al mostrar los deportes: {e}")

#flujo principal del programa
try:
    archivo_alturas = "alturas.txt"
    archivo_promedios = "promedios.txt"

    print("opciones:")
    print("1. grabar rangos de alturas")
    print("2. calcular y grabar promedios")
    print("3. mostrar disciplinas con atletas más altos que el promedio general")
    opcion = input("elige una opción (1/2/3): ").strip()

    if opcion == "1":
        grabar_rango_alturas(archivo_alturas)
    elif opcion == "2":
        grabar_promedio(archivo_alturas, archivo_promedios)
    elif opcion == "3":
        mostrar_mas_altos(archivo_promedios)
    else:
        print("opción inválida")
except Exception as e:
    print(f"ocurrió un error inesperado: {e}")
