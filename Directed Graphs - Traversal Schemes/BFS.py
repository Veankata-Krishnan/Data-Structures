import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Function to perform BFS traversal and return traversal path
def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    bfs_traversal = []
    traversal_edges = []  

    visited.add(start_node)
    
    while queue:
        node = queue.popleft()
        bfs_traversal.append(node)
        
        for adjacent in graph[node]:
            if adjacent not in visited:
                visited.add(adjacent)
                queue.append(adjacent)
                traversal_edges.append((node, adjacent))  
    
    return bfs_traversal, traversal_edges

# Visualization function for BFS
def display(graph, bfs_edges):
    G = nx.DiGraph()  
    for node, adjacents in graph.items():
        for adjacent in adjacents:
            G.add_edge(node, adjacent)
    
    pos = nx.spring_layout(G)
    
    plt.figure(figsize=(10, 6))
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
    nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='gray', arrows=True)
    nx.draw_networkx_edges(G, pos, edgelist=bfs_edges, edge_color='red', width=2, arrows=True, label="BFS Path")

    plt.legend(["BFS Path"])
    plt.title("Directed Graph Traversal Visualization (BFS in Red)")
    plt.show()

# Read graph input from user
graph = {}
V = int(input("Enter the number of vertices in the graph: "))

for i in range(V):
    vertex = input(f"Enter vertex {i+1}: ")
    adjacent_vertices = input(f"Enter the adjacent vertices of vertex {vertex} (space-separated): ").split()
    graph[vertex] = adjacent_vertices

# Get the starting node for BFS
start_node = input("Enter the starting node for BFS traversal: ")

# Perform BFS from the starting node
bfs_result, bfs_edges = bfs(graph, start_node)

print("BFS Traversal:", bfs_result)

# Visualize the graph with BFS traversal path
display(graph, bfs_edges)
