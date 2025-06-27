# #1.	Declarar el diccionario con clave y valor de los países y capitales de América Latina
# print("Claudia Coello")
# paises = {"Ecuador": "Quito", "Peru":"Lima","Colombia":"Bogota"}
# print(paises)
# #2.	Acceder a un valor del diccionario de países y capitales.
# print("Claudia Coello")
# paises = {"Ecuador": "Quito", "Peru":"Lima","Colombia":"Bogota"}
# print(paises["Ecuador"])

# #3.	Agregar un elemento al diccionario de países y capitales.
# print("Claudia Coello")
# paises = {"Ecuador": "Quito", "Peru":"Lima","Colombia":"Bogota"}
# paises["Bolivia"] = "La paz"
# print(paises)

# #4.	Modificar un elemento del diccionario de países y capitales.
# print("Claudia Coello")
# paises = {"Ecuador": "Quito", "Peru":"Lima","Colombia":"Bogota"}
# paises["Bolivia"] = "Montevideo"
# print(paises)

# #5.	Eliminar un elemento del diccionario de países y capitales.
# print("Claudia Coello")
# paises = {"Ecuador": "Quito", "Peru":"Lima","Colombia":"Bogota"}
# del paises["Peru"]
# print(paises)

# #6.	Eliminar un elemento con la función pop
# print("Claudia Coello")
# paises = {"Ecuador": "Quito", "Peru":"Lima","Colombia":"Bogota"}
# paises.pop("Colombia")
# print(paises)

# #7.	Acceder un elemento en concreto 
# print("Claudia Coello")
# paises = {"Ecuador": "Quito", "Peru":"Lima","Colombia":"Bogota"}
# print(paises["Peru"])

# #8.	Crear diccionarios con diferentes tipos de datos
# print("Claudia Coello")
# persona = {"Nombre" : "Claudia", "Apellido" : "Coello", "edad":21, "Pais":"Ecuador"}
# for elemento in persona:
#     print(elemento)
# for elemento in persona.values():
#     print(elemento)
    
# for elemento in persona.items():
#     print(elemento)

# #9.	Con valores de tipo lista
# print("Claudia Coello")
# semestre = {"materias" : ["Algoritmos", "Redes", "Arquitectura"], "notas" : [10,9,8],"pasatiempos" : ["bailar","pintar","leer"]}
# print(semestre["pasatiempos"][1])

#     10. Un diccionario puede contener otro diccionario
# print("Claudia Coello")
# diccionario = {'diccionario anidado':{"saludo":'hola'}, 'diccionario normal':'hola'}
# print(diccionario)
# print(diccionario['diccionario anidado'])

# #     11. Consultar las claves del diccionario
# print("Claudia Coello")
# paises = {"Ecuador": "Quito", "Peru":"Lima","Colombia":"Bogota"}
# claves = paises.keys()
# print('Las claves son : ', claves)

# for i in paises:
#     print('Otro metodo es: ', i)

# #     12. Consultar los valores del diccionario
# print("Claudia Coello")
# paises = {"Ecuador": "Quito", "Peru":"Lima","Colombia":"Bogota"}
# valores = paises.values()
# print('Las valores son : ', valores)

# #     13. Consultar la longitud del diccionario
# print("Claudia Coello")
# paises = {"Ecuador": "Quito", "Peru":"Lima","Colombia":"Bogota"}
# longitud = len(paises)
# print('La longitud del diccionario es: ', longitud)

# #     14. Recorrer el diccionario con for e imprimir claves
# print("Claudia Coello")
# paises = {"Ecuador": "Quito", "Peru":"Lima","Colombia":"Bogota"}

# for i in paises.keys():
#     print(i)
#     15. Recorrer el diccionario con for e imprimir clave y valor
# print("Claudia Coello")
# paises = {"Ecuador": "Quito", "Peru":"Lima","Colombia":"Bogota"}

# for i in paises.items():
#     print(i)

# #     16. Escribir un programa que guarde en una variable el diccionario 
# # {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un 
# # mensaje de aviso si la divisa no está en el diccionario.
# print("Claudia Coello")
# monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
# divisa = input('Ingrese una divisa: ')

# if divisa in monedas:
#     print('Su símbolo es:', monedas[divisa])
# else:
#     print('La divisa no está en el diccionario')
   

#     17. Escribir un programa que pregunte al usuario su nombre, edad, dirección y
#  teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje
#  <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
direccion = input("Ingrese su direccion: ")
telefono = int(input("Ingrese su telefono: "))

persona = {'nombre' : nombre, 'edad' : edad, 'direccion' : direccion, 'telefono' : telefono}

print(f'{nombre} tiene {edad} años, vive en {direccion} y su número de teléfono es {telefono}.')
