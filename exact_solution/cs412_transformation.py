# Make an input graph to the hamiltonian cycle problem complete
def hamiltonian_to_tsp(G, V):

    # O(V^2)
    for v in G:                             # O(V)
        for u in V:                         # O(V)
            if u not in G[v] and u != v:    # O(1) 
                G[v][u] = float('inf')      # O(1)
    return



def main():

    n = int(input())
    G = {}
    V = set()
    for _ in range(n):
        v1, v2, w = input().strip().split()
        if v1 not in G:
            G[v1] = {}
        if v2 not in G:
            G[v2] = {}
        V.add(v1)
        V.add(v2)
        G[v1][v2] = float(w)
        G[v2][v1] = float(w)
    tsp = hamiltonian_to_tsp(G, V)
    return

if __name__ == "__main__":
    main()
