# ==============================================================================
# MINIGAMES DE TRABALHO
# ==============================================================================

screen minigame_clicker(item_text, max_items, bg_image):
    # Define as posições e o set de itens na primeira renderização da screen
    default positions = [(renpy.random.randint(100, 1100), renpy.random.randint(100, 600)) for i in range(max_items)]
    default remaining_items = set(range(max_items))
    default time_left = 10.0
    
    # Imagem de fundo
    add bg_image
    
    # Overlay escuro
    add Solid("#00000066")
    
    # Textos da HUD do minigame
    text _("Trabalho em Progresso!"):
        xalign 0.5 
        yalign 0.05 
        size 40 
        color "#ffffff" 
        outlines [(2, "#000000")]
    
    $ collected = max_items - len(remaining_items)
    text _("Itens coletados: [collected]/[max_items]"):
        xalign 0.5 
        yalign 0.12 
        size 30 
        color "#ffcc00" 
        outlines [(2, "#000000")]
        
    text _("Tempo: [time_left:.1f]s"):
        xalign 0.5 
        yalign 0.18 
        size 25 
        color "#ff4444" 
        outlines [(2, "#000000")]
        
    timer 0.1 action If(time_left > 0.1, true=SetScreenVariable("time_left", time_left - 0.1), false=Return(False)) repeat True
    
    # Renderiza os itens que ainda não foram clicados
    for i in remaining_items:
        textbutton item_text:
            xpos positions[i][0]
            ypos positions[i][1]
            text_size 60
            action RemoveFromSet(remaining_items, i)
            
    # Checa condição de vitória
    if len(remaining_items) == 0:
        timer 0.5 action Return(True)


screen minigame_corrida(target_clicks=30, time_limit=10.0):
    default clicks = 0
    default time_left = time_limit

    # Overlay escuro
    add Solid("#00000099")

    text _("Corra! Clique rápido!"):
        xalign 0.5 
        yalign 0.1 
        size 50 
        color "#ffffff" 
        outlines [(2, "#000")]

    text _("Tempo: [time_left:.1f]s"):
        xalign 0.5 
        yalign 0.2 
        size 40 
        color "#ff4444" 
        outlines [(2, "#000")]

    bar value clicks range target_clicks:
        xalign 0.5 
        yalign 0.3 
        xmaximum 600
        ymaximum 40

    button:
        xalign 0.5 
        yalign 0.6
        xysize (300, 300)
        background Solid("#44aa44")
        hover_background Solid("#66cc66")
        action SetScreenVariable("clicks", clicks + 1)
        text "CORRER!" align (0.5, 0.5) size 50 color "#fff" outlines [(2, "#000")]

    timer 0.1 action If(time_left > 0.1, true=SetScreenVariable("time_left", time_left - 0.1), false=Return(False)) repeat True

    if clicks >= target_clicks:
        timer 0.1 action Return(True)


label minigame_biblioteca:
    scene expression "images/cenarios/biblioteca.png" with dissolve
    
    menu:
        "Você encontrou uma oportunidade para organizar os livros da biblioteca. Isso renderá algum dinheiro."
        "Organizar Livros (Gastar 15 Energia)":
            if store.player_stats["energy"] >= 15:
                $ update_player_stat("energy", -15)
                
                # Inicia o minigame
                call screen minigame_clicker("📚", 5, "images/cenarios/biblioteca.png")
                $ result = _return
                
                if result:
                    # Recompensa
                    mc "Ufa! Terminei de organizar os livros."
                    $ update_player_stat("money", 50)
                    $ update_player_stat("intelligence", 5)
                    narrator "Você ganhou 50 de dinheiro e 5 de Intelecto!"
                else:
                    mc "Ah, eu demorei demais... não consegui terminar."
                    narrator "Você falhou no trabalho e não recebeu nada."
            else:
                mc "Estou muito cansado para isso agora..."
        "Voltar":
            pass
            
    return

