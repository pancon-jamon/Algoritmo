grafo = {
    "A" : ["B", "C"],
    "B" : ["D"],
    "C" : ["D"],
    "D" : []
}

def topo_sort(grafo):
    visitados = set()
    orden = []

    def dfs(nodo):
        visitados.add(nodo)
        for vecino in grafo[nodo]:
            if vecino not in visitados:
                dfs(vecino)
        orden.append(nodo)
    for nodo in grafo:
        if nodo not in visitados:
            dfs(nodo)
    return orden[::-1]

print("Orden topologico: ", topo_sort(grafo))