"""
    Brute force algorithm for finding the shortest path
    in the traveling salesperson problem.
"""

from itertools import permutations
from os import system
def main():
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
    print(f"{best:.4f}\n{" ".join(best_path)}")

## Approximation Algorithm: iterative improvement

if __name__ == "__main__":
    main()
