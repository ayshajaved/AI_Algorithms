# Uninformed Search Algorithms and Their Types

Uninformed search algorithms, also called blind search algorithms, explore the search space without any domain-specific heuristics. They use only problem definition details: initial state, possible actions, and goal check.

## Types of Uninformed Search Algorithms

### 1. Breadth-First Search (BFS)
- Explores nodes level by level.
- Uses a queue (FIFO).
- Guarantees shortest path for equal step costs.
- Example: In a graph with nodes \(P, Q, R, S, T\), BFS visits \(P \to Q \to R \to S \to T\).
- Time Complexity: \(O(V + E)\)
- Space Complexity: \(O(V)\)

### 2. Depth-First Search (DFS)
- Explores as deep as possible along branches before backtracking.
- Uses a stack or recursion.
- Memory efficient but may get stuck in infinite depths.
- Example: Visits a path deeply, e.g., \(A \to B \to D\) before exploring other branches.
- Time Complexity: \(O(V + E)\)
- Space Complexity: \(O(V)\)

### 3. Uniform Cost Search (UCS)
- Expands lowest cumulative cost node first.
- Uses a priority queue.
- Guarantees least-cost path in weighted graphs.
- Example: In a weighted graph, UCS finds the optimal path by always expanding the cheapest path so far.
- Time Complexity: Depends on graph and path costs.
- Space Complexity: High due to storing visited nodes.

### 4. Depth-Limited Search
- DFS variant limiting search to a max depth \(l\).
- Avoids infinite descending.
- Example: Searches only up to depth 3 in a graph.
- Time Complexity: \(O(b^{l})\), where \(b\) is branching factor.
- Space Complexity: Same as DFS.

### 5. Iterative Deepening Depth-First Search (IDDFS)
- Repeatedly applies depth-limited search with increasing depth.
- Combines DFS’s space efficiency and BFS’s completeness.
- Example: Performs depth-limited search at depth = 0, then 1, then 2, etc.
- Time Complexity: \(O(b^d)\), \(d\) = depth of shallowest solution.
- Space Complexity: \(O(bd)\)

### 6. Bidirectional Search
- Simultaneous search from start and goal states.
- Meets in the middle, reducing search space.
- Example: Route planning by searching from both cities until paths meet.
- Time Complexity: \(O(b^{d/2})\)
- Space Complexity: Higher due to two search frontiers.

---

