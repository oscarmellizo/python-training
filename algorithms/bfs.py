from collections import deque

def bfs_shortest_bus_route(graph, start, end):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        print("1.", queue)
        current_stop, route = queue.popleft()
        print("2.", current_stop, route)
        if current_stop == end:
            return route
        
        if current_stop not in visited:
            visited.add(current_stop)
            for neighbor in graph[current_stop]:
                if neighbor not in visited:
                    queue.append((neighbor, route + [neighbor]))
                    print("3.", neighbor, queue)

# Ejemplo de uso
bus_routes = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'E'],
    'E': ['B', 'D', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['F']
}

start_stop = 'A'
end_stop = 'G'
shortest_route = bfs_shortest_bus_route(bus_routes, start_stop, end_stop)
print("La ruta de autobús más corta desde", start_stop, "a", end_stop, "es:", shortest_route)
