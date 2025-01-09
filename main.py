import numpy as np
import functions as fun
import search

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

tetete = [
    [1, 2, 3],
    [0, 4, 5],
    [7, 8, 6]
]

visited = set()  # Conjunto de estados visitados

# board = fun.move(board, "right")
# board = fun.move(board, "down")

# Converte para arrays NumPy para facilitar a comparação
board_array = np.array(board)
objective_board_array = np.array(objective_board)

# Marca o estado inicial como visitado
fun.mark_visited(board, visited)
fun.mark_visited(tetete, visited)

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
    # Verifica se o vizinho já foi visitado
    if not fun.is_visited(neighbor, visited):
        print(f"Vizinho {idx + 1}:")
        print(np.array(neighbor))
        # Marca como visitado
        fun.mark_visited(neighbor, visited)
    else:
        print(f"Vizinho {idx + 1}: Já visitado")




# Profundidade máxima para a DFS
MAX_DEPTH = 20

# Executa a busca bidirecional
intersection = search.bidirectional_search(board, objective_board, MAX_DEPTH)

if intersection:
    print("Interseção encontrada!")
    print("Estado intermediário:", np.array(intersection))
else:
    print("Não foi possível encontrar uma solução.")