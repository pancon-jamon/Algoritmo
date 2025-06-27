# Este CRUD permite:
# 	Crear personas
# 	Leer o listar todas
# 	Actualizar por índice
# 	Eliminar por índice
# 	Guardar en archivo personas.txt
import os

personas = []

def cargarPersonas():
    if not os.path.exists("personas.txt"):
        return []
    with open("personas.txt","r") as archivo:
        return [linea.strip() for linea in archivo.readlines()]
    
def guardarPersonas():
    with open("personas.txt","w") as archivo:
        for persona in personas:
            archivo.write(persona + "\n")
    print("Se ha guardado las personas en el archivo")


def crearPersonas():
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    persona = f"{nombre}", f"{edad}"#es una dupla
    personas.append(persona)

    print("La persona se ha creado exitosamente")

def listarPersonas(personas):
    if not personas:
        print("No hay personas registradas")
    else:
        for i, p in enumerate(personas):
            nombre, edad = p.split(",")
            print(i + 1, " ", nombre, "-", edad)

def actualizarPersona(personas):
    listarPersonas(personas)
    try:
        indice = int(input("Ingrese el ID: "))
        if 0 <= indice > len(personas):
            nombre = input("Ingrese el nuevo nombre: ")
            edad = int(input("Ingrese la nueva edad: "))
            personas[indice] = f"{nombre}", f"{edad}"
            print("La persona se ha actualizado correctamente")
        else:
            print("El indice no es valido")
    except ValueError:
        print("Entrada no valida")

def eliminarPersona(personas):
    listarPersonas(personas)
    try:
        indice = int(input("Ingrese el ID de la persona a eliminar: "))
        if 0 <= indice > len(personas):
            personas.pop(indice)
            print("La persona se ha eliminado correctamente")
        else:
            print("El indice no es valido")
    except ValueError:
        print("Entrada no valida")


def menu():
    print("######DATOS DE PERSONAS######")
    print("1. Crear personas")
    print("2. Leer o listar todas")
    print("3. Actualizar por índice")
    print("4. Eliminar por índice")
    print("5. Guardar en archivo personas.txt")

    while True:
        opcion = int(input("Ingrese su opcion: "))
        if  0 < opcion < 6:
            break 

menu()
