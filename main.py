import numpy as np
import functions as fun

# Estado inicial do puzzle
board = [
    [1, 2, 3],
    [4, 0, 5],
    [7, 8, 6]
]

# Estado final esperado do puzzle
objective_board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# board = fun.move(board, "right")
board = fun.move(board, "down")

# Converte para arrays NumPy para facilitar a comparação
board_array = np.array(board)
objective_board_array = np.array(objective_board)

# # Verifica se são iguais
# if np.array_equal(board_array, objective_board_array):
#     print("As matrizes são iguais! O puzzle está resolvido.")
# else:
#     print("As matrizes são diferentes. O puzzle ainda não está resolvido.")

print("Tabuleiro original:")
print(board_array)

print("\nEstados vizinhos:")
neighbors = fun.generate_neighbors(board_array)
for idx, neighbor in enumerate(neighbors):
    print(f"Vizinho {idx + 1}:")
    print(np.array(neighbor))