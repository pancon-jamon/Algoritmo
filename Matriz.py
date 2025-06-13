# matriz = [[1, 2], [3, 4], [5, 6]]

# print("Imprimir por filas")
# #Recorre filas
# for fila in matriz:
#     print(fila)

# print("Imprimir por elementos")
# #recorre valores    
# for fila in matriz:
#     for elemento in fila:
#         print(elemento, end = " ")
#     print()

matriz = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]


#Mostrar todos los elementos de la matriz fila por fila
for fila in matriz:
    print(fila)

#Mostrar todos los elementos de la matriz elemento por elemento en columna
for fila in matriz:
    for elemento in fila:
        print(elemento)
    print()

#Mostrar todos los elementos de la matriz en formato de matriz
for fila in matriz:
    print(fila)

#Leer el ultimo elemento de cada fila
for fila in matriz:
    print(fila[-1])

#Generar una matriz con elementos de tipo enteros desde el teclado 
#El usuario debe especificar las filas y columnas e ingrese los valores
filas = int(input("Ingrese el numero de filas: "))
columnas = int(input("Ingrese el numero de columnas: "))

matriz = []

for fila in range(filas):
    fila = []
    for elemento in range(columnas):
        elemento = int(input("Ingrese el elemento: "))
        fila.append(elemento)
    matriz.append(fila)

#Leer la matriz
for fila in matriz:
    for elemento in fila:
        print(elemento, end = " ")
    print()
    