label minigame_cinema:
    scene expression "images/cenarios/cinema.png" with dissolve
    
    menu:
        "A sala do cinema está uma bagunça após a última sessão. Você pode ajudar a limpar."
        "Limpar a Sala (Gastar 15 Energia)":
            if store.player_stats["energy"] >= 15:
                $ update_player_stat("energy", -15)
                
                # Inicia o minigame
                call screen minigame_clicker("🍿", 6, "images/cenarios/cinema.png")
                $ result = _return
                
                if result:
                    # Recompensa
                    mc "Tudo limpo! A sala está pronta para a próxima sessão."
                    $ update_player_stat("money", 60)
                    $ update_player_stat("charisma", 5)
                    narrator "Você ganhou 60 de dinheiro e 5 de Carisma!"
                else:
                    mc "O cinema é muito grande, não consegui limpar tudo a tempo."
                    narrator "Você falhou no trabalho e não recebeu nada."
            else:
                mc "Estou sem energia para limpar agora..."
        "Voltar":
            pass
            
    return

label minigame_quadra:
    scene expression "images/cenarios/QUADRA.png" with dissolve
    
    menu:
        "As bolas do último jogo ficaram espalhadas pela quadra toda. Organizar isso pode render um trocado."
        "Organizar Bolas (Gastar 15 Energia)":
            if store.player_stats["energy"] >= 15:
                $ update_player_stat("energy", -15)
                
                # Inicia o minigame
                call screen minigame_clicker("🏀", 5, "images/cenarios/QUADRA.png")
                $ result = _return
                
                if result:
                    # Recompensa
                    mc "Beleza, as bolas estão organizadas."
                    $ update_player_stat("money", 50)
                    $ update_player_stat("fitness", 5)
                    narrator "Você ganhou 50 de dinheiro e 5 de Físico!"
                else:
                    mc "Estou muito cansado, perdi muito tempo e não terminei."
                    narrator "Você falhou no trabalho e não recebeu nada."
            else:
                mc "Não consigo correr atrás dessas bolas agora..."
        "Voltar":
            pass
            
    return

    return

# ==============================================================================
# MINIGAMES DE EVENTOS EXTRAS
# ==============================================================================

screen minigame_hidden_object(time_limit=3.0, bg_image="images/cenarios/sala_arte.png"):
    default items = ["🖌️", "🎨", "🖼️", "🗿", "🏺", "🎭"]
    default target_item = renpy.random.choice(items)
    default positions = [(renpy.random.randint(100, 1100), renpy.random.randint(200, 600)) for i in range(15)]
    default grid_items = [renpy.random.choice(items) for i in range(15)]
    default time_left = time_limit
    
    add bg_image
    add Solid("#000000dd")
    
    text _("Encontre Rápido: [target_item]"):
        xalign 0.5 yalign 0.05 size 60 color "#fff" outlines [(2, "#000")]
        
    text _("Tempo: [time_left:.1f]s"):
        xalign 0.5 yalign 0.15 size 40 color "#ff4444" outlines [(2, "#000")]
        
    # Inject target item to ensure it exists
    $ if target_item not in grid_items: grid_items[0] = target_item
    
    timer 0.1 action If(time_left > 0.1, true=SetScreenVariable("time_left", time_left - 0.1), false=Return(False)) repeat True
    
    for i in range(15):
        textbutton grid_items[i]:
            xpos positions[i][0]
            ypos positions[i][1]
            text_size 50
            action If(grid_items[i] == target_item, true=Return(True), false=Return(False))

label minigame_galeria:
    scene expression "images/cenarios/sala_arte.png" with dissolve
    menu:
        "Ajudar a organizar o acervo da galeria. (Gastar 15 Energia)"
        "Organizar (15 Energia)":
            if store.player_stats["energy"] >= 15:
                $ update_player_stat("energy", -15)
                
                $ rounds = 5
                $ won = True
                while rounds > 0:
                    call screen minigame_hidden_object(3.0, "images/cenarios/sala_arte.png")
                    if not _return:
                        $ won = False
                        $ rounds = 0
                    else:
                        $ rounds -= 1
                        
                if won:
                    mc "Terminei! Consegui achar todos."
                    $ update_player_stat("money", 50)
                    $ update_player_stat("creativity", 5)
                    narrator "Você ganhou 50 de Dinheiro e 5 de Criatividade!"
                else:
                    mc "Me perdi nos itens. O tempo acabou."
            else:
                mc "Estou cansado demais."
        "Voltar":
            pass
    return

