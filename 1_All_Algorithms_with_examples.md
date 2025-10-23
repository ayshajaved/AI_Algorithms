# **Requirement of Search Algorithms / Techniques**

### **1. Motion Requirement**

The first requirement is that a search algorithm should **cause motion**, meaning it should be able to move from one state to another within the state space.

### **2. Systematic Requirement**

The second requirement is that the search process must be **systematic**, exploring all possible paths in an organized and logical manner to ensure that an optimal or valid solution is found.

---

## **State Space Concept**

A **state space** is the set of all possible configurations (states) that can be reached from the **initial state** of a problem.
A **state space search algorithm** explores these states to find a path from the **initial state** to a **goal state**.

---

# **Algorithm Categories and Their Types**

---

## **1. Sorting Algorithms**

These algorithms arrange data in a specific order (ascending or descending).

**Examples:**

* **Quick Sort** – Uses divide and conquer; selects a pivot and partitions data.
* **Merge Sort** – Divides array, sorts halves, then merges them.
* **Bubble Sort** – Repeatedly swaps adjacent elements.
* **Insertion Sort** – Builds the sorted list one element at a time.
* **Selection Sort** – Selects the smallest (or largest) element each iteration.
* **Heap Sort** – Uses a heap data structure for sorting.
* **Radix Sort** – Non-comparative integer sorting using digit positions.

---

## **2. Search Algorithms**

Algorithms used to find specific data or paths within a data structure or problem space.

### **A. Uninformed (Blind) Search Algorithms**

Operate without domain-specific knowledge; explore systematically.

**Examples:**

* **Breadth-First Search (BFS)** – Explores all nodes at one depth before moving deeper.
* **Depth-First Search (DFS)** – Explores as far as possible along each branch.
* **Uniform Cost Search (UCS)** – Expands the least-cost node first.
* **Iterative Deepening DFS** – Combines BFS’s completeness with DFS’s space efficiency.
* **Bidirectional Search** – Searches simultaneously from start and goal.

---

### **B. Informed (Heuristic) Search Algorithms**

Use heuristics to estimate cost to reach the goal and guide the search efficiently.

**Examples:**

* **Greedy Best-First Search** – Selects node that appears closest to the goal.
* **A*** – Combines path cost and heuristic; finds optimal path.
* **Hill Climbing** – Moves towards increasing value or improvement.
* **Iterative Deepening A*** – Combines depth-limited search with heuristics.
* **Linear Search** – Sequentially checks each element in a list.
* **Binary Search** – Efficiently searches sorted data by halving the range.

---

## **3. Machine Learning Algorithms**

Algorithms that learn from data and improve performance automatically.

### **Supervised Learning**

Learn from labeled data.
**Examples:**

* Decision Trees
* Support Vector Machines (SVM)
* Neural Networks
* Random Forest
* Logistic Regression

### **Unsupervised Learning**

Find hidden patterns in unlabeled data.
**Examples:**

* K-Means Clustering
* Principal Component Analysis (PCA)
* Autoencoders

### **Reinforcement Learning**

Learn via rewards and punishments.
**Examples:**

* Q-Learning
* SARSA
* Policy Gradients

### **Semi-Supervised Learning**

Uses both labeled and unlabeled data.

### **Ensemble Methods**

Combine multiple models for better accuracy.
**Examples:**

* Bagging
* Boosting (AdaBoost, Gradient Boosting)
* Stacking

---

## **4. Brute Force Algorithms**

Try every possible solution until the correct one is found.

**Examples:**

* Naive String Matching
* Exhaustive Search for Combinatorial Problems
* Backtracking (basic form)

---

## **5. Divide and Conquer Algorithms**

Divide problem into subproblems, solve independently, and combine results.

**Examples:**

* Merge Sort
* Quick Sort
* Binary Search
* Strassen’s Matrix Multiplication

---

## **6. Dynamic Programming Algorithms**

Break problems into overlapping subproblems and reuse results.

**Examples:**

* Fibonacci Number Calculation
* Knapsack Problem
* Longest Common Subsequence
* Matrix Chain Multiplication
* Bellman-Ford Algorithm

