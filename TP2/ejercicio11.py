"""Resolver el siguiente problema, diseñando las funciones a utilizar:
 Una clínica necesita un programa para atender a sus pacientes. Cada paciente que 
ingresa se anuncia en la recepción indicando su numero de afiliado (numero entero 
de 4 dígitos) y además indica si viene por una urgencia (ingresando un 0) o con 
turno (ingresando un 1). Para finalizar se ingresa -1 como numero de socio. Luego 
se solicita:
 a. Mostrar un listado de los pacientes atendidos por urgencia y un listado de 
los pacientes atendidos por turno en el orden que llegaron a la clínica.
 b. Realizar la búsqueda de un numero de afiliado e informar cuántas veces fue 
atendido por turno y cuántas por urgencia. Repetir esta búsqueda hasta 
que se ingrese -1 como numero de afiliado."""

#se exporta la libreria de re
import re 

#se define la funcion principal

#se crea la expresión regular para validar un número de afiliado
afiliado_pattern = re.compile(r"^\d{4}$")

#se define la funcion 
def registrar_pacientes(none)-> list:
    """
    pre: esta funcion no requiere parametros externos

    post: esta funcion retorna dos listas
    
    """
    urgencias = []
    turnos = []
    #crea un bucle donde se solicitan los numeros de afiliado
    while True:
        numero_afiliado = input("Ingrese el número de afiliado (4 dígitos) o -1 para finalizar: ")
        if numero_afiliado == "-1":
            break
        if not afiliado_pattern.match(numero_afiliado):
            print("El número de afiliado debe ser un entero de 4 dígitos.")
            continue
        #se solicita y asigna el ipo de urgencia 
        tipo = input("Ingrese 0 para urgencia o 1 para turno: ")
        if tipo == "0":
            urgencias.append(int(numero_afiliado))
        elif tipo == "1":
            turnos.append(int(numero_afiliado))
        else:
            print("Entrada inválida. Debe ingresar 0 o 1.")
    #retorna las listas ya creadas
    return urgencias, turnos

#se define la funcion
def listar_pacientes(urgencias = list, turnos= list) -> str:
    """
    pre: esta funcion recibe dos listas

    post: esta lista imprime en pantalla los numeros de afiliados de los pacientes
    """
    print("\nPacientes atendidos por urgencia:")
    if urgencias:
        for paciente in urgencias:
            print(paciente)
    else:
        print("No hubo pacientes atendidos por urgencia.")
    
    print("\nPacientes atendidos por turno:")
    if turnos:
        for paciente in turnos:
            print(paciente)
    else:
        print("No hubo pacientes atendidos por turno.")

#se define la funcion
def buscar_afiliado(urgencias= list, turnos= list)-> str:
    """
    pre: 

    post:
    """
    while True:
        numero_afiliado = input("Ingrese el número de afiliado a buscar (o -1 para finalizar): ")
        if numero_afiliado == "-1":
            break
        if not afiliado_pattern.match(numero_afiliado):
            print("El número de afiliado debe ser un entero de 4 dígitos.")
            continue

        numero_afiliado = int(numero_afiliado)
        urgencia_count = urgencias.count(numero_afiliado)
        turno_count = turnos.count(numero_afiliado)
        
        print(f"El afiliado {numero_afiliado} fue atendido {urgencia_count} veces por urgencia y {turno_count} veces por turno.")

#se asignan los valores y se llama a las funciones
print("Registro de pacientes")
urgencias, turnos = registrar_pacientes()
listar_pacientes(urgencias, turnos)
print("\nBúsqueda de afiliados")
buscar_afiliado(urgencias, turnos)
