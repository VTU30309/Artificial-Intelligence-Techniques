import random

def generate_random_solution(num_cities):
    route = list(range(num_cities))
    random.shuffle(route)
    return route

# Example
print("Random route (5 cities):", generate_random_solution(5))
print("Random route (5 cities):", generate_random_solution(5))
