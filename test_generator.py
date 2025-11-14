import random
import sys

"""
Generates a list of complete graph edges with random weights for testing purposes.

Usage: python3 test_generator.py <number_of_vertices> > output.txt
"""

def main(n_vertices):
    print(f"{n_vertices} {n_vertices * (n_vertices + 1) // 2}")
    for i in range(n_vertices):
        for j in range(i, n_vertices):
            print(f"v{i} v{j} {random.uniform(0.1, 1000)}")
    return

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 test_generator.py <number_of_vertices>")
        sys.exit(1)
    main(int(sys.argv[1]))
