""". En geometría un vector es un segmento de recta orientado que va desde un punto 
A hasta un punto B. Los vectores en el plano se representan mediante un par ordenado de números reales (x, y) llamados componentes. Para representarlos basta 
con unir el origen de coordenadas con el punto indicado en sus componentes: 
Dos vectores son ortogonales cuando son perpendiculares entre sí. Para determinarlo basta calcular su producto escalar y verificar si es igual a 0. Ejemplo: A = (2,3) y B = (-3,2) => 2 * (-3) + 3 * 2 = -6 + 6 = 0 => Son ortogonales
Escribir una función que reciba dos vectores en forma de tuplas y devuelva un valor 
de verdad indicando si son ortogonales o no. Desarrollar también un programa que 
permita verificar el comportamiento de la función. """

#se define la funcion
def son_ortogonales(vector1=tuple, vector2=tuple)-> bool:
    """
    pre: recibe dos tuplas representando los vectores en el plano
    post: devuelve True si los vectores son ortogonales, False si no lo son
    """
    #se calcula el producto escalar de los dos vectores
    producto_escalar = vector1[0] * vector2[0] + vector1[1] * vector2[1]
    
    #si el producto escalar es 0, los vectores son ortogonales
    return producto_escalar == 0

#programa principal
#se ngresan los dos vectores
vector1 = tuple(map(float, input("Ingresa las componentes del primer vector (x, y): ").split()))
vector2 = tuple(map(float, input("Ingresa las componentes del segundo vector (x, y): ").split()))

#se verifica si los vectores son ortogonales
if son_ortogonales(vector1, vector2):
   print("Los vectores son ortogonales.")
else:
    print("Los vectores no son ortogonales.")
