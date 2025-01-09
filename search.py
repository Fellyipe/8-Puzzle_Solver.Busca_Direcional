from collections import deque
import numpy as np
import functions as fun

# Busca em profundidade limitada (DFS)
def depth_first_search(start_board, max_depth):
    stack = [(start_board, 0, [])]  # (estado, profundidade, caminho)
    visited = set()

    while stack:
        board, depth, path = stack.pop()
        if depth > max_depth:
            continue

        fun.mark_visited(board, visited)
        neighbors = fun.generate_neighbors(board)

        for neighbor in neighbors:
            if fun.mark_visited(neighbor, visited):
                stack.append((neighbor, depth + 1, path + [neighbor]))

    return visited

# Busca em largura (BFS)
def breadth_first_search(goal_board):
    queue = deque([(goal_board, [])])  # (estado, caminho)
    visited = set()

    while queue:
        board, path = queue.popleft()
        fun.mark_visited(board, visited)
        neighbors = fun.generate_neighbors(board)

        for neighbor in neighbors:
            if fun.mark_visited(neighbor, visited):
                queue.append((neighbor, path + [neighbor]))

    return visited

# Busca bidirecional
def bidirectional_search(start_board, goal_board, max_depth):
    visited_start = depth_first_search(start_board, max_depth)
    visited_goal = breadth_first_search(goal_board)

    for state in visited_start:
        if fun.is_visited(state, visited_goal):
            return state  # Interseção encontrada

    return None  # Sem interseção