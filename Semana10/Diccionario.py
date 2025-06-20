#1.	Declarar el diccionario con clave y valor de los países y capitales de América Latina
print("Claudia Coello")
paises = {"Ecuador": "Quito", "Peru":"Lima","Colombia":"Bogota"}
print(paises)
#2.	Acceder a un valor del diccionario de países y capitales.
print("Claudia Coello")
print(paises["Ecuador"])

#3.	Agregar un elemento al diccionario de países y capitales.
print("Claudia Coello")
paises["Bolivia"] = "La paz"
print(paises)

#4.	Modificar un elemento del diccionario de países y capitales.
print("Claudia Coello")
paises["Bolivia"] = "Montevideo"
print(paises)

#5.	Eliminar un elemento del diccionario de países y capitales.
print("Claudia Coello")
del paises["Peru"]
print(paises)

#6.	Eliminar un elemento con la función pop
print("Claudia Coello")
paises.pop("Colombia")
print(paises)

#7.	Acceder un elemento en concreto 
print("Claudia Coello")
print(paises["Bolivia"])

#8.	Crear diccionarios con diferentes tipos de datos
print("Claudia Coello")
persona = {"Claudia" : "Nombre", "Coello" : "Apellido", 21:"edad", "Ecuador":"Pais"}
for elemento in persona:
    print(elemento)
for elemento in persona.values():
    print(elemento)
    
for elemento in persona.items():
    print(elemento)

#9.	Con valores de tipo lista
print("Claudia Coello")
semestre = {["Algoritmos", "Redes", "Arquitectura"] : "materias", [10,9,8] : "notas", ["bailar","pintar","leer"] : "pasatiempos"}
print(semestre["pasatiempos"][1])
