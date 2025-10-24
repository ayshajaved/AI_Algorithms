# Depth-First Search (DFS) using OOP — Without Built-in Functions

class Graph:
    def __init__(self):
        self.graph = {}  # Dictionary to store adjacency list

    def add_edge(self, node, neighbors):
        """Add a node and its neighbors to the graph."""
        self.graph[node] = neighbors

    def dfs(self, start_node):
        """Perform Depth-First Search traversal."""
        visited = []     # List to track visited nodes
        stack = [start_node]  # Use list as a stack

        print("Depth-First Search Traversal:")

        while len(stack) > 0:
            # Pop last element (LIFO)
            current_node = stack[-1]
            del stack[-1]

            if current_node not in visited:
                print(current_node, end=" ")
                visited.append(current_node)

                # Add neighbors to stack (reverse to maintain order)
                for neighbor in self.graph[current_node][::-1]:
                    if neighbor not in visited:
                        stack.append(neighbor)


# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge('5', ['3', '7'])
    g.add_edge('3', ['2', '4'])
    g.add_edge('7', ['8'])
    g.add_edge('2', [])
    g.add_edge('4', ['8'])
    g.add_edge('8', [])

    # Run DFS starting from node '5'
    g.dfs('5')

# Depth-First Search (DFS) using built-in functions (simple version)

class Graph:
    def __init__(self):
        self.graph = {}  # Store all nodes and their connections

    def add_edge(self, node, neighbors):
        """Add a node and its connected neighbors"""
        self.graph[node] = neighbors

    def dfs(self, node, visited=None):
        """Recursive DFS traversal"""
        # If visited set is not created yet, make one
        if visited is None:
            visited = set()

        # Mark the current node as visited
        visited.add(node)
        print(node, end=" ")

        # Visit all neighbors that are not visited yet
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)  # Recursive call


# Example use
if __name__ == "__main__":
    g = Graph()
    g.add_edge('5', ['3', '7'])
    g.add_edge('3', ['2', '4'])
    g.add_edge('7', ['8'])
    g.add_edge('2', [])
    g.add_edge('4', ['8'])
    g.add_edge('8', [])

    print("Depth-First Search Traversal:")
    g.dfs('5')
