"""Desarrollar un programa para eliminar todos los comentarios de un programa escrito en lenguaje Python. Tener en cuenta que los comentarios comienzan con el 
signo # (siempre que éste no se encuentre encerrado entre comillas simples o dobles) y que también se considera comentario a las cadenas de documentación 
(docstrings)."""

#se define la funcion
import re

def eliminar_comentarios(archivo_entrada: str, archivo_salida: str):
    """
    pre: archivo_entrada es un archivo python valido
    post: se graba un archivo sin comentarios ni docstrings en archivo_salida
    """
    try:
        with open(archivo_entrada, "r", encoding="utf-8") as entrada:
            codigo = entrada.read()

        #se elimina docstrings (triple comillas simples o dobles)
        codigo_sin_docstrings = re.sub(r"'''.*?'''|\"\"\".*?\"\"\"", "", codigo, flags=re.DOTALL)

        #se eliminan comentarios que comienzan con #
        lineas = codigo_sin_docstrings.splitlines()
        lineas_sin_comentarios = []
        for linea in lineas:
            #se elimina el comentario si no esta dentro de una cadena
            if "#" in linea:
                nueva_linea = re.sub(r"#.*", "", linea)
                lineas_sin_comentarios.append(nueva_linea.rstrip())
            else:
                lineas_sin_comentarios.append(linea.rstrip())

        #se unen las lineas sin comentarios
        codigo_limpio = "\n".join(lineas_sin_comentarios)

        with open(archivo_salida, "w", encoding="utf-8") as salida:
            salida.write(codigo_limpio)

        print(f"archivo limpio guardado en {archivo_salida}")
    except FileNotFoundError:
        print(f"el archivo {archivo_entrada} no existe")
    except Exception as e:
        print(f"ocurrió un error al procesar el archivo: {e}")

#flujo principal
try:
    archivo_entrada = input("ingresa el nombre del archivo de entrada: ").strip()
    archivo_salida = input("ingresa el nombre del archivo de salida: ").strip()
    eliminar_comentarios(archivo_entrada, archivo_salida)
except Exception as e:
    print(f"ocurrió un error inesperado: {e}")
