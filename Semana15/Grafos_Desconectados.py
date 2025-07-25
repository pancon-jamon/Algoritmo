from collections import deque
grafo = {
    "A" : ["B"],
    "B" : ["A"],
    "C" : ["D"],
    "D" : ["C"]
}

def verificarCamino(grafo, origen, destino):
    visitados = set()
    cola = deque([origen])

    while cola:
        nodo = cola.popleft()
        if nodo == destino:
            return True
        visitados.add(nodo)
        for vecino in grafo[nodo]:
            if vecino not in visitados and vecino not in cola:
                cola.append(vecino)
    return False

def bfsDesconectado(grafo, inicio):
    visitados = set()
    cola = deque([inicio])

    while cola:
        nodo = cola.popleft()
        if nodo not in visitados:
            print(nodo, end=" ")
            visitados.add(nodo)  
        for vecino in grafo[nodo]:
            if vecino not in visitados and vecino not in cola:
                cola.append(vecino) 
        print()

print("Recorrido grafo desde cada nodo, incluso del nodo desconectado")
for nodo in grafo:
    print(f"FBS desde {nodo}")
    bfsDesconectado(grafo, "A")

print("Hay camino entre A y D?", verificarCamino(grafo, "A", "D"))
print("Hay camino entre A y B?", verificarCamino(grafo, "A", "B"))
print("Hay camino entre C y D?", verificarCamino(grafo, "C", "D"))
print("Hay camino entre B y C?", verificarCamino(grafo, "B", "C"))