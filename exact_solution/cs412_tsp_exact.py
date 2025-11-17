"""
    Brute force algorithm for finding the shortest path
    in the traveling salesperson problem.
"""

from itertools import permutations
import sys
from time import perf_counter

def main(testing=False):
    G = {}
    nodes = set()
    v, e = input().strip().split()
    v, e = int(v), int(e)
    
    # Build our graph using the input
    for _ in range(e):
        v1, v2, ew = input().split()
        if v1 not in G:
            G[v1] = {}
        if v2 not in G:
            G[v2] = {}
        G[v1][v2] = float(ew)
        G[v2][v1] = float(ew)
        nodes.add(v1)
        nodes.add(v2)
    
    start = perf_counter()
    # Try all permutations of the paths to find a shortest distance path
    node_permutations = permutations(nodes)
    best = float('inf')
    for perm in node_permutations:
        curr = 0
        for i in range(len(perm)):
            if i == len(perm) - 1:
                curr += G[perm[i]][perm[0]]
            else:
                curr += G[perm[i]][perm[i + 1]]
        if min(curr, best) != best:
            best = curr
            best_path = perm + (perm[0],)
    delta = (perf_counter() - start)
    if not testing:
        print(f"{best:.4f}\n{" ".join(best_path)}")
    else:
        print(f"Execution time for {v} locations: {delta:.10f} seconds")

## Approximation Algorithm: iterative improvement

if __name__ == "__main__":
    if sys.argv[-1] == "test":
        main(True)
    else:
        main()
