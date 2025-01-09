# Retorna a posição (linha, coluna) do zero dada uma matriz
def find_zero(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return i, j

# Move o zero dada uma matriz e uma direção
def move(board, direction):
    i, j = find_zero(board)
    new_board = board.copy()
    
    if direction == "up" and i > 0:
        new_board[i][j], new_board[i-1][j] = new_board[i-1][j], new_board[i][j]
    elif direction == "down" and i < 2:
        new_board[i][j], new_board[i+1][j] = new_board[i+1][j], new_board[i][j]
    elif direction == "left" and j > 0:
        new_board[i][j], new_board[i][j-1] = new_board[i][j-1], new_board[i][j]
    elif direction == "right" and j < 2:
        new_board[i][j], new_board[i][j+1] = new_board[i][j+1], new_board[i][j]
    else:
        return None

    return new_board

# Função para gerar todos os estados vizinhos
def generate_neighbors(board):
    directions = ["up", "down", "left", "right"]
    neighbors = []

    for direction in directions:
        new_board = move(board, direction)
        if new_board is not None:  # Adiciona somente estados válidos
            neighbors.append(new_board)

    return neighbors

# Converte uma matriz para uma tupla (necessário para armazenar estados em um conjunto)
def board_to_tuple(board):
    return tuple(tuple(row) for row in board)

# Verifica se um estado foi visitado
def is_visited(board, visited):
    board_tuple = board_to_tuple(board)
    return board_tuple in visited

# Marca um estado como visitado
def mark_visited(board, visited):
    board_tuple = tuple(map(tuple, board))
    if board_tuple not in visited:
        visited.add(board_tuple)
        return True
    return False
