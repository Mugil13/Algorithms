def min_distance(distance, visited):
    min_dist = float('inf')
    min_vertex = -1
    for v in range(len(distance)):
        if not visited[v] and distance[v] < min_dist:
            min_dist = distance[v]
            min_vertex = v
    return min_vertex

def dijkstra(graph, source):
    n = len(graph)
    visited = [False] * n
    distance = [float('inf')] * n
    distance[source] = 0
    predecessor = [-1] * n

    for _ in range(n):
        u = min_distance(distance, visited)
        visited[u] = True
        for v in range(n):
            if graph[u][v] != 0 and not visited[v]:
                new_dist = distance[u] + graph[u][v]
                if new_dist < distance[v]:
                    distance[v] = new_dist
                    predecessor[v] = u  

    return distance, predecessor
    
def printSolution(distance, predecessor, source):
    print("Vertex \t Shortest Distance from Source \t\t Path")
    for i in range(len(distance)):
        if distance[i] == float('inf'):
            print(f"{i} \t\t\t {distance[i]} \t\t\t No path")
        else:
            print(f"{i} \t\t\t {distance[i]} \t\t\t {get_path(predecessor, i, source)}")

def get_path(predecessor, vertex, source):
    path = []
    current = vertex
    while current != -1:
        path.append(current)
        current = predecessor[current]
    path.reverse()
    return ' -> '.join(map(str, path))

vertices = int(input("Enter the number of vertices: "))
source_vertex = int(input("Enter the source vertex: "))

print("\n")
adj_matrix = []
for i in range(vertices):
    row = []
    for j in range(vertices):
        element = int(input(f"Enter the weight from vertex {i} to vertex {j}: "))
        row.append(element)
    print("\n")
    adj_matrix.append(row)

shortest_distance, predecessor = dijkstra(adj_matrix, source_vertex)
printSolution(shortest_distance, predecessor, source_vertex)
