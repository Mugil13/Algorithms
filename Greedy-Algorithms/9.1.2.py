def prims(adj_matrix):
    n = len(adj_matrix)
    mst = [] 
    visited = [False] * n
    visited[0] = True  
    edges = []

    for i in range(1, n):
        if adj_matrix[0][i] != 0:
            edges.append((0, i, adj_matrix[0][i]))

    while len(mst) < n - 1:
        min_edge = min(edges, key=lambda x: x[2])
        edges.remove(min_edge)
        u, v, weight = min_edge
        if not visited[v]:
            mst.append((u, v, weight))
            visited[v] = True
            for i in range(n):
                if adj_matrix[v][i] != 0 and not visited[i]:
                    edges.append((v, i, adj_matrix[v][i]))
    return mst

vertices = int(input("Enter the number of vertices: "))
print("\n")

adj_matrix = []
for i in range(vertices):
    row = []
    for j in range(vertices):
        element = int(input(f"Enter the weight from vertex {i} to vertex {j}: "))
        row.append(element)
    print("\n")
    adj_matrix.append(row)  

minimum_spanning_tree = prims(adj_matrix)
print("-----MINIMUM SPANNING TREE-----")
print("Edge \t Weight")
total_cost = 0
for u, v, weight in minimum_spanning_tree:
    print(f"{u} - {v} \t {weight}")
    total_cost += weight

print("\nThe Minimum cost is: ", total_cost)