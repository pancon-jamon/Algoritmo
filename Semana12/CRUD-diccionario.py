# El programa guarda los datos en un archivo de texto y cada registro se almacena como una línea en formato clave: valor.
# CRUD (Crear, Leer, Actualizar, Eliminar) de personas, donde:
# •	Cada persona tiene una cédula, nombre y edad.
# •	Los datos se guardan en un archivo personas.txt.
# •	Cada persona se representa con un diccionario, usando la cédula como clave única.
# •	Menú interactivo.
import os

archivo = "estudiantes.txt"

def cargarDatos():
    if  not os.path.exists(archivo):
        return {}
    with open(archivo, "r") as f:
        lineas = f.readlines()
        datos = {}
        for linea in lineas:
            try:
                estudiante = eval(linea.strip())#convertimos text a diccionario
                cedula = estudiante["cedula"]#extraemos el numero de cedula como clave
                datos[cedula] = estudiante
            except:#si falla saltamos
                continue
        return datos
    
def guardarDatos(datos):
    with open(archivo, "w") as f:
        for estudiante in datos.values():
            f.write(str(estudiante) + "\n")
    print("Datos guardados correctamente")

def crearEstudiante(datos):
    cedula = input("Ingrese la cedula: ")
    if cedula in datos:
        print("La cedula ya existe")
        return

    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    estudiante = {"cedula" : cedula, "nombre" : nombre, "edad" : edad}
    datos[cedula] = estudiante
    print("Estudiante agregado")

#Tambien deberia leer el archivo
def leerEstudiante(datos):
    if not datos:
        print("no hay registros")
    else:
        for estudiante in datos.values():
            print(f"Cedula: {estudiante["cedula"]}, Nombre: {estudiante["nombre"]}, Edad : {estudiante["edad"]}")

def actualizarCedula(datos):
    cedula = input("Ingrese la cedula del estudiante a actualizar: ")
    if cedula not in datos:
        print("La cedula no existe")
        return
    
    nombre = input("Ingrese el nuevo nombre: ")
    edad = input("Nueva edad: ")
    datos[cedula]["nombre"] = nombre
    datos[cedula]["edad"] = edad
    print("Estudiante actualizado")

def eliminarEstudiante(datos):
    cedula = input("Ingrese la cedula del estudiante a eliminar: ")
    if cedula in datos:
        del datos[cedula]
        print("estudiante eliminado")
    else:
        print("La cedula no existe")

def menu():
    datos = cargarDatos()
    while True:
        print("\n---CRUD ESTUDIANTES---")
        print("1.Crear estudiante")
        print("2.Leer estudiante")
        print("3.Actualizar estudiante")
        print("4.Eliminar estudiante")
        print("5.Guardar cambios")
        print("6.Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            crearEstudiante(datos)

        elif opcion == "2":
            leerEstudiante(datos)

        elif opcion == "3":
            actualizarCedula(datos)

        elif opcion == "4":
            eliminarEstudiante(datos)

        elif opcion == "5":
            guardarDatos(datos)

        elif opcion == "6":
            confirmar = input("Desea salir sin guardar los cambios?(s/n): ").lower()
            if confirmar == "s":
                print("Saliendo sin guradar")
                break
            else:
                print("Regresando al menu")

        else:
            print("Opcion no valida")

menu()
