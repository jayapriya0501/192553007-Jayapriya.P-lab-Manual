import random
import math

def objective_function(x):
    return -(x - 3)**2 + 10

def get_neighbor(x, step_size=0.5):
    return x + random.uniform(-step_size, step_size)

def simulated_annealing(start, max_iterations=1000, initial_temp=100):
    current = start
    current_value = objective_function(current)
    best = current
    best_value = current_value
    temperature = initial_temp
    
    for i in range(max_iterations):
        neighbor = get_neighbor(current)
        neighbor_value = objective_function(neighbor)
        
        delta = neighbor_value - current_value
        
        if delta > 0 or random.random() < math.exp(delta / temperature):
            current = neighbor
            current_value = neighbor_value
            
            if current_value > best_value:
                best = current
                best_value = current_value
        
        temperature *= 0.995  # Cool down
        
        if i % 100 == 0:
            print(f"Iteration {i}: x = {current:.3f}, f(x) = {current_value:.3f}, temp = {temperature:.3f}")
    
    return best, best_value

# Example usage
if __name__ == "__main__":
    start_point = random.uniform(-10, 10)
    print(f"Starting from: {start_point:.3f}")
    
    result = simulated_annealing(start_point)
    print(f"Final result: x = {result[0]:.3f}, f(x) = {result[1]:.3f}")