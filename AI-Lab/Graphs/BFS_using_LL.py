from collections import deque

class Node:
    """Node class for linked list representation of adjacency list"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Linked list to store adjacent vertices"""
    def __init__(self):
        self.head = None
    
    def add_node(self, data):
        """Add a new node to the linked list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def display(self):
        """Display all nodes in the linked list"""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

class Graph:
    """Graph class using adjacency list with linked lists"""
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [LinkedList() for _ in range(vertices)]
    
    def add_edge(self, u, v):
        """Add an edge between vertices u and v"""
        # Add v to u's adjacency list
        self.adj_list[u].add_node(v)
        # For undirected graph, add u to v's adjacency list
        self.adj_list[v].add_node(u)
    
    def display_graph(self):
        """Display the graph structure"""
        for i in range(self.vertices):
            print(f"Vertex {i}: {self.adj_list[i].display()}")
    
    def bfs(self, start_vertex):
        """
        Breadth-First Search traversal starting from start_vertex
        Returns the BFS traversal order
        """
        # Check if start vertex is valid
        if start_vertex >= self.vertices or start_vertex < 0:
            return []
        
        # Keep track of visited vertices
        visited = [False] * self.vertices
        
        # Queue for BFS (using deque for efficient operations)
        queue = deque([start_vertex])
        visited[start_vertex] = True
        
        # Store the traversal order
        bfs_order = []
        
        while queue:
            # Dequeue a vertex
            current_vertex = queue.popleft()
            bfs_order.append(current_vertex)
            
            # Get all adjacent vertices of current vertex
            current = self.adj_list[current_vertex].head
            while current:
                adjacent_vertex = current.data
                if not visited[adjacent_vertex]:
                    visited[adjacent_vertex] = True
                    queue.append(adjacent_vertex)
                current = current.next
        
        return bfs_order
    
    def bfs_shortest_path(self, start, end):
        """
        Find shortest path between start and end vertices using BFS
        Returns the path as a list of vertices
        """
        if start >= self.vertices or end >= self.vertices or start < 0 or end < 0:
            return []
        
        if start == end:
            return [start]
        
        visited = [False] * self.vertices
        parent = [-1] * self.vertices
        queue = deque([start])
        visited[start] = True
        
        while queue:
            current_vertex = queue.popleft()
            
            # Explore all adjacent vertices
            current = self.adj_list[current_vertex].head
            while current:
                adjacent_vertex = current.data
                if not visited[adjacent_vertex]:
                    visited[adjacent_vertex] = True
                    parent[adjacent_vertex] = current_vertex
                    queue.append(adjacent_vertex)
                    
                    # If we reached the destination
                    if adjacent_vertex == end:
                        # Reconstruct path
                        path = []
                        vertex = end
                        while vertex != -1:
                            path.append(vertex)
                            vertex = parent[vertex]
                        return path[::-1]  # Reverse to get correct order
                
                current = current.next
        
        return []  # No path found

# Example usage and testing
def main():
    # Create a graph with 6 vertices (0 to 5)
    g = Graph(6)
    
    # Add edges
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 5)
    
    print("Graph structure:")
    g.display_graph()
    print()
    
    # Perform BFS from vertex 0
    print("BFS traversal starting from vertex 0:")
    bfs_result = g.bfs(0)
    print(bfs_result)
    print()
    
    # Find shortest path between vertices
    print("Shortest path from vertex 0 to vertex 5:")
    path = g.bfs_shortest_path(0, 5)
    print(path)
    print()
    
    # Test BFS from different starting points
    print("BFS traversal starting from vertex 2:")
    bfs_result_2 = g.bfs(2)
    print(bfs_result_2)

if __name__ == "__main__":
    main()