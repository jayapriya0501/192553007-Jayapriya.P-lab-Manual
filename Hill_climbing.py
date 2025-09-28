import random

def objective_function(x):
    return -(x - 3) ** 2 + 10

def hill_climbing(start, max_iterations=100):
    current = start
    current_value = objective_function(current)
    
    for i in range(max_iterations):
        neighbors = [current + 0.1, current - 0.1]
        best_neighbor = max(neighbors, key=objective_function)
        best_value = objective_function(best_neighbor)
        
        if best_value <= current_value:
            print(f"Local maximum at iteration {i}")
            break
        
        current = best_neighbor
        current_value = best_value
        print(f"Iteration {i}: x = {current:.3f}, f(x) = {current_value:.3f}")
    
    return current, current_value

def hill_climbing_random_restart(restarts=3):
    best_state, best_value = None, float('-inf')
    
    for i in range(restarts):
        start = random.uniform(-10, 10)
        print(f"\nRestart {i+1} from {start:.3f}")
        state, value = hill_climbing(start, 50)
        
        if value > best_value:
            best_state, best_value = state, value
    
    return best_state, best_value

# Example usage
if __name__ == "__main__":
    print("Simple Hill Climbing:")
    result = hill_climbing(random.uniform(-10, 10))
    print(f"Final: x = {result[0]:.3f}, f(x) = {result[1]:.3f}")
    
    print("\nHill Climbing with Random Restart:")
    best = hill_climbing_random_restart()
    print(f"Best overall: x = {best[0]:.3f}, f(x) = {best[1]:.3f}")