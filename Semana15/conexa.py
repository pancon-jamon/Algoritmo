#DFS para contar componentes conexas
from collections import deque
grafo = {
    "A" : ["B"],
    "B" : ["A"],
    "C" : ["D"],
    "D" : ["C"]
}

def contarComponente(grafo):
    visitados = set()
    componentes = 0

    def dfs(nodo):
        visitados.add(nodo)
        for vecino in grafo[nodo]:
            if vecino not in visitados:
                dfs(vecino)

    for nodo in grafo:
        if nodo not in visitados:
            dfs(nodo)
            componentes += 1
    return componentes

print("Componentes conexos: ", contarComponente(grafo))