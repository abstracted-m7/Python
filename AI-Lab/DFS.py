'''
#Basic way DFS with TC(O(1)), SC(O(n^2))--
from collections import deque
def dfs_shortest_path(graph, start, goal):
    stack = [[start]]  
    visited = set()

    while stack:
        path = stack.pop() 
        vertex = path[-1]  

        if vertex == goal:
            return path

     
        if vertex not in visited:
            visited.add(vertex)

        
            for neighbor in graph[vertex]:
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)

    return None  

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'] 
}

# Find a path from 'A' to 'F' using DFS
path = dfs_shortest_path(graph, 'A', 'F')
print("DFS path:", path)
'''

'''
Optimized way DFS with TC(O(1)) & SC(O(1)) --
'''
from collections import deque

def dfs_path_optimized(graph, start, goal):
    stack = [start]
    visited = set()
    parent = {start: None}  # Track parent relationships instead of full paths
    
    while stack:
        vertex = stack.pop()
        
        if vertex == goal:
            # Reconstruct path from parent relationships
            path = []
            current = goal
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]  # Reverse to get start->goal order
        
        if vertex not in visited:
            visited.add(vertex)
            
            for neighbor in graph[vertex]:
                if neighbor not in visited and neighbor not in parent:
                    parent[neighbor] = vertex
                    stack.append(neighbor)
    
    return None

def dfs_traverse_all(graph, start):  #for travarse the graph
    stack = [start]
    visited = set()
    traversal_order = []
    
    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.add(vertex)
            traversal_order.append(vertex)
            
            # Add neighbors in reverse order to maintain left-to-right traversal
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return traversal_order


# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B'] 
}

# Disconnected graph example
disconnected_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B'],
    'E': ['F'],  # Disconnected component
    'F': ['E'],
    'G': []      # Isolated node
}

print("=== Path Finding ===")
# DFS path (space optimized)
dfs_path = dfs_path_optimized(graph, 'A', 'D')
print(f"DFS path (optimized): {dfs_path}")


print("\n=== Graph Traversal ===")
# DFS traversal from starting node
dfs_order = dfs_traverse_all(graph, 'A')
print(f"DFS traversal from A: {dfs_order}")



