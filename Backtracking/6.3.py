def is_safe(v, graph, color, c):
    for i in range(len(graph)):
        if graph[v][i] and c == color[i]:
            return False
    return True

def graph_coloring(graph, k, color, v):
    if v == len(graph):
        return True
    
    for c in range(1, k + 1):
        if is_safe(v, graph, color, c):
            color[v] = c
            if graph_coloring(graph, k, color, v + 1):
                return True  
            color[v] = 0
    return False

def color_graph(graph, k):
    color = [0] * len(graph)
    if not graph_coloring(graph, k, color, 0):
        print("No solution exists.")
    else:
        print("Graph coloring possible with at most", k, "colors.")
        print("Coloring:", color)

k = 3 # Number of colors
print("The maximum number of colours is: ", k)
graph1 = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

print("\nAdjacency matrix is: ", graph1)
color_graph(graph1, k)   

graph2 = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]

print("\nAdjacency matrix is: ", graph2)
color_graph(graph2, k)   

graph3 = [
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0]
]

print("\nAdjacency matrix is: ", graph3)
color_graph(graph3, k)   