label minigame_laboratorio:
    scene expression "images/cenarios/lab.png" with dissolve
    menu:
        "Organizar a estrutura de dados do laboratório. (Gastar 15 Energia)"
        "Estruturar Dados (15 Energia)":
            if store.player_stats["energy"] >= 15:
                $ update_player_stat("energy", -15)
                call screen minigame_memoria(30.0, ["💻", "💾", "🔋", "🖥️"])
                if _return:
                    mc "Rede estruturada."
                    $ update_player_stat("money", 60)
                    $ update_player_stat("intelligence", 5)
                    narrator "Você ganhou 60 de Dinheiro e 5 de Intelecto!"
                else:
                    mc "Os servidores caíram antes de eu terminar."
            else:
                mc "Estou cansado demais."
        "Voltar":
            pass
    return

label minigame_jogos:
    scene expression "images/cenarios/Arcade.jpg" with dissolve
    menu:
        "Ajudar na manutenção das máquinas de arcade. (Gastar 15 Energia)"
        "Consertar Máquinas (15 Energia)":
            if store.player_stats["energy"] >= 15:
                $ update_player_stat("energy", -15)
                # Reutiliza o corrida clicker mas disfarçado
                call screen minigame_corrida(25, 5.0)
                if _return:
                    mc "Consegui fechar todas as manutenções!"
                    $ update_player_stat("money", 50)
                    $ update_player_stat("charisma", 5)
                    narrator "Você ganhou 50 de Dinheiro e 5 de Carisma!"
                else:
                    mc "Essas máquinas são muito velhas, não consegui."
            else:
                mc "Estou cansado demais."
        "Voltar":
            pass
    return

# ==============================================================================
# MINIGAME DE MEMÓRIA (CARTAS)
# ==============================================================================

init python:
    import random
    import time
    
    class MemoryGame:
        def __init__(self, pairs=4, emojis=None):
            self.pairs = pairs
            self.cards = []
            for i in range(pairs):
                self.cards.append(i)
                self.cards.append(i)
            random.shuffle(self.cards)
            self.state = [0] * (pairs * 2)
            self.first_selected = -1
            self.wait_until = 0
            self.matches = 0
            if emojis:
                self.emojis = emojis
            else:
                self.emojis = ["⚖️", "📖", "📜", "💼"]
            
        def can_click(self):
            return time.time() > self.wait_until
            
        def click(self, idx):
            if not self.can_click(): return
            if self.state[idx] != 0: return 
            
            if self.first_selected == -1:
                self.first_selected = idx
                self.state[idx] = 1
            else:
                self.state[idx] = 1
                if self.cards[self.first_selected] == self.cards[idx]:
                    self.state[self.first_selected] = 2
                    self.state[idx] = 2
                    self.matches += 1
                    self.first_selected = -1
                else:
                    self.wait_until = time.time() + 0.8
            renpy.restart_interaction()
                    
        def update(self):
            if self.first_selected != -1 and self.wait_until > 0 and time.time() > self.wait_until:
                for i in range(len(self.state)):
                    if self.state[i] == 1:
                        self.state[i] = 0
                self.first_selected = -1
                self.wait_until = 0
                renpy.restart_interaction()
                
        def is_win(self):
            return self.matches >= self.pairs

