import pygame
import sys
import numpy as np

def draw_board(screen, board, tile_size, images):
    """
    Desenha o tabuleiro usando imagens.
    'images' é um dicionário que mapeia cada número à sua imagem.
    A célula vazia pode ser representada pela imagem '0' ou simplesmente ignorada.
    """
    screen.fill((30, 30, 30))
    rows, cols = board.shape
    for i in range(rows):
        for j in range(cols):
            rect = pygame.Rect(j * tile_size, i * tile_size, tile_size, tile_size)
            value = board[i, j]
            if value in images:
                img = pygame.transform.scale(images[value], (tile_size, tile_size))
                screen.blit(img, rect)
            else:
                # Se não houver imagem para o valor, desenha um retângulo vazio
                pygame.draw.rect(screen, (0, 0, 0), rect)
            pygame.draw.rect(screen, (230, 218, 218), rect, 2)
    pygame.display.flip()



def diff_states(state1, state2):
    """
    Compara dois estados e retorna as posições do zero (célula vazia) em cada estado.
    Supõe que apenas uma troca ocorreu.
    Retorna:
      (posição do zero em state1, posição do zero em state2)
    """
    pos1 = np.argwhere(state1 == 0)[0]
    pos2 = np.argwhere(state2 == 0)[0]
    return tuple(pos1), tuple(pos2)

def animate_move(screen, images, start_state, end_state, tile_size, duration=500, fps=30):
    """
    Anima a transição suave entre start_state e end_state.
    - duration: duração total da animação (ms).
    - fps: frames por segundo.
    
    A função identifica a peça que se moveu (aquela que trocou com o zero)
    e interpola sua posição entre o estado inicial e final.
    """
    clock = pygame.time.Clock()
    frames = int(fps * (duration / 1000))
    
    # Identifica as posições do zero em cada estado
    pos_zero_start, pos_zero_end = diff_states(start_state, end_state)
    # A peça que se moveu é a que trocou com o zero:
    # Ela estava na posição de pos_zero_end no start_state e se deslocou para a posição de pos_zero_start no end_state.
    moving_from = pos_zero_end  
    moving_to = pos_zero_start  
    moving_piece = start_state[moving_from[0], moving_from[1]]
    
    # Converter as posições para coordenadas em pixels
    start_px = (moving_from[1] * tile_size, moving_from[0] * tile_size)
    end_px = (moving_to[1] * tile_size, moving_to[0] * tile_size)
    
    for f in range(frames):
        t = f / frames  # fator de interpolação entre 0 e 1
        # Calcula a posição intermediária
        current_x = int(start_px[0] + (end_px[0] - start_px[0]) * t)
        current_y = int(start_px[1] + (end_px[1] - start_px[1]) * t)

        # Criar uma cópia temporária do estado final com dois zeros
        temp_board = end_state.copy()
        temp_board[moving_from[0], moving_from[1]] = 0
        temp_board[moving_to[0], moving_to[1]] = 0

        # Primeiro, desenha o estado base (end_state)
        draw_board(screen, temp_board, tile_size, images)
        # Em seguida, sobrepõe a imagem da peça que se move na posição interpolada
        rect = pygame.Rect(current_x, current_y, tile_size, tile_size)
        piece_img = pygame.transform.scale(images[moving_piece], (tile_size, tile_size))
        screen.blit(piece_img, rect)
        
        pygame.display.flip()
        clock.tick(fps)

def animate_solution(solution_path, images, tile_size=100, delay=500, move_duration=300, exit_callback=None):
    """
    Anima o caminho da solução:
      - Para cada par de estados consecutivos, anima a transição suave usando animate_move.
      - Exibe cada estado final da transição por um período (delay).
      
    Parâmetros:
      - solution_path: lista de np.array representando cada estado do caminho.
      - images: dicionário de imagens para as peças.
      - tile_size: tamanho de cada célula.
      - delay: tempo de pausa (ms) entre os movimentos.
      - move_duration: duração da animação de cada movimento (ms).
    """
    pygame.init()
    
    # Define a janela com base no tamanho do tabuleiro
    rows, cols = solution_path[0].shape
    if rows == 3:
        tile_size = 200
    elif rows == 4:
        tile_size = 150
    width = cols * tile_size
    height = rows * tile_size
    
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Animação do 8-Puzzle")
    clock = pygame.time.Clock()
    running = True
    
    # Desenha o estado inicial
    draw_board(screen, solution_path[0], tile_size, images)
    pygame.time.delay(delay)
    
    # Anima cada transição
    for idx in range(len(solution_path) - 1):
        if not running:
            break

        start_state = solution_path[idx]
        end_state = solution_path[idx + 1]

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
                break

        animate_move(screen, images, start_state, end_state, tile_size, duration=move_duration)
        # Após a animação, exibe o estado final
        draw_board(screen, end_state, tile_size, images)
        pygame.time.delay(delay)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        clock.tick(30)

    # Chama a função de retorno ANTES de encerrar o pygame
    if exit_callback:
        exit_callback()

    pygame.quit()