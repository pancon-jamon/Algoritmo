#Camino minimo, necesita grafo dirigido
import heapq
grafo = {
    "A": [("B", 1), ("C", 4)],
    "B": [("C", 2), ("D", 5)],
    "C": [("D", 1)],
    "D": [],
}

def djikstra(grafo, inicio):
    distancias = {nodo: float("inf") for nodo in grafo}
    distancias[inicio] = 0
    cola = [(0,inicio)]

    while cola:
        distancia_actual, nodo_actual = heapq.heappop(cola)
        for vecino, peso in grafo[nodo_actual]:
            nueva_distancia = distancia_actual + peso
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                heapq.heappush(cola, (nueva_distancia, vecino))
    return distancias

resultado = djikstra(grafo, "A")
print("Distancias minimas desde A: ", resultado)