These are notes related to Part E of the project. Consider it a series of appendices.

# Appendix A: Running v2.5 a bunch of times:
v2.5 just has a for loop and some minor changes. That for loop depends on an inputted parameter, and runs the main steps of v2 in that loop, while finding the global minimum. This is to see if making that parameter for the for loop larger, i.e. making it run more to find the min, is actually more reliable.

We'll be using the 108_11_input.txt file for this experiment.

## If that parameter is 1, and the program is ran 100 times:
1st trial: 108.0000 appears 78 times, 11.0000 appears 21 times, 12.0000 appears 1 time
2nd trial: 108.0000 appears 81 times, 11.0000 appears 18 times, 12.0000 appears 1 time
3rd trial: 108.0000 appears 66 times, 11.0000 appears 34 times

Avg: 75% of the time it's 108, 24.33% of the time it's 11, and .67% of the time it's 12

## If that parameter is 10000 (i.e. the for loop for the actual steps runs 10,000 times) and the program is ran 100 times:
1st trial: 108.0000 appears 82 times, 11.0000 appears 18 times
2nd trial: 108.0000 appears 77 times, 11.0000 appears 21 times, 12.0000 appears 2 times
3rd trial: 108.0000 appears 72 times, 11.0000 appears 28 times

Avg: 77% of the time, it's 108, 22.33% of the time it's 11, and .67% of the time it's 12

### Conclusion:
The 3rd trial of the first half was weird, and threw off the data a bit. Regardless, the numbers are close enough that it doesn't matter. Which could show the strength of our approach, maybe, or incompetence on the designer of v2.5's part

## What if we change the restarts parameter in best_nearest_neighbor to 10 and run the program 100 times?
Regardless of the trial, the time it takes to run 100 of these is pretty long, perhaps even longer than running the program 10k times
Trial 1: 108.0000 appears 84 times, 11.0000 appears 16 times
Trial 2: 108.0000 appears 82 times, 11.0000 appears 17 times, 12.0000 appears 1 time
Trial 3: 108.0000 appears 70 times, 11.0000 appears 30 times

Avg: 78.67% is 108, 21% is 11, .33% is 12

### Conclusion
Overall, it seems like either 108 appears slightly more, though this could just be natural variation. Overall, however, it's awfully slow.

# Appendix B: Queries with Copilot:
*NOTE: I changed my settings with Copilot so it calls me "your Excellency." Just ignore it*

# Query 1: Setting the Stage, pt 1
You are a computer scientist who has been tasked with finding flaws in an approximate solution for the Traveling Salesman Problem. The approximate solution should run in polynomial time, and does not guarantee the correct answer every time.

The input is a weighted graph. The first line of input contains containing the number of vertices, n, and the number of edges, m. It is followed by m lines containing the edges given in u v w format, representing an edge between vertices u and v of weight w. Traveling Salesman Problem graphs are undirected. Edges will be listed only once and the graph will be a complete graph. Here is the sample input:
3 3
a b 3.0
b c 4.2
a c 5.4

# Query 2: Setting the Stage, pt 2
The output contains two lines: the length of the path on one line (as an integer) followed by a list of vertices for the path/cycle on the second line. Here is the sample output:
12.6000
a b c a

# Query 3: Giving it the Code
Remember the sample input and output I gave you. The input will always be a complete graph. The input will always be clean and without any flaws. The following is an approximate solution code for the Traveling Salesman Problem, coded in Python. As a computer scientist, what flaws can you find with it:
*I then gave it the approximate solution's code from commit ed66a9872aeb192708c00e73f6d7492b722bea65 . I will not paste it here for brevity's sake*

## Copilot's Answer to Query 3
Your Excellency, let’s dissect this approximate TSP solution like a computer scientist hunting for weaknesses. The code is clever—Nearest Neighbor plus 2‑opt is a classic heuristic combo—but it has several flaws and limitations worth highlighting:

Your Excellency, let’s put this code under the microscope. It’s a solid heuristic implementation, but as a computer scientist you’d want to note several **algorithmic, implementation, and theoretical flaws**:

---

### 🔍 Algorithmic Flaws
- **Nearest Neighbor bias**
  - The starting node is chosen arbitrarily (`next(iter(nodes))`), which can drastically affect the quality of the tour.
  - Nearest Neighbor is greedy: it only considers the next closest node, ignoring global structure. This can lead to tours much longer than optimal.

