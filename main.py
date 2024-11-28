import numpy as np

# Estado inicial do puzzle
tabuleiro_inicial = [
    [1, 2, 3],
    [4, 0, 5],
    [7, 8, 6]
]

# Estado final esperado do puzzle
tabuleiro_objetivo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Converte para arrays NumPy para facilitar a comparação
array_inicial = np.array(tabuleiro_inicial)
array_objetivo = np.array(tabuleiro_objetivo)

# Verifica se são iguais
if np.array_equal(array_inicial, array_objetivo):
    print("As matrizes são iguais! O puzzle está resolvido.")
else:
    print("As matrizes são diferentes. O puzzle ainda não está resolvido.")