"""
Improved approximate algorithm for the Traveling Salesperson Problem.

Changes:
1. Multi-start nearest neighbor: run from all nodes, keep best.
2. Randomized restarts: optional diversification.
3. Canonical output: normalize cycle to start at smallest node.
4. Cleaner 2-opt implementation with slicing reversal.
5. Precomputed distance matrix for efficiency.
"""

import sys
import random
from time import perf_counter


def tour_length(G, path):
    """Compute total length of a tour, including return to start."""
    total = 0
    for i in range(len(path) - 1):
        total += G[path[i]][path[i + 1]]
    total += G[path[-1]][path[0]]
    return total


def nearest_neighbor(G, nodes, start=None):
    """Nearest Neighbor heuristic starting from a given node."""
    if start is None:
        start = random.choice(list(nodes))
    unvisited = set(nodes)
    unvisited.remove(start)

    path = [start]
    current = start

    while unvisited:
        next_node = min(unvisited, key=lambda x: G[current][x])
        path.append(next_node)
        unvisited.remove(next_node)
        current = next_node

    return path


def best_nearest_neighbor(G, nodes, restarts=1):
    """Run nearest neighbor from all nodes and optional random restarts."""
    best_path = None
    best_len = float("inf")

    # Try all starting nodes
    for start in nodes:
        path = nearest_neighbor(G, nodes, start)
        length = tour_length(G, path)
        if length < best_len:
            best_len = length
            best_path = path

    # Randomized restarts
    for _ in range(restarts):
        path = nearest_neighbor(G, nodes)
        length = tour_length(G, path)
        if length < best_len:
            best_len = length
            best_path = path

    return best_path


def two_opt(G, path):
    """2-opt local search improvement."""
    improved = True
    while improved:
        improved = False
        for i in range(1, len(path) - 2):
            for j in range(i + 1, len(path) - 1):
                if j - i == 1:
                    continue
                # Current edges
                d1 = G[path[i - 1]][path[i]] + G[path[j]][path[j + 1]]
                # New edges if reversed
                d2 = G[path[i - 1]][path[j]] + G[path[i]][path[j + 1]]
                if d2 < d1:
                    path[i:j + 1] = reversed(path[i:j + 1])
                    improved = True
    return path


def canonical_cycle(path):
    """Rotate cycle to start at lexicographically smallest node."""
    min_index = min(range(len(path)), key=lambda i: path[i])
    rotated = path[min_index:] + path[:min_index]
    return rotated + [rotated[0]]


def main(testing=False):
    G = {}
    nodes = set()

    # Read number of vertices and edges
    v, e = input().strip().split()
    v, e = int(v), int(e)

    # Build adjacency dictionary
    for _ in range(e):
        v1, v2, ew = input().split()
        ew = float(ew)
        if v1 not in G:
            G[v1] = {}
        if v2 not in G:
            G[v2] = {}
        G[v1][v2] = ew
        G[v2][v1] = ew
        nodes.add(v1)
        nodes.add(v2)

    start = perf_counter()

    # Step 1: Multi-start nearest neighbor + random restarts
    nn_path = best_nearest_neighbor(G, nodes, restarts=3)

    # Step 2: Run 2-opt for local improvement
    opt_path = two_opt(G, nn_path)

    # Step 3: Canonical cycle
    best_path = canonical_cycle(opt_path)

    # Compute final path length
    best = tour_length(G, opt_path)

    delta = perf_counter() - start

    if not testing:
        print(f"{best:.4f}")
        print(" ".join(best_path))
    else:
        print(f"Execution time for {v} locations: {delta:.10f} seconds")


if __name__ == "__main__":
    if sys.argv[-1] == "test":
        main(True)
    else:
        main()
