import networkx as nx
import matplotlib.pyplot as plt
import itertools
import random
import math
from GenerateGraphs import *
from cristophersHandcraft import kruskal_mst, OperationCounter, subgraph, min_weight_matching, eulerian_circuit_handcraft

def draw_graph(G, path=None):
    """
    Draws the graph with edge weights and highlights a given path.

    Parameters:
    - G (networkx.Graph): The graph to be drawn.
    - path (list): A list of nodes representing the path to be highlighted (optional).
    """
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    labels = nx.get_edge_attributes(G, 'weight')
    rounded_labels = {k: round(v, 2) for k, v in labels.items()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=rounded_labels)
    
    if path is not None:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

    plt.show()
    


def minimum_spanning_tree(G, operation_counter):
    mst_handcraft, operation_counter = kruskal_mst(G, operation_counter)
    mst_networkx = nx.minimum_spanning_tree(G, weight='weight')
    return mst_handcraft, operation_counter

def odd_degree_vertices(G, operation_counter):
    odd_ver_list = []
    for v,d in G.degree():
        operation_counter.count()
        if d%2 == 1:
            operation_counter.count()
            odd_ver_list.append(v)
    

    #res = [v for v, d in G.degree() if d % 2 == 1]

    return odd_ver_list, operation_counter

def minimum_weight_perfect_matching(G, odd_vertices, operation_counter):
    subgraph = G.subgraph(odd_vertices)
    matching = nx.algorithms.matching.min_weight_matching(subgraph, weight='weight')

    #subgraph_hand, operation_counter = subgraph(G, odd_vertices, operation_counter)
    #matching_hand, operation_counter = min_weight_matching(G, odd_vertices, operation_counter)
    return matching, operation_counter


def eulerian_circuit_handcraft(multigraph, operation_counter):
    #res_eulerian = list(eulerian_circuit_handcraft(multigraph, operation_counter))
    res_eulerian = list(nx.eulerian_circuit(multigraph))
    for _ in range(len(res_eulerian)):
        operation_counter.count()
    return res_eulerian, operation_counter#list(nx.eulerian_circuit(multigraph))

def christofides_tsp(G, operation_counter):
    # Step 1: Minimum Spanning Tree (MST)
    mst, operation_counter = minimum_spanning_tree(G, operation_counter)
    
    # Step 2: Find vertices with odd degree in MST
    odd_vertices, operation_counter = odd_degree_vertices(mst, operation_counter)
    
    # Step 3: Minimum Weight Perfect Matching (MWPM) on odd degree vertices
    matching, operation_counter = minimum_weight_perfect_matching(G, odd_vertices, operation_counter)
    
    # Step 4: Combine MST and MWPM to create an Eulerian multigraph
    multigraph = nx.MultiGraph(mst)
    for u, v in matching:
        multigraph.add_edge(u, v, weight=G[u][v]['weight'])
    
    # Step 5: Find an Eulerian circuit in the multigraph
    euler_circuit, operation_counter = eulerian_circuit_handcraft(multigraph, operation_counter)
    
    # Step 6: Convert the Eulerian circuit to a Hamiltonian circuit (TSP tour)
    tsp_path = []
    visited = set()
    for u, v in euler_circuit:
        operation_counter.count()
        if u not in visited:
            operation_counter.count()
            tsp_path.append(u)
            operation_counter.count()
            visited.add(u)
    tsp_path.append(tsp_path[0])  # Returning to the start
    operation_counter.count()
    
    total_cost = sum(G[tsp_path[i]][tsp_path[i + 1]]['weight'] for i in range(len(tsp_path) - 1))
    for _ in range(len(tsp_path)):
        operation_counter.count()
    return tsp_path, total_cost, operation_counter



