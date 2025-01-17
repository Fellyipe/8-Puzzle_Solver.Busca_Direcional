import numpy as np

# Retorna a posição (linha, coluna) do zero dada uma matriz
def find_zero(board):
    return np.argwhere(board == 0)[0]  # Encontra a posição do valor 0

# Move o zero dada uma matriz e uma direção
def move(board, direction):
    i, j = find_zero(board)
    length = len(board)
    new_board = board.copy()  # Copia a matriz

    if direction == "up" and i > 0:
        new_board[i, j], new_board[i-1, j] = new_board[i-1, j], new_board[i, j]
    elif direction == "down" and i < length - 1:
        new_board[i, j], new_board[i+1, j] = new_board[i+1, j], new_board[i, j]
    elif direction == "left" and j > 0:
        new_board[i, j], new_board[i, j-1] = new_board[i, j-1], new_board[i, j]
    elif direction == "right" and j < length - 1:
        new_board[i, j], new_board[i, j+1] = new_board[i, j+1], new_board[i, j]
    else:
        return None

    return new_board

# Função para gerar todos os estados vizinhos
def generate_neighbors(board):
    directions = ["up", "down", "left", "right"]
    neighbors = []

    for direction in directions:
        new_board = move(board, direction)
        if new_board is not None:
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
    board_tuple = board_to_tuple(board)
    if board_tuple not in visited:
        visited.add(board_tuple)
        return True
    return False

# Converte para uma lista 1D e conta o número de inversões em um tabuleiro.
def count_inversions(board):
    # Uma inversão ocorre quando um número maior aparece antes de um número menor,
    # ao considerar a lista de peças do tabuleiro (ignorando o 0).

    flat_board = board.flatten()
    inversions = 0
    
    # Conta as inversões: Um número é uma inversão se ele aparece antes de outro número menor que ele
    for i in range(len(flat_board)):
        for j in range(i + 1, len(flat_board)):
            if flat_board[i] > flat_board[j] and flat_board[i] != 0 and flat_board[j] != 0:
                inversions += 1
                
    return inversions

# Função para verificar se o tabuleiro é solucionável
def is_solvable(board, goal_board):
    # Obtém as dimensões do tabuleiro
    n = board.shape[0]

    # Conta as inversões do tabuleiro inicial e do final
    inversions_start = count_inversions(board)
    inversions_goal = count_inversions(goal_board)

    # Um tabuleiro de tamanho ímpar é solucionável se a paridade 
    # do número de inversões no estado inicial for igual à paridade 
    # do número de inversões no estado objetivo.
    if n % 2 == 1:
        return inversions_start % 2 == inversions_goal % 2

    # Um tabuleiro de tamanho par é solucionável se a paridade 
    # do número de inversões somada à paridade da linha do espaço 
    # vazio (contada de baixo para cima) for igual no estado inicial e no estado objetivo.
    else:
        start_zero_row = np.where(board == 0)[0][0]
        goal_zero_row = np.where(goal_board == 0)[0][0]
        
        return ((inversions_start + start_zero_row) % 2 == (inversions_goal + goal_zero_row) % 2)