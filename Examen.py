# Solo el usuario "adminfifa" con la clave "fifa123" puede manejar la gestión de equipos. 
# Si alguien intenta acceder con credenciales incorrectas, el sistema de logueo se presentará indefinidamente hasta que se 
# ingresen los datos correctos.
print("Claudia Coello")
usuario = "adminfifa"
clave = "fifa123"

equiposRegistrados = []
idActual = 0

while True:
    usuarioIngresado = input("Ingrese su usuario: ")
    claveIngresada= input("Ingrese su clave: ")

    if(usuarioIngresado == usuario and claveIngresada == clave):
        print("Acceso concedido")
        break
    else:
        print("Usuario o clave incorrecta.")
        

print("Bienvenido al sistema de gestion del Mundial Clubes 2025.")

# El sistema mediante la gestión de una lista y un menú principal, debe permitir cumplir los siguientes requerimientos:
# •	Registrar nuevos equipos que se unan a la competición.
# •	Mostrar la lista de equipos para verificar quiénes están confirmados.
# •	Actualizar nombres de equipos en caso de cambios oficiales.
# •	Eliminar equipos que no cumplan con los requisitos del torneo.
# •	Buscar equipos por nombre para confirmar su participación.

#######################         Claudia Coello          ##################
condicion = True
while condicion:
    print("\t\tMundial de Clubes 2025 - Gestion de equipos")

    print("1.-Registrar equipo")
    print("2.-Mostrar equipos")
    print("3.-Actualizar equipo")
    print("4.-Eliminar equipo")
    print("5.-Buscar equipo")
    print("6.-Salir")
    opcion = int(input("Ingrese una opcion: "))

    while opcion < 1 or opcion >= 7:
        opcion = int(input("Opcion no valida. Porfavor ingrese una opcion entre 1-6: "))
#######################         Claudia Coello          ##################
    match opcion:
        case 1:
            print("Selecciono opcion 1")
            print("Registrar equipo")

            while True:
                equipo_A_Registrar = input("Ingrese el nombre del equipo: ")
                if(equipo_A_Registrar is ""):
                    print("El nombre del equipo no puede estar vacio")
                else:
                    break

            idActual += 1
            equiposRegistrados.append(equipo_A_Registrar)
            equiposRegistrados.append(idActual)

            print("Equipo registrado correctamente")
#######################         Claudia Coello          ##################
        case 2:
            print("Selecciono opcion 2")
            print("Lista de equipos registrados")
            
            for contador in range(0, len(equiposRegistrados), 2):
                print(f"{equiposRegistrados[contador + 1]}. {equiposRegistrados[contador]} ")
#######################         Claudia Coello          ##################
        case 3:
            print("Selecciono opcion 3")
            print("Actualizar equipo")

            for contador in range(0, len(equiposRegistrados), 2):
                print(f"{equiposRegistrados[contador + 1]}. {equiposRegistrados[contador]} ")

            while True:
                idActualizar = int(input("Ingrese el id del equipo a actualizar: "))

                if idActualizar in equiposRegistrados:
                    actualizarNombre = input("Ingrese el nuevo nombre: ")
                    equiposRegistrados[idActualizar] = actualizarNombre
                    break
                else:
                    print("Id invalido")

                
#######################         Claudia Coello          ##################        
        case 4:
            print("Selecciono opcion 4")
            print("Eliminar equipo")

            for contador in range(0, len(equiposRegistrados), 2):
                print(f"{equiposRegistrados[contador + 1]}. {equiposRegistrados[contador]} ")

            while True:
                idEliminar = input("Ingrese el id del equipo: ")
                if(idEliminar in equiposRegistrados):
                    
                    equiposRegistrados[idEliminar].remove
                    equiposRegistrados[idEliminar + 1].remove
                break
#######################         Claudia Coello          ##################
        case 5:
            print("Selecciono opcion 5")
            print("Buscar equipo")

            while True:
                equipoBuscar = input("Ingrese el nombre del equipo a buscar: ")

                if(equipoBuscar in equiposRegistrados):
                    for contador in range(0, len(equiposRegistrados), 2):
                        if(equiposRegistrados[contador] == equipoBuscar):
                            print(f"{equiposRegistrados[contador + 1]}. {equiposRegistrados[contador]} ")
                    break
                else:
                    print("El equipo no esta registrado")
                    break
#######################         Claudia Coello          ##################
        case 6:
            print("Selecciono opcion 6")
            print("Saliendo del programa...")
            condicion = False
    
print("Gracias por usar nuestro programa")
