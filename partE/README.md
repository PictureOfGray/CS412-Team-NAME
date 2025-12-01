These are notes related to Part E of the project.

Objective, per Molloy and paraphrased by Dorian C.:
-Use a generative AI to break our approximation, then repair it. See how many holes you can plug up, so to speak.
  -If you plug up everything, try to break it again.
Hint from Molloy:
-The longer you run it, the closer you get to our optimal answer. How does adding more time improve things?

# Running v2.5 a bunch of times:
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

## Conclusion:
The 3rd trial of the first half was weird, and threw off the data a bit. Regardless, the numbers are close enough that it doesn't matter. Which could show the strength of our approach, maybe, or incompetence on the designer of v2.5's part

## What if we change the restarts parameter in best_nearest_neighbor to 10 and run the program 100 times?
Trial 1: 108.0000 appears 56 times, 11.0000 appears 17 times

# Queries with Copilot:
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
*NOTE: This gave me an incorrect example. I give it the definition of the TSP and tell it to create another one *

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
