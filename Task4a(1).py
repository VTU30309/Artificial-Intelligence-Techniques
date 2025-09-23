# Mini-Max Algorithm Implementation

def minimax(depth, node_index, is_max, values, max_depth):
    # Base case: If we reach a leaf node
    if depth == max_depth:
        return values[node_index]

    if is_max:
        return max(
            minimax(depth + 1, node_index * 2, False, values, max_depth),
            minimax(depth + 1, node_index * 2 + 1, False, values, max_depth)
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, values, max_depth),
            minimax(depth + 1, node_index * 2 + 1, True, values, max_depth)
        )


# Example usage
if __name__ == "__main__":
    # Example tree with leaf node values
    values = [3, 5, 6, 9, 1, 2, 0, -1]  # Utility values at leaf nodes
    max_depth = 3  # Depth of the tree

    optimal_value = minimax(0, 0, True, values, max_depth)
    print(f"The optimal value is: {optimal_value}")
