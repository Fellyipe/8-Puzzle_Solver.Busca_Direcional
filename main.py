import numpy as np
import functions as fun
import search
import time

# Estado inicial do puzzle
initial_board = np.array([
    [4, 2, 3],
    [6, 8, 1],
    [7, 0, 5]
])

# Estado final esperado do puzzle
objective_board = np.array([
    [4, 3, 7],
    [8, 5, 1],
    [0, 2, 6]
])

# Estado inicial do puzzle 4x4
initial_board_4x4 = np.array([
    [12, 2, 10, 4],
    [13, 5, 3, 1],
    [8, 9, 11, 7],
    [6, 0, 14, 15]
])

# Estado final esperado do puzzle 4x4
objective_board_4x4 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 0]
])

# Estado inicial do puzzle 5x5
initial_board_5x5 = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 0, 15],
    [16, 17, 18, 14, 20],
    [21, 22, 23, 19, 24]
])

# Estado final esperado do puzzle 5x5
objective_board_5x5 = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 0]
])

# Profundidade máxima para a DFS
MAX_DEPTH = 20

if fun.is_solvable(initial_board, objective_board):
    print("\033[32mEsse tabuleiro é solucionável\033[0m\n")

    # Executa a busca bidirecional
    start_time = time.time()
    intersection = search.bidirectional_search(initial_board, objective_board)
    end_time = time.time()
    elapsed_time = end_time - start_time

    if intersection.any():
        print("Interseção encontrada!")
        print("Estado da intersecção:\n", np.array(intersection))
    else:
        print("Não foi possível encontrar uma solução.")


    print(f"\nTempo de execução: {elapsed_time:.4f} segundos")

else:
    print("\033[31mEsse tabuleiro não é solucionável!\033[0m")