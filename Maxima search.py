import random

def objective_function(x, y):
    return -(x**2 + y**2) + 4*x + 6*y + 10

def gradient_ascent(start_x, start_y, learning_rate=0.1, max_iterations=100):
    x, y = start_x, start_y
    
    for i in range(max_iterations):
        # Calculate partial derivatives (gradient)
        grad_x = -2*x + 4
        grad_y = -2*y + 6
        
        # Update position
        x += learning_rate * grad_x
        y += learning_rate * grad_y
        
        if i % 20 == 0:
            value = objective_function(x, y)
            print(f"Iteration {i}: ({x:.3f}, {y:.3f}) = {value:.3f}")
    
    return x, y, objective_function(x, y)

def random_search_maxima(bounds, max_iterations=1000):
    best_x, best_y = None, None
    best_value = float('-inf')
    
    for i in range(max_iterations):
        x = random.uniform(bounds[0], bounds[1])
        y = random.uniform(bounds[0], bounds[1])
        value = objective_function(x, y)
        
        if value > best_value:
            best_x, best_y, best_value = x, y, value
        
        if i % 200 == 0:
            print(f"Iteration {i}: Best = ({best_x:.3f}, {best_y:.3f}) = {best_value:.3f}")
    
    return best_x, best_y, best_value

# Example usage
if __name__ == "__main__":
    print("Gradient Ascent:")
    result = gradient_ascent(0, 0)
    print(f"Maximum found at: ({result[0]:.3f}, {result[1]:.3f}) = {result[2]:.3f}")
    
    print("\nRandom Search:")
    result = random_search_maxima((-5, 5))
    print(f"Maximum found at: ({result[0]:.3f}, {result[1]:.3f}) = {result[2]:.3f}")