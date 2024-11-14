def dfs(graph, start, end, path, visited, shortest_path):
    # If we reached the destination node, check if the current path is the shortest one
    if start == end:
        if not shortest_path or len(path) < len(shortest_path):
            shortest_path.clear()
            shortest_path.extend(path)
        return

    visited.add(start)  # Mark the current node as visited

    for neighbor in graph[start]:
        if neighbor not in visited:
            path.append(neighbor)  # Add the neighbor to the path
            dfs(graph, neighbor, end, path, visited, shortest_path)
            path.pop()  # Backtrack (remove the neighbor from the path)

    visited.remove(start)  
    
def find_shortest_path(graph, start, end):
    visited = set()
    path = [start]
    shortest_path = []

    dfs(graph, start, end, path, visited, shortest_path)
    
    return shortest_path

# Example graph as adjacency list (dictionary representation)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start = 'A'
end = 'F'
shortest_path = find_shortest_path(graph, start, end)

print("Shortest path:", shortest_path)
