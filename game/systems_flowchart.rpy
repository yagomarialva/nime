# ==============================================================================
# SISTEMA DE SELEÇÃO DE CAPÍTULOS E GATING (FLOWCHART)
# ==============================================================================

init python:
    class ChapterNode(object):
        def __init__(self, id, name, subtitle, required_stats=None, required_affinity=None):
            self.id = id
            self.name = name
            self.subtitle = subtitle
            # Dicionário de atributos exigidos e seu valor teto para a fase (o jogo cobra 70% desse teto)
            self.required_stats = required_stats or {}
            self.required_affinity = required_affinity or {}
            
    class FlowchartSystem(object):
        def __init__(self):
            self.nodes = {}
            self.node_order = []
            
        def add_node(self, node):
            self.nodes[node.id] = node
            self.node_order.append(node.id)
            
        def calculate_gating(self, next_node_id):
            if next_node_id not in self.nodes:
                return True, ""
                
            node = self.nodes[next_node_id]
            failures = []
            
            # Checa Atributos numéricos (Money, Energy, Intelecto, etc)
            for stat, max_val in node.required_stats.items():
                required_val = int(max_val * 0.70)
                current_val = store.player_stats.get(stat, 0)
                if current_val < required_val:
                    # Mapeamento para PT-BR
                    stat_names = {"energy": "Energia", "money": "Dinheiro", "fitness": "Físico", "intelligence": "Intelecto", "charisma": "Carisma", "creativity": "Criatividade"}
                    stat_pt = stat_names.get(stat, stat.capitalize())
                    failures.append(f"{stat_pt} ({current_val}/{required_val})")
                    
            # Checa Afinidade de Personagens
            if node.required_affinity:
                for char, max_pts in node.required_affinity.items():
                    required_val = int(max_pts * 0.70)
                    current_val = getattr(store, f"points_{char}", 0)
                    if current_val < required_val:
                        failures.append(f"Afinidade com {char.capitalize()} ({current_val}/{required_val})")
                    
            if failures:
                return False, "Requisitos Pendentes: " + " | ".join(failures)
            return True, ""

    # Inicialização do gerenciador e cadastro dos capítulos
    flowchart_system = FlowchartSystem()
    
    # Exemplo de configuração de Chapters
    flowchart_system.add_node(ChapterNode("intro", "Prólogo", "A Chegada", required_stats={}))
    flowchart_system.add_node(ChapterNode("capitulo1", "Capítulo 1", "A Casa da Rua Aurora", required_stats={"energy": 10}, required_affinity={"samantha": 10}))
    flowchart_system.add_node(ChapterNode("capitulo2", "Capítulo 2", "A Terceira Vaga Remanescente", required_stats={"energy": 20}, required_affinity={"nicole": 10}))
    flowchart_system.add_node(ChapterNode("capitulo3", "Capítulo 3", "A Crise da Conta de Luz", required_stats={"money": 50}, required_affinity={"camille": 15}))
    flowchart_system.add_node(ChapterNode("capitulo4", "Capítulo 4", "Silêncio Fúnebre", required_stats={"charisma": 20}, required_affinity={"huey": 15}))
    flowchart_system.add_node(ChapterNode("capitulo5", "Capítulo 5", "A Mãe da Nicole", required_stats={"intelligence": 40}, required_affinity={"nicole": 20, "samantha": 20}))
    flowchart_system.add_node(ChapterNode("capitulo6", "Capítulo 6", "O Incêndio", required_stats={"fitness": 30}, required_affinity={"katia": 20}))
    flowchart_system.add_node(ChapterNode("capitulo7", "Capítulo 7", "O Acampamento na Praia", required_stats={"creativity": 30}, required_affinity={"larissa": 25}))
    flowchart_system.add_node(ChapterNode("capitulo8", "Capítulo 8", "O Retorno e a Reforma", required_stats={"energy": 80, "money": 100}, required_affinity={"samantha": 30, "nicole": 30}))
    flowchart_system.add_node(ChapterNode("capitulo9", "Capítulo 9", "A Defesa da República", required_stats={"intelligence": 80, "charisma": 80}, required_affinity={"camille": 40, "katia": 40}))
    flowchart_system.add_node(ChapterNode("capitulo10", "Capítulo 10", "Despedidas", required_stats={"fitness": 50}, required_affinity={"huey": 50, "larissa": 50}))
    flowchart_system.add_node(ChapterNode("capitulo11", "Capítulo 11", "Fim de Ano", required_stats={}, required_affinity={}))
    flowchart_system.add_node(ChapterNode("capitulo12", "Capítulo 12", "O Retorno", required_stats={}, required_affinity={}))
    flowchart_system.add_node(ChapterNode("capitulo13", "Capítulo 13", "Decisões", required_stats={}, required_affinity={}))
    flowchart_system.add_node(ChapterNode("capitulo14", "Capítulo 14", "O Fim se Aproxima", required_stats={}, required_affinity={}))
    flowchart_system.add_node(ChapterNode("capitulo15", "Capítulo 15", "Para Sempre", required_stats={}, required_affinity={}))
    flowchart_system.add_node(ChapterNode("epilogo", "Epílogo", "A Carta", required_stats={}))