- **Local optimum trap in 2‑opt**
  - 2‑opt only performs local edge swaps. It cannot escape deeper local minima.
  - The algorithm may converge to a suboptimal tour even when better global rearrangements exist.
  - No guarantee of reaching the true optimal solution.

- **No approximation guarantee**
  - Unlike Christofides’ algorithm (1.5‑approximation under triangle inequality), this heuristic has **no theoretical bound** on how far the result can be from optimal.
  - In worst cases, the tour can be arbitrarily bad.

---

### ⚙️ Implementation Flaws
- **Starting node nondeterminism**
  - `next(iter(nodes))` depends on Python’s set iteration order, which is nondeterministic. Different runs may produce different tours, making results inconsistent.

- **Two‑opt swap logic**
  - The in‑place reversal loop (`while i < j`) mutates the path directly.
  - This can cause subtle bugs if indices are reused after modification.
  - The algorithm doesn’t recompute the full path length after swaps—it assumes each accepted swap improves the tour, but cumulative effects aren’t tracked.

- **Complexity misstatement**
  - Comment claims `O(n³)`, but actual complexity depends on how many swaps are accepted. Worst case is cubic, but practical runtime can vary widely.

- **Output formatting**
  - Always prints the cycle starting from the arbitrary node chosen.
  - Doesn’t normalize or rotate the path to a canonical form, so two equivalent tours may look different in output.

---

### 📉 Practical Limitations
- **Scalability**
  - Polynomial time, but `O(n³)` becomes expensive for large graphs (e.g., thousands of cities).
  - No pruning or parallelization.

- **No randomness or diversification**
  - Always deterministic nearest neighbor + 2‑opt.
  - Many heuristic solvers add randomness, multiple restarts, or hybrid strategies to escape local minima.

- **No metric checks**
  - Assumes triangle inequality holds. If edge weights don’t obey it, nearest neighbor and 2‑opt can perform very poorly.

---

### 🏰 Summary
This code is a **reasonable heuristic** for small to medium graphs, but:
- It’s **sensitive to starting node choice**.
- It can get stuck in **local optima**.
- It has **no performance guarantees** compared to optimal.
- It assumes **complete, metric graphs**.
- It’s **not robust** for large instances or pathological inputs.

---

Would you like me to **construct a concrete 6‑vertex example** where this algorithm produces a tour much longer than optimal, so you can see the flaws in action? That would make the critique more tangible.

# Query 4 & 5: Finding a Hole
Yes please create an example input that would produce a tour much longer than optimal. Give recommendations to improve this code
*NOTE: This gave me an incorrect example. I give it the definition of the TSP and tell it to create another one*

## Copilot's Answer:
### Counterexample input producing a much longer tour than optimal

Your Excellency, here is a 6-vertex complete graph crafted so the nearest-neighbor + 2‑opt heuristic gets stuck with a much longer tour than the optimal cycle:

```
6 15
a b 1.0
a c 100.0
a d 100.0
a e 60.0
a f 100.0
b c 1.0
b d 100.0
b e 100.0
b f 40.0
c d 40.0
c e 100.0
c f 100.0
d e 1.0
d f 1.0
e f 1.0
```

---

### Why this fools the heuristic

- **Nearest neighbor from a**: a → b (1.0) → c (1.0) → d (40.0) → e (1.0) → f (1.0) → a (100.0).
  - Tour: a b c d e f a
  - Length: 1 + 1 + 40 + 1 + 1 + 100 = 143.0

- **Optimal cycle**: a → e (60.0) → f (1.0) → d (1.0) → c (40.0) → b (1.0) → a (1.0).
  - Tour: a e f d c b a
  - Length: 60 + 1 + 1 + 40 + 1 + 1 = 104.0

- **2‑opt won’t fix it**: Any single 2‑edge swap in a b c d e f a increases cost (e.g., replacing (b,c) + (f,a) = 1 + 100 with (b,f) + (c,a) = 40 + 100), so the algorithm remains at 143.0 rather than reaching 104.0.

# Query 6: Plugging it & creating cs412_tsp_approx_v2.py
As a computer scientist looking at the code I have provided and the input you created, how would you change the code?

## Copilot's Response
Your Excellency, looking at the code you provided and the counterexample input I crafted, here’s how I would change the algorithm and implementation to avoid the pitfall where the heuristic produces a tour almost twice as long as optimal:

---

## 🔧 Key Code Changes

