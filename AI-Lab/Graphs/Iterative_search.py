# Simple Graph class
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, start, end):
        if start not in self.graph:
            self.graph[start] = []
        self.graph[start].append(end)
    
    def get_neighbors(self, node):
        return self.graph.get(node, [])

# Depth Limited Search (Helper function)
def depth_limited_search(graph, start, goal, limit):
    if start == goal:
        return True, [start]
    
    if limit <= 0:
        return False, []
    
    for neighbor in graph.get_neighbors(start):
        found, path = depth_limited_search(graph, neighbor, goal, limit - 1)
        if found:
            return True, [start] + path
    
    return False, []

# Iterative Deepening Search (Main function)
def iterative_deepening_search(graph, start, goal, max_depth=10):
    for depth in range(max_depth + 1):
        print(f"Searching at depth {depth}...")
        
        found, path = depth_limited_search(graph, start, goal, depth)
        
        if found:
            print(f"Found goal at depth {depth}!")
            return True, path
    
    print("Goal not found within max depth")
    return False, []

# Example usage
if __name__ == "__main__":
    # Create a simple graph
    g = Graph()
    
    # Add edges to make this graph:
    #   A → B → D
    #   A → C → E
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'E')
    
    print("Graph:")
    for node, neighbors in g.graph.items():
        print(f"{node} → {neighbors}")
    
    print("\n" + "="*30)
    
    # Test 1: Find D starting from A
    print("Test 1: Find D starting from A")
    found, path = iterative_deepening_search(g, 'A', 'D', 5)
    if found:
        print(f"Path: {' → '.join(path)}")
    
    print()
    
    # Test 2: Find E starting from A  
    print("Test 2: Find E starting from A")
    found, path = iterative_deepening_search(g, 'A', 'E', 5)
    if found:
        print(f"Path: {' → '.join(path)}")
    
    print()
    