screen minigame_memoria(time_limit=30.0, emojis=None):
    default game = MemoryGame(4, emojis)
    default time_left = time_limit
    
    add Solid("#000000dd")
    
    text _("Memória: Conecte os pares!"):
        xalign 0.5 yalign 0.05 size 50 color "#ffffff" outlines [(2, "#000")]
        
    text _("Tempo: [time_left:.1f]s"):
        xalign 0.5 yalign 0.12 size 40 color "#ff4444" outlines [(2, "#000")]
        
    timer 0.1 action [Function(game.update), If(time_left > 0.1, true=SetScreenVariable("time_left", time_left - 0.1), false=Return(False))] repeat True
    
    grid 4 2:
        xalign 0.5 yalign 0.5
        spacing 20
        for i in range(8):
            if game.state[i] == 0:
                button:
                    xysize (150, 200)
                    background Solid("#4444aa")
                    hover_background Solid("#5555cc")
                    action Function(game.click, i)
                    text "?" align (0.5, 0.5) size 80 color "#fff"
            elif game.state[i] == 1:
                button:
                    xysize (150, 200)
                    background Solid("#aaaaaa")
                    action NullAction()
                    text game.emojis[game.cards[i]] align (0.5, 0.5) size 80 color "#000"
            else:
                button:
                    xysize (150, 200)
                    background Solid("#44aa44")
                    action NullAction()
                    text game.emojis[game.cards[i]] align (0.5, 0.5) size 80 color "#000"
                    
    if game.is_win():
        timer 0.5 action Return(True)

# ==============================================================================
# MINIGAMES DE REFORMA DA CASA (CAPÍTULO 6)
# ==============================================================================

label minigame_reforma_sala:
    scene expression "images/cenarios/sala_jantar.png" with dissolve
    menu:
        "A sala precisa de reparos no reboco e organização dos escombros. (Gastar 15 Energia)"
        "Organizar e Reparar (15 Energia)":
            if store.player_stats["energy"] >= 15:
                $ update_player_stat("energy", -15)
                call screen minigame_memoria(30.0, ["🧱", "🔨", "🪵", "🔩"])
                if _return:
                    mc "Consegui! As paredes parecem muito mais estáveis agora."
                    $ update_player_stat("intelligence", 5)
                    narrator "Você ganhou 5 de Intelecto por aprender sobre alvenaria!"
                else:
                    mc "Ah não, as ferramentas misturaram todas... perdi o dia de trabalho."
            else:
                mc "Estou cansado demais para levantar um martelo."
        "Voltar":
            pass
    return

label minigame_reforma_cozinha:
    scene expression "images/cenarios/cozinha_escura.png" with dissolve
    menu:
        "A fiação da cozinha derreteu e tem fuligem por toda parte. (Gastar 15 Energia)"
        "Limpar e Reconfigurar (15 Energia)":
            if store.player_stats["energy"] >= 15:
                $ update_player_stat("energy", -15)
                call screen minigame_corrida(25, 6.0)
                if _return:
                    mc "A cozinha tá respirável e a tomada funciona!"
                    $ update_player_stat("charisma", 5)
                    narrator "Você ganhou 5 de Carisma por tornar o ambiente agradável novamente!"
                else:
                    mc "É muita fuligem, eu não consigo terminar rápido o bastante..."
            else:
                mc "Estou sem fôlego para lutar contra a poeira agora."
        "Voltar":
            pass
    return

label minigame_reforma_quintal:
    scene expression "images/cenarios/quintal.png" with dissolve
    menu:
        "O entulho do segundo andar foi jogado todo no quintal e precisa ser separado. (Gastar 15 Energia)"
        "Separar Entulho (15 Energia)":
            if store.player_stats["energy"] >= 15:
                $ update_player_stat("energy", -15)
                call screen minigame_clicker("🗑️", 6, "images/cenarios/quintal.png")
                if _return:
                    mc "O gramado voltou a aparecer! Bom trabalho físico."
                    $ update_player_stat("fitness", 5)
                    narrator "Você ganhou 5 de Físico por carregar entulho pesado!"
                else:
                    mc "Sobra muito lixo, o sol tá quente demais."
            else:
                mc "Minhas costas doem muito para carregar peso agora."
        "Voltar":
            pass
    return
