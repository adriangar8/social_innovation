import numpy as np
from scipy.spatial import distance_matrix
import numpy as np
import networkx as nx
from tqdm import tqdm
import matplotlib.pyplot as plt

print()

# Number of cities per instance and number of instances
num_cities = 7
num_instances = 10

# Generate random coordinates for cities in a 2D plane
np.random.seed(42)  # For reproducibility
city_coordinates = np.random.rand(num_instances, num_cities, 2) * 100  # Scaling to increase range

# Plotting the city coordinates
for i in tqdm(range(num_instances)):
    G = nx.Graph()
    G.add_nodes_from(range(num_cities))
    pos = {city: (city_coordinates[i][city][0], city_coordinates[i][city][1]) for city in range(num_cities)}
    nx.draw(G, pos, with_labels=True)

    # Save fig for the first 10 instances
    if i < 10:
        plt.savefig(f"city_graphs/city_coordinates_{i}.png")
        plt.close()
    else:
        break

print()
print(city_coordinates)
print()

print(city_coordinates.shape)
print()

def nearest_neighbor_tour(coordinates):
    """Generates a TSP tour using the nearest neighbor heuristic."""
    num_cities = coordinates.shape[0]

    print(num_cities)
    print()

    unvisited = list(range(num_cities))
    tour = [unvisited.pop(0)]  # Start at the first city
    while unvisited:
        last_visited = tour[-1]
        next_city = min(unvisited, key=lambda city: np.linalg.norm(coordinates[last_visited] - coordinates[city]))
        tour.append(next_city)
        unvisited.remove(next_city)

    print(tour)
    print()

    return tour

# Compute the nearest neighbor tours for a subset of our data (first 100 instances for demonstration)
tsp_solutions = np.array([nearest_neighbor_tour(city_coordinates[i]) for i in range(100)])

print(tsp_solutions.shape)
print()
