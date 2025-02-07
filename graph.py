import networkx as nx
import matplotlib.pyplot as plt
import functions as fun

def update_graph(G, current_state, visited_dict, title="Grafo da Busca"):
    """
    Atualiza o grafo com os estados presentes em visited_dict e destaca o nó current_state.
    
    Parâmetros:
      - G: Objeto Graph do NetworkX.
      - current_state: Estado atual (em formato de np.array) que será destacado.
      - visited_dict: Dicionário de visitados (por exemplo, visited_start ou visited_goal), onde as chaves são a representação do estado.
      - title: Título do gráfico.
    """
    G.clear()
    # Adiciona nós e arestas a partir do visited_dict
    for state_tuple, path in visited_dict.items():
        G.add_node(state_tuple)
        # Se o caminho tiver pelo menos 2 estados, adiciona arestas entre cada par consecutivo
        for i in range(len(path) - 1):
            G.add_edge(fun.board_to_tuple(path[i]), fun.board_to_tuple(path[i+1]))
    
    # Define o layout do grafo
    pos = nx.spring_layout(G, seed=42)  # Usando uma semente para consistência
    plt.clf()  # Limpa a figura atual
    nx.draw(G, pos, with_labels=False, node_size=100, node_color="lightblue", edge_color="gray")
    
    # Destaca o nó current_state
    current_node = fun.board_to_tuple(current_state)
    if current_node in G.nodes():
        nx.draw_networkx_nodes(G, pos, nodelist=[current_node], node_size=120, node_color="orange")
    
    plt.title(title)
    plt.draw()
    plt.pause(0.001)


def update_dual_graphs(G1, G2, title="Grafo das Buscas"):
    """
    Atualiza dois subplots: um para o grafo da busca DFS e outro para o grafo da busca BFS.
    Destaca os nós que são comuns (interseção) entre os dois grafos.
    
    Parâmetros:
      - G1: Grafo (networkx.Graph) dos estados visitados pela busca a partir do início.
      - G2: Grafo dos estados visitados pela busca a partir do objetivo.
      - current_1_state: estado atual da DFS (para eventual destaque).
      - current_2_state: estado atual da BFS.
      - title: título geral da figura.
    """
    # Configura o modo interativo (caso não esteja ativo)
    # plt.ion()
    
    # Cria (ou reusa) a figura com um identificador fixo (ex: 1)
    fig = plt.figure(1)
    fig.clf()  # Limpa a figura para a nova atualização

    # Cria dois subplots lado a lado
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    
    # Gera layouts (pode usar a mesma semente para consistência)
    pos_dfs = nx.spring_layout(G1, seed=42)
    pos_bfs = nx.spring_layout(G2, seed=42)
    
    # Desenha os grafos
    nx.draw(G1, pos=pos_dfs, with_labels=False, node_color='lightblue', ax=ax1, node_size=100)
    nx.draw(G2, pos=pos_bfs, with_labels=False, node_color='lightgreen', ax=ax2, node_size=100)
    
    # Encontra os nós comuns (interseção)
    common_nodes = set(G1.nodes()).intersection(set(G2.nodes()))
    
    # Se houver interseção, destaque esses nós com outra cor (ex: laranja)
    if common_nodes:
        nx.draw_networkx_nodes(G1, pos=pos_dfs, nodelist=list(common_nodes), node_color='orange', ax=ax1, node_size=120)
        nx.draw_networkx_nodes(G2, pos=pos_bfs, nodelist=list(common_nodes), node_color='orange', ax=ax2, node_size=120)
    
    # Adiciona títulos aos subplots
    ax1.set_title("Busca a partir do Início (DFS)")
    ax2.set_title("Busca a partir do Objetivo (BFS)")
    
    # Título geral da figura
    plt.suptitle(title)
    
    # Atualiza a figura e pausa um instante para visualização
    plt.draw()
    plt.pause(0.001)
    plt.clf()  # Limpa a figura para a próxima atualização