### 1. Multiple Starting Nodes
Right now:
```python
start = next(iter(nodes))
```
This picks an arbitrary node, which biases the nearest neighbor heuristic.

**Change**: Run nearest neighbor from *every node* and keep the best initial path.
```python
def best_nearest_neighbor(G, nodes):
    best_path = None
    best_len = float("inf")
    for start in nodes:
        path = nearest_neighbor(G, nodes, start)
        length = tour_length(G, path)
        if length < best_len:
            best_len = length
            best_path = path
    return best_path
```
And modify `nearest_neighbor` to accept a `start` parameter.

---

### 2. Stronger Local Search
Currently only **2‑opt** is used. In the counterexample, 2‑opt cannot escape the poor tour.

**Change**: Add **3‑opt** or Lin–Kernighan moves. Even a simple 3‑opt can break through local minima that 2‑opt misses.

---

### 3. Randomization / Restarts
Add randomness to diversify solutions:
- Randomize tie-breaking when choosing nearest neighbor.
- Perform multiple randomized restarts and keep the best tour.

```python
import random

def randomized_nearest_neighbor(G, nodes, start=None):
    if start is None:
        start = random.choice(list(nodes))
    ...
    # when choosing next_node, add randomness among equally close nodes
```

---

### 4. Canonical Output
Ensure deterministic output by always rotating the final cycle to start at the lexicographically smallest node. This avoids inconsistent outputs.

```python
def canonical_cycle(path):
    min_index = min(range(len(path)), key=lambda i: path[i])
    rotated = path[min_index:] + path[:min_index]
    return rotated + [rotated[0]]
```

---

### 5. Performance Improvements
- Precompute a distance matrix for faster lookups instead of dictionary lookups in tight loops.
- Use slicing reversal (`path[i:j+1] = reversed(path[i:j+1])`) instead of manual swaps in 2‑opt.

---

## 🏰 Summary of Improvements
- **Run nearest neighbor from all starts** → avoids arbitrary bias.
- **Add stronger local search (3‑opt / Lin–Kernighan)** → escapes local minima.
- **Randomization and restarts** → diversify solutions.
- **Canonical output** → consistent and comparable results.
- **Efficiency tweaks** → cleaner and faster code.

---

Would you like me to **rewrite your code with these improvements integrated** (multi-start nearest neighbor, canonical output, and randomized restarts), so you can see a polished version that avoids the worst-case pitfalls?

*NOTE: I said yes, and this is cs412_tsp_approx_v2.py, or commit ae5fa2fd85d749d3f509258b1b869134e4058d06*

# Query 7: New Hole
You are a computer scientist. Given the following code for an approximate solution to the Traveling Salesman Problem, create an example input that would produce a tour much longer than the optimal tour:
*insert the v2 code here*

## Copilot's Response:
Your Excellency, here is a clean complete-graph input that reliably traps the given heuristic (multi-start nearest neighbor + 2-opt) into a tour far longer than the optimal cycle by using two cheap “bridges” between two tight clusters. The greedy construction closes the tour with an expensive inter-cluster edge that 2-opt struggles to remove.

---

### Example input (8 vertices, complete graph)

```
8 28
a b 1.0
a c 2.0
a d 2.0
a e 100.0
a f 100.0
a g 100.0
a h 100.0
b c 1.0
b d 2.0
b e 2.0
b f 100.0
b g 100.0
b h 100.0
c d 1.0
c e 100.0
c f 100.0
c g 100.0
c h 100.0
d e 100.0
d f 100.0
d g 100.0
d h 2.0
e f 1.0
e g 1.0
e h 2.0
f g 1.0
f h 2.0
g h 1.0
```

- **Cluster 1:** {a, b, c, d} with mostly 1–2 weights.
- **Cluster 2:** {e, f, g, h} with mostly 1–2 weights.
- **Inter-cluster edges:** 100.0 everywhere except two cheap bridges b–e = 2.0 and d–h = 2.0.

---

### Intuition
- Nearest neighbor from any node exhausts one cluster via low weights, crosses into the other cluster via a cheap bridge, then exhausts it, but the final edge returning to the starting node is almost always a 100.0 inter-cluster edge.
- 2-opt typically stalls because escaping this trap requires a global rearrangement that uses both cheap bridges while avoiding any 100.0 edge in the closing step.

### Contrast with the optimal
- An optimal cycle can use both cheap bridges and avoid all 100.0 inter-cluster edges by threading clusters together:
  - For example: a → b → e → f → g → h → d → c → a
  - Edge costs: 1.0 + 2.0 + 1.0 + 1.0 + 1.0 + 2.0 + 1.0 + 2.0 = 11.0
