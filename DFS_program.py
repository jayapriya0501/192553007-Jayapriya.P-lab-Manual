def dfs_recursive(graph, vertex, visited, result):
    visited.add(vertex)
    result.append(vertex)
    
    for neighbor in graph.get(vertex, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, result)

def dfs_traversal(graph, start):
    visited = set()
    result = []
    dfs_recursive(graph, start, visited, result)
    return result

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor in reversed(graph.get(vertex, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result

def dfs_path_exists(graph, start, goal, visited=None):
    if visited is None:
        visited = set()
    
    if start == goal:
        return True
    
    visited.add(start)
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            if dfs_path_exists(graph, neighbor, goal, visited):
                return True
    return False

# Example usage
if __name__ == "__main__":
    graph = {0: [1, 2], 1: [0, 2, 4], 2: [0, 1, 3], 3: [2], 4: [1]}
    
    print("Graph:", graph)
    print("DFS recursive from 2:", dfs_traversal(graph, 2))
    print("DFS iterative from 2:", dfs_iterative(graph, 2))
    print("Path exists 0 to 4:", dfs_path_exists(graph, 0, 4))