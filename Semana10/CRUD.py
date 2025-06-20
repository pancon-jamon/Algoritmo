"""18.	Diccionario que permite gestionar notas
Realiza lo siguiente:

-	Crear una función para añadir las notas (agregarNota), con los parámetros: nota, título, contenido.
-	Crear una función para ver las notas (verNotas)
-	Crear una función para editar las notas (editarNota)
-	Crear una función para eliminar las notas (eliminarNota)
-	Crear una función que muestre el menú
"""
notas = {}
def agregarNota(notas,titulo,contenido):
    notas[titulo] = contenido

def verNotas():
    if not notas:
        print("No existe ninguna nota")
    else:
        for titulo, contenido in notas.items:
            print(titulo, ":", contenido)

def editarNota(notas, titulo, nuevoContenido):
    if titulo in notas:
        notas[titulo] = nuevoContenido
        print("La nota se actualizo exitosamente")
    else:
        print("La nota de la asignatura no existe")

def eliminarNota(notas, titulo):
    if titulo in notas:
        del notas[titulo]
    else:
        print("La nota de la asignatura ", titulo," no exite")

while True:
    print("###Bienvenido al SAEW###")
    print("1. Agregar Nota ")
    print("2. Ver Nota ")
    print("3. Editar Nota ")
    print("4. Eliminar Nota ")
    print("5. Salir ")
    opcion = int(input("Ingrese la opcion que desea hacer: "))
    match opcion:
        case 1:
            titulo = input("Ingrese la asignatura")
            contenido = float(input("Ingrese la nota"))
            agregarNota(notas, titulo, contenido)
            print("La nota se ha agregado correctamente")
        case 2:
        
        case 3:
        
        case 4:

        case 5:
