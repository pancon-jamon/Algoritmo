# Este CRUD permite:
# 	Crear personas
# 	Leer o listar todas
# 	Actualizar por índice
# 	Eliminar por índice
# 	Guardar en archivo personas.txt
import os

personas = []
ruta = "Semana11/Archivos/personas.txt"

def cargarPersonas():
    global personas
    if not os.path.exists(ruta):
        personas = []
        return
    with open(ruta,"r") as archivo:
        personas = [linea.strip().split(",") for linea in archivo.readlines()]
    
def guardarPersonas():
    with open(ruta,"w") as archivo:
        for persona in personas:
            archivo.write(f"{persona[0]},{persona[1]}\n")
    print("Se ha guardado las personas en el archivo")

def crearPersonas():
    nombre = input("Ingrese el nombre: ")
    edad = input("Ingrese la edad: ") 
    personas.append([nombre, edad])
    print("La persona se ha creado exitosamente")

def listarPersonas():
    if not personas:
        print("No hay personas registradas")
    else:
        for i, p in enumerate(personas):
            print(f"{i + 1}. {p[0]} - {p[1]}")

def actualizarPersona():
    listarPersonas()
    try:
        indice = int(input("Ingrese el ID: ")) - 1
        if 0 <= indice < len(personas):
            nombre = input("Ingrese el nuevo nombre: ")
            edad = input("Ingrese la nueva edad: ")
            personas[indice] = [nombre, edad]
            print("La persona se ha actualizado correctamente")
        else:
            print("El índice no es válido")
    except ValueError:
        print("Entrada no válida")

def eliminarPersona():
    listarPersonas()
    try:
        indice = int(input("Ingrese el ID de la persona a eliminar: ")) - 1
        if 0 <= indice < len(personas):
            personas.pop(indice)
            print("La persona se ha eliminado correctamente")
        else:
            print("El índice no es válido")
    except ValueError:
        print("Entrada no válida")


def menu():
    print("######DATOS DE PERSONAS######")
    print("1. Crear personas")
    print("2. Leer o listar todas")
    print("3. Actualizar por índice")
    print("4. Eliminar por índice")
    print("5. Guardar en archivo personas.txt")
    print("6. Salir")

    while True:
        try:
            opcion = int(input("Ingrese su opcion(entre 1 y 6): "))
            if  0 < opcion < 7:
                
                match opcion:
                    case 1:
                        print("Elijio la opcion 1: Crear personas")
                        crearPersonas()
                    case 2:
                        print("Elijio la opcion 2: Leer o listar todas")
                        listarPersonas()
                    case 3:
                        print("Elijio la opcion 3: Actualizar por índice")
                        actualizarPersona()
                    case 4:
                        print("Elijio la opcion 4: Eliminar por índice")
                        eliminarPersona()
                    case 5:
                        print("Elijio la opcion 5:  Guardar en archivo personas.txt")
                        cargarPersonas()
                    case 6:
                        print("Saliendo...")
                        break
                    case _:
                        print("Opcion no valida")
        except ValueError:
            print('Ingrese un numero')

     

menu()
