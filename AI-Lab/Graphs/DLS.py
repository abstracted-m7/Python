def depth_limited_search(graph, start_node, goal_node, depth_limit):
    # Recursive helper function for DLS
    def recursive_dls(current_node, current_depth):
        if current_node == goal_node:
            return [current_node]  # Goal found, return path
        if current_depth == depth_limit:
            return "cutoff"  # Depth limit reached
        
        # Explore neighbors
        for neighbor in graph.get(current_node, []):
            result = recursive_dls(neighbor, current_depth + 1)
            if result == "cutoff":
                continue  # Continue searching other paths at the same depth
            elif result != "failure":
                return [current_node] + result  # Path found
        
        return "failure"  # No path found within this branch

    return recursive_dls(start_node, 0)

# Example Usage (assuming a graph representation)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [], 'E': [], 'F': [], 'G': []
}
path = depth_limited_search(graph, 'A', 'G', 2)

if path == "failure":
    print("Path not found")
elif path == "cutoff":
    print("Search cutoff due to depth limit")
else:
    print(f"The path is: {path}")
