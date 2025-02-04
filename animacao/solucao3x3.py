import pygame
import time
import json

# Configurações
WIDTH, HEIGHT = 300, 300
TILE_SIZE = WIDTH // 3
FONT_SIZE = 40

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 150, 255)



# Carrega o caminho da solução do arquivo JSON
with open("solucao3x3.json", "r") as f:
    solucao = json.load(f)

solucao = [[[None if num == 0 else num for num in row] for row in grid] for grid in solucao]

# Inicializar pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animação - 8 Fichas")
font = pygame.font.Font(None, FONT_SIZE)


def draw_board(state):
    screen.fill(WHITE)
    for row in range(3):
        for col in range(3):
            value = state[row][col]
            if value is not None:
                pygame.draw.rect(screen, BLUE, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                text = font.render(str(value), True, WHITE)
                screen.blit(text, (col * TILE_SIZE + TILE_SIZE // 3, row * TILE_SIZE + TILE_SIZE // 4))
    pygame.display.flip()

# Loop de animação
running = True
step = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if step < len(solucao):
        draw_board(solucao[step])
        step += 1
        time.sleep(0.4)
    else:
        running = False

input("Pressione Enter para encerrar...")
pygame.quit()
