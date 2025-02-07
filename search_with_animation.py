from collections import deque
import functions as fun
import pygame
import animation
import matplotlib.pyplot as plt
import networkx as nx
from graph import update_graph, update_dual_graphs, bbetter_update_dual_graphs

def bidirectional_search_dfs_bfs_animated(start_board, goal_board, images, exit_callback=None):
    plt.ion()
    G1 = nx.Graph()
    G2 = nx.Graph()

    pygame.init()
    tile_size = 100
    rows, cols = start_board.shape
    if rows == 3:
        tile_size = 200
    elif rows == 4:
        tile_size = 150
    elif rows == 5:
        tile_size = 120
    rows, cols = start_board.shape
    width = cols * tile_size
    height = rows * tile_size

    screen = pygame.display.set_mode((2 * width + 20, height))
    pygame.display.set_caption("Animação do 8-Puzzle")
    clock = pygame.time.Clock()
    running = True

    animation.draw_board(screen, start_board, tile_size, images, 0, 0)
    animation.draw_board(screen, start_board, tile_size, images, width + 20, 0)
    pygame.time.delay(500)
    
    # Inicialização
    stack = [(start_board, [start_board])]  # Pilha para DFS
    queue = deque([(goal_board, [goal_board])])  # Fila para BFS
    
    # Dicionários para armazenar os estados visitados e seus caminhos
    visited_start = {fun.board_to_tuple(start_board): [start_board]}
    visited_goal = {fun.board_to_tuple(goal_board): [goal_board]}

    board_tuple1 = None
    board_tuple2 = None

    # Busca alternada
    while stack and queue:
        pygame.time.delay(500)
        # Passo da busca em profundidade
        if stack:
            board, path_from_start = stack.pop()
            animation.draw_board(screen, board, tile_size, images, 0, 0)
            board_tuple1 = fun.board_to_tuple(board)
            G1.add_node(board_tuple1)

            if board_tuple1 in visited_goal:
                path_from_goal = visited_goal[board_tuple1]
                bbetter_update_dual_graphs(G1, G2, visited_start, visited_goal, board_tuple1, board_tuple2, fun.board_to_tuple(start_board), fun.board_to_tuple(goal_board), board_tuple1)
                solution_path = path_from_start + list(reversed(path_from_goal))[1:] # Combina os caminhos
                break
            
            neighbors = fun.generate_neighbors(board)
            for neighbor in neighbors:
                neighbor_tuple = fun.board_to_tuple(neighbor)
                if neighbor_tuple not in visited_start:
                    new_path = path_from_start + [neighbor]
                    visited_start[neighbor_tuple] = new_path
                    stack.append((neighbor, new_path))

        # Passo da busca em largura
        if queue:
            board, path_from_goal = queue.popleft()
            animation.draw_board(screen, board, tile_size, images, width + 20, 0)
            board_tuple2 = fun.board_to_tuple(board)
            G2.add_node(board_tuple2)

            if board_tuple2 in visited_start:
                path_from_start = visited_start[board_tuple2]
                bbetter_update_dual_graphs(G1, G2, visited_start, visited_goal, board_tuple1, board_tuple2, fun.board_to_tuple(start_board), fun.board_to_tuple(goal_board), board_tuple2)
                solution_path = path_from_start + list(reversed(path_from_goal))[1:] # Combina os caminhos
                break
            
            neighbors = fun.generate_neighbors(board)
            for neighbor in neighbors:
                neighbor_tuple = fun.board_to_tuple(neighbor)
                if neighbor_tuple not in visited_goal:
                    new_path = path_from_goal + [neighbor]
                    visited_goal[neighbor_tuple] = new_path
                    queue.append((neighbor, new_path))
        bbetter_update_dual_graphs(G1, G2, visited_start, visited_goal, board_tuple1, board_tuple2, fun.board_to_tuple(start_board), fun.board_to_tuple(goal_board))
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
                break
        #update_dual_graphs(G1, G2, title="Atualização dos Grafos das Buscas")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        clock.tick(30)

    if exit_callback:
        exit_callback()

    pygame.quit()

