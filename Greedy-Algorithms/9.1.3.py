def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def apply_union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskals(vertices, graph):
    minimum_spanning_tree = []
    i, e = 0, 0
    edges = []
    for u in range(vertices):
        for v in range(vertices):
            if graph[u][v] != 0:
                edges.append([u, v, graph[u][v]])
    edges = sorted(edges, key=lambda item: item[2])
    parent = []
    rank = []
    for node in range(vertices):
        parent.append(node)
        rank.append(0)
    while e < vertices - 1:
        u, v, w = edges[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            e = e + 1
            minimum_spanning_tree.append([u, v, w])
            apply_union(parent, rank, x, y)
    
    return minimum_spanning_tree
    
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

minimum_spanning_tree = kruskals(vertices, adj_matrix)

print("-----MINIMUM SPANNING TREE-----")
print("Edge \t Weight")
total_cost = 0
for u, v, weight in minimum_spanning_tree:
    print(f"{u} - {v} \t {weight}")
    total_cost += weight

print("\nThe Minimum cost is: ", total_cost)
