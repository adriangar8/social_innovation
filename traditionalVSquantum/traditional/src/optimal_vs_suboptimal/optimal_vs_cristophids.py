from CristophersTSP import christofides_tsp
from GenerateGraphs import generate_metric_complete_graph
from cristophersHandcraft import OperationCounter
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from optimal_solution_algo import *

# Create a complete weighted graph
max_num_nodes = 25
num_of_times = 10

cities_vs_cost_opt = dict()
cities_vs_cost_cris = dict()
error_dict = dict()

path_cost = 0
operations_counts = []
for num_nodes in range(2,max_num_nodes):
    
    
    G = generate_metric_complete_graph(num_nodes, coord_range=(0, 100))
    
    operation_counter_cris = OperationCounter()
    operation_counter_opt = OperationCounter()

    tsp_path, cris_cost, operation_counter = christofides_tsp(G, operation_counter_cris)
    opt_cost, opt_path = held_karp(G, operation_counter_opt)

    operations_counts.append(operation_counter.counter)
    print("Christofides TSP Path:", tsp_path, cris_cost, operation_counter.counter)
    print("Optimal TSP Path:", opt_path, opt_cost, operation_counter.counter)
    cities_vs_cost_opt[num_nodes] = opt_cost
    cities_vs_cost_cris[num_nodes] = cris_cost
    error_dict[num_nodes] = abs(cris_cost - opt_cost)/opt_cost * 100
    

print(error_dict.keys(), error_dict.values())
#plt.figure(figsize=(10, 5))
fig, ax = plt.subplots(figsize=(12, 6))

plt.title('CitiesVSCost')
plt.xlabel('Number of cities')
plt.ylabel('Travelling cost')

#plt.plot(keys, values, marker='o')
ax.plot(list(cities_vs_cost_opt.keys()), list(cities_vs_cost_opt.values()), label="Optimal")
ax.plot(list(cities_vs_cost_cris.keys()), list(cities_vs_cost_cris.values()), label="Cristophides")
bars = ax.bar(list(error_dict.keys()),list(error_dict.values()),color='red', label="Error")
# Add labels to each bar
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.1f}%', ha='center', va='bottom')
plt.legend()
plt.savefig(f"CitiesVSComplexityCristophides.png", format="PNG")
plt.show() 