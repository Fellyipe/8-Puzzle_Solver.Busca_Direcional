import pygame
import pygame_menu
import time
import search
import numpy as np
import functions as fun
from animation import animate_solution

# Inicialização do Pygame
pygame.init()
surface = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Menu - N-Puzzle")

tile_images = {
    1: pygame.image.load("imagens/1.png").convert_alpha(),
    2: pygame.image.load("imagens/2.png").convert_alpha(),
    3: pygame.image.load("imagens/3.png").convert_alpha(),
    4: pygame.image.load("imagens/4.png").convert_alpha(),
    5: pygame.image.load("imagens/5.png").convert_alpha(),
    6: pygame.image.load("imagens/6.png").convert_alpha(),
    7: pygame.image.load("imagens/7.png").convert_alpha(),
    8: pygame.image.load("imagens/8.png").convert_alpha(),
    9: pygame.image.load("imagens/9.png").convert_alpha(),
    10: pygame.image.load("imagens/10.png").convert_alpha(),
    11: pygame.image.load("imagens/11.png").convert_alpha(),
    12: pygame.image.load("imagens/12.png").convert_alpha(),
    13: pygame.image.load("imagens/13.png").convert_alpha(),
    14: pygame.image.load("imagens/14.png").convert_alpha(),
    15: pygame.image.load("imagens/15.png").convert_alpha(),
    16: pygame.image.load("imagens/16.png").convert_alpha(),
    17: pygame.image.load("imagens/17.png").convert_alpha(),
    18: pygame.image.load("imagens/18.png").convert_alpha(),
    19: pygame.image.load("imagens/19.png").convert_alpha(),
    20: pygame.image.load("imagens/20.png").convert_alpha(),
    21: pygame.image.load("imagens/21.png").convert_alpha(),
    22: pygame.image.load("imagens/22.png").convert_alpha(),
    23: pygame.image.load("imagens/23.png").convert_alpha(),
    24: pygame.image.load("imagens/24.png").convert_alpha(),
    0: pygame.image.load("imagens/25.png").convert_alpha()
}

# Variáveis globais
selected_algorithm = 1
selected_board_size = 1
show_animation = False
execution_time = None
objective_board = None
result_label = None

# Função para iniciar a busca com a variante escolhida
def start_search():
    global execution_time, solution_path, result_label

    solution_path = None    
    initial_board = None

    if selected_board_size == 1:
        initial_board = np.array([
            [1, 2, 3],
            [8, 0, 5],
            [4, 7, 6]
        ])
        objective_board = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ])
    elif selected_board_size == 2:
        initial_board = np.array([
            [5, 1, 2, 4],
            [9, 6, 3, 7],
            [10, 11, 0, 8],
            [13, 14, 15, 12]
        ])
        objective_board = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]
    ])
    elif selected_board_size == 3:
        initial_board = np.array([
            [2, 6, 8, 3, 4],
            [16, 1, 13, 9, 5],
            [0, 7, 12, 14, 10],
            [21, 11, 17, 19, 15],
            [22, 23, 18, 24, 20]
        ])
        objective_board = np.array([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 0]
    ])

    if fun.is_solvable(initial_board, objective_board):
        result_label.set_title("Esse tabuleiro é solucionável")
    else:
        result_label.set_title("Tabuleiro insolucionável!")
        return

    start_time = time.time()

    if selected_algorithm == 1:
        solution_path = search.bidirectional_search_dfs_bfs(initial_board, objective_board)
    elif selected_algorithm == 2:
        solution_path = search.bidirectional_search_bfs_dfs(initial_board, objective_board)
    elif selected_algorithm == 3:
        solution_path = search.bidirectional_search_dfs_dfs(initial_board, objective_board)
    elif selected_algorithm == 4:
        solution_path = search.bidirectional_search_bfs_bfs(initial_board, objective_board)

    execution_time = time.time() - start_time

    if solution_path:
        result_label.set_title(f"Tempo: {execution_time:.4f}s | Movimentos: {len(solution_path)}")
    else:
        result_label.set_title("Nenhuma solução encontrada.")

# Função para desenhar o menu principal
def draw_menu():
    global selected_algorithm, selected_board_size, show_animation, result_label
    
    menu = pygame_menu.Menu('N-Puzzle - Solucionador', 600, 600, theme=pygame_menu.themes.THEME_DARK)

    # Adiciona um dropdown para escolher o algoritmo
    menu.add.dropselect('Algoritmo :', 
                      [('DFS/BFS', 1), ('BFS/DFS', 2), ('DFS/DFS', 3), ('BFS/BFS', 4)],
                      default=selected_algorithm - 1, selection_color=(200, 200, 215), background_color=(40, 41, 35),   
                    font_color=(255, 255, 255), font_size=26, onchange=lambda selected, value: set_algorithm(value))
    
    # Adiciona um dropdown para escolher o tabuleiro
    menu.add.dropselect('Tabuleiro :', 
                      [('3x3', 1), ('4x4', 2), ('5x5', 3)],
                      default=selected_board_size - 1, selection_color=(200, 200, 215), background_color=(40, 41, 35),   
                    font_color=(255, 255, 255), font_size=26, onchange=lambda selected, value: set_board_size(value))

    menu.add.button('Iniciar Busca', start_search)
    menu.add.button('Mostrar animação', show_animation_solution)
    
    result_label = menu.add.label('Resultados: Aguardando...', font_size=26)

    # Botão para sair
    menu.add.button('Sair', pygame_menu.events.EXIT)

    return menu

# Função para setar o algoritmo escolhido
def set_algorithm(value):
    global selected_algorithm
    selected_algorithm = value

# Função para setar o tamanho do tabuleiro
def set_board_size(value):
    global selected_board_size
    selected_board_size = value

    # Função para mostrar a animação após a busca
def show_animation_solution():
    if solution_path:
        animate_solution(solution_path, tile_images, tile_size=120, delay=150, move_duration=100, exit_callback=main)
    else:
        result_label.set_title("Nenhuma solução para animar.")

# Loop principal do menu
def main():

    global selected_algorithm, selected_board_size, show_animation

    # Chama o menu principal
    menu = draw_menu()
    
    while True:
        surface.fill((40, 40, 40))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
        menu.update(events)
        menu.draw(surface)
        pygame.display.flip()

if __name__ == '__main__':
    main()