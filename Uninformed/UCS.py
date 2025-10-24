import heapq  # Built-in priority queue (min-heap)

class Graph:
    def __init__(self):
        self.graph = {}  # Store graph as adjacency list

    def add_edge(self, node, neighbor, cost):
        """Add an edge with its cost"""
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append((neighbor, cost))

    def ucs(self, start, goal):
        """Uniform Cost Search algorithm"""
        visited = set()
        queue = []  # Priority queue
        heapq.heappush(queue, (0, start))  # (cost, node)

        while queue:
            cost, node = heapq.heappop(queue)

            if node in visited:
                continue

            visited.add(node)
            print(f"Visited: {node}  |  Current cost: {cost}")

            if node == goal:
                print(f"\nReached goal '{goal}' with total cost = {cost}")
                return

            for neighbor, edge_cost in self.graph.get(node, []):
                if neighbor not in visited:
                    total_cost = cost + edge_cost
                    heapq.heappush(queue, (total_cost, neighbor))


# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 1)

    print("Uniform Cost Search (Using Built-ins):")
    g.ucs('A', 'D')

'''
UCS without built-in functions
'''
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor, cost):
        """Add an edge with cost"""
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append((neighbor, cost))

    def get_lowest_cost_node(self, queue):
        """Find and remove the node with the smallest cost manually"""
        min_index = 0
        for i in range(1, len(queue)):
            if queue[i][1] < queue[min_index][1]:
                min_index = i
        node, cost = queue[min_index]
        del queue[min_index]
        return node, cost

    def ucs(self, start, goal):
        """Uniform Cost Search without built-in functions"""
        visited = []   # Track visited nodes
        queue = [(start, 0)]  # (node, cost)

        while len(queue) > 0:
            node, cost = self.get_lowest_cost_node(queue)

            if node in visited:
                continue

            visited.append(node)
            print(f"Visited: {node}  |  Current cost: {cost}")

            if node == goal:
                print(f"\nReached goal '{goal}' with total cost = {cost}")
                return

            for neighbor, edge_cost in self.graph[node]:
                if neighbor not in visited:
                    total_cost = cost + edge_cost
                    queue.append((neighbor, total_cost))


# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 1)

    print("Uniform Cost Search (Without Built-ins):")
    g.ucs('A', 'D')
