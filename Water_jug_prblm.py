from collections import deque

def get_moves(state, cap1, cap2):
    j1, j2 = state
    moves = [
        (cap1, j2),  # Fill jug 1
        (j1, cap2),  # Fill jug 2
        (0, j2),     # Empty jug 1
        (j1, 0),     # Empty jug 2
        (max(0, j1 - (cap2 - j2)), min(cap2, j1 + j2)),  # Pour 1 to 2
        (min(cap1, j1 + j2), max(0, j2 - (cap1 - j1)))   # Pour 2 to 1
    ]
    return moves

def water_jug_bfs(cap1, cap2, target):
    start = (0, 0)
    if target in start:
        return [start]
    
    queue = deque([(start, [start])])
    visited = {start}
    
    while queue:
        state, path = queue.popleft()
        
        for next_state in get_moves(state, cap1, cap2):
            if next_state not in visited:
                new_path = path + [next_state]
                
                if target in next_state:
                    return new_path
                
                visited.add(next_state)
                queue.append((next_state, new_path))
    
    return None

def print_solution(solution):
    if solution:
        print("Solution steps:")
        for i, state in enumerate(solution):
            print(f"Step {i}: {state}")
    else:
        print("No solution found")

# Example usage
if __name__ == "__main__":
    print("Water Jug Problem: 4L and 3L jugs, target 2L")
    solution = water_jug_bfs(4, 3, 2)
    print_solution(solution)
    
    print("\nWater Jug Problem: 5L and 3L jugs, target 4L")
    solution = water_jug_bfs(5, 3, 4)
    print_solution(solution)