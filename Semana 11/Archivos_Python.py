# PARTE 1: ARCHIVOS
# Nivel Básico
import os
# # os.makedirs("Archivos", exist_ok=True)
# # 1. Crear un archivo de texto y escribir varias líneas
# # Escribe 3 líneas en un archivo llamado saludo.txt.
# with open("Archivos/saludo.txt", "w") as archivo:
#     archivo.write("Claudia Coello\n")
#     archivo.write("saluda a la clase de\n")
#     archivo.write("Algoritmos y Estructura de datos\n")

# # 2. Leer un archivo línea por línea
# # Lee el archivo saludo.txt e imprime cada línea.
# with open("Archivos/saludo.txt", "r") as archivo:
#     print(archivo.read())
# with open("Archivos/saludo.txt", "r") as archivo:
#     print(archivo.readlines())
# with open("Archivos/saludo.txt", "r") as archivo:
#     print(archivo.readline())
# with open("Archivos/saludo.txt", "r") as archivo:
#     for linea in archivo:
        # print(linea.strip())

# # 3. Crear un archivo solo si no existe (modo 'x')
# # Intenta crear registro.txt, si ya existe, muestra un mensaje de error.
# try:
#     with open("registro.txt","x") as archivo:
#         archivo.write("Creando solo un archivo con el modo x")
# except FileExistsError:
#     print("Error. El archivo ya existe")

# # 4. Contar cuántas líneas tiene un archivo
# # Cuenta las líneas del archivo saludo.txt.
# with open("Archivos/saludo.txt", "r") as archivo:
#     lineas = archivo.readlines()
#     print("Numero de lineas: ",len(lineas))

# # 5. Copiar el contenido de un archivo a otro
# with open("Archivos/saludo.txt", "r") as archivoOriginal, open("Archivos/copiaSaludo.txt", "w") as archivoCopia:
#     archivoCopia.write(archivoOriginal.read())
    
# # Nivel Intermedio
# # 6. Agregar texto a un archivo existente
# # Agrega una línea nueva a saludo.txt sin borrar lo anterior.
# with open("Archivos/saludo.txt", "a") as archivo:
#     archivo.write("\nSeguimos aprendiendo archivos.")
#     archivo.write("Es muy facil.\n")

# # 7. Leer un archivo y contar cuántas veces aparece una palabra
# # Cuenta cuántas veces aparece la palabra "Python".
# with open("Archivos/saludo.txt", "r") as archivo:
#     contenido = archivo.read()
#     print("La palabra archivos aparece, ", contenido.count("archivos"), "veces")

# # 8. Leer un archivo y mostrar solo las líneas que 
# # contienen una palabra clave
# # Imprime solo las líneas que contengan "Hola".
# with open("Archivos/saludo.txt", "r") as archivo:
#     for lineas in archivo:
#         if "aprendiendo" in lineas:
#             print("La palabra aprendiendo aparece, ", lineas.strip(), "veces")

# # 9. Escribir una lista de nombres en un archivo
# # Escribe una lista de nombres en nombres.txt, uno por línea.
# nombres = ["Claudia", "Maria","Pedro"]
# with open("Archivos/nombres.txt", "w") as archivo:
#     for nombre in nombres:
#         archivo.write(nombre + "\n")

# # 10. Leer los nombres desde el archivo y mostrarlos en mayúsculas
# with open("Archivos/nombres.txt", "r") as archivo:
#     print(archivo.read().upper())


# # 11. Crear y escribir en un archivo
# # Crea un archivo llamado datos.txt y escribe 3 líneas.
# with open("Archivos/datos.txt", "w") as archivo:
#     archivo.write("Hola\n")
#     archivo.write("como\n")
#     archivo.write("estas?")

# # 12. Leer e imprimir el contenido del archivo línea por línea
# # Lee el archivo datos.txt e imprime cada línea sin saltos de línea dobles.
# with open("Archivos/datos.txt", "r") as archivo:
#     print(archivo.read())

# 13. Contar cuántas líneas tiene un archivo
# Cuenta cuántas líneas tiene el archivo datos.txt.
# with open("Archivos/datos.txt", "r") as archivo:
#     lineas = archivo.readlines()
#     print("El numero de lineas es: ", len(lineas))

# # 14. Agregar una línea a un archivo existente
# # Añade la línea "Cuarta línea" al final del archivo datos.txt.
# with open("Archivos/datos.txt", "a+") as archivo:
#     archivo.write("\nCuarta línea")      #Cuando usamos "a" o "+", el cursor queda al final del archivo
#     archivo.seek(0)                      #Debemos mover cursor al byte inicial, el inicio del archivo
#     print(archivo.read())          


# # 15. Buscar una palabra clave en el archivo
# # Imprime solo las líneas que contienen la palabra "línea".
# with open("Archivos/datos.txt", 'r') as archivo:
#     for linea in archivo:
#         if "línea" in linea:
#             print(linea.strip())

# # 16. Copiar el contenido de un archivo a otro
# # Copia todo el contenido de datos.txt a un nuevo archivo llamado copia_datos.txt.
# with open("Archivos/datos.txt", 'r') as archivo, open("Archivos/copia_datos.txt", 'w') as archivoCopia:
#     contenidoOriginal = archivo.read()
#     archivoCopia.write(contenidoOriginal)

# 17: Crear un archivo con nombre personalizado
# Pídele al usuario un nombre para el archivo y una línea de texto, y guárdala.

# nombreArchivo = input("Ingrese el nombre del archivo: ")
# rutaArchivo = os.path.join("Semana11/Archivos", nombreArchivo)
# if os.path.exists(rutaArchivo):
#     print("El archivo ya existe")
# else:
#     with open(rutaArchivo + ".txt", "a") as archivo:
#         lineaTexto = input("Ingrese una linea para el archivo: ")
#         archivo.write(lineaTexto + "\n")

