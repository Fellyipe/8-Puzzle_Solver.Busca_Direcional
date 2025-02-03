import numpy as np
import functions as fun
import search
import time

# Estado inicial do puzzle
initial_board = np.array([
    [1, 2, 3],
    [8, 0, 5],
    [4, 7, 6]
])

# Estado final esperado do puzzle
objective_board = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
])

# Estado inicial do puzzle 4x4
initial_board_4x4 = np.array([
    [5, 1, 2, 4],
    [9, 6, 3, 7],
    [10, 11, 0, 8],
    [13, 14, 15, 12]
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
    solution_path = search.bidirectional_search(initial_board, objective_board)
    end_time = time.time()
    elapsed_time = end_time - start_time

    if solution_path:
        print("Interseção encontrada!")
        print("Caminho da solução encontrado:")
        fun.print_solution_path(solution_path)
    else:
        print("Não foi possível encontrar uma solução.")


    print(f"\nTempo de execução: {elapsed_time:.4f} segundos")

else:
    print("\033[31mEsse tabuleiro não é solucionável!\033[0m")