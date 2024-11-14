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
