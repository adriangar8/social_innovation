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

# Example usage
num_nodes = 6
G = generate_metric_complete_graph(num_nodes, coord_range=(0, 100))
draw_graph(G)

# Optionally, you can apply TSP algorithms here and visualize the result
# For example, using the previously defined Christofides' algorithm:
def christofides_tsp(G):
    def minimum_spanning_tree(G):
        return nx.minimum_spanning_tree(G, weight='weight')

    def odd_degree_vertices(G):
        return [v for v, d in G.degree() if d % 2 == 1]

    def minimum_weight_perfect_matching(G, odd_vertices):
        subgraph = G.subgraph(odd_vertices)
        matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')
        return matching

    def eulerian_circuit(multigraph):
        return list(nx.eulerian_circuit(multigraph))

    # Step 1: Minimum Spanning Tree (MST)
    mst = minimum_spanning_tree(G)
    
    # Step 2: Find vertices with odd degree in MST
    odd_vertices = odd_degree_vertices(mst)
    
    # Step 3: Minimum Weight Perfect Matching (MWPM) on odd degree vertices
    matching = minimum_weight_perfect_matching(G, odd_vertices)
    
    # Step 4: Combine MST and MWPM to create an Eulerian multigraph
    multigraph = nx.MultiGraph(mst)
    for u, v in matching:
        multigraph.add_edge(u, v, weight=G[u][v]['weight'])
    
    # Step 5: Find an Eulerian circuit in the multigraph
    euler_circuit = eulerian_circuit(multigraph)
    
    # Step 6: Convert the Eulerian circuit to a Hamiltonian circuit (TSP tour)
    tsp_path = []
    visited = set()
    for u, v in euler_circuit:
        if u not in visited:
            tsp_path.append(u)
            visited.add(u)
    tsp_path.append(tsp_path[0])  # Returning to the start
    
    return tsp_path

tsp_path = christofides_tsp(G)
print("Christofides TSP Path:", tsp_path)
draw_graph(G, tsp_path)