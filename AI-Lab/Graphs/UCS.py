import heapq
from collections import defaultdict, deque

class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v, weight):
        """Add weighted edge to the graph"""
        self.graph[u].append((v, weight))
    
    def get_neighbors(self, node):
        return self.graph[node]

class UCS:
    
    def __init__(self, graph):
        self.graph = graph
    
    def search(self, start, goal):

        # Priority queue: (cost, node, path)
        priority_queue = [(0, start, [start])]
        
        # Set to keep track of visited nodes with their minimum cost
        visited = {}
        
        while priority_queue:
            current_cost, current_node, path = heapq.heappop(priority_queue)
            
            # Skip if we've already found a better path to this node
            if current_node in visited and visited[current_node] <= current_cost:
                continue
            
            # Mark node as visited with current cost
            visited[current_node] = current_cost
            
            # Check if goal is reached
            if current_node == goal:
                return path, current_cost
            
            # Explore neighbors
            for neighbor, edge_cost in self.graph.get_neighbors(current_node):
                new_cost = current_cost + edge_cost
                
                # Only add to queue if we haven't visited or found a better path
                if neighbor not in visited or visited[neighbor] > new_cost:
                    new_path = path + [neighbor]
                    heapq.heappush(priority_queue, (new_cost, neighbor, new_path))
        
        # Goal not found
        return None, float('inf')
    
    def search_with_details(self, start, goal):

        priority_queue = [(0, start, [start])]
        visited = {}
        nodes_explored = 0
        step_details = []
        
        while priority_queue:
            current_cost, current_node, path = heapq.heappop(priority_queue)
            nodes_explored += 1
            
            step_info = {
                'step': nodes_explored,
                'current_node': current_node,
                'current_cost': current_cost,
                'current_path': path.copy(),
                'queue_size': len(priority_queue)
            }
            step_details.append(step_info)
            
            if current_node in visited and visited[current_node] <= current_cost:
                continue
            
            visited[current_node] = current_cost
            
            if current_node == goal:
                return {
                    'path': path,
                    'cost': current_cost,
                    'nodes_explored': nodes_explored,
                    'step_details': step_details,
                    'success': True
                }
            
            for neighbor, edge_cost in self.graph.get_neighbors(current_node):
                new_cost = current_cost + edge_cost
                
                if neighbor not in visited or visited[neighbor] > new_cost:
                    new_path = path + [neighbor]
                    heapq.heappush(priority_queue, (new_cost, neighbor, new_path))
        
        return {
            'path': None,
            'cost': float('inf'),
            'nodes_explored': nodes_explored,
            'step_details': step_details,
            'success': False
        }

# Example usage and testing
def create_sample_graph():
    """Create a sample graph for testing UCS"""
    g = Graph()
    
    # Add edges (node1, node2, weight)
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'C', 1)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 8)
    g.add_edge('C', 'E', 10)
    g.add_edge('D', 'E', 2)
    g.add_edge('D', 'F', 6)
    g.add_edge('E', 'F', 3)
    
    return g

def demonstrate_ucs():
  
    # Create sample graph
    graph = create_sample_graph()
    ucs = UCS(graph)
    
    # Test cases
    test_cases = [
        ('A', 'F'),
        ('A', 'E'),
        ('B', 'F'),
        ('A', 'G')  # Non-existent goal
    ]
    

    # Detailed search example
    print("Searching from A to F with step details:")
    
    result = ucs.search_with_details('A', 'F')
    
    if result['success']:
        print(f"Path: {' -> '.join(result['path'])}")
        print(f"Cost: {result['cost']}")
        print(f"Nodes explored: {result['nodes_explored']}")


if __name__ == "__main__":
    demonstrate_ucs()
