""" Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso 
para poder cargar los camiones de reparto. La empresa cuenta con N camiones, y 
cada uno puede transportar hasta media tonelada (500 kilogramos). En un cajón 
caben 100 naranjas con un peso de entre 200 y 300 gramos cada una. Si el peso 
de alguna naranja se encuentra fuera del rango indicado se la clasifica para 
procesar como jugo. Desarrollar un programa para ingresar la cantidad de naranjas 
cosechadas e informar cuántos cajones se pueden llenar, cuántas naranjas son para 
jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente 
reparto. Simular el peso de cada unidad generando un número entero al azar entre 
150 y 350.
 Además, se desea saber cuántos camiones se necesitan para transportar la cose
cha, considerando que la ocupación del camión no debe ser inferior al 80%; en 
caso contrario el camión no serán despachado por su alto costo."""

#importar libreria random
import random

#definir la función
def clasificar_naranjas(cantidad_naranjas = int) -> int:
    """
    pre:esta variable recibe un numero entero

    post: esta variable retorna valores enteros
    """
    #peso promedio por caja en kg (cada caja tiene 100 naranjas y cada naranja tiene un peso promedio de 500g)
    peso_caja = 100 * (500 / 2 / 1000) 

    #generar aleatoriamente el peso de las naranjas dentro de los parámetros
    naranjas = [random.randint(150, 350) for i in range(cantidad_naranjas)]

    #clasificar las naranjas
    naranjas_jugo = 0
    naranjas_cajas = []
    for peso in naranjas:
        if peso < 200 or peso > 300:
            naranjas_jugo += 1
        else:
            naranjas_cajas.append(peso)
    
    #calcular cuántos cajones se pueden llenar con las naranjas
    cantidad_cajones = len(naranjas_cajas) // 100
    sobrante_naranjas = len(naranjas_cajas) % 100

    #calcular el peso total de las naranjas en las cajas en kg
    peso_total_naranjas = (len(naranjas_cajas) * (500 / 1000))

    #calcular cuántos camiones se necesitan
    camiones_necesarios = peso_total_naranjas / 500
    camiones_reales = int(camiones_necesarios)
    
    #ajustar si el último camión no alcanza el 80% de su capacidad
    if (peso_total_naranjas % 500) / 500 < 0.8 and (peso_total_naranjas % 500) > 0:
        camiones_reales -= 1

    #retornar todos los valores calculados
    return cantidad_cajones, naranjas_jugo, sobrante_naranjas, camiones_reales

#asignación de variables y ejecución del programa
cantidad_naranjas = int(input("Ingrese la cantidad de naranjas cosechadas: "))

cantidad_cajones, naranjas_jugo, sobrante_naranjas, camiones_necesarios = clasificar_naranjas(cantidad_naranjas)

print(f"Cantidad de cajones llenos: {cantidad_cajones}")
print(f"Cantidad de naranjas para jugo: {naranjas_jugo}")
print(f"Sobrante de naranjas para el siguiente reparto: {sobrante_naranjas}")
print(f"Cantidad de camiones necesarios: {camiones_necesarios}")
