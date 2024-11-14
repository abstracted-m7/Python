from collections import deque

def bfs(graph, start, goal):
    # Queue to store (node, path)
    queue = deque([(start, [start])])  
    visited = set([start])  # Set to track visited nodes
    
    while queue:
        node, path = queue.popleft()
        
        # If we've reached the goal, return the path
        if node == goal:
            return path
        
        # Explore all ngbr of the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))  # Append the new path to the queue
    
    return None  

def find_shortest_path(graph, start, goal):
    return bfs(graph, start, goal)

# Example graph as adjacency list (dictionary representation)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Test the BFS function
start = 'A'
goal = 'F'

shortest_path = find_shortest_path(graph, start, goal)

print("Shortest path:", shortest_path)