---

## **7. Greedy Algorithms**

Make locally optimal choices to reach a global optimum.

**Examples:**

* Dijkstra’s Shortest Path
* Prim’s Minimum Spanning Tree
* Kruskal’s Minimum Spanning Tree
* Huffman Coding

---

## **8. Backtracking Algorithms**

Incrementally build candidates and backtrack when no feasible solution exists.

**Examples:**

* N-Queens Problem
* Sudoku Solver
* Hamiltonian Path Problem
* Subset Sum Problem

---

## **9. Recursive Algorithms**

Use self-calling functions to solve smaller subproblems.

**Examples:**

* Factorial Calculation
* Tower of Hanoi
* Tree Traversals (Preorder, Inorder, Postorder)
* Merge Sort (Recursive implementation)

---

## **10. Graph Algorithms**

Algorithms specifically designed for graph structures.

**Examples:**

* Depth-First Search (DFS)
* Breadth-First Search (BFS)
* Dijkstra’s Algorithm
* Bellman-Ford Algorithm
* Floyd-Warshall Algorithm
* A* Search
* Minimum Spanning Tree (Prim’s, Kruskal’s)

---

## **11. Ensemble Algorithms (Machine Learning)**

Combine multiple models to enhance prediction accuracy.

**Examples:**

* Bagging
* Boosting (AdaBoost, Gradient Boosting)
* Stacking
* Random Forest

---

## **12. Parallel and Distributed Algorithms**

Divide computation across multiple processors or machines for efficiency.

**Examples:**

* MapReduce
* Parallel Quicksort
* Distributed Consensus (Paxos, Raft)
* Parallel Matrix Multiplication

---

## **13. Adversarial Search Algorithms**

Used in **game-playing** and **competitive environments**, where multiple agents act with opposing goals.
The algorithm must consider the possible moves of an **opponent** and plan accordingly.

### **Key Characteristics:**

* Environment is **multi-agent** and **competitive** (zero-sum).
* Aim is to **maximize own gain** while **minimizing opponent’s gain**.
* Commonly used in AI for **games like Chess, Checkers, Tic-Tac-Toe**, etc.

### **Common Adversarial Algorithms:**

**1. Minimax Algorithm**

* Evaluates all possible moves by both players.
* Chooses the move that **maximizes the player’s minimum payoff** (i.e., assumes opponent plays optimally).

**2. Alpha-Beta Pruning**

* Optimization of Minimax to **skip unnecessary branches** that cannot affect the final decision.
* Improves efficiency while producing the same result as Minimax.

**3. Expectiminimax Algorithm**

* Extension of Minimax for **stochastic games** (where chance is involved).
* Used in games like **Backgammon**, which includes dice rolls.

**Examples of Use:**

* **Chess AI** – Uses Minimax with Alpha-Beta Pruning.
* **Tic-Tac-Toe Solver** – Simple Minimax example.
* **Go AI** – Uses advanced Monte Carlo Tree Search (MCTS).

---

# ✅ **Summary Table**

| **Category**         | **Purpose**                           | **Examples**                |
| -------------------- | ------------------------------------- | --------------------------- |
| Sorting              | Arrange data                          | Quick Sort, Merge Sort      |
| Search               | Find data or path                     | BFS, DFS, A*, Binary Search |
| ML                   | Learn patterns                        | SVM, Decision Tree          |
| Brute Force          | Try all possibilities                 | Naive Search                |
| Divide & Conquer     | Divide problems                       | Quick Sort, Binary Search   |
| Dynamic Programming  | Optimize with overlapping subproblems | Knapsack, LCS               |
| Greedy               | Choose locally best                   | Dijkstra, Prim              |
| Backtracking         | Incremental trial and error           | N-Queens                    |
| Recursive            | Self-calling                          | Tower of Hanoi              |
| Graph                | Work on graphs                        | BFS, Kruskal                |
| Ensemble             | Combine models                        | Random Forest               |
| Parallel/Distributed | Concurrent computing                  | MapReduce                   |
| Adversarial          | Competitive games                     | Minimax, Alpha-Beta         |

---
