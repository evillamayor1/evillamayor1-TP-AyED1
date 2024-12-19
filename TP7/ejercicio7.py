"""ados dos numeros enteros no negativos, devolver el resultado de calcular el Máximo Comun Divisor (también llamado Divisor Comun Mayor) basándose en las siguientes propiedades:
MCD(X, X) = X
MCD(X, Y) = MCD(Y, X)
Si X > Y => MCD(X, Y) = MCD(X–Y, Y)
Utilizando la funcion anterior calcular el MCD de todos los elementos de una lista de 
numeros enteros, sabiendo que MCD(X,Y,Z) = MCD(MCD(X,Y),Z) No se permite 
utilizar iteraciones en ninguna etapa del proceso"""

#se define la funcion

def mcd(x: int, y: int) -> int:
    """
    Pre: x y y son numeros enteros no negativos

    Post: se devuelve el MCD de x y y segun las propiedades dadas

    """
    if x == y:  # caso base: MCD(X, X) = X
        return x
    if x > y:  # caso: X > Y
        return mcd(x - y, y)
    return mcd(y, x)  #caso: X <= Y, se aplica la propiedad MCD(X, Y) = MCD(Y, X)


def mcd_lista(nums: list[int]) -> int:
    """
    Pre: nums es una lista de numeros enteros no negativos con al menos un elemento

    Post: se devuelve el MCD de todos los elementos de la lista

    """
    if len(nums) == 1:  #caso base: si queda un solo numero, su MCD es el mismo
        return nums[0]
    return mcd(nums[0], mcd_lista(nums[1:]))  #aplica recursion para MCD(X, Y, Z)
