def calculate_route_length(route, distance_matrix):
    length = 0
    for i in range(len(route) - 1):
        length += distance_matrix[route[i]][route[i+1]]
    length += distance_matrix[route[-1]][route[0]]  # return to start
    return length

# Example
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
route = [0, 1, 2, 3]
print("Route:", route)
print("Length of route:", calculate_route_length(route, distance_matrix))
