"""Un comercio de electrodomésticos necesita para su línea de cajas un programa que 
le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan 
dos números enteros, correspondientes al total de la compra y al dinero recibido. 
Informar cuántos billetes de cada denominación deben ser entregados como vuelto, 
de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes 
de $5000, $1000, $500, $200, $100, $50 y $10. Emitir un mensaje de error si el 
dinero recibido fuera insuficiente o si el cambio no pudiera entregarse debido a falta 
de billetes con denominaciones adecuadas. Ejemplo: Si la compra es de $3170 y se 
abona con $5000, el vuelto debe contener 1 billete de $1000, 1 billete de $500, 1 
billete de $200, 1 billete de $100 y 3 billetes de $10."""

#definir la funcion
def calcular_cambio(total_compra = int, total_recibido = int):
    #se definen las denominaciones de los billetes disponibles
    denominaciones = [5000, 1000, 500, 200, 100, 50, 10]

    #se comprueba primero si se puede pagar el producto
    if total_compra > total_recibido:
        return "dinero insuficiente"
    
    #se comprueba si es necesario entregar cambio
    cambio = total_recibido - total_compra
    if cambio == 0:
        return "no es necesario entregar cambio"
    
    #se calculan la cantidad de billetes que se necesitan de cada denominacion
    total_cambio = {}
    for den in denominaciones:
        if cambio > den:
            cant_billetes = cambio // den
            total_cambio[den] = cant_billetes
            cambio %= den
    
    #de darse el caso que no haya denominaciones para pagar el producto se produce un error
    if cambio > 0:
        return "imposible entregar cambio adecuado"
    
    #se le indica al usuario la cantidad de billetes a entregar
    mensaje = "Billetes a entregar:\n"
    for den in denominaciones:
        if den in total_cambio:
            mensaje += f"${den}: {total_cambio[den]} billete(s)\n"
    return mensaje


#se definen los valores para la funcion
total_a_pagar = int(input("ingrese el total a pagar:"))
total_entregado = int(input("ingrese el monto entregado"))

#se da uso a la funcion
total = calcular_cambio(total_a_pagar, total_entregado)
print(total)