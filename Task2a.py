def generate_neighbours(route):
    neighbours = []
    for i in range(len(route)):
        for j in range(i + 1, len(route)):
            neighbour = route.copy()
            neighbour[i], neighbour[j] = neighbour[j], neighbour[i]
            neighbours.append(neighbour)
    return neighbours

# Example
route = [0, 1, 2, 3]
print("Original route:", route)
print("Neighbours:")
for n in generate_neighbours(route):
    print(n)
