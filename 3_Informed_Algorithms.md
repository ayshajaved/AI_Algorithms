# Informed Search Algorithms and Their Types

Informed search algorithms, also known as heuristic search algorithms, use additional knowledge called heuristics to guide the search process more efficiently towards the goal. A heuristic function estimates the cost or distance from a given node to the goal, allowing the algorithm to prioritize exploring the most promising paths first. This reduces the search space and often speeds up finding an optimal or near-optimal solution compared to uninformed search.

## Key Features of Informed Search Algorithms
- Use heuristic information to guide search.
- Aim to reduce the number of states explored.
- Often find better solutions faster than uninformed search.
- May guarantee optimality if heuristics are admissible (never overestimate the true cost) and consistent.
- Commonly used in pathfinding, robotics, games, and optimization problems.

## Types of Informed Search Algorithms

### 1. Greedy Best-First Search
- Selects the next node based solely on the heuristic value \(h(n)\), which estimates the cost to reach the goal.
- It chooses the node that appears closest to the goal according to the heuristic.
- **Advantages:** Fast and efficient in smaller or well-informed search spaces.
- **Limitations:** May not find the optimal path because it ignores the cost so far.
- **Example:** Navigating a map choosing the path that seems closest to the destination.

### 2. A* Search Algorithm
- Combines the actual cost to reach a node \(g(n)\) and the heuristic estimate to the goal \(h(n)\) in the evaluation function:
  \[
  f(n) = g(n) + h(n)
  \]
- Guarantees an optimal solution if \(h(n)\) is admissible and consistent.
- Balances exploration of paths that are cheap so far and estimated to be close to the goal.
- **Applications:** Widely used in robotics, games, and GPS navigation.

### 3. Iterative Deepening A* (IDA*)
- Combines the memory efficiency of depth-first search with the heuristic guidance of A*.
- Performs iterative deepening with cost thresholds based on \(f(n)\).
- Suitable for very large or memory-constrained problems.
- **Example:** Solving puzzles like the 15-puzzle efficiently in limited memory.

### 4. Beam Search
- Explores a limited number of nodes (beam width) at each level, guided by heuristics.
- Balances breadth-first search with heuristic guidance but prunes less promising branches early.
- Often used in natural language processing and speech recognition.
- **Limitation:** May miss the optimal solution due to node pruning.

## Applications of Informed Search Algorithms
- Pathfinding in robotics (e.g., robot navigation avoiding obstacles).
- Route optimization in GPS and transportation systems.
- AI game playing (e.g., NPC navigation and decision making).
- Puzzle solving and problem optimization.

---

