def minimax_alpha_beta(node, depth, alpha, beta, maximizing_player, game_tree):
    if depth == 0 or node not in game_tree:
        return node  # Leaf node value
    if maximizing_player:
        max_eval = float('-inf')
        for child in game_tree[node]:
            eval_score = minimax_alpha_beta(child, depth - 1, alpha, beta, False, game_tree)
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                print(f"Pruning at node {node}, child {child}")
                break  # Beta cutoff
        return max_eval
    else:
        min_eval = float('inf')
        for child in game_tree[node]:
            eval_score = minimax_alpha_beta(child, depth - 1, alpha, beta, True, game_tree)
            min_eval = min(min_eval, eval_score)
            beta = min(beta, eval_score)
            if beta <= alpha:
                print(f"Pruning at node {node}, child {child}")
                break  # Alpha cutoff
        return min_eval
def find_best_move(game_tree, root, depth):
    best_move = None
    best_value = float('-inf')
    for child in game_tree[root]:
        value = minimax_alpha_beta(child, depth - 1, float('-inf'), float('inf'), False, game_tree)
        print(f"Move to {child}: value = {value}")
        if value > best_value:
            best_value = value
            best_move = child
    return best_move, best_value
if __name__ == "__main__":
    game_tree = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': [3, 5],
        'E': [6, 9],
        'F': [1, 2],
        'G': [0, 1]
    } # Game tree representation: node -> [children]
    print("Alpha-Beta Pruning Example:")
    best_move, best_value = find_best_move(game_tree, 'A', 3)
    print(f"Best move: {best_move}, Best value: {best_value}")