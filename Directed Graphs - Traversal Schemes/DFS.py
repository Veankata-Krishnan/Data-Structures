# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 21:25:01 2024

@author: Admin
"""

import networkx as nx
import matplotlib.pyplot as plt

# Function to perform DFS traversal and return traversal path
def dfs(graph, start_node):
    visited = set()
    dfs_traversal = []
    traversal_edges = []

    # Helper function for recursive DFS
    def dfs_helper(node):
        visited.add(node)
        dfs_traversal.append(node)
        
        for adjacent in graph[node]:
            if adjacent not in visited:
                traversal_edges.append((node, adjacent))
                dfs_helper(adjacent)
    
    # Start DFS from the specified starting node
    dfs_helper(start_node)
    
    # Check for disconnected nodes and perform DFS on each
    for node in graph:
        if node not in visited:
            dfs_helper(node)
    
    return dfs_traversal, traversal_edges


# Visualization function for DFS with Directed Graph
def display(graph, dfs_edges):
    G = nx.DiGraph()  # Use directed graph

    # Add nodes and directed edges to the graph
    for node, adjacents in graph.items():
        for adjacent in adjacents:
            G.add_edge(node, adjacent)
    
    pos = nx.spring_layout(G)
    
    plt.figure(figsize=(10, 6))
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
    nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='gray', arrows=True)
    nx.draw_networkx_edges(G, pos, edgelist=dfs_edges, edge_color='blue', width=2, style='dashed', arrows=True, label="DFS Path")

    plt.legend(["DFS Path"])
    plt.title("Directed Graph Traversal Visualization (DFS in Blue)")
    plt.show()

# Read graph input from user
graph = {}
V = int(input("Enter the number of vertices in the graph: "))

for i in range(V):
    vertex = input(f"Enter vertex {i+1}: ")
    adjacent_vertices = input(f"Enter the adjacent vertices of vertex {vertex} (space-separated): ").split()
    graph[vertex] = adjacent_vertices

start_node = input("Enter the starting node: ")

dfs_result,dfs_edges = dfs(graph,start_node)
print("DFS Traversal:", dfs_result)
display(graph, dfs_edges)

