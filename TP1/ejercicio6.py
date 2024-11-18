"""Desarrollar una función que reciba como parámetros dos números enteros positivos 
y devuelva como valor de retorno el número que resulte de concatenar ambos 
parámetros. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se per
mite utilizar facilidades de Python no vistas en clase."""

def concatenar(n1 = int, n2 = int) -> int:
    """
    Pre: esta funcion recibe unicamente dos valores enteros

    post: esta funcion retorna un entero

    """
    #se transforman los enteros en str para concatenarlos
    str_n1 = str(n1) 
    str_n2 = str(n2)

    #se concatenan ambos valores
    concatenacion = str_n1 + str_n2

    #se vuelven enteros nuevamente tras concatenar ambos valores y se retorna el resultado
    resultado = int(concatenacion)
    return resultado

#se definen los valores de las variables y se muestran al usuario
n1 = int(input("ingrese un numero:"))
n2 = int(input("ingrese un numero:"))

resultado = concatenar(n1, n2)

print(resultado)