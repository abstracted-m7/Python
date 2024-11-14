from collections import deque

def bfs_shortest_path(graph, start, goal):
    queue = deque([[start]]) 
    visited = set()

    while queue:
        path = queue.popleft() 
        vertex = path[-1]      

        if vertex == goal:
            return path

   
        if vertex not in visited:
            visited.add(vertex)

            for neighbor in graph[vertex]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None  

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'] 
}

path = bfs_shortest_path(graph, 'A', 'F')
