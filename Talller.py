# #TALLER:
# # 1.	Crear una función doblar valor que multiplique a un número por dos
# print("Claudia Coello")
# def doblar(num):
#     numeroDoblado = num * 2
#     return numeroDoblado

# numero = float(input("Ingrese un numero: "))
# print(f"El doble de: {numero} es {doblar(numero)}")

# #2.	Crear una función doblar valor que multiplique los elementos de una lista
# print("Claudia Coello")
# def doblarLista(lista):
#     for i, n in enumerate(lista):
#         lista[i] *= 2

# lista = [1,2,3,4,5]
# doblarLista(lista)
# print(lista)

# 3.	El ejercicio anterior pero que el usuario ingrese por teclado:

# print("Claudia Coello")

# def doblarLista(lista):
#     for i, n in enumerate(lista):
#         lista[i] *= 2

# nuevaLista = []

# while True:
#     valor = int(input("Ingrese el valor: "))
#     nuevaLista.append(valor)

#     respuesta = input("Desea continuar?(si/no): ")
#     if respuesta != 'si':
#         break
    
# doblarLista(nuevaLista)
# print(nuevaLista)

# size = int(input("Ingrese el tamano de la nueva lista: "))
# for i in range(0, size - 1):
#     numero = float(input("Ingrese el numero: "))
#     nuevaLista.append(numero)

# doblarLista(nuevaLista)
# print(nuevaLista)

# # 4.	Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, 
# # valiéndose de una función para decidirlo. 
# #            Nota: El correo se considerará válido si tiene el símbolo "@".
# print("Claudia Coello")

# def validarCorreo(correo):
#     corroborar = True
#     for arroba in correo:
#         if arroba == '@':
#             print("El correo es valido")
#             corroborar = False
#     if corroborar:
#         print("El correo es invalido")
        

# correo = str(input("Ingrese su correo electronico: "))
# validarCorreo(correo)

# # 5.	Pedir que el usuario ingrese valores hasta que ingrese el 0. 
# # Por cada valor, mostrar la suma de sus dígitos. Use una función que sume. 
# print("Claudia Coello")

# def sumarDigitos(valor):
#     suma = 0
#     while valor != 0:
#         digito = valor % 10
#         suma += digito
#         valor = valor // 10
#     return suma

# numero = int(input("Ingrese el numero: "))
# while numero != 0:
#     print("La suma de los digitos es: ", sumarDigitos(numero))
#     numero = int(input("Ingrese el numero: "))


# 6.	Determinar la suma de las coordenadas de salida, dado que un usuario ingresa las mismas por teclado.
print("Claudia Coello")

def sumaCoordenadas(x, y):
    suma

    return suma

x = int(input("Ingrese el valor para las x: "))
y = int(input("Ingrese el valor para las y: "))
# 7.	Pedir que el usuario ingrese valores hasta que ingrese el cero. Por cada valor, mostrar la suma de sus dígitos. Mediante una función realice la suma.  
# 8.	Solicitar al usuario que ingrese un número entero e imprimir en pantalla si es primo o no. Utilice una función booleana que lo decida.
# 9.	Imprimir en pantalla la cantidad de ocurrencias de un dígito que se encuentra en un número entero ingresado por el usuario.
# Nota: El usuario digitará tanto el número entero como el dígito. 
# Utilice una función que calcule la frecuencia.

# 10.	Calcular el factorial de un numero ingresado por el usuario.
# Nota: Utilice una o más funciones, según sea necesario.

# 11.	Escribir un programa que pida números al usuario, mostrar el factorial de cada uno y, al finalizar, la cantidad total de números leídos en total. 
# Nota: Utilice una o más funciones, si es necesario. 

