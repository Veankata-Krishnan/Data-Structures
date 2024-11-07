# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 08:08:47 2024

@author: Admin
"""

import sys
import networkx as nx 
import matplotlib.pyplot as plt

# Function to find the vertex with minimum distance value
def min_distance(dist, spt_set, V):
    min_val = sys.maxsize
    min_index = -1
    for v in range(1,V):
        if dist[v] < min_val and not spt_set[v]:
            min_val = dist[v]
            min_index = v
    return min_index

# Dijkstra's algorithm function
def dijkstra(graph, src, V):
    dist = [sys.maxsize] * V  # Initialize distances to infinity
    dist[src] = 0  # Distance to the source is 0
    spt_set = [False] * V  # Shortest path set
    parent = [-1] * V  # Array to store the shortest path tree

    for _ in range(V):
        u = min_distance(dist, spt_set, V)  # Get the minimum distance vertex
        spt_set[u] = True  # Mark the vertex as processed

        # Update the distance values of the adjacent vertices
        for v in range(1,V):
            if graph[u][v] and not spt_set[v] and dist[u] != sys.maxsize and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]
                parent[v] = u  # Set parent of v to u


    # Print the calculated shortest distances
    print("\nDestination Vertex \t Distance from Source")
    for i in range(1,V):
        if dist[i] == sys.maxsize:
            print(i,"\t\t\t\t\t INF")
        else:
            print_path(parent, parent[j])
            print(i, "\t\t\t\t\t", dist[i])

# Function to print the path
def print_path(parent, j):
    if parent[j] == -1:  # Base case: source vertex has no parent
        print(j, end=" ")
        return
    print_path(parent, parent[j])
    print(j, end=" ")
    
# Function to visualize the directed graph 
def display(graph, V):
    G = nx.DiGraph()  # Create a directed graph
    # Add edges to the graph with weights
    for i in range(1,V):
        for j in range(1,V):
            if graph[i][j] != 0 and graph[i][j] != sys.maxsize:  # If there's an edge from i to j
                G.add_edge(i, j, weight=graph[i][j])

    # Get edge labels (weights)
    edge_labels = {(i, j): graph[i][j] for i in range(1,V) for j in range(1,V) if graph[i][j] != 0 and graph[i][j] != sys.maxsize}

    pos = nx.spring_layout(G)  # Layout for visualization
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold', arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Show plot
    plt.show() 

# User input for the graph in matrix form (one by one)
V = int(input("Enter the number of vertices (V): "))

graph = [[sys.maxsize for _ in range(1,V+1)] for _ in range(1,V+1)]  # Initialize an m x m matrix

# Input the adjacency matrix
print("Enter the adjacency matrix values (INF for no connection and 0 for no self loops):")
for i in range(1,V+1):
    row_input = input()
    row_values = row_input.split()
    for j in range(1,V+1):
        if row_values[j-1] == "INF":
            graph[i][j] = sys.maxsize  # No edge between i and j
        else:
            graph[i][j] = int(row_values[j-1])  # Edge weight
                
src = int(input("\nEnter the source vertex: "))

#Dijkstra's algorithm
dijkstra(graph, src, V+1)

# Visualize the directed graph using networkx
display(graph, V+1)