def bidirectional_search_bfs_dfs_animated(start_board, goal_board, images, exit_callback=None):
    plt.ion()
    G1 = nx.Graph()
    G2 = nx.Graph()

    pygame.init()
    tile_size = 100
    rows, cols = start_board.shape
    if rows == 3:
        tile_size = 200
    elif rows == 4:
        tile_size = 150
    elif rows == 5:
        tile_size = 120
    rows, cols = start_board.shape
    width = cols * tile_size
    height = rows * tile_size

    screen = pygame.display.set_mode((2 * width + 20, height))
    pygame.display.set_caption("Animação do 8-Puzzle")
    clock = pygame.time.Clock()
    running = True

    animation.draw_board(screen, start_board, tile_size, images, 0, 0)
    animation.draw_board(screen, start_board, tile_size, images, width + 20, 0)
    pygame.time.delay(500)
    
    # Inicialização
    queue_start = deque([(start_board, [start_board])])  # Pilha para DFS
    stack_goal = [(goal_board, [goal_board])]  # Fila para BFS
    
    # Dicionários para armazenar os estados visitados e seus caminhos
    visited_start = {fun.board_to_tuple(start_board): [start_board]}
    visited_goal = {fun.board_to_tuple(goal_board): [goal_board]}

    board_tuple1 = None
    board_tuple2 = None

    # Busca alternada
    while queue_start and stack_goal:
        pygame.time.delay(500)
        # Passo da busca em profundidade
        if queue_start:
            board, path_from_start = queue_start.popleft()
            animation.draw_board(screen, board, tile_size, images, 0, 0)
            board_tuple1 = fun.board_to_tuple(board)
            G1.add_node(board_tuple1)

            if board_tuple1 in visited_goal:
                path_from_goal = visited_goal[board_tuple1]
                bbetter_update_dual_graphs(G1, G2, visited_start, visited_goal, board_tuple1, board_tuple2, fun.board_to_tuple(start_board), fun.board_to_tuple(goal_board), board_tuple1)
                solution_path = path_from_start + list(reversed(path_from_goal))[1:] # Combina os caminhos
                break
            
            neighbors = fun.generate_neighbors(board)
            for neighbor in neighbors:
                neighbor_tuple = fun.board_to_tuple(neighbor)
                if neighbor_tuple not in visited_start:
                    new_path = path_from_start + [neighbor]
                    visited_start[neighbor_tuple] = new_path
                    queue_start.append((neighbor, new_path))

        # Passo da busca em largura
        if stack_goal:
            board, path_from_goal = stack_goal.pop()
            animation.draw_board(screen, board, tile_size, images, width + 20, 0)
            board_tuple2 = fun.board_to_tuple(board)
            G2.add_node(board_tuple2)

            if board_tuple2 in visited_start:
                path_from_start = visited_start[board_tuple2]
                bbetter_update_dual_graphs(G1, G2, visited_start, visited_goal, board_tuple1, board_tuple2, fun.board_to_tuple(start_board), fun.board_to_tuple(goal_board), board_tuple2)
                solution_path = path_from_start + list(reversed(path_from_goal))[1:] # Combina os caminhos
                break
            
            neighbors = fun.generate_neighbors(board)
            for neighbor in neighbors:
                neighbor_tuple = fun.board_to_tuple(neighbor)
                if neighbor_tuple not in visited_goal:
                    new_path = path_from_goal + [neighbor]
                    visited_goal[neighbor_tuple] = new_path
                    stack_goal.append((neighbor, visited_goal[neighbor_tuple]))
        bbetter_update_dual_graphs(G1, G2, visited_start, visited_goal, board_tuple1, board_tuple2, fun.board_to_tuple(start_board), fun.board_to_tuple(goal_board))
        #update_dual_graphs(G1, G2, title="Atualização dos Grafos das Buscas")
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
                break

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        clock.tick(30)

    if exit_callback:
        exit_callback()

    pygame.quit()

