import random

# 1) Neighbours: all 2-swap permutations
def generate_neighbours(route):
    neighbours = []
    n = len(route)
    for i in range(n - 1):
        for j in range(i + 1, n):
            neighbour = route.copy()
            neighbour[i], neighbour[j] = neighbour[j], neighbour[i]
            neighbours.append(neighbour)
    return neighbours

# 2) Route length (round trip)
def calculate_route_length(route, distance_matrix):
    total = 0
    for i in range(len(route) - 1):
        total += distance_matrix[route[i]][route[i + 1]]
    total += distance_matrix[route[-1]][route[0]]  # return to start
    return total

# 3) Random route
def generate_random_solution(num_cities):
    route = list(range(num_cities))
    random.shuffle(route)
    return route

# 4) Hill Climbing (best-improvement)
def hill_climbing(distance_matrix, max_iterations=1000, start=None):
    current_solution = start[:] if start is not None else generate_random_solution(len(distance_matrix))
    current_cost = calculate_route_length(current_solution, distance_matrix)

    for _ in range(max_iterations):
        neighbours = generate_neighbours(current_solution)
        # pick the best neighbour by cost
        best_neighbour = min(neighbours, key=lambda r: calculate_route_length(r, distance_matrix))
        best_cost = calculate_route_length(best_neighbour, distance_matrix)

        if best_cost < current_cost:
            current_solution, current_cost = best_neighbour, best_cost
        else:
            break  # local optimum

    return current_solution, current_cost

# ---- Example run ----
if __name__ == "__main__":
    random.seed(42)  # reproducible demo
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]

    best_route, best_cost = hill_climbing(distance_matrix)
    print("Best route:", best_route)
    print("Best cost:", best_cost)