def abetter_update_dual_graphs(G1, G2, visited_start, visited_goal,
                         current_1_state, current_2_state,
                         title="Grafo das Buscas"):
    """
    Atualiza dois grafos (um para DFS e outro para BFS) em subplots lado a lado na mesma janela.
    Constrói os grafos a partir dos dicionários visited_start e visited_goal, adiciona arestas baseadas
    nos caminhos e destaca os nós atuais de cada busca.

    Parâmetros:
      - G1: Objeto Graph do NetworkX para a busca a partir do início.
      - G2: Objeto Graph do NetworkX para a busca a partir do objetivo.
      - visited_start: Dicionário de estados visitados pela busca do início (chave: representação do estado, valor: caminho).
      - visited_goal: Dicionário de estados visitados pela busca do objetivo.
      - current_1_state: Estado atual (np.array) da busca iniciada a partir do início.
      - current_2_state: Estado atual (np.array) da busca iniciada a partir do objetivo.
      - title: Título geral da figura.
    """
    # plt.ion()  # Ativa o modo interativo se ainda não estiver ativo
    fig = plt.figure(1)
    fig.clf()  # Limpa a figura para atualizar

    # Cria dois subplots (um para cada busca)
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    # --- Construindo o grafo DFS ---
    G1.clear()
    first_G1_node = None
    for state_tuple, path in visited_start.items():
        G1.add_node(state_tuple)
        # Adiciona as arestas baseadas no caminho (se houver pelo menos 2 estados)
        for i in range(len(path) - 1):
            n1 = fun.board_to_tuple(path[i])
            n2 = fun.board_to_tuple(path[i+1])
            G1.add_edge(n1, n2)
        if first_G1_node is None:
            first_G1_node = state_tuple

    # --- Construindo o grafo BFS ---
    G2.clear()
    first_G2_node = None
    for state_tuple, path in visited_goal.items():
        G2.add_node(state_tuple)
        for i in range(len(path) - 1):
            n1 = fun.board_to_tuple(path[i])
            n2 = fun.board_to_tuple(path[i+1])
            G2.add_edge(n1, n2)
        if first_G1_node is None:
            first_G1_node = state_tuple

    # Layout para os dois grafos
    pos_dfs = nx.spring_layout(G1, seed=42)
    pos_bfs = nx.spring_layout(G2, seed=42)

    # Desenha o grafo DFS
    nx.draw(G1, pos=pos_dfs, with_labels=False, node_size=100, node_color="lightblue", edge_color="gray", ax=ax1)
    # Destaca o nó atual da DFS
    current_dfs_node = fun.board_to_tuple(current_1_state)
    if current_dfs_node in G1.nodes():
        nx.draw_networkx_nodes(G1, pos=pos_dfs, nodelist=[current_dfs_node], node_size=120, node_color="orange", ax=ax1)
    ax1.set_title("Busca a partir do Início (DFS)")

    # Desenha o grafo BFS
    nx.draw(G2, pos=pos_bfs, with_labels=False, node_size=100, node_color="lightgreen", edge_color="gray", ax=ax2)
    # Destaca o nó atual da BFS
    current_bfs_node = fun.board_to_tuple(current_2_state)
    if current_bfs_node in G2.nodes():
        nx.draw_networkx_nodes(G2, pos=pos_bfs, nodelist=[current_bfs_node], node_size=120, node_color="orange", ax=ax2)
    ax2.set_title("Busca a partir do Objetivo (BFS)")

    plt.suptitle(title)
    plt.draw()
    plt.pause(0.001)