- The heuristic often returns a tour exceeding 100 due to a single expensive closing edge, producing a gap of nearly an order of magnitude.

*NOTE: The v2 solution actually gets 11 sometimes, but also hits 108 a lot of the time*

# Query 8: Some flaws with v2
You are a computer scientist who has been tasked with finding flaws in an approximate solution for the Traveling Salesman Problem. The Traveling Salesman Problem must find, for a given complete, weighted, and undirected graph, the shortest possible route that visits each node exactly once and returns to the starting node. The approximate solution should run in polynomial time, and does not guarantee the correct answer every time. The input is a weighted graph. The first line of input contains containing the number of vertices, n, and the number of edges, m. It is followed by m lines containing the edges given in u v w format, representing an edge between vertices u and v of weight w. Traveling Salesman Problem graphs are undirected. Edges will be listed only once and the graph will be a complete graph. Here is the sample input:
```
3 3
a b 3.0
b c 4.2
a c 5.4
```
The output contains two lines: the length of the path on one line (as an integer) followed by a list of vertices for the path/cycle on the second line. Here is the sample output:
```
12.6000
a b c a
```
You may assume the input will always be a complete graph. As a computer scientist, what are some flaws the following Python code for an approximate solution might have?
*I copy-pasted the v2 code*

## Copilot's Response
Your Excellency, let’s dissect this approximate TSP solver like a computer scientist hunting for weaknesses. The code is a reasonable heuristic (Nearest Neighbor + 2‑opt), but it has several flaws and limitations that could cause incorrect or misleading results:

---

