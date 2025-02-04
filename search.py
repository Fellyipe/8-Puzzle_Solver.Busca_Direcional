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

def bidirectional_mixed_search(start_board, goal_board):
    queue_start = deque([(start_board, [start_board])])  # Busca em largura (BFS)
    stack_goal = [(goal_board, [goal_board])]  # Busca em profundidade (DFS)
    
    visited_start = {fun.board_to_tuple(start_board): [start_board]}
    visited_goal = {fun.board_to_tuple(goal_board): [goal_board]}
    
    while queue_start and stack_goal:
        if queue_start:
            board, path_from_start = queue_start.popleft()
            board_tuple = fun.board_to_tuple(board)

            if board_tuple in visited_goal:
                path_from_goal = visited_goal[board_tuple]
                return path_from_start + list(reversed(path_from_goal))[1:]
            
            neighbors = fun.generate_neighbors(board)
            for neighbor in neighbors:
                neighbor_tuple = fun.board_to_tuple(neighbor)
                if neighbor_tuple not in visited_start:
                    visited_start[neighbor_tuple] = path_from_start + [neighbor]
                    queue_start.append((neighbor, visited_start[neighbor_tuple]))
        
        if stack_goal:
            board, path_from_goal = stack_goal.pop()
            board_tuple = fun.board_to_tuple(board)

            if board_tuple in visited_start:
                path_from_start = visited_start[board_tuple]
                return path_from_start + list(reversed(path_from_goal))[1:]
            
            neighbors = fun.generate_neighbors(board)
            for neighbor in neighbors:
                neighbor_tuple = fun.board_to_tuple(neighbor)
                if neighbor_tuple not in visited_goal:
                    visited_goal[neighbor_tuple] = path_from_goal + [neighbor]
                    stack_goal.append((neighbor, visited_goal[neighbor_tuple]))
    
    return None  # Nenhuma solução encontrada

def bidirectional_breadth_first_search(start_board, goal_board):
    queue_start = deque([(start_board, [start_board])])
    queue_goal = deque([(goal_board, [goal_board])])
    
    visited_start = {fun.board_to_tuple(start_board): [start_board]}
    visited_goal = {fun.board_to_tuple(goal_board): [goal_board]}
    
    while queue_start and queue_goal:
        if queue_start:
            board, path_from_start = queue_start.popleft()
            board_tuple = fun.board_to_tuple(board)

            if board_tuple in visited_goal:
                path_from_goal = visited_goal[board_tuple]
                return path_from_start + list(reversed(path_from_goal))[1:]
            
            neighbors = fun.generate_neighbors(board)
            for neighbor in neighbors:
                neighbor_tuple = fun.board_to_tuple(neighbor)
                if neighbor_tuple not in visited_start:
                    visited_start[neighbor_tuple] = path_from_start + [neighbor]
                    queue_start.append((neighbor, visited_start[neighbor_tuple]))
        
        if queue_goal:
            board, path_from_goal = queue_goal.popleft()
            board_tuple = fun.board_to_tuple(board)

            if board_tuple in visited_start:
                path_from_start = visited_start[board_tuple]
                return path_from_start + list(reversed(path_from_goal))[1:]
            
            neighbors = fun.generate_neighbors(board)
            for neighbor in neighbors:
                neighbor_tuple = fun.board_to_tuple(neighbor)
                if neighbor_tuple not in visited_goal:
                    visited_goal[neighbor_tuple] = path_from_goal + [neighbor]
                    queue_goal.append((neighbor, visited_goal[neighbor_tuple]))
    
    return None  # Nenhuma solução encontrada

def bidirectional_depth_first_search(start_board, goal_board):
    stack_start = [(start_board, [start_board])]
    stack_goal = [(goal_board, [goal_board])]
    
    visited_start = {fun.board_to_tuple(start_board): [start_board]}
    visited_goal = {fun.board_to_tuple(goal_board): [goal_board]}
    
    while stack_start and stack_goal:
        if stack_start:
            board, path_from_start = stack_start.pop()
            board_tuple = fun.board_to_tuple(board)

            if board_tuple in visited_goal:
                path_from_goal = visited_goal[board_tuple]
                return path_from_start + list(reversed(path_from_goal))[1:]
            
            neighbors = fun.generate_neighbors(board)
            for neighbor in neighbors:
                neighbor_tuple = fun.board_to_tuple(neighbor)
                if neighbor_tuple not in visited_start:
                    visited_start[neighbor_tuple] = path_from_start + [neighbor]
                    stack_start.append((neighbor, visited_start[neighbor_tuple]))
        
        if stack_goal:
            board, path_from_goal = stack_goal.pop()
            board_tuple = fun.board_to_tuple(board)

            if board_tuple in visited_start:
                path_from_start = visited_start[board_tuple]
                return path_from_start + list(reversed(path_from_goal))[1:]
            
            neighbors = fun.generate_neighbors(board)
            for neighbor in neighbors:
                neighbor_tuple = fun.board_to_tuple(neighbor)
                if neighbor_tuple not in visited_goal:
                    visited_goal[neighbor_tuple] = path_from_goal + [neighbor]
                    stack_goal.append((neighbor, visited_goal[neighbor_tuple]))
    
    return None  # Nenhuma solução encontrada