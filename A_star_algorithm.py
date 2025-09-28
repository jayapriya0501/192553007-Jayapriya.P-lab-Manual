import heapq

def heuristic(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def get_neighbors(pos, grid):
    neighbors = []
    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        x, y = pos[0] + dx, pos[1] + dy
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0:
            neighbors.append((x, y))
    return neighbors

def a_star(grid, start, goal):
    open_list = [(0, start, [])]
    visited = set()
    
    while open_list:
        f_cost, current, path = heapq.heappop(open_list)
        
        if current == goal:
            return path + [current]
        
        if current in visited:
            continue
        visited.add(current)
        
        for neighbor in get_neighbors(current, grid):
            if neighbor not in visited:
                g_cost = len(path) + 1
                h_cost = heuristic(neighbor, goal)
                new_f_cost = g_cost + h_cost
                heapq.heappush(open_list, (new_f_cost, neighbor, path + [current]))
    
    return None

# Example usage
if __name__ == "__main__":
    grid = [
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    
    start = (0, 0)
    goal = (4, 4)
    
    path = a_star(grid, start, goal)
    print("Path found:", path if path else "No path exists")