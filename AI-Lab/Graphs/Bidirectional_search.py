
def build_path(start_visited, goal_visited, meeting_point):
    # Build path from start to meeting point
    path = []
    current = meeting_point
    while current is not None:
        path.append(current)
        current = start_visited[current]
    
    path.reverse()  # Reverse to get correct order
    
    # Add path from meeting point to goal
    current = goal_visited[meeting_point]
    while current is not None:
        path.append(current)
        current = goal_visited[current]
    
    return path

def simple_bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]
    
    # Two queues for BFS from both directions
    start_queue = [start]
    goal_queue = [goal]
    
    # Track visited nodes
    start_visited = {start: None}
    goal_visited = {goal: None}
    
    while start_queue or goal_queue:
        # Forward search
        if start_queue:
            node = start_queue.pop(0)
            if node in goal_visited:
                return build_path(start_visited, goal_visited, node)
            for neighbor in graph[node]:
                if neighbor not in start_visited:
                    start_visited[neighbor] = node
                    start_queue.append(neighbor)
        
        # Backward search
        if goal_queue:
            node = goal_queue.pop(0)
            if node in start_visited:
                return build_path(start_visited, goal_visited, node)
            for neighbor in graph[node]:
                if neighbor not in goal_visited:
                    goal_visited[neighbor] = node
                    goal_queue.append(neighbor)
    
    return []  # No path



graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B', 'G'],
        'E': ['B', 'F', 'H'],
        'F': ['C', 'E', 'I'],
        'G': ['D'],
        'H': ['E', 'I'],
        'I': ['F', 'H']
    }
print("\n" + "="*40)
print("SIMPLE VERSION:")
result = simple_bidirectional_search(graph, 'A', 'I')
print(f"A to I: {' -> '.join(result) if result else 'No path'}")