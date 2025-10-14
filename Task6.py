# Map Coloring using Constraint Satisfaction (Greedy Algorithm)

# Graph Representation (Adjacency List)
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['A', 'C']
}

# Available color list
colors = ['Red', 'Green', 'Blue', 'Yellow']

# Dictionary to store color assigned to each node
assigned_colors = {}

def greedy_coloring(graph):
    for node in graph:
        # Find colors used by adjacent nodes
        used_colors = set(assigned_colors.get(neigh) for neigh in graph[node] if neigh in assigned_colors)
        
        # Assign the lowest-numbered available color
        for color in colors:
            if color not in used_colors:
                assigned_colors[node] = color
                break

    return assigned_colors

# Run the algorithm
result = greedy_coloring(graph)

# Display the result
print("Map Coloring Result (No adjacent same colors):\n")
for node, color in result.items():
    print(f"Territory {node} --> {color}")
