import random
import itertools

def distance(city1, city2):
    return ((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)**0.5

def total_distance(tour, cities):
    total = 0
    for i in range(len(tour)):
        total += distance(cities[tour[i]], cities[tour[(i + 1) % len(tour)]])
    return total

def tsp_brute_force(cities):
    n = len(cities)
    min_distance = float('inf')
    best_tour = None
    
    for tour in itertools.permutations(range(n)):
        dist = total_distance(tour, cities)
        if dist < min_distance:
            min_distance = dist
            best_tour = tour
    
    return best_tour, min_distance

def tsp_nearest_neighbor(cities):
    n = len(cities)
    unvisited = set(range(1, n))
    tour = [0]
    
    while unvisited:
        current = tour[-1]
        nearest = min(unvisited, key=lambda x: distance(cities[current], cities[x]))
        tour.append(nearest)
        unvisited.remove(nearest)
    
    return tour, total_distance(tour, cities)

if __name__ == "__main__":
    cities = [(0, 0), (1, 2), (3, 1), (2, 3), (1, 0)]
    
    print("Cities:", cities)
    tour, dist = tsp_nearest_neighbor(cities)
    print(f"Nearest Neighbor - Tour: {tour}, Distance: {dist:.2f}")
    
    if len(cities) <= 5:  # Only for small instances
        tour, dist = tsp_brute_force(cities)
        print(f"Brute Force - Tour: {tour}, Distance: {dist:.2f}")