def bidirectional_search_bfs_bfs_animated(start_board, goal_board, images, exit_callback=None):
    plt.ion()
    G1 = nx.Graph()
    G2 = nx.Graph()

    pygame.init()
    tile_size = 100
    rows, cols = start_board.shape
    if rows == 3:
        tile_size = 200
    elif rows == 4:
        tile_size = 150
    elif rows == 5:
        tile_size = 120
    width = cols * tile_size
    height = rows * tile_size

    screen = pygame.display.set_mode((2 * width + 20, height))
    pygame.display.set_caption("Animação do 8-Puzzle")
    clock = pygame.time.Clock()
    running = True

    animation.draw_board(screen, start_board, tile_size, images, 0, 0)
    animation.draw_board(screen, start_board, tile_size, images, width + 20, 0)
    pygame.time.delay(500)
    
    # Inicialização
    queue_start = deque([(start_board, [start_board])])
    queue_goal = deque([(goal_board, [goal_board])])
    
    # Dicionários para armazenar os estados visitados e seus caminhos
    visited_start = {fun.board_to_tuple(start_board): [start_board]}
    visited_goal = {fun.board_to_tuple(goal_board): [goal_board]}

    board_tuple1 = None
    board_tuple2 = None

    # Busca alternada
    while queue_start and queue_goal:
        pygame.time.delay(500)
        # Passo da busca em profundidade
        if queue_start:
            board, path_from_start = queue_start.popleft()
            animation.draw_board(screen, board, tile_size, images, 0, 0)
            board_tuple1 = fun.board_to_tuple(board)
            G1.add_node(board_tuple1)

            if board_tuple1 in visited_goal:
                path_from_goal = visited_goal[board_tuple1]
                bbetter_update_dual_graphs(G1, G2, visited_start, visited_goal, board_tuple1, board_tuple2, fun.board_to_tuple(start_board), fun.board_to_tuple(goal_board), board_tuple1)
                solution_path = path_from_start + list(reversed(path_from_goal))[1:] # Combina os caminhos
                break
            
            neighbors = fun.generate_neighbors(board)
            for neighbor in neighbors:
                neighbor_tuple = fun.board_to_tuple(neighbor)
                if neighbor_tuple not in visited_start:
                    new_path = path_from_start + [neighbor]
                    visited_start[neighbor_tuple] = new_path
                    queue_start.append((neighbor, visited_start[neighbor_tuple]))

        # Passo da busca em largura
        if queue_goal:
            board, path_from_goal = queue_goal.popleft()
            animation.draw_board(screen, board, tile_size, images, width + 20, 0)
            board_tuple2 = fun.board_to_tuple(board)
            G2.add_node(board_tuple2)

            if board_tuple2 in visited_start:
                path_from_start = visited_start[board_tuple2]
                bbetter_update_dual_graphs(G1, G2, visited_start, visited_goal, board_tuple1, board_tuple2, fun.board_to_tuple(start_board), fun.board_to_tuple(goal_board), board_tuple2)
                solution_path = path_from_start + list(reversed(path_from_goal))[1:] # Combina os caminhos
                break
            
            neighbors = fun.generate_neighbors(board)
            for neighbor in neighbors:
                neighbor_tuple = fun.board_to_tuple(neighbor)
                if neighbor_tuple not in visited_goal:
                    new_path = path_from_goal + [neighbor]
                    visited_goal[neighbor_tuple] = new_path
                    queue_goal.append((neighbor, visited_goal[neighbor_tuple]))
        bbetter_update_dual_graphs(G1, G2, visited_start, visited_goal, board_tuple1, board_tuple2, fun.board_to_tuple(start_board), fun.board_to_tuple(goal_board))
        #update_dual_graphs(G1, G2, title="Atualização dos Grafos das Buscas")
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
                break

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        clock.tick(30)

    if exit_callback:
        exit_callback()

    pygame.quit()

