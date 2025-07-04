def merge_sort(lista, nivel=0, corrida=[0]):
    corrida[0] += 1
    num_corrida = corrida[0]
    espacio = "  " * nivel
    
    print(f"\n{espacio} CORRIDA #{num_corrida}")
    print(f"{espacio} Entrada: {lista}")
    
    if len(lista) > 1:
        mitad = len(lista)//2
        mitad1 = lista[:mitad]
        mitad2 = lista[mitad:]
        
        print(f"{espacio} Dividiendo: {mitad1} | {mitad2}")
        
        merge_sort(mitad1, nivel+1, corrida)
        merge_sort(mitad2, nivel+1, corrida)
        
        i = j = k = 0
        
        print(f"{espacio} Fusionando...")
        
        while i < len(mitad1) and j < len(mitad2):
            if mitad1[i] < mitad2[j]:
                lista[k] = mitad1[i]
                i += 1
            else:
                lista[k] = mitad2[j]
                j += 1
            k += 1
        
        while i < len(mitad1):
            lista[k] = mitad1[i]
            i += 1
            k += 1
        
        while j < len(mitad2):
            lista[k] = mitad2[j]
            j += 1
            k += 1
        
        print(f"{espacio} Resultado parcial: {lista}")

# Lista a ordenar
numeros = [12, 4, 15, 2, 7, 1, 8, 4, 9, 3]

# Proceso
print("\n" + "="*50)
print(" INICIO DE MERGE SORT")
print(f"Lista original: {numeros}")
print("="*50)

merge_sort(numeros)

print("\n" + "="*50)
print(f"ORDENACIÓN COMPLETADA")
print(f"Lista ordenada: {numeros}")
print(f"Total de corridas: {numeros[-1]}")  # Usamos el último elemento del contador
print("="*50)