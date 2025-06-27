# #Iterar una tupla
# print("Claudia Coello")
# lista = [1,2,3]
# tupla = tuple(lista)

# for i in tupla:
#     print(i)
# #2.	Anidar tuplas. Acceder al elemento ‘a’
# print("Claudia Coello")
# tupla = 1, 2, ('a', 'b'), 3
# elemento = tupla[2][0]
# print(elemento)
# #3.	Asignar el valor de una tupla con n elementos a n variables.
# print("Claudia Coello")
# tupla = (1, 2, 3)
# a,b,c = tupla
# print(a)
# print(b)
# print(c)
# #Contar el numero de veces que se repite un elemento en la tupla
# print("Claudia Coello")
# tupla = (1, 1, 1, 3, 5)
# print(tupla.count(1))

# #5.	Verificar la posición de un elemento:
# # index(<obj>[,index]) : permite buscar el índice del primer elemento que coincida con un valor específico, a partir de una posición determinada.

# # Con un parámetro
# print("Claudia Coello")
# tupla = (7, 7, 7, 3, 5)
# print(tupla.index(7,2))
# #7.	Imprimir el apellido y el nombre
# print("Claudia Coello")
# nombres = ("Claudia", "Coello")
# nombre, apellido = nombres
# print(f"{nombre}, {apellido}")

# #8.	Imprimir el orden de llegada de los atletas (enumerate)
# print("Claudia Coello")
# atletas = ("Lorena Chulde", "Juan Perez", "Maria Mera", "Pedro Robayo")

# for atleta in enumerate(atletas, + 1):
#     print("Orden", atleta[0],"atleta:",atleta[1])

# #9.	Verificar que es un objeto enumerate

# atletas = ("Lorena Chulde", "Juan Perez", "Maria Mera", "Pedro Robayo")
# posicion = enumerate(atletas)
# print(posicion)

# #10.	Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite. Usando count
# print("Claudia Coello")
# numeros = (5,4,3,2,1,6,45,6,7,8,9,2,6,3,2,1,6,7)
# numero = int(input("Ingrese un numero: "))
# print(numeros.count(numero))

# #11.	Crea una tupla con números e indica el numero con mayor valor y el que menor tenga. Usando max, min
# print("Claudia Coello")
# numeros = (5,4,3,2,1,6,45,6,7,8,9,2,6,3,2,1,6,7) 
# print(max(numeros))
# print(min(numeros))
# #12.	Crea una tupla con valores ya predefinidos del 1 al 10, pide un índice por teclado y muestra el valor de la tupla.
# print("Claudia Coello")
# tupla = (1,2,3,4,5,6,7,8,9,10)
# indice = int(input("Ingrese un indice: "))
# print(tupla[indice])
# #13.	Convertir una lista en tupla haciendo uso de al función tuple().
# print("Claudia Coello")
# lista = [6, 7, 8, 9, 10]
# listaTupla = tuple(lista)
# print(listaTupla)
# #Encontrar el numero mayor y menor en una tupla
# print("Claudia Coello")
# numeros = (5,4,3,2,1,6,45,6,7,8,9,2,6,3,2,1,6,7) 
# numMayor = numeros[0]
# numMenor = numeros[0]
# for i in range(1, len(numeros)):
#     if numeros[i] > numMayor:
#         numMayor = numeros[i]

# for i in range(1, len(numeros)):
#     if numeros[i] < numMenor:
#         numMenor = numeros[i]
# print("El mayor es: ", numMayor)
# print("El menor es: ", numMenor)
# #15.	Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la 
# # longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error.
# #El programa termina cuando el usuario introduce un cero.
# print("Claudia Coello")
# meses_del_year = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre','Octubre', 'Noviembre', 'Diciembre')
# def mostrarMeses():
#     numero = 0
#     numeroMeses = len(meses_del_year)
#     while True:
#         try:
#             numero = int(input(f"Ingrese un numero entre 1 y {numeroMeses} o 0 para salir: "))

#             if numero > len(meses_del_year) or numero < 0:
#                 raise ValueError (f"Error ingrese un numero entre 1 y {numeroMeses} o 0 para salir: ")
            
#             if numero == 0:
#                 break

#             print("Mes: ",meses_del_year[numero - 1])
            
#         except Exception as e:
#             print("Error:", e)
        

# mostrarMeses()
# # 16. Crea una función que reciba una tupla de números y devuelva la suma de todos sus elementos.
# print("Claudia Coello")
# tupla = (1,2,3,4,5)

# def sumaElementosTupla(tupla):
#     suma = 0
#     for i in tupla:
#         suma += i

#     return suma

# print(tupla)
# print(f"La suma de sus elementos es: {sumaElementosTupla(tupla)}")


# 17. Crea una función que reciba una tupla de números y devuelva una nueva tupla con el valor 
# mínimo y máximo.
# print("Claudia Coello")
# tupla = (10,1,20,13,4,5)

# def minMaxTupla(tupla):
#     tuplaMinMax = (min(tupla), max(tupla))

#     return tuplaMinMax

# tuplaMinMax = minMaxTupla(tupla)
# print(tuplaMinMax)

# 18. Crea una función que reciba una tupla y un valor, y retorne cuántas veces aparece ese valor en la tupla.

def aparicionesEnTupla(tupla, numero):
    contador = 0
    for i in tupla:
        if i == numero:
            contador += 1
    return contador

tupla = (1,1,2,5,8,5,8)
numeroApariciones = aparicionesEnTupla(tupla, int(input("Ingrese un numero para contar la cntidad de veces que aparece: ")))
print(tupla)
print(f"El numero de apariciones en la tupla es: {numeroApariciones}")