def bidirectional_search_dfs_dfs_animated(start_board, goal_board, images, exit_callback=None):
    plt.ion()
    G1 = nx.Graph()
    G2 = nx.Graph()

    pygame.init()
    tile_size = 100
    rows, cols = start_board.shape
    if rows == 3:
        tile_size = 200
    elif rows == 4:
        tile_size = 150
    elif rows == 5:
        tile_size = 120
    rows, cols = start_board.shape
    width = cols * tile_size
    height = rows * tile_size

    screen = pygame.display.set_mode((2 * width + 20, height))
    pygame.display.set_caption("Animação do 8-Puzzle")
    clock = pygame.time.Clock()
    running = True

    animation.draw_board(screen, start_board, tile_size, images, 0, 0)
    animation.draw_board(screen, start_board, tile_size, images, width + 20, 0)
    pygame.time.delay(500)
    
    # Inicialização
    stack_start = [(start_board, [start_board])]  # Pilha para DFS
    stack_goal = [(goal_board, [goal_board])]
    
    # Dicionários para armazenar os estados visitados e seus caminhos
    visited_start = {fun.board_to_tuple(start_board): [start_board]}
    visited_goal = {fun.board_to_tuple(goal_board): [goal_board]}

    board_tuple1 = None
    board_tuple2 = None

    # Busca alternada
    while stack_start and stack_goal:
        pygame.time.delay(500)
        # Passo da busca em profundidade
        if stack_start:
            board, path_from_start = stack_start.pop()
            animation.draw_board(screen, board, tile_size, images, 0, 0)
            board_tuple1 = fun.board_to_tuple(board)
            G1.add_node(board_tuple1)

            if board_tuple1 in visited_goal:
                path_from_goal = visited_goal[board_tuple1]
                bbetter_update_dual_graphs(G1, G2, visited_start, visited_goal, board_tuple1, board_tuple2, fun.board_to_tuple(start_board), fun.board_to_tuple(goal_board), board_tuple1)
                solution_path = path_from_start + list(reversed(path_from_goal))[1:] # Combina os caminhos
                break
            
            neighbors = fun.generate_neighbors(board)
            for neighbor in neighbors:
                neighbor_tuple = fun.board_to_tuple(neighbor)
                if neighbor_tuple not in visited_start:
                    new_path = path_from_start + [neighbor]
                    visited_start[neighbor_tuple] = new_path
                    stack_start.append((neighbor, new_path))

        # Passo da busca em largura
        if stack_goal:
            board, path_from_goal = stack_goal.pop()
            animation.draw_board(screen, board, tile_size, images, width + 20, 0)
            board_tuple2 = fun.board_to_tuple(board)
            G2.add_node(board_tuple2)

            if board_tuple2 in visited_start:
                path_from_start = visited_start[board_tuple2]
                bbetter_update_dual_graphs(G1, G2, visited_start, visited_goal, board_tuple1, board_tuple2, fun.board_to_tuple(start_board), fun.board_to_tuple(goal_board), board_tuple2)
                solution_path = path_from_start + list(reversed(path_from_goal))[1:] # Combina os caminhos
                break
            
            neighbors = fun.generate_neighbors(board)
            for neighbor in neighbors:
                neighbor_tuple = fun.board_to_tuple(neighbor)
                if neighbor_tuple not in visited_goal:
                    new_path = path_from_goal + [neighbor]
                    visited_goal[neighbor_tuple] = new_path
                    stack_goal.append((neighbor, visited_goal[neighbor_tuple]))
        bbetter_update_dual_graphs(G1, G2, visited_start, visited_goal, board_tuple1, board_tuple2, fun.board_to_tuple(start_board), fun.board_to_tuple(goal_board))
        #update_dual_graphs(G1, G2, title="Atualização dos Grafos das Buscas")
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
                break

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        clock.tick(30)

    if exit_callback:
        exit_callback()

    pygame.quit()