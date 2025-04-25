#AreaEstructuraSecuencial
#Calcular el area de un circulo pidiendo al usuario por consola el radio (pi * (radio ^2))#

print("###AREA DEL CIRCULO###")
radio = float(input("Ingrese el radio del circulo: "))

pi = 3.1416
area = pi * ( radio ** 2)

print("El area es: ", round(area,2))