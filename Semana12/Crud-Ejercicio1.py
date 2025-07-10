#     1. Escribir un programa que permita gestionar la base de datos de clientes de una empresa. 
# Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su cédula, 
# y el valor será otro diccionario con los datos del cliente (nombre, dirección, telefono, correo, 
# preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. 
# El programa debe preguntar al usuario por una opción del siguiente menú: 
#         ◦ Añadir cliente, 
#         ◦ Eliminar cliente, 
#         ◦ Mostrar cliente, 
#         ◦ Listar todos los clientes, 
#         ◦ Listar clientes preferentes, 
#         ◦ Terminar. 

# En función de la opción elegida el programa tendrá que hacer lo siguiente:
#     • Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
#     • Preguntar por la cédula del cliente y eliminar sus datos de la base de datos.
#     • Preguntar por la cédula del cliente y mostrar sus datos.
#     • Mostrar lista de todos los clientes de la base datos con su cédula y nombre.
#     • Mostrar la lista de clientes preferentes de la base de datos con su cédula y nombre.
#     • Terminar el programa.
import os
pacientes = {}
ruta = "Semana12/Archivos/pacientes.txt"

def pedirCedula():
    while True:
        cedula = input("Ingrese el número de cédula: ").strip()
        if cedula == "":
            print("No puede dejar el campo en blanco.")
            continue
        try:
            cedula = int(cedula)
            break
        except ValueError:
            print("La cédula debe ser un número.")
    return cedula

def cargarPacientes():
    global pacientes
    if not os.path.exists(ruta):
        pacientes = {}
        return
    with open(ruta,"r") as archivo:
        for linea in archivo:
            partes = linea.strip().split(",")
            cedula = int(partes[0])
            datos = partes[1:]
            pacientes[cedula] = datos

    return pacientes

def guardarPacientesEnArchivo():
    with open(ruta, "w") as archivo:
        for cedula, datos in pacientes.items():
            linea = f"{cedula},{datos[0]},{datos[1]},{datos[2]},{datos[3]},{datos[4]}/n"
            archivo.write(linea)

def anadirPaciente():
    cedula = pedirCedula()

    while True:
        nombre = input("Ingrese su nombre: ").strip()
        if nombre == "":
            print("No puede dejar el campo en blanco.")
            nombre = input("Ingrese su nombre: ").strip()
            continue
        else:
            break

    while True:
        direccion = input("Ingrese su direccion: ").strip()
        if direccion == "":
            print("No puede dejar el campo en blanco.")
            direccion = input("Ingrese su direccion: ").strip()
            continue
        else:
            break

    while True:
        telefono = input("Ingrese su telefono: ").strip()
        if telefono == "":
            print("No puede dejar el campo en blanco.")
            continue
        try:
            telefono = int(telefono)
            break  
        except ValueError:
            print("Telefono invalido. Ingrese solo numeros.")

    while True:
        correo = input("Ingrese su correo: ").strip()
        
        if correo == "":
            print("No puede dejar el campo en blanco.")
        elif "@" not in correo:
            print("Debe ingresar un correo válido (debe contener '@').")
        else:
            break
    
    while True:
        preferente = input("Ingrese si es preferente o no (s/n): ").strip().lower()
        
        if preferente == "":
            print("No puede dejar el campo en blanco.")
        elif preferente != "s" and preferente != "n":
            print("Debe ingresar un preferente válido (s/n).")
        else:
            break
    if preferente == "s":
        preferenteBooleano = True
    elif preferente == "n":
        preferenteBooleano = False

    pacientes[cedula] = [nombre, direccion, telefono, correo, preferenteBooleano]
    guardarPacientesEnArchivo()

def eliminarPaciente():
    cedula = pedirCedula()

    if cedula in pacientes:
        del pacientes[cedula]
        guardarPacientesEnArchivo()
    else: 
        print("La cedula que esta intentando ingresar no existe")

def mostrarCliente():
    cedula_A_Mostrar = pedirCedula()
    if cedula_A_Mostrar in pacientes:
        print(f"Cedula: {cedula_A_Mostrar} \t-\t Nombre: {pacientes[cedula_A_Mostrar][0]}")

def mostrarClientes():
    for cedula, datos in pacientes.items():
        print(f"Cedula : {cedula} \t-\t Nombre : {datos[0]}")

def mostrarClientesPreferentes():
    for cedula, datos in pacientes.items():
        if datos[-1]:
            print(f"Cedula: {cedula} \t-\t Nombre: {datos[0]}")

def menu():
    pacientes = cargarPacientes()
    while True:
        print("1.Añadir cliente")
        print("2.Eliminar cliente ")
        print("3.Mostrar cliente") 
        print("4.Listar todos los clientes")
        print("5.Listar clientes preferentes ")
        print("6.Terminar")
        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            print("Eligio: Añadir cliente")
            anadirPaciente()

        if opcion == 2:
            print("Eligio: Eliminar cliente")
            eliminarPaciente()

        if opcion == 3:
            print("Eligio: Mostrar cliente")
            mostrarCliente()

        if opcion == 4:
            print("Eligio: Mostrar todos los clientes")
            mostrarClientes()

        if opcion == 5:
            print("Eligio: Mostrar clientes preferentes")
            mostrarClientesPreferentes()

        if opcion == 6:
            print("Saliendo...")
            break
        else:
            print('Opcion no valida')

menu()
