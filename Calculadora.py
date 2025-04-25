##Realizar una calculadora que sume, reste, multiplique, divide, y potencie

print("Bienvenidos a las clase de algoritmos y estructuras de datos")
print("\nMi nombre es Claudia Coello")
print("\nCALCULADORA")

nombre = ""
numeroUno = 0
numeroDos = 0

print("Ingrese su nombre: ")
nombre = input()

print("Introduzca el primer numero")
numeroUno = int(input())

print("Introduzca el segundo numero")
numeroDos = int(input())

suma = numeroUno + numeroDos
print("La suma de los dos numeros es: ", suma)

resta = numeroUno - numeroDos
print("La resta de los dos numeros es: ", resta)

multiplicacion = numeroUno * numeroDos
print("La multiplicacion de los dos numeros es: ", multiplicacion)

division = numeroUno // numeroDos
print("La division entera de los dos numeros es: ", division)

potencia = numeroUno ** numeroDos
print("La potencia de los dos numeros es:", potencia)

modulo = numeroUno % numeroDos
print("El modulo de los dos numeros es:", potencia)