def bbetter_update_dual_graphs(G1, G2, visited_start, visited_goal,
                         current_1_state, current_2_state, start_state, goal_state, intersection=None,
                         title="Grafo das Buscas"):
    """
    Atualiza dois grafos (um para DFS e outro para BFS) em subplots lado a lado na mesma janela.
    Se houver interseção, os grafos são mesclados e desenhados juntos.

    Parâmetros:
      - G1: Grafo da busca do início (DFS).
      - G2: Grafo da busca do objetivo (BFS).
      - visited_start: Estados visitados pela busca do início.
      - visited_goal: Estados visitados pela busca do objetivo.
      - current_1_state: Estado atual da busca DFS.
      - current_2_state: Estado atual da busca BFS.
      - intersection: Nó onde as buscas se encontraram (se houver).
      - title: Título do gráfico.
    """

    plt.ion()
    fig = plt.figure(1)
    fig.clf()  # Limpa a figura para atualizar

    # Se houver interseção, combinamos os grafos DFS e BFS
    if intersection:

        G_merged = nx.Graph()
        # Adiciona nós e arestas do DFS
        for state_array, path in visited_start.items():
            state_tuple = tuple(state_array)
            G_merged.add_node(state_tuple)
            for i in range(len(path) - 1):
                G_merged.add_edge(fun.board_to_tuple(path[i]), fun.board_to_tuple(path[i + 1]))
        
        # Adiciona nós e arestas do BFS
        for state_array, path in visited_goal.items():
            state_tuple = tuple(state_array)
            G_merged.add_node(state_tuple)
            for i in range(len(path) - 1):
                G_merged.add_edge(fun.board_to_tuple(path[i]), fun.board_to_tuple(path[i + 1]))

        # G_merged.add_edges_from(G1.edges())
        # G_merged.add_edges_from(G2.edges())

        pos = nx.spring_layout(G_merged, seed=42)

        # Desenha o grafo mesclado
        plt.subplot(111)
        nx.draw(G_merged, pos, with_labels=False, node_size=100, node_color="lightgray", edge_color="gray")

        nx.draw_networkx_nodes(G_merged, pos, nodelist=list(visited_start.keys()), node_size=100, node_color="lightblue")
        nx.draw_networkx_nodes(G_merged, pos, nodelist=list(visited_goal.keys()), node_size=100, node_color="lightgreen")

        # Destaca os nós iniciais (azul e verde)
        nx.draw_networkx_nodes(G_merged, pos, nodelist=[start_state], node_size=120, node_color="blue", label="Início DFS")
        nx.draw_networkx_nodes(G_merged, pos, nodelist=[goal_state], node_size=120, node_color="green", label="Início BFS")

        # Destaca o nó de interseção em vermelho
        nx.draw_networkx_nodes(G_merged, pos, nodelist=[intersection], node_size=120, node_color="red", label="Interseção")

        plt.legend()
        plt.title("Grafo Combinado - Interseção Encontrada!")
    else:
        # Criamos dois subplots normais (caso ainda não tenha interseção)
        ax1 = fig.add_subplot(121)
        ax2 = fig.add_subplot(122)

        # --- Construindo o grafo DFS ---
        G1.clear()
        for state_tuple, path in visited_start.items():
            G1.add_node(state_tuple)
            for i in range(len(path) - 1):
                G1.add_edge(fun.board_to_tuple(path[i]), fun.board_to_tuple(path[i+1]))

        # --- Construindo o grafo BFS ---
        G2.clear()
        for state_tuple, path in visited_goal.items():
            G2.add_node(state_tuple)
            for i in range(len(path) - 1):
                G2.add_edge(fun.board_to_tuple(path[i]), fun.board_to_tuple(path[i+1]))

        # Layout para os dois grafos
        pos_dfs = nx.spring_layout(G1, seed=42)
        pos_bfs = nx.spring_layout(G2, seed=42)

        # Desenha o grafo DFS
        nx.draw(G1, pos=pos_dfs, with_labels=False, node_size=100, node_color="lightblue", edge_color="gray", ax=ax1)
        nx.draw_networkx_nodes(G1, pos=pos_dfs, nodelist=[start_state], node_size=120, node_color="blue", ax=ax1)
        current_dfs_node = fun.board_to_tuple(current_1_state)
        if current_dfs_node in G1.nodes():
            nx.draw_networkx_nodes(G1, pos=pos_dfs, nodelist=[current_dfs_node], node_size=120, node_color="orange", ax=ax1)
        
        ax1.set_title("Busca a partir do Início (DFS)")

        # Desenha o grafo BFS
        nx.draw(G2, pos=pos_bfs, with_labels=False, node_size=100, node_color="lightgreen", edge_color="gray", ax=ax2)
        nx.draw_networkx_nodes(G2, pos=pos_bfs, nodelist=[goal_state], node_size=120, node_color="green", ax=ax2)
        current_bfs_node = fun.board_to_tuple(current_2_state)
        if current_bfs_node in G2.nodes():
            nx.draw_networkx_nodes(G2, pos=pos_bfs, nodelist=[current_bfs_node], node_size=120, node_color="orange", ax=ax2)
        
        ax2.set_title("Busca a partir do Objetivo (BFS)")

    plt.suptitle(title)
    plt.draw()
    plt.pause(0.001)
    plt.draw()
    plt.pause(0.001)






