#      A
#     / \
#    B   C
#   / \   \
#  D   E   F 
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': None,
    'E': None,
    'F': None
}
def dfs(grafo, nodo_actual):
    if grafo[nodo_actual]:
        for vecino in grafo[nodo_actual]:
            dfs(grafo, vecino)
    print(nodo_actual, end=' ')

nodo_actual = 'A'

print("Recorrido DFS desde el nodo", nodo_actual)
dfs(grafo, nodo_actual)