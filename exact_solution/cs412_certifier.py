"""
    Takes a certificate string for a problem instance
    and verifies its correctness in polynomial time.
"""
def certifier(certificate, problem_instance):
    path = certificate.strip().split()
    G, V = problem_instance

    # Make sure its a cycle
    if path[0] != path[-1]:
        print_answer(certificate, False)
        return

    for i in range(len(path) - 1):
        if (path[i] not in G or path[i + 1] not in G 
                or G[path[i]][path[i + 1]] == float("inf") 
                or path[i + 1] not in V):
            print_answer(certificate, False)
            return
        V.remove(path[i + 1])

    if len(V) == 0:
        print_answer(certificate, True)
        return
    print_answer(certificate, False)
    return

def print_answer(certificate, answer=False):
    if answer:
        print(f"Answer for certificate {certificate}: YES")
    else:
        print(f"Answer for certificate {certificate}: NO")


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
    certificate = input().strip()
    certifier(certificate, (G, nodes))
    return

if __name__ == "__main__":
    main()
