from CristophersTSP import christofides_tsp
from GenerateGraphs import generate_metric_complete_graph
from cristophersHandcraft import OperationCounter
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Create a complete weighted graph
max_num_nodes = 100
num_of_times = 20

cities_vs_complexity = dict()

for num_nodes in range(2,max_num_nodes):
    operations_counts = []
    for i in range(num_of_times):
        G = generate_metric_complete_graph(num_nodes, coord_range=(0, 100))
        #draw_graph(G)
        operation_counter = OperationCounter()
        # Apply Christofides' algorithm
        tsp_path, total_cost, operation_counter = christofides_tsp(G, operation_counter)
        #print("Christofides TSP Path:", tsp_path, total_cost, operation_counter.counter)
        operations_counts.append(operation_counter.counter)
        # Visualize the graph and the TSP path
        '''pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        path_edges = list(zip(tsp_path, tsp_path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)
        plt.savefig(f"Graph_path{num_nodes}.png", format="PNG")'''
        #plt.show()
    cities_vs_complexity[num_nodes] = np.mean(operations_counts)

print(cities_vs_complexity.keys(), cities_vs_complexity.values())
plt.figure(figsize=(10, 5))
plt.title('CitiesVSComplexity Cristophides')
plt.xlabel('Number of cities')
plt.ylabel('Number of operations')
#plt.plot(keys, values, marker='o')
plt.plot(list(cities_vs_complexity.keys()), list(cities_vs_complexity.values()))
plt.savefig(f"CitiesVSComplexityCristophides.png", format="PNG")
plt.show()   