# with open(rutaArchivo+ ".txt", "r") as archivo:
#     contenido = archivo.readlines()
#     for i in contenido:
#         print(i.strip())

# # 18: Escribir múltiples líneas hasta que el usuario escriba "salir"
# # Permite ingresar varias líneas y las guarda en mensajes.txt, hasta que se escriba "salir".

# with open("Semana11/Archivos/mensaje.txt", "a") as archivo:   
#     while True:
#         mensaje = input("Escriba un mensaje o salir para salir:")
#         if mensaje.lower() == "salir":
#             break
#         else:
#             archivo.write(mensaje + "\n")
# with open("Semana11/Archivos/mensaje.txt", "r") as archivo:
#     contenido = archivo.readlines()
#     for i in contenido:
#         print(i.strip())
        
# # 19: Leer un archivo cuyo nombre lo da el usuario
# # Solicita el nombre de un archivo y muestra su contenido línea por línea.
# nombreArchivo = input("Ingrese el nombre del archivo: ")
# archivoPersonalizado = "Semana11/Archivos/" + nombreArchivo + ".txt"
# if not os.path.exists(archivoPersonalizado):
#     print("El archivo no existe")
# else:
#     with open(archivoPersonalizado, "r") as archivo:
#         contenido = archivo.readlines()
#         for i in contenido:
#             print(i.strip())

# # 20 Guardar una lista de nombres ingresados por el usuario
# # Pide al usuario varios nombres y guárdalos en nombres.txt.
# listaNombres = []
# cantidadNombre = int(input("Cuantos nombres quiere ingresar?: "))

# for i in range(cantidadNombre):
#     nombre = input(f"Ingrese el nombre n{i + 1}: ")
#     listaNombres.append(nombre + "\n")

# with open("Semana11/Archivos/nombres.txt", "w") as archivo:
#     archivo.writelines(listaNombres)

# with open("Semana11/Archivos/nombres.txt", "r") as archivo:
#         contenido = archivo.readlines()
#         for i in contenido:
#             print(i.strip())
# # 21.	Crear un Archivo
# # Si se abre el archivo se le escribe contenido y se ejecuta nuevamente el script, 
# # se borra el contenido porque los sobreescribe.

# # 22.	 Escribir en un archivo
# with open("Semana11/Archivos/archivoTexto.txt", "w") as archivo:
#     archivo.write("Hola" + "\n")
# with open("Semana11/Archivos/archivoTexto.txt", "r") as archivo:
#         contenido = archivo.readlines()
#         for i in contenido:
#             print(i.strip())
# # 23.	Escribir en un archivo más lineas
# # Si quiero sobreescribir , que no quede el texto anterior cambior la “a” por “w”
# with open("Semana11/Archivos/saludoTexto.txt", "a") as archivo:
#     archivo.write("soy" + "\n")
#     archivo.write("Claudia" + "\n")
# with open("Semana11/Archivos/saludoTexto.txt", "r") as archivo:
#         contenido = archivo.readlines()
#         for i in contenido:
#             print(i.strip())
# # 24.	Sobrescribir en un archivo mas lineas
# print("Antes de sobreescribir: \n")
# with open("Semana11/Archivos/sobreescribirTexto.txt", "w") as archivo:
#     archivo.write("Hola" + "\n")
#     archivo.write("como estas?" + "\n")

# with open("Semana11/Archivos/sobreescribirTexto.txt", "r") as archivo:
#         contenido = archivo.readlines()
#         for i in contenido:
#             print(i.strip())
# with open("Semana11/Archivos/sobreescribirTexto.txt", "w") as archivo:
#     archivo.write("Linea sobreescrita" + "\n")
#     archivo.write("otra linea sobreescrita" + "\n")

# print("Despues de sobreescribir: \n")
# with open("Semana11/Archivos/sobreescribirTexto.txt", "r") as archivo:
#         contenido = archivo.readlines()
#         for i in contenido:
#             print(i.strip())

# # 25.	Seguir escribiendo líneas en un archivo
# print("ANTES")
# with open("Semana11/Archivos/sobreescribirTexto.txt", "r") as archivo:
#         contenido = archivo.readlines()
#         for i in contenido:
#             print(i.strip())

# with open("Semana11/Archivos/sobreescribirTexto.txt", "a") as archivo:
#     archivo.write("Linea agregada" + "\n")
#     archivo.write("otra linea agregada" + "\n")

# print("DESPUES")
# with open("Semana11/Archivos/sobreescribirTexto.txt", "r") as archivo:
#         contenido = archivo.readlines()
#         for i in contenido:
#             print(i.strip())

# # 26.	Abrir un archivo y leerlo
# with open("Semana11/Archivos/sobreescribirTexto.txt", "r") as archivo:
#         contenido = archivo.readlines()
#         for i in contenido:
#             print(i.strip())

# # 27.	 Abrir una archivo y leerlo desde otra ruta
# with open("Semana11/Archivos/sobreescribirTexto.txt", "r") as archivo:
#         contenido = archivo.readlines()
#         for i in contenido:
#             print(i.strip())

# # 28.	Abrir un archivo y leerlo línea por línea con while
# contador = 1
# with open("Semana11/Archivos/nombres.txt", "r") as archivo:
#     linea = archivo.readline()
    
#     while linea:
#         print(f"Línea {contador}: {linea.strip()}")  # strip() quita \n al final
#         contador += 1
#         linea = archivo.readline()

# 29.	Abrir un archivo y leerlo línea por línea con FOR
with open("Semana11/Archivos/nombres.txt", "r") as archivo:
    linea = archivo.readlines()
    for i in linea:
        print(i.strip())
