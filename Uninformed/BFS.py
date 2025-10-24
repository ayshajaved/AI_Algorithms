# Breadth-First Search (BFS)
class Graph:
    def __init__(self):
        # Dictionary to store graph nodes and their neighbors
        self.graph = {}

    def add_edge(self, node, neighbors):
        """Add a node and its list of neighbors to the graph."""
        self.graph[node] = neighbors

    def bfs(self, start_node):
        """Perform BFS traversal starting from start_node."""
        visited = []       # List to keep track of visited nodes
        queue = []         # List used as a queue

        # Start by visiting the first node
        visited.append(start_node)
        queue.append(start_node)

        print("Breadth-First Search Traversal:")

        # Loop runs until queue is empty
        while len(queue) > 0:
            # Remove the first element manually (FIFO)
            current_node = queue[0]
            del queue[0]

            # Print the current node
            print(current_node, end=" ")

            # Visit each neighbor
            for neighbor in self.graph[current_node]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)


# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge('5', ['3', '7'])
    g.add_edge('3', ['2', '4'])
    g.add_edge('7', ['8'])
    g.add_edge('2', [])
    g.add_edge('4', ['8'])
    g.add_edge('8', [])

    # Run BFS starting from node '5'
    g.bfs('5')


# Breadth-First Search (BFS) Built in functions
from collections import deque

class Graph:
    def __init__(self):
        # Initialize an empty adjacency list
        self.graph = {}

    def add_edge(self, node, neighbors):
        """Add a node and its neighbors to the graph."""
        self.graph[node] = neighbors

    def bfs(self, start_node):
        """Perform Breadth-First Search traversal starting from 'start_node'."""
        visited = set()           # To keep track of visited nodes
        queue = deque([start_node])  # Use deque for efficient FIFO operations

        print("Breadth-First Search Traversal:")

        while queue:
            # Remove the first node from the queue
            current = queue.popleft()

            if current not in visited:
                print(current, end=" ")
                visited.add(current)

                # Add all unvisited neighbors to the queue
                for neighbor in self.graph.get(current, []):
                    if neighbor not in visited:
                        queue.append(neighbor)


# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge('5', ['3', '7'])
    g.add_edge('3', ['2', '4'])
    g.add_edge('7', ['8'])
    g.add_edge('2', [])
    g.add_edge('4', ['8'])
    g.add_edge('8', [])

    # Run BFS starting from node '5'
    g.bfs('5')