def better_update_dual_graphs(G_dfs, G_bfs, visited_start, visited_goal,
                         current_dfs_state, current_bfs_state, intersection=None,
                         title="Grafo das Buscas"):
    """
    Atualiza dois grafos (DFS e BFS) em subplots lado a lado.
    Se houver interseção, os grafos são mesclados e desenhados juntos.

    Parâmetros:
      - G_dfs: Grafo DFS.
      - G_bfs: Grafo BFS.
      - visited_start: Estados visitados pela busca DFS.
      - visited_goal: Estados visitados pela busca BFS.
      - current_dfs_state: Estado atual da DFS.
      - current_bfs_state: Estado atual da BFS.
      - intersection: Nó onde as buscas se encontraram (se houver).
      - title: Título do gráfico.
    """
    plt.ion()  # Ativa o modo interativo
    fig = plt.figure(1)
    fig.clf()  # Limpa a figura para atualizar

    if intersection:
        # Criamos um grafo mesclado
        G_merged = nx.Graph()
        G_merged.add_edges_from(G_dfs.edges())
        G_merged.add_edges_from(G_bfs.edges())

        # Adicionamos os nós explicitamente para garantir que nenhum seja perdido
        for node in G_dfs.nodes():
            G_merged.add_node(node)
        for node in G_bfs.nodes():
            G_merged.add_node(node)

        # 🔥 Conectar os dois lados pelo nó de interseção
        G_merged.add_edge(intersection, intersection)  # Auto-aresta para evidenciar a conexão

        # Layout do grafo unificado
        pos = nx.spring_layout(G_merged, seed=42)

        # Desenha o grafo combinado
        nx.draw(G_merged, pos, with_labels=False, node_size=100, node_color="lightblue", edge_color="gray")

        # 🟥 Destaca o nó de interseção em vermelho
        nx.draw_networkx_nodes(G_merged, pos, nodelist=[intersection], node_size=150, node_color="red")

        plt.title("Grafo Combinado - Interseção Encontrada!")
    else:
        # Criamos dois subplots normais (caso ainda não tenha interseção)
        ax1 = fig.add_subplot(121)
        ax2 = fig.add_subplot(122)

        # --- Construindo o grafo DFS ---
        G_dfs.clear()
        for state_tuple, path in visited_start.items():
            G_dfs.add_node(state_tuple)
            for i in range(len(path) - 1):
                G_dfs.add_edge(fun.board_to_tuple(path[i]), fun.board_to_tuple(path[i+1]))

        # --- Construindo o grafo BFS ---
        G_bfs.clear()
        for state_tuple, path in visited_goal.items():
            G_bfs.add_node(state_tuple)
            for i in range(len(path) - 1):
                G_bfs.add_edge(fun.board_to_tuple(path[i]), fun.board_to_tuple(path[i+1]))

        # Layout para os dois grafos
        pos_dfs = nx.spring_layout(G_dfs, seed=42)
        pos_bfs = nx.spring_layout(G_bfs, seed=42)

        # Desenha o grafo DFS
        nx.draw(G_dfs, pos=pos_dfs, with_labels=False, node_size=100, node_color="lightblue", edge_color="gray", ax=ax1)
        current_dfs_node = fun.board_to_tuple(current_dfs_state)
        if current_dfs_node in G_dfs.nodes():
            nx.draw_networkx_nodes(G_dfs, pos=pos_dfs, nodelist=[current_dfs_node], node_size=120, node_color="orange", ax=ax1)
        ax1.set_title("Busca a partir do Início (DFS)")

        # Desenha o grafo BFS
        nx.draw(G_bfs, pos=pos_bfs, with_labels=False, node_size=100, node_color="lightgreen", edge_color="gray", ax=ax2)
        current_bfs_node = fun.board_to_tuple(current_bfs_state)
        if current_bfs_node in G_bfs.nodes():
            nx.draw_networkx_nodes(G_bfs, pos=pos_bfs, nodelist=[current_bfs_node], node_size=120, node_color="orange", ax=ax2)
        ax2.set_title("Busca a partir do Objetivo (BFS)")

    plt.suptitle(title)
    plt.draw()
    plt.pause(0.001)
    plt.draw()
    plt.pause(0.001)