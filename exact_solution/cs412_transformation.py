def hamiltonian_to_tsp(G, V):
    # Make the graph complete in polynomial time
    return

def main():
    n = int(input())
    G = {}
    V = set()
    for _ in range(n):
        v1, v2, w = input().strip().split()
        if v1 not in G:
            G[v1] = {}
        V.add(v1)
        V.add(v2)
        G[v1][v2] = float(w)
    tsp = hamiltonian_to_tsp(G, V)
    return

if __name__ == "__main__":
    main()
