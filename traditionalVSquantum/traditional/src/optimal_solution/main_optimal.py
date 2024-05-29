from GenerateGraphs import *
from optimal_solution_algo import *
from estimation_optimal import print_estimation


# Create a weighted graph
max_num_nodes = 20

cities_vs_complexity = dict()

for num_nodes in range(2, max_num_nodes):
    G = generate_metric_complete_graph(num_nodes, coord_range=(0, 100))
    operation_counter = OperationCounter()
    opt_cost, opt_path = held_karp(G, operation_counter)
    print("Optimal TSP Path:", opt_path)
    print("Optimal TSP Cost:", opt_cost)
    print("Operation Counter: ", operation_counter.counter)
    cities_vs_complexity[num_nodes] = operation_counter.counter

n,y = print_estimation()




# Add titles and labels
'''plt.title('Estimated optimal complexity')
plt.xlabel('$n$')
plt.ylabel('$2^{n}$')
plt.legend()
plt.grid(True)'''



plt.figure(figsize=(10, 5))
plt.title('CitiesVSComplexity Optimal')
plt.xlabel('Number of cities')
plt.ylabel('Number of operations')
#plt.plot(keys, values, marker='o')
plt.plot(list(cities_vs_complexity.keys()), list(cities_vs_complexity.values()),  label='experiment')
plt.plot(n, y, marker='o', linestyle='-', color='r', label='expected')
plt.legend()


plt.savefig(f"CitiesVSComplexityOptimal.png", format="PNG")
plt.show()



