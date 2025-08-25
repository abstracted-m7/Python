
def depth_limited_search(graph, start, goal, depth_limit):
    def dls(node, depth):
        if depth == 0:
            return None  # Depth limit reached
        if node == goal:
            return [node]  # Goal found
        for neighbor in graph.get(node, []):
            path = dls(neighbor, depth - 1)
            if path:
                return [node] + path  # Append current node to the path
        return None  # No path found

    return dls(start, depth_limit)


# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': []
}

start_node = 'A'
goal_node = 'E'
depth_limit = 2

result = depth_limited_search(graph, start_node, goal_node, depth_limit)
if result:
    print(f"Path found: {result}")
else:
    print("No path found within the depth limit.")