# ==============================================================================
# VARIÁVEIS DE ESTADO DO JOGADOR
# ==============================================================================
# Registram o progresso do jogador. A lista principal agora usa o persistent original do jogo.
default played_chapters = set()

# ==============================================================================
# UI: TELA DO FLUXOGRAMA
# ==============================================================================

screen chapter_select():
    tag menu
    
    # Fundo Sólido Escuro
    add Solid("#12121e")
    
    # Cabeçalho Superior Direito
    vbox:
        xalign 0.95
        yalign 0.05
        text "CHAPTER SELECT" size 60 color "#ffffff44" bold True # Fonte grande translúcida
        text "Navegue pelo seu Destino" size 24 color "#aaaaaa" xalign 1.0
        
    # Botão de Sair do Menu
    textbutton "Voltar ao Jogo":
        xalign 0.05
        yalign 0.05
        action Return("back")
        text_size 28
        
    # Container do Fluxograma Horizontal
    viewport:
        xalign 0.5
        yalign 0.5
        xsize 1600
        ysize 500
        scrollbars "horizontal"
        mousewheel True
        draggable True
        
        hbox:
            yalign 0.5
            xalign 0.5
            spacing 0
            
            python:
                nodes_list = flowchart_system.node_order
                
            for i, n_id in enumerate(nodes_list):
                $ node = flowchart_system.nodes[n_id]
                
                # Garante que o jogo base tem a lista persistente
                python:
                    if not hasattr(persistent, "unlocked_chapters") or persistent.unlocked_chapters is None:
                        persistent.unlocked_chapters = ["intro", "capitulo1"]
                        
                $ is_unlocked = n_id in persistent.unlocked_chapters
                $ is_played = n_id in played_chapters
                
                # NÓ (NODE)
                vbox:
                    yalign 0.5
                    spacing 10
                    
                    if is_played or is_unlocked:
                        # Nó Desbloqueado / Jogado (Thumbnail + Play)
                        button:
                            xysize (240, 135)
                            background Solid("#2a2a3e")
                            hover_background Solid("#4a4a6e")
                            action Return(n_id)
                            
                            # Simulando a miniatura e o ícone de play translúcido
                            add Solid("#ffffff22") align (0.5, 0.5)
                            text "▶" size 40 color "#ffffff88" align (0.5, 0.5)
                            
                        # Descrição do Nó
                        text node.name size 22 bold True color "#ffffff" xalign 0.5
                        text node.subtitle size 16 color "#aaaaaa" xalign 0.5
                        
                    else:
                        # Nó Bloqueado (Ícone circular azul com cadeado)
                        frame:
                            xysize (240, 135)
                            background None
                            # Simulando o círculo azul
                            add Solid("#0055aa", xysize=(80,80)) align (0.5, 0.5)
                            text "🔒" size 30 align (0.5, 0.5)
                            
                        text "Bloqueado" size 22 bold True color "#666666" xalign 0.5
                        
                # LINHA DE CONEXÃO
                if i < len(nodes_list) - 1:
                    $ next_id = nodes_list[i+1]
                    $ next_unlocked = next_id in persistent.unlocked_chapters
                    
                    frame:
                        yalign 0.4
                        xsize 80
                        ysize 4
                        padding (0,0)
                        
                        if next_unlocked:
                            background Solid("#ffffff") # Sólida Branca
                        else:
                            background Solid("#ffffff44") # Translúcida / Tracejada
                            
    # HUD DE PROGRESSO (Canto Inferior Esquerdo)
    frame:
        background Solid("#1b1b2f")
        xalign 0.05
        yalign 0.95
        padding (25, 20)
        
        vbox:
            spacing 15
            text "Progresso de Capítulos" size 20 color "#ffffff" bold True
            
            python:
                total_nodes = len(nodes_list)
                played_count = len(played_chapters)
                progresso = int((played_count / float(total_nodes)) * 100) if total_nodes > 0 else 0
                
            bar:
                value progresso
                range 100
                xsize 400
                ysize 25
                left_bar Solid("#4CAF50")
                right_bar Solid("#333333")
                
            text f"{progresso}% Concluído" size 16 color "#88cc88" xalign 1.0
