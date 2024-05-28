import itertools
import numpy as np
import trace

class OperationCounter:
    def __init__(self):
        self.counter = 0

    def count(self):
        self.counter += 1


def held_karp(G, operation_counter):
    n = len(G.nodes)
    for _ in range(n):
        operation_counter.count()
    # Initialize memoization table
    C = {}
    # Base cases: distance from start node to itself is 0
    for k in range(1, n):
        C[(1 << k, k)] = (G[0][k]['weight'], 0)
        operation_counter.count

    # Iterate subsets of increasing size and fill memoization table
    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            
            bits = 0
            for bit in subset:
                operation_counter.count()
                bits |= 1 << bit
            for k in subset:
                
                prev_bits = bits & ~(1 << k)
                res = []
                for m in subset:
                    operation_counter.count()
                    if m == k:
                        continue
                    res.append((C[(prev_bits, m)][0] + G[m][k]['weight'], m))
                    operation_counter.count()
                C[(bits, k)] = min(res)

    # Calculate the optimal path
    bits = (1 << n) - 2
    res = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + G[k][0]['weight'], k))
        operation_counter.count()
    opt, parent = min(res)

    # Reconstruct the path
    path = []
    for i in range(n - 1):
        operation_counter.count()
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        operation_counter.count()
        _, parent = C[(bits, parent)]
        operation_counter.count()
        bits = new_bits
    path.append(0)
    for _ in range(len(path)):
        operation_counter.count()
    return opt, list(reversed(path))

