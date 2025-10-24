import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor, cost):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append((neighbor, cost))

    def astar(self, start, goal, heuristic):
        """A* Search Algorithm using built-in heapq"""
        visited = set()
        queue = []  # Priority queue
        heapq.heappush(queue, (0 + heuristic[start], 0, start))  # (f, g, node)

        while queue:
            f, g, node = heapq.heappop(queue)

            if node in visited:
                continue
            visited.add(node)
            print(f"Visited: {node} | g(n): {g} | h(n): {heuristic[node]} | f(n): {f}")

            if node == goal:
                print(f"\nReached goal '{goal}' with total cost = {g}")
                return

            for neighbor, edge_cost in self.graph.get(node, []):
                if neighbor not in visited:
                    g_new = g + edge_cost
                    f_new = g_new + heuristic[neighbor]
                    heapq.heappush(queue, (f_new, g_new, neighbor))

if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 1)

    heuristic = {'A': 7, 'B': 6, 'C': 2, 'D': 0}

    print("A* Search (Using Built-ins):")
    g.astar('A', 'D', heuristic)


'''
A* Search without built-in functions
'''

class GraphManual:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor, cost):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append((neighbor, cost))

    def get_lowest_f(self, queue):
        """Manually find node with smallest f"""
        min_index = 0
        for i in range(1, len(queue)):
            if queue[i][0] < queue[min_index][0]:
                min_index = i
        f, g, node = queue[min_index]
        del queue[min_index]
        return f, g, node

    def astar(self, start, goal, heuristic):
        visited = []
        queue = [(heuristic[start], 0, start)]  # (f, g, node)

        while len(queue) > 0:
            f, g, node = self.get_lowest_f(queue)

            if node in visited:
                continue
            visited.append(node)
            print(f"Visited: {node} | g(n): {g} | h(n): {heuristic[node]} | f(n): {f}")

            if node == goal:
                print(f"\nReached goal '{goal}' with total cost = {g}")
                return

            for neighbor, edge_cost in self.graph[node]:
                if neighbor not in visited:
                    g_new = g + edge_cost
                    f_new = g_new + heuristic[neighbor]
                    queue.append((f_new, g_new, neighbor))

if __name__ == "__main__":
    g = GraphManual()
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 1)

    heuristic = {'A': 7, 'B': 6, 'C': 2, 'D': 0}

    print("A* Search (Without Built-ins):")
    g.astar('A', 'D', heuristic)
