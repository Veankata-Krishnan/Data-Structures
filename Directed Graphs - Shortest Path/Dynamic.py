# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 09:48:32 2024

@author: Admin
"""

import sys
import networkx as nx
import matplotlib.pyplot as plt

# Function to implement Dynamic Programming algorithm for shortest path
def dynamic_programming_shortest_path(graph, V):
    # Create a distance matrix initialized to the input graph's adjacency matrix
    dist = [[graph[i][j] for j in range(V)] for i in range(V)]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] != sys.maxsize and dist[k][j] != sys.maxsize:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Return the final shortest distance matrix
    return dist

# Function to visualize the graph using networkx and matplotlib
def display(graph, V):
    G = nx.Graph()  # Create an undirected graph

    # Add edges to the graph with weights
    for i in range(V):
        for j in range(V):
            if graph[i][j] != 0 and graph[i][j] != sys.maxsize:  # If there's an edge from i to j
                G.add_edge(i, j, weight=graph[i][j])

    # Get edge labels (weights)
    edge_labels = {(i, j): graph[i][j] for i in range(V) for j in range(V) if graph[i][j] != 0 and graph[i][j] != sys.maxsize}

    pos = nx.spring_layout(G)  # Layout for visualization
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold', arrows=False)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Show plot
    plt.show()

# Input graph initialization
V = int(input("Enter the number of vertices (V): "))

# Create an adjacency matrix initialized to infinity for no edges
graph = [[sys.maxsize for _ in range(V+1)] for _ in range(V+1)]

# Input the adjacency matrix
print("Enter the adjacency matrix values (INF for no connection and 0 for no self loops):")
for i in range(1,V+1):
    row_input = input()
    row_values = row_input.split()
    for j in range(1,V+1):
        if row_values[j-1] == "INF":
            graph[i][j] = sys.maxsize  # No edge between i and j
        else:
            graph[i][j] = int(row_values[j - 1])  # Edge weight

# Ask the user for the source vertex
src = int(input("Enter the source vertex: "))

# Run Dynamic Programming for shortest path
dist = dynamic_programming_shortest_path(graph, V+1)

# Print the shortest distances from the source vertex
print(f"\nShortest distances from vertex {src}:")
for j in range(1,V+1):
    if dist[src][j] == sys.maxsize:
        print(f"Vertex {src} to Vertex {j}: INF (no path)")
    else:
        print(f"Vertex {src} to Vertex {j}: {dist[src][j]}")

# Visualize the directed graph
display(graph, V+1)
