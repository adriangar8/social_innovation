import networkx as nx
import random
import matplotlib.pyplot as plt
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def generate_metric_complete_graph(num_nodes, coord_range=(0, 100)):
    """
    Generates a complete graph with nodes embedded in a 2D Euclidean space.

    Parameters:
    - num_nodes (int): Number of nodes in the graph.
    - coord_range (tuple): The range (min, max) for the node coordinates.

    Returns:
    - G (networkx.Graph): A complete graph with Euclidean distances as weights.
    """
    G = nx.complete_graph(num_nodes)
    positions = {i: (random.uniform(*coord_range), random.uniform(*coord_range)) for i in G.nodes()}
    nx.set_node_attributes(G, positions, 'pos')

    for (u, v) in G.edges():
        G[u][v]['weight'] = euclidean_distance(positions[u], positions[v])
    
    return G