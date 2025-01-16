# Função de busca printa os novos vizinhos, que não haviam sido descobertos, a cada iteração de cada busca (DFS e BFS)

import numpy as np
import functions as fun
import search

# Estado inicial do puzzle
initial_board = np.array([
    [0, 2, 3],
    [1, 4, 5],
    [7, 8, 6]
])

# Estado final esperado do puzzle
objective_board = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
])

# Estado inicial do puzzle 4x4
initial_board_4x4 = np.array([
    [5, 1, 2, 3],
    [9, 6, 7, 4],
    [13, 10, 11, 8],
    [0, 14, 15, 12]
])

# Estado final esperado do puzzle 4x4
objective_board_4x4 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 0]
])

# Profundidade máxima para a DFS
MAX_DEPTH = 20

# Executa a busca bidirecional
intersection = search.bidirectional_search(initial_board, objective_board)

if intersection.any():
    print("Interseção encontrada!")
    print("Estado da intersecção:\n", np.array(intersection))
else:
    print("Não foi possível encontrar uma solução.")