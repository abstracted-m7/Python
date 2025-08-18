
from collections import deque

def bfs_shortest_path(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a 
        # new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

# DFS to find all paths
def dfs_all_paths(graph, start, goal, path=None, visited=None):

    if path is None:
        path = [start]

    if visited is None:
        visited = set()

    if start == goal:
        return [path]
    
    paths = [] #empty list for storing the path

    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            new_paths = dfs_all_paths(graph, neighbor, goal, path + [neighbor], visited.copy()) #recursive way passing new values
            for p in new_paths:
                paths.append(p)
    return paths


# validate the arguments and passing values
if __name__ == "__main__":

    graph ={
        'A': ['B','C'],
        'B': ['A', 'D'],
        'C': ['A','F'],
        'D': ['B', 'E'],
        'E': ['D','F'],
        'F': ['E', 'C']
    }

    print(f"The graph is : {graph}")

    print()

    start_node = input("Enter the start node : ")
    goal_node = input("Enter the goal node : ")


    #Finding the shortest path
    path = bfs_shortest_path(graph, start_node, goal_node)

    if path:
        print(f"The shortest path is : {path}")
    else:
        print(f"Path not found from {start_node} to {goal_node}") #edge case handle


    print()

    #passing arguments to the dfs function
    all_paths = dfs_all_paths(graph, start_node, goal_node)
    
    #redirect all paths and finding the critical path
    if all_paths:
        # Critical path = longest path
        critical = max(all_paths, key=len)
        print(f"All paths: {all_paths}")
        print(f"The critical path (longest) is : {critical}")
    else:
        print("No path found!")