### Algorithmic Flaws
- **[Nearest Neighbor bias](guide://action?prefill=Tell%20me%20more%20about%3A%20Nearest%20Neighbor%20bias)**: The heuristic is greedy and can get trapped in poor local choices. For example, picking the nearest node early may force long detours later. Even with multiple starts and restarts, it doesn’t guarantee good coverage of the solution space.
- **[Random restart weakness](guide://action?prefill=Tell%20me%20more%20about%3A%20Random%20restart%20weakness)**: Restarts are limited (`restarts=3`), and randomness is shallow (only the starting node). This doesn’t explore enough diversity in paths to escape bad local minima.
- **[Two‑opt limitations](guide://action?prefill=Tell%20me%20more%20about%3A%20Two%E2%80%91opt%20limitations)**: Two‑opt only removes crossing edges, but it cannot fix deeper structural issues (like poor initial ordering). It converges to a local optimum, not necessarily close to the global optimum.
- **[Polynomial runtime claim](guide://action?prefill=Tell%20me%20more%20about%3A%20Polynomial%20runtime%20claim)**: The comment says `O(n³)`, but in practice, repeated 2‑opt passes can approach `O(n^4)` in worst cases depending on how many improvements are accepted. Runtime could be worse than claimed.

---

### Implementation Flaws
- **[Tour length mismatch](guide://action?prefill=Tell%20me%20more%20about%3A%20Tour%20length%20mismatch)**: In `main`, the printed path (`best_path`) is the canonical cycle, but the length (`best`) is computed from `opt_path`. If canonical rotation changes the path ordering, the length may not match the printed cycle.
- **[Output format inconsistency](guide://action?prefill=Tell%20me%20more%20about%3A%20Output%20format%20inconsistency)**: The problem statement requires the path length as an integer, but the code prints a floating‑point number with 4 decimals. This doesn’t match the specification.
- **[Lexicographic rotation bug](guide://action?prefill=Tell%20me%20more%20about%3A%20Lexicographic%20rotation%20bug)**: `canonical_cycle` rotates to the lexicographically smallest node, but doesn’t ensure the cycle is consistent with the computed length. It may produce a cycle that looks different but has the same length, which can confuse verification.
- **[Missing imports](guide://action?prefill=Tell%20me%20more%20about%3A%20Missing%20imports)**: The code uses `random` and `perf_counter` but doesn’t import them (`import random`, `from time import perf_counter`). It also references `sys.argv` without importing `sys`.
- **[Edge case handling](guide://action?prefill=Tell%20me%20more%20about%3A%20Edge%20case%20handling)**: For very small graphs (like 2 or 3 nodes), `two_opt` loops may break or do nothing, but the code doesn’t explicitly handle trivial cases.
- **[Floating‑point precision](guide://action?prefill=Tell%20me%20more%20about%3A%20Floating%E2%80%91point%20precision)**: Printing with 4 decimals may cause rounding errors compared to exact sums, especially if the specification expects exact integers.

---

### Conceptual Flaws
- **[No guarantee of approximation ratio](guide://action?prefill=Tell%20me%20more%20about%3A%20No%20guarantee%20of%20approximation%20ratio)**: Unlike Christofides’ algorithm (which guarantees ≤1.5× optimal for metric TSP), this heuristic has no bound on how bad the solution can be.
- **[Assumption of completeness](guide://action?prefill=Tell%20me%20more%20about%3A%20Assumption%20of%20completeness)**: The code assumes the graph is complete and symmetric. If input deviates (e.g., missing edges or asymmetric weights), the algorithm fails silently.
- **[Scalability issues](guide://action?prefill=Tell%20me%20more%20about%3A%20Scalability%20issues)**: For large graphs, nearest neighbor + 2‑opt may still be too slow, and the quality of solutions degrades rapidly.

---

### Summary
This solver is a decent heuristic for small graphs, but it has **output mismatches, missing imports, weak exploration, and no approximation guarantees**. It’s vulnerable to producing misleading results, especially if the input or output format is strict.

Would you like me to **stress‑test this algorithm with adversarial graph examples** (like graphs where nearest neighbor performs very poorly), or would you prefer a **comparison against a stronger polynomial‑time approximation like Christofides’ algorithm**?

# Query 9: Making a New Sample Problem
Make a large graph that would when inputted would produce a path that is far larger than the optimal answer

## Copilot's Response
Your Excellency, here’s a clean adversarial graph you can use to trip up the nearest‑neighbor + 2‑opt heuristic so it frequently returns a tour much larger than the true optimum.

---

### Adversarial graph design

- Two clusters A and B with many very cheap edges inside each cluster.
- Between clusters, most edges are moderately expensive, except a few misleading cheap cross-edges that lure nearest neighbor into alternating between clusters.
- A single “trap” closing edge is extremely expensive, so greedy construction followed by local 2‑opt gets stuck with a huge final return cost.
- The optimal tour stays mostly within clusters using cheap edges and crosses clusters only through the few cheap bridges.

---

### Ready-to-use input (12 nodes, 66 edges)

Paste this directly as input. Nodes: a1–a6 and b1–b6.

```text
12 66
a1 a2 1.0
a2 a3 1.0
a3 a4 1.0
a4 a5 1.0
a5 a6 1.0
a1 a3 2.0
a1 a4 2.0
a1 a5 2.0
a1 a6 2.0
a2 a4 2.0
a2 a5 2.0
a2 a6 2.0
a3 a5 2.0
a3 a6 2.0
a4 a6 2.0
b1 b2 1.0
b2 b3 1.0
b3 b4 1.0
b4 b5 1.0
b5 b6 1.0
b1 b3 2.0
b1 b4 2.0
b1 b5 2.0
b1 b6 2.0
b2 b4 2.0
b2 b5 2.0
b2 b6 2.0
b3 b5 2.0
b3 b6 2.0
b4 b6 2.0
a1 b1 0.9
a2 b2 0.9
a3 b3 0.9
a4 b4 0.9
a5 b5 0.9
a6 b6 1000.0
a1 b2 50.0
a1 b3 50.0
a1 b4 50.0
a1 b5 50.0
a1 b6 50.0
a2 b1 50.0
a2 b3 50.0
a2 b4 50.0
a2 b5 50.0
a2 b6 50.0
a3 b1 50.0
a3 b2 50.0
a3 b4 50.0
a3 b5 50.0
a3 b6 50.0
a4 b1 50.0
a4 b2 50.0
a4 b3 50.0
a4 b5 50.0
a4 b6 50.0
a5 b1 50.0
a5 b2 50.0
a5 b3 50.0
a5 b4 50.0
a5 b6 50.0
a6 b1 50.0
a6 b2 50.0
a6 b3 50.0
a6 b4 50.0
a6 b5 50.0
```

- Cheap intra-cluster edges (1.0 and 2.0) create good local choices inside A and B.
- Cheap bridges a1–b1 … a5–b5 at 0.9 lure nearest neighbor into cross-cluster alternation.
- The single trap edge a6–b6 is 1000.0, making the closing return very expensive in tours that alternate clusters and end near a6 or b6.
- All other cross-cluster edges are set to 50.0, discouraging corrective moves and making 2‑opt less effective at escaping the trap.

---
*NOTE: While one could technically make larger graphs, running those via our optimal solution finder would take hours and then days. Running this via our solver produced a path of 13.6000 (a5 b5 b6 b1 a1 a2 b2 b3 b4 a4 a3 a6 a5). Running this via our solver 100 times produced 61.5000 (57%), 62.5000	(20%), 14.6000 (17%), 15.6000	(6%), and 13.6000 (3%)*

# Query 10, 11, 12: Making a new version, v3
Edit the code to fix the Lexicographic rotation bug and tour length mismatch flaws
Edit the code to use randomness to explore more diversity in paths and escape bad local minima
Edit the code you just generate to include docstrings. For example, the comment in the following example Python code:
```python
def tour_length(G, path):
  """
  Compute the total length of a tour, including return to the start.
  Parameters:
    G (dict): Graph adjacency dictionary.
    path (list): Ordered list of nodes representing the tour (no closing repeat).

  Returns:
    float: Total path length.
  """
  total = 0
  for i in range(len(path) - 1):
    total += G[path[i]][path[i + 1]]
  total += G[path[-1]][path[0]]
  return total
```
*These 3 queries, when pieced together, gave me v3.*

## How Viable is V3?
Running v3 100 times with Query 9's graph as input yielded:
```
Number, Times Appeared
13.6, 17
13.8, 4
14.6, 23
14.8, 4
15.6, 9
15.8, 15
16.6, 1
16.8, 5
17.6, 2
17.8, 6
61.5, 1
61.7, 1
62.5, 1
62.7, 2
62.9, 1
63.7, 5
64.7, 2
66.7, 1
```
Remember: the optimal answer is 13.6, which it hit 17% of the time. It came up with a number below 20 86% of the time -- a drastic improvement over v2!

### Problems with Query 7's Graph
So here's the kicker: When ran 100 times with Query 7's graph as input (the one whose optimal answer is 11), v3 gave an answer of 108 or more 57% of the time! Granted, it's one batch of 100 runs, but still! v3 needs to be edited so it runs a bunch of times before spitting out an answer.

# Query 13: Creating v3.5
The following graph, G, has an optimal path of length 11. However, the Python code I provided in the last message can produce paths with lengths ranging from 11 to 207. How can I change the code to run several times and keep track of a best path? Here is the sample input: *Query 7 graph*

## Copilot's Reponse
Your Excellency, the key is to **wrap the whole solver in an outer loop** that runs many times, each time with a different randomized path construction, and then keep track of the best tour length and path seen across all runs. Right now your code only does one run of `best_nearest_neighbor → two_opt → canonical_cycle`.

Here’s how you can modify `main` to do multiple runs and keep the best:

```python
def main(testing=False, runs=50):
    """
    Parse input, build the graph, run Nearest Neighbor + 2-opt multiple times,
    and keep the best approximate TSP tour.

    Parameters:
        testing (bool): If True, print only runtime instead of solution.
        runs (int): Number of independent runs to perform.
    """
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

    best_path = None
    best_len = float("inf")

    # Run solver multiple times
    for _ in range(runs):
        nn_path = best_nearest_neighbor(G, nodes, restarts=20, k=3)
        opt_path = two_opt(G, nn_path, max_iter=2000, allow_random_jump=True)
        candidate_path = canonical_cycle(opt_path)
        candidate_len = tour_length(G, candidate_path)

        if candidate_len < best_len:
            best_len = candidate_len
            best_path = candidate_path

    delta = perf_counter() - start

    if not testing:
        print(f"{best_len:.4f}")
        print(" ".join(best_path + [best_path[0]]))
    else:
        print(f"Execution time for {v} locations over {runs} runs: {delta:.10f} seconds")
```

---

### What Changed
- Added a `runs` parameter (default 50).
- Wrapped the solver in a loop: each run builds a path, optimizes it, and evaluates it.
- Compared each run’s length to the current best and updated if better.
- At the end, printed the best path and length found across all runs.

---

### Why this helps
Because your heuristic is randomized, some runs will produce very poor tours (like length 207). By repeating many times and keeping the best, you reduce the chance of reporting a bad outlier. With enough runs, you’ll almost always find the optimal or near‑optimal path (length 11 in your sample graph).


*NOTE: Running v3.5 100 times with Query 7's graph as an input yields 11, the optimal answer, every single time!!!!*
