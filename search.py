from collections import deque
import functions as fun

# Realiza a busca bidirecional
def bidirectional_search(start_board, goal_board):
    # Inicialização
    stack = [start_board]  # Pilha para DFS
    queue = deque([goal_board])  # Fila para BFS
    visited_start = set()  # Estados visitados pelo início
    visited_goal = set()  # Estados visitados pelo final

    # Marca os estados iniciais como visitados
    fun.mark_visited(start_board, visited_start)
    fun.mark_visited(goal_board, visited_goal)

    i = 0

    # Busca alternada
    while stack and queue:
        i += 1
        # Passo da busca em profundidade
        if stack:
            board = stack.pop()
            if fun.board_to_tuple(board) in visited_goal:
                return board  # Encontrou a interseção
            neighbors = fun.generate_neighbors(board)
            
            for neighbor in neighbors:
                if not fun.is_visited(neighbor, visited_start):
                    fun.mark_visited(neighbor, visited_start)
                    stack.append(neighbor)
                    # print("\n\033[34mDFS Vizinho na iteração \033[0m" + str(i))
                    # print(neighbor)

        # Passo da busca em largura
        if queue:
            board = queue.popleft()
            if fun.board_to_tuple(board) in visited_start:
                return board  # Encontrou a interseção
            neighbors = fun.generate_neighbors(board)
            for neighbor in neighbors:
                if not fun.is_visited(neighbor, visited_goal):
                    fun.mark_visited(neighbor, visited_goal)
                    queue.append(neighbor)
                    # print("\n\033[33mBFS Vizinho na iteração \033[0m" + str(i))
                    # print(neighbor)

    # Se nenhum estado intermediário for encontrado
    return None