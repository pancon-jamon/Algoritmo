#Compara dos elementos de la lista adyacentes y los compara, si el elemento actual es mayor al siguiente se
# intercambian hasta quedar ordenada
def ordenar(lista):
    size = len(lista)
    for i in range(0,size - 1):
        for j in range(0, size - 1):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    return lista

numero = [6,3,8,2,7]
print("La lista original es: ", numero)
print("La lista ordenada es: ",ordenar(numero))
#Analizar y explicar paso a paso en qué consiste el Algoritmo de ordenamiento por Selección. 
# Realizar la prueba de escritorio.
#Divide la funcion en dos, la parte ordenada y la desordenada, busca el elemento mas
# pequeno en esta ultima y lo coloca al final de la parte ordenada, asi va construyendo una
#lista ordenada
def seleccion_sort(lista):
    for i in range(len(lista)):#Recorre toda la lista
        minimo = i#Supone que el primer elemento es el menor
        for j in range(i,len(lista)):#Recorre la lista desordenada buscando el menor
            if(lista[j] < lista[minimo]):#Si encuentra un numero menor guarda su posicion
                minimo = j
        if(minimo != i):#Si el actual no es el minimo, intercambian
            aux = lista[i]
            lista[i] = lista[minimo]
            lista[minimo] = aux
    print(lista)

lista = [6,5,3,1,8,7,2,4]
print("Antes")
print(lista)
print("Despues")
seleccion_sort(lista)

def insertion_sort(lista):
    for i in range(1, len(lista)):# Empieza desde el segundo elemento (índice 1)
        valorActual = lista[i]# Guarda el valor actual para compararlo
        posicion = i - 1# Posición del elemento anterior (parte ordenada)

        while posicion >= 0 and lista[posicion] > valorActual:# Mueve los elementos mayores que `valorActual` una posición adelante
            lista[posicion + 1] = lista[posicion]  # Desplaza el elemento mayor
            posicion -= 1                          # Retrocede para comparar con el anterior

        lista[posicion + 1] = valorActual# Inserta `valorActual` en su posición correcta

    return lista

numeros = [8,4,2,9,5]
print('Lista desordenada: ',numeros)
ordenados = insertion_sort(numeros)
print('Lista ordenada: ',ordenados)
