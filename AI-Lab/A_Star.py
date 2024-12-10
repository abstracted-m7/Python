from queue import PriorityQueue

def a_star_search(graph, start, goal, heuristic):
    """
    Perform A* search on a given graph.

    Parameters:
        graph (dict): The graph represented as an adjacency list where each key is a node
                      and the value is a list of tuples (neighbor, cost).
        start (str): The starting node.
        goal (str): The goal node.
        heuristic (dict): A dictionary containing heuristic values for each node.

    Returns:
        list: The optimal path from start to goal.
    """
    # Priority queue to store nodes with their f-score (priority)
    open_set = PriorityQueue()
    open_set.put((0, start))

    # Store the cost to reach each node
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    # Store the path (came from)
    came_from = {}

    while not open_set.empty():
        current_priority, current_node = open_set.get()

        # If the goal is reached, reconstruct the path
        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            return path[::-1]

        # Explore neighbors
        for neighbor, cost in graph[current_node]:
            tentative_g_score = g_score[current_node] + cost

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic[neighbor]
                open_set.put((f_score, neighbor))

    return []  # Return an empty list if no path is found

# Example usage
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 4)],
    'C': [('F', 2)],
    'D': [('G', 5)],
    'E': [('G', 1)],
    'F': [('G', 3)],
    'G': []
}

heuristic = {
    'A': 7, 'B': 6, 'C': 5, 'D': 4, 'E': 3, 'F': 2, 'G': 0
}

start = 'A'
goal = 'G'

optimal_path = a_star_search(graph, start, goal, heuristic)
print(f"Optimal path from {start} to {goal}: {optimal_path}")
