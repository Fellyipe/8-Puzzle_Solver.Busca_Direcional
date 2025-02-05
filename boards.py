import numpy as np

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

initial_board_01_3x3 = np.array([[2, 8, 4], [6, 7, 5], [3, 1, 0]])
initial_board_02_3x3 = np.array([[4, 0, 5], [6, 3, 7], [8, 2, 1]])
initial_board_03_3x3 = np.array([[6, 2, 3], [8, 4, 5], [7, 1, 0]])
initial_board_04_3x3 = np.array([[6, 4, 8], [5, 3, 1], [2, 7, 0]])
initial_board_05_3x3 = np.array([[0, 3, 6], [1, 5, 8], [2, 7, 4]])
initial_board_06_3x3 = np.array([[3, 7, 0], [8, 6, 2], [4, 1, 5]])
initial_board_07_3x3 = np.array([[5, 2, 8], [7, 3, 0], [6, 4, 1]])
initial_board_08_3x3 = np.array([[7, 4, 8], [3, 5, 0], [1, 2, 6]])
initial_board_09_3x3 = np.array([[2, 3, 1], [8, 4, 0], [7, 5, 6]])
initial_board_10_3x3 = np.array([[6, 0, 2], [4, 1, 5], [8, 7, 3]])

initial_board_01_4x4 = np.array([
    [5, 10,  1,  6],
    [7, 13,  3,  0],
    [14, 9,  2, 15],
    [8, 12,  4, 11]
])

initial_board_02_4x4 = np.array([
    [4,  9,  6,  0],
    [2,  1, 14, 10],
    [15, 13, 5,  3],
    [7,  8, 11, 12]
])

initial_board_03_4x4 = np.array([
    [1, 14,  9, 11],
    [2,  5, 10,  8],
    [4, 13,  3, 12],
    [7,  6, 15,  0]
])
initial_board_04_4x4 = np.array([
    [1, 2, 6, 3],
    [5, 10, 0, 4],
    [7, 11, 8, 15],
    [9, 13, 14, 12]
])

initial_board_05_4x4 = np.array([
    [10, 5, 1, 6],
    [13, 0, 2, 3],
    [7, 4, 11, 8],
    [9, 14, 12, 15]
])

initial_board_01_5x5 = np.array([
    [17, 4, 5, 24, 0],
    [9, 22, 2, 14, 3],
    [11, 23, 8, 13, 15],
    [16, 1, 6, 12, 18],
    [10, 21, 7, 19, 20]
])

initial_board_02_5x5 = np.array([
    [11, 6, 4, 2, 0],
    [9, 10, 3, 5, 13],
    [17, 24, 20, 15, 14],
    [23, 16, 21, 19, 8],
    [12, 18, 22, 7, 1]
])

initial_board_03_5x5 = np.array([
    [10, 17, 5, 2, 13],
    [6, 23, 0, 3, 11],
    [12, 14, 22, 8, 9],
    [19, 18, 21, 4, 1],
    [24, 20, 16, 15, 7]
])

initial_board_04_5x5 = np.array([
    [9, 10, 16, 11, 21],
    [2, 17, 23, 15, 8],
    [4, 0, 6, 5, 20],
    [19, 1, 3, 7, 14],
    [24, 18, 22, 12, 13]
])

initial_board_05_5x5 = np.array([
    [11, 9, 5, 17, 3],
    [12, 10, 21, 18, 22],
    [7, 24, 0, 23, 15],
    [19, 1, 4, 16, 20],
    [2, 8, 13, 6, 14]
])