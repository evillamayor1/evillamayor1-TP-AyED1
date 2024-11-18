"""Escribir funciones lambda para:
 a. Informar si un número es oblongo. Se dice que un número es oblongo cuando 
se puede obtener multiplicando dos números naturales consecutivos. Por ejem
plo 6 es oblongo porque resulta de multiplicar 2 * 3.
 b. Informar si un número es triangular. Un número se define como triangular si 
puede expresarse como la suma de un grupo de números naturales consecuti
vos comenzando desde 1. Por ejemplo 10 es un número triangular porque se 
obtiene sumando 1+2+3+4.
 Ambas funciones lambda reciben como único parámetro el número a evaluar y de
vuelven True o False. No se permite utilizar ayudas externas a las mismas.
"""

#crear la funcion lambda a
es_oblongo = lambda n: any(n == i * (i + 1) for i in range(1, int(n**0.5) + 1))

#crear la funcion lambda b
es_triangular = lambda n: (8 * n + 1) ** 0.5 == int((8 * n + 1) ** 0.5)