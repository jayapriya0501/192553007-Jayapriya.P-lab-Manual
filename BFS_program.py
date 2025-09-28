from collections import deque

def bfs_traversal(graph, start):
    visited = set([start])
    queue = deque([start])
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

def bfs_shortest_path(graph, start, goal):
    if start == goal:
        return [start]
    
    visited = set([start])
    queue = deque([(start, [start])])
    
    while queue:
        vertex, path = queue.popleft()
        
        for neighbor in graph.get(vertex, []):
            if neighbor == goal:
                return path + [neighbor]
            
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None

# Example usage
if __name__ == "__main__":
    # Create graph as adjacency list
    graph = {
        0: [1, 2],
        1: [0, 2, 4],
        2: [0, 1, 3],
        3: [2],
        4: [1]
    }
    
    print("Graph:", graph)
    print("BFS traversal from 2:", bfs_traversal(graph, 2))
    print("Shortest path 0 to 3:", bfs_shortest_path(graph, 0, 3))