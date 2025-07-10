#     2. Una agencia de viajes para armar un paquete toma en cuenta las siguientes opciones: 

#     • Viaje a Galápagos con crucero = $1.500
#     • Viaje a Cuenca con museos = $350
#     • Viaje a Guayaquil = $450
#     • Viaje a Loja = $250
#['Viaje a Galápagos con crucero',1500], ['Viaje a Cuenca con museos',350], ['Viaje a Guayaquil', 450], ['Viaje a Loja', 250]
# El gerente de la empresa en base a los requisitos solicita desarrollar un sistema de gestión de tours 
# (CRUD) de todos los clientes que van a requerir contratar un paquete en el cual se presente un menú de 
# opciones con la siguiente información:

#     • Registrar paquetes      [descripcion,costo]
#     • Registrar reservas      cedula: [nombre,paquete,numPersonas,costoTotal]
#     • Mostrar reservas agendadas
#     • Mostrar detalle de una reserva
#     • Guardar la reserva en un archivo
#     • Salir del sistema
import os
opcionesPaquetes = []
reservas = {}
rutaPaquetes = 'Semana12/Archivos/paquetes.txt'
rutaReservas = 'Semana12/Archivos/reservas.txt'

def cargarDatos():
    global opcionesPaquetes
    global reservas

    if not os.path.exists(rutaPaquetes) or not os.path.exists(rutaReservas):
        open(rutaReservas, 'w').close()
        open(rutaPaquetes, 'w').close()

    with open(rutaPaquetes, 'r') as archivo:
        opcionesPaquetes = archivo.readlines()

    with open(rutaReservas, 'r') as archivoReservas:
        for lineas in archivoReservas:
            partes = lineas.strip().split(',')
            cedula = partes[0]
            datos = partes[1:]
            reservas[cedula] = datos
    return opcionesPaquetes, reservas

def registrarPaquetes():
    descripcion = input('Ingrese la descripcion del paquete:\n ')
    costo = input('Ingrese el costo del paquete')
    opcionesPaquetes.append([descripcion,float(costo)])

    with open(rutaPaquetes, 'w') as archivo:
        archivo.write(opcionesPaquetes)

def seleccionarPaquete():
    print('Paquetes: \n')
    contador = 1
    for paquete in opcionesPaquetes:
        print(f'{contador}. {paquete[0]}, por {paquete[1]}')
        contador += 1

    paqueteSeleccionado = int(input('Ingrese el paquete que desea adquirir: '))
    for i in range(1,len(opcionesPaquetes)+1):
        if i == paqueteSeleccionado:
            return i
        
    return -1000
      
def registrarReserva():
    cedula = input('Ingrese la cedula del que va a reservar: ')
    paquete = opcionesPaquetes[seleccionarPaquete()]
    nombre = input('Ingese el nombre del que va a reservar: ')
    numPersonas = int(input('Ingrese el numero de personas: '))
    costoTotal = numPersonas * paquete[1]
    reservas[cedula] = [nombre, paquete,numPersonas, costoTotal]

def mostrarReservasAgendadas():
    for cedula, datos in reservas.items():
        print(f'Reserva con cedula: {cedula} \tA nombre de: {datos[0]}')

def mostrarDetallesReserva():
    cedulaReservaDetalle = int(input('Ingrese la cedula del cual se hizo la reserva: '))
    if cedulaReservaDetalle in reservas.keys():
        print(f'Reserva con cedula: {reservas[cedulaReservaDetalle]} \tA nombre de: {reservas[cedulaReservaDetalle][0]} \t Paquete: {reservas[cedulaReservaDetalle][1]}')

def guardarReservaArchivo():
    cedulaReservaGuardar = int(input('Ingrese la cedula del cual se hizo la reserva: '))
    reserva_a_guardar = {}
    if cedulaReservaGuardar in reservas.keys():
        reserva_a_guardar = reservas[cedulaReservaGuardar]
        with open(rutaReservas, 'w') as archivo:
            archivo.write(reserva_a_guardar)
    else:
        print("La reserva a esa cedula no existe")

def menu():
    opcionesPaquetes, reservas = cargarDatos()
    
    while True:
        print('1.Registrar paquetes')
        print('2.Registrar reservas')
        print('3.Mostrar reservas agendadas')
        print('4.Mostrar detalle de una reserva')
        print('5.Guardar la reserva en un archivo')
        print('6.Salir del sistema')

        while True:
            try:
                opcion = int(input('Ingrese una opcion: '))
                if opcion < 1 or opcion > 6:
                    print('Ingrese un numero entre 1-6') 
                else:
                    break
            except ValueError:
                print('Ingrese un numero.')

        if opcion == 1:
            print('Seleccionaste: Registrar paquetes')
            registrarPaquetes()
        if opcion == 2:
            print('Seleccionaste: Registrar reservas')
            registrarReserva()
        if opcion == 3:
            print('Seleccionaste: Mostrar reservas agendadas')
            mostrarReservasAgendadas()
        if opcion == 4:
            print('Seleccionaste: Mostrar detalle de una reserva')
            mostrarDetallesReserva()
        if opcion == 5:
            print('Seleccionaste: Guardar la reserva en un archivo')
            guardarReservaArchivo()
        if opcion == 6:
            print('Saliendo...')
            break


menu()
