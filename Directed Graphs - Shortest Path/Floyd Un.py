import sys
import networkx as nx
import matplotlib.pyplot as plt

# Function to implement Floyd's algorithm
def floyd_warshall(graph, V):
    # Create a distance matrix initialized to the input graph's adjacency matrix
    dist = [[graph[i][j] for j in range(V)] for i in range(V)]

    # Iterate over all pairs of vertices
    for k in range(V):
        for i in range(V):
            for j in range(V):
                # Update the distance if a shorter path is found through vertex k
                if dist[i][k] != sys.maxsize and dist[k][j] != sys.maxsize and dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # Return the final shortest distance matrix
    return dist

# Function to visualize the graph using networkx and matplotlib
def visualize_graph_networkx(graph, V):
    G = nx.Graph()  # Create an undirected graph

    # Add edges to the graph with weights
    for i in range(V):
        for j in range(V):
            if graph[i][j] != 0 and graph[i][j] != sys.maxsize:  # If there's an edge from i to j
                G.add_edge(i, j, weight=graph[i][j])

    # Get edge labels (weights)
    edge_labels = {(i, j): graph[i][j] for i in range(V) for j in range(V) if graph[i][j] != 0 and graph[i][j] != sys.maxsize}

    pos = nx.spring_layout(G)  # Layout for visualization
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=2000, font_size=10, font_weight='bold', arrows=False)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Show plot
    plt.show()

# Input graph initialization
V = int(input("Enter the number of vertices (V): "))

# Create an adjacency matrix initialized to infinity for no edges
graph = [[sys.maxsize for _ in range(V)] for _ in range(V)]

# Input the adjacency matrix
print("Enter the adjacency matrix values (use 0 for no self-loops, INF for no connection):")
for i in range(V):
    for j in range(i, V):  # Only fill the upper triangle for undirected graphs
        if i == j:
            graph[i][j] = 0  # Distance to self is zero
        else:
            val = input(f"Enter value for edge from {i} to {j} (INF for no connection): ")
            if val == "INF":
                graph[i][j] = sys.maxsize  # No edge between i and j
                graph[j][i] = sys.maxsize  # Symmetric for undirected graph
            else:
                graph[i][j] = int(val)  # Edge weight
                graph[j][i] = graph[i][j]  # Symmetric for undirected graph

# Ask the user for the source vertex
src = int(input("Enter the source vertex: "))

# Run Floyd's algorithm
dist = floyd_warshall(graph, V)

# Print the shortest distances from the source vertex
print(f"\nShortest distances from vertex {src}:")
for j in range(V):
    if dist[src][j] == sys.maxsize:
        print(f"Vertex {src} to Vertex {j}: INF (no path)")
    else:
        print(f"Vertex {src} to Vertex {j}: {dist[src][j]}")

# Visualize the undirected graph
visualize_graph_networkx(graph, V)
