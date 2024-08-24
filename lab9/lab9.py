print("Task 1 Minimax Algorithm Implementation")

import math

# Function to check if the node is a terminal node (leaf node)
def is_terminal_node(node):
    # In this example, terminal nodes are represented by integers (leaf nodes)
    return isinstance(node, int)

# Function to evaluate the value of a node (for terminal nodes)
def evaluate_node(node):
    # Simply return the node's value
    return node

# Function to get the children of a node
def get_children(node):
    # For the sake of this example, we assume the following structure:
    game_tree = {
        'Root': [3, 5, 6, 9],
        3: [],
        5: [],
        6: [],
        9: []
    }
    return game_tree[node]

# Minimax algorithm implementation
def minimax(node, depth, maximizingPlayer):
    if depth == 0 or is_terminal_node(node):
        return evaluate_node(node)
    
    if maximizingPlayer:
        maxEval = -math.inf
        for child in get_children(node):
            eval = minimax(child, depth - 1, False)
            maxEval = max(maxEval, eval)
        return maxEval
    else:
        minEval = math.inf
        for child in get_children(node):
            eval = minimax(child, depth - 1, True)
            minEval = min(minEval, eval)
        return minEval

# Example usage of Minimax
def example_minimax():
    # Start from the 'Root', depth = 1 (just one level of depth), maximizing player starts
    return minimax('Root', 1, True)

# Execute Minimax
result = example_minimax()
print(f"Minimax result: {result}")


print("Task 2 Alpha beta pruning  Implementation")

import math

# Function to check if the node is a terminal node (leaf node)
def is_terminal_node(node):
    # In this example, terminal nodes are represented by integers (leaf nodes)
    return isinstance(node, int)

# Function to evaluate the value of a node (for terminal nodes)
def evaluate_node(node):
    # Simply return the node's value
    return node

# Function to get the children of a node
def get_children(node):
    # For the sake of this example, we assume the following structure:
    game_tree = {
        'Root': [3, 5, 6, 9],
        3: [],
        5: [],
        6: [],
        9: []
    }
    return game_tree[node]

# Alpha-Beta Pruning algorithm implementation
def minimax(node, depth, maximizingPlayer, alpha, beta):
    if depth == 0 or is_terminal_node(node):
        return evaluate_node(node)
    
    if maximizingPlayer:
        maxEval = -math.inf
        for child in get_children(node):
            eval = minimax(child, depth - 1, False, alpha, beta)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = math.inf
        for child in get_children(node):
            eval = minimax(child, depth - 1, True, alpha, beta)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval

# Example usage of Alpha-Beta Pruning
def example_alpha_beta():
    # Start from the 'Root', depth = 1, maximizing player starts, initial alpha = -inf, beta = +inf
    return minimax('Root', 1, True, -math.inf, math.inf)

# Execute Alpha-Beta Pruning
result_ab = example_alpha_beta()
print(f"Alpha-Beta Pruning result: {result_ab}")
