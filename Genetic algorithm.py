import random

def fitness(individual):
    # Maximize sum of bits (simple example)
    return sum(individual)

def create_individual(length):
    return [random.randint(0, 1) for _ in range(length)]

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(individual, mutation_rate=0.1):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]
    return individual

def genetic_algorithm(pop_size=20, gene_length=10, generations=50):
    population = [create_individual(gene_length) for _ in range(pop_size)]
    
    for gen in range(generations):
        population.sort(key=fitness, reverse=True)
        
        if gen % 10 == 0:
            best = population[0]
            print(f"Generation {gen}: Best = {best}, Fitness = {fitness(best)}")
        
        new_population = population[:pop_size//2]  # Keep top half
        
        while len(new_population) < pop_size:
            parent1 = random.choice(population[:pop_size//2])
            parent2 = random.choice(population[:pop_size//2])
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([mutate(child1), mutate(child2)])
        
        population = new_population[:pop_size]
    
    return max(population, key=fitness)

# Example usage
if __name__ == "__main__":
    best_individual = genetic_algorithm()
    print(f"Best solution: {best_individual}")
    print(f"Fitness: {fitness(best_individual)}")