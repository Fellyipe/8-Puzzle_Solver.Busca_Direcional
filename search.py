from collections import deque
import functions as fun

# Realiza a busca bidirecional
def bidirectional_search(start_board, goal_board):
    # Inicialização
    stack = [(start_board, [start_board])]  # Pilha para DFS
    queue = deque([(goal_board, [goal_board])])  # Fila para BFS
    
    # Dicionários para armazenar os estados visitados e seus caminhos
    visited_start = {fun.board_to_tuple(start_board): [start_board]}
    visited_goal = {fun.board_to_tuple(goal_board): [goal_board]}

    # Marca os estados iniciais como visitados
    fun.mark_visited(start_board, visited_start)
    fun.mark_visited(goal_board, visited_goal)

    # Busca alternada
    while stack and queue:
        # Passo da busca em profundidade
        if stack:
            board, path_from_start = stack.pop()
            board_tuple = fun.board_to_tuple(board)

            if board_tuple in visited_goal:
                path_from_goal = visited_goal[board_tuple]
                solution_path = path_from_start + list(reversed(path_from_goal))[1:] # Combina os caminhos
                return solution_path  # Encontrou a interseção
            
            neighbors = fun.generate_neighbors(board)
            for neighbor in neighbors:
                neighbor_tuple = fun.board_to_tuple(neighbor)
                if neighbor_tuple not in visited_start:
                    new_path = path_from_start + [neighbor]
                    visited_start[neighbor_tuple] = new_path
                    stack.append((neighbor, new_path))

        # Passo da busca em largura
        if queue:
            board, path_from_goal = queue.popleft()
            board_tuple = fun.board_to_tuple(board)

            if board_tuple in visited_start:
                path_from_start = visited_start[board_tuple]
                solution_path = path_from_start + list(reversed(path_from_goal))[1:] # Combina os caminhos
                return solution_path  # Encontrou a interseção
            
            neighbors = fun.generate_neighbors(board)
            for neighbor in neighbors:
                neighbor_tuple = fun.board_to_tuple(neighbor)
                if neighbor_tuple not in visited_goal:
                    new_path = path_from_goal + [neighbor]
                    visited_goal[neighbor_tuple] = new_path
                    queue.append((neighbor, new_path))

    # Se nenhum estado intermediário for encontrado
    return None