#Funcion sin parametros
print("Claudia Coello")
def saludar():
    nombre = input("Ingrese su nombre: ")
    print(f"Hola clase de algoritmos, mi nombre es: {nombre}")

saludar()

#Funcion con un parametros
print("Claudia Coello")

def saludarConParam(nombre):
    print(f"Hola clase de algoritmos, mi nombre es: {nombre}")

nombre=input("Ingrese su nombre: ")
saludarConParam(nombre)

#Funcion con varios parametros
print("Claudia Coello")

def multiplicar(numUno, numDos):
    multiplicacion = numUno * numDos
    return multiplicacion

numUno = float(input("Ingrese el primer numero a multiplicar"))
numDos = float(input("Ingrese el segundo numero a multiplicar"))
print(f"La multiplicacion es: {multiplicar(numUno, numDos)}")

