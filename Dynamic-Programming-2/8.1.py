INF = float('inf')

def floyd_warshall(graph):
    V = len(graph)

    dist = [row[:] for row in graph] 

    # Floyd-Warshall algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] != INF and dist[k][j] != INF and dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

V = int(input("Enter the number of vertices: "))
print("-----ADJACENCY MATRIX-----")
graph = []
for i in range(V):
    row = []
    for j in range(V):
        weight_input = input(f"Enter weight from vertex {i} to vertex {j} (enter 'INF' for infinity): ")
        if weight_input.upper() == 'INF':
            weight = INF
        else:
            weight = int(weight_input)
        row.append(weight)
    graph.append(row)

result = floyd_warshall(graph)

print("-----SHORTEST PATH MATRIX-----")
for i in range(V):
    for j in range(V):
        if result[i][j] == INF:
            print('INF', end='\t')
        else:
            print(result[i][j], end='\t')
    print()
