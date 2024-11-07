import sys
import networkx as nx
import matplotlib.pyplot as plt

# Prim's Algorithm for MST
def prim_mst(matrix):
    num_vertices = len(matrix)
    selected_nodes = [False] * num_vertices
    mst_edges = []  
    edge_count = 0  
    selected_nodes[0] = True

    while edge_count < num_vertices - 1:
        min_edge = sys.maxsize
        u, v = -1, -1

        for i in range(num_vertices):
            if selected_nodes[i]:
                for j in range(num_vertices):
                    if not selected_nodes[j] and matrix[i][j]:  
                        if matrix[i][j] < min_edge:
                            min_edge = matrix[i][j]
                            u, v = i, j

        if u != -1 and v != -1:
            selected_nodes[v] = True
            mst_edges.append((u, v, min_edge))
            edge_count += 1

    return mst_edges

# Helper function to find the root of a node (for Kruskal's Algorithm)
def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])  
    return parent[node]

# Helper function to union two subsets (for Kruskal's Algorithm)
def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)
    
    if root_u != root_v:
        if rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        elif rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

# Kruskal's Algorithm for MST
def kruskal_mst(matrix):
    num_vertices = len(matrix)
    edges = []
    
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if matrix[i][j] != 0:
                edges.append((matrix[i][j], i, j))

    edges.sort()

    parent = list(range(num_vertices))
    rank = [0] * num_vertices
    mst_edges = []

    for edge in edges:
        weight, u, v = edge
        if find(parent, u) != find(parent, v):  
            mst_edges.append((u, v, weight))
            union(parent, rank, u, v)

    return mst_edges

# Visualize MST using NetworkX and Matplotlib
def display(edges, num_vertices, title):
    G = nx.Graph()
    for u, v, weight in edges:
        G.add_edge(u, v, weight=weight)
    
    pos = nx.spring_layout(G)
    edge_labels = {(u, v): weight for u, v, weight in edges}
    
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=700, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    plt.title(title)
    plt.show()


V = int(input('Enter the no. of vertices : '))

graph = [[0]*V for _ in range(V)]
edges = []

for i in range(V):
    for j in range(i + 1, V):
        weight = int(input(f"Edge weight for ({i+1}, {j+1}): "))
        graph[i][j] = weight
        graph[j][i] = weight  # Symmetric for undirected graph
        if weight != 0:
            edges.append((i, j, weight))

    
display(edges, V, "Undirected Graph")
    # Find MST using Prim's algorithm
mst_prim = prim_mst(graph)
print("\nMST using Prim's algorithm:")
for edge in mst_prim:
    print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]}")
    
    # Visualize Prim's MST
display(mst_prim, V, "MST using Prim's Algorithm")

    # Find MST using Kruskal's algorithm
mst_kruskal = kruskal_mst(graph)
print("\nMST using Kruskal's algorithm:")
for edge in mst_kruskal:
    print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]}")
    
display(mst_kruskal, V, "MST using Kruskal's Algorithm")

