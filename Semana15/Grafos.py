from collections import deque
grafo = {
    "A" : ["B", "C"],
    "B" : ["A", "D"],
    "C" : ["A", "D"],
    "D" : ["B", "C"]
}

def mostrar_grafo(grafo):
    print("Grafo: ")
    for nodo in grafo:
        print(f"{nodo} => {grafo[nodo]}")

print("Recorrido de grafos por anchura")
def bfs(grafo, inicio):
    print(f"Recorrido BFS desde {inicio}: ")
    visitados = set()
    cola = deque([inicio])

    while cola:
        nodo = cola.popleft()
        if nodo not in visitados:
            print(nodo, end=" ")
            visitados.add(nodo)
            for vecino in grafo:
                if vecino not in visitados and vecino not in cola:
                    cola.append(vecino)
            print()

bfs(grafo, "A")

print("Recorrido de grafos profundidad")
def dfs(grafo, nodo, visitados = None):#preorden y usa pila
    if visitados is None:
        visitados = set()
    print(nodo, end=" ")
    visitados.add(nodo)
    for vecino in grafo[nodo]:
        if vecino not in visitados:
            dfs(grafo, vecino, visitados)

dfs(grafo, "A")

