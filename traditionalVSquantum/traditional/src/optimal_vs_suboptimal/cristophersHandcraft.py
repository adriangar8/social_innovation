import networkx as nx


class OperationCounter:
    def __init__(self):
        self.counter = 0

    def count(self):
        self.counter += 1


def kruskal_mst(G, counter):
    mst = nx.Graph()
    subtrees = {v: v for v in G.nodes()}
    
    def find(v):
        while v != subtrees[v]:
            counter.count()
            v = subtrees[v]
        return v
    
    def union(v1, v2):
        root1 = find(v1)
        root2 = find(v2)
        if root1 != root2:
            counter.count()
            subtrees[root2] = root1
    
    edges = sorted(G.edges(data=True), key=lambda e: e[2]['weight'])
    for u, v, data in edges:
        counter.count()  # Counting edge processing
        if find(u) != find(v):
            union(u, v)
            mst.add_edge(u, v, weight=data['weight'])
            counter.count()  # Counting edge addition to MST
            
    return mst, counter

def subgraph(G, vertices, operation_counter):
    """
    Returns the subgraph induced by the specified vertices.

    Parameters:
    - G (dict): The graph represented as a dictionary of adjacency lists.
    - vertices (list): List of vertices to include in the subgraph.

    Returns:
    - subgraph (dict): The induced subgraph represented as a dictionary of adjacency lists.
    """
    subgraph = {v: {} for v in vertices}
    for v in vertices:
        for neighbor, weight in G[v].items():
            operation_counter.count()
            if neighbor in vertices:
                subgraph[v][neighbor] = weight
                operation_counter.count()
    return subgraph, operation_counter

def min_weight_matching(G, odd_vertices, operation_counter):
    """
    Finds a minimum weight perfect matching on the odd degree vertices of the graph.

    Parameters:
    - G (dict): The graph represented as a dictionary of adjacency lists.
    - odd_vertices (list): List of vertices with odd degree.

    Returns:
    - matching (list): List of edges representing the minimum weight perfect matching.
    """
    matching = []
    used = set()
    print(odd_vertices)
    for u in odd_vertices:
        operation_counter.count()
        
        if u not in used:
            min_weight = float('inf')
            min_v = None
            for v in odd_vertices:
                operation_counter.count()
                print("Weights",G)
                print("Weights",G[u][v]['weight'])
                if u != v and v not in used and G[u][v]['weight'] < min_weight:
                    operation_counter.count()
                    min_weight = G[u][v]
                    operation_counter.count()
                    min_v = v
            matching.append((u, min_v))
            operation_counter.count()
            used.add(u)
            operation_counter.count()
            used.add(min_v)
            operation_counter.count()
    return matching, operation_counter


def eulerian_circuit_handcraft(G, opeartaion_counter):
    """
    Finds an Eulerian circuit in the multigraph using Fleury's algorithm.

    Parameters:
    - G (dict): The graph represented as a dictionary of adjacency lists.

    Returns:
    - circuit (list): List of edges representing the Eulerian circuit.
    """
    def dfs(u, circuit):
        while adj_list[u]:
            opeartaion_counter.count()
            v = adj_list[u].pop()
            if (u, v) in edges or (v, u) in edges:
                opeartaion_counter.count()
                edges.remove((u, v) if (u, v) in edges else (v, u))
                dfs(v, circuit)

        opeartaion_counter.count()
        circuit.append(u)

    # Construct adjacency lists and set of edges
    adj_list = {v: list(G[v].keys()) for v in G}
    for _ in len(adj_list.items()):
        opeartaion_counter.count()
    edges = {(u, v) for u in G for v in G[u]}
    for _ in len(edges.items()):
        opeartaion_counter.count()

    # Find a vertex with odd degree (start)
    start = next(iter(G))
    for v in G:
        opeartaion_counter.count()
        if len(G[v]) % 2 == 1:
            opeartaion_counter.count()
            start = v
            break

    # Perform depth-first search to find the Eulerian circuit
    circuit = []
    dfs(start, circuit)

    # Reverse the circuit to get the correct order
    circuit.reverse()
    for _ in len(circuit):
        opeartaion_counter.count()


    # Construct the list of edges representing the circuit
    circuit_edges = [(circuit[i], circuit[i + 1]) for i in range(len(circuit) - 1)]
    for _ in len(circuit_edges):
        opeartaion_counter.count()

    return circuit_edges, opeartaion_counter
