init python:
    import random

    # 1. Larissa: Jogo da Memória
    def init_memory_game():
        store.memory_cards = ["mito", "mito", "krebs", "krebs", "dna", "dna", "celula", "celula"]
        random.shuffle(store.memory_cards)
        store.memory_revealed = [False] * 8
        store.memory_matched = [False] * 8
        store.memory_first_pick = -1
        store.memory_pairs_found = 0
        store.memory_can_click = True
        store.memory_dialogue_pending = False

    def click_memory_card(idx):
        if not store.memory_can_click or store.memory_revealed[idx] or store.memory_matched[idx]:
            return
            
        store.memory_revealed[idx] = True
        
        if store.memory_first_pick == -1:
            store.memory_first_pick = idx
        else:
            store.memory_can_click = False
            first = store.memory_first_pick
            if store.memory_cards[first] == store.memory_cards[idx]:
                store.memory_matched[first] = True
                store.memory_matched[idx] = True
                store.memory_pairs_found += 1
                store.memory_dialogue_pending = True
            store.memory_first_pick = -1

    def reset_memory_miss():
        for i in range(8):
            if not store.memory_matched[i]:
                store.memory_revealed[i] = False
        store.memory_can_click = True

    # 2. Camille: Jogo de Foco
    def init_focus_game():
        store.focus_x = 0.0
        store.focus_dir = 1
        store.focus_speed = 0.05
        store.focus_score = 0
        store.focus_timer = 10.0

    def update_focus_game():
        store.focus_timer -= 0.1
        store.focus_x += store.focus_speed * store.focus_dir
        if store.focus_x > 1.0:
            store.focus_x = 1.0
            store.focus_dir = -1
        elif store.focus_x < 0.0:
            store.focus_x = 0.0
            store.focus_dir = 1

    def click_focus():
        if 0.4 <= store.focus_x <= 0.6:
            store.focus_score += 1
            store.focus_speed += 0.02
        else:
            store.focus_score = max(0, store.focus_score - 1)

    # 3. Samantha: Sequence (Setas)
    def init_sequence_game():
        store.seq_target = [random.choice(["up", "down", "left", "right"]) for _ in range(5)]
        store.seq_current = 0
        store.seq_timer = 8.0

    def click_sequence(dir):
        if store.seq_target[store.seq_current] == dir:
            store.seq_current += 1
        else:
            store.seq_current = 0 # reset on miss
            
    # 4. Katia: Clicker de Papeis
    def init_clicker_game():
        store.clicker_docs = []
        for i in range(10):
            store.clicker_docs.append({
                "x": random.uniform(0.1, 0.9),
                "y": random.uniform(0.2, 0.8),
                "clicked": False
            })
        store.clicker_timer = 10.0
        store.clicker_done = 0

    def click_document(idx):
        if not store.clicker_docs[idx]["clicked"]:
            store.clicker_docs[idx]["clicked"] = True
            store.clicker_done += 1

    # 5. Nicole: Diplomacia (Puzzle)
    def init_diplomacy_game():
        store.diplomacy_timer = 15.0
        store.diplomacy_patience = 100.0

    def update_diplomacy():
        store.diplomacy_timer -= 0.1
        store.diplomacy_patience -= 0.6

    # 6. Huey: Simon Says
    def init_simon_game():
        store.simon_sequence = [random.choice(["#ff0000", "#0000ff", "#00ff00", "#ffff00"]) for _ in range(4)]
        store.simon_showing = True
        store.simon_tick = 0
        store.simon_user_idx = 0
        store.simon_timer = 0.0

    # 7. Harem: Gestão de Estresse
    def init_harem_game():
        store.harem_stress = [0.0] * 6
        store.harem_names = ["Larissa", "Camille", "Samantha", "Katia", "Nicole", "Huey"]
        store.harem_timer = 15.0
        store.harem_lost = False

    def update_harem_game():
        store.harem_timer -= 0.1
        for i in range(6):
            store.harem_stress[i] += random.uniform(0.5, 2.0)
            if store.harem_stress[i] >= 100.0:
                store.harem_lost = True

    def click_harem(idx):
        store.harem_stress[idx] = max(0.0, store.harem_stress[idx] - 25.0)

# ==========================================
# SCREENS DOS MINIJOGOS
# ==========================================

# 1. Larissa - Jogo da Memória
screen minigame_memory():
    modal True
    zorder 200
    
    add Solid("#000000cc")
    
    # Se errou, timer para virar de volta
    if not store.memory_can_click and not store.memory_dialogue_pending:
        timer 1.0 action Function(reset_memory_miss)
        
    # Se acertou, sai da screen pra tocar o diálogo
    if store.memory_dialogue_pending:
        timer 0.5 action Return("match")

    vbox:
        xalign 0.5 yalign 0.5
        spacing 20
        text "Quiz de Biologia: Encontre os Pares" size 40 color "#fff" xalign 0.5
        
        grid 4 2:
            spacing 15
            for i in range(8):
                if store.memory_revealed[i]:
                    frame:
                        xysize (150, 150)
                        background Solid("#ffffff")
                        text store.memory_cards[i].upper() align (0.5, 0.5) color "#000" size 25
                else:
                    button:
                        xysize (150, 150)
                        background Solid("#444444")
                        action Function(click_memory_card, i)
                        text "?" align (0.5, 0.5) color "#fff" size 40

# 2. Camille - Jogo de Foco
screen minigame_focus():
    modal True
    zorder 200
    add Solid("#000000cc")
    
    timer 0.1 repeat True action Function(update_focus_game)
    
    if store.focus_score >= 3:
        timer 0.1 action Return("win")
    if store.focus_timer <= 0:
        timer 0.1 action Return("lose")

    vbox:
        xalign 0.5 yalign 0.5
        spacing 30
        text "Alinhe as energias terrenas (3 acertos)" size 40 color "#fff" xalign 0.5
        text "Tempo: [store.focus_timer:.1f] | Acertos: [store.focus_score]/3" size 30 color "#fff" xalign 0.5
        
        frame:
            xsize 600 ysize 50
            background Solid("#333")
            # Zona verde no centro
            frame:
                xsize 120 ysize 50
                xalign 0.5
                background Solid("#00ff0066")
            
            # Cursor
            frame:
                xsize 10 ysize 60
                yalign 0.5
                xpos store.focus_x
                background Solid("#fff")
                
        textbutton "RESPIRAR":
            xalign 0.5
            text_size 30
            action Function(click_focus)

# 3. Samantha - Sequência de Digitação
screen minigame_sequence():
    modal True
    zorder 200
    add Solid("#000000cc")
    
    timer 0.1 repeat True action SetVariable("seq_timer", store.seq_timer - 0.1)
    
    if store.seq_current >= 5:
        timer 0.1 action Return("win")
    if store.seq_timer <= 0:
        timer 0.1 action Return("lose")
        
    vbox:
        xalign 0.5 yalign 0.5
        spacing 30
        text "Debugue o Código! Tempo: [store.seq_timer:.1f]" size 40 color "#fff" xalign 0.5
        
        hbox:
            xalign 0.5
            spacing 20
            for i in range(5):
                if i < store.seq_current:
                    text store.seq_target[i].upper() color "#00ff00" size 35
                elif i == store.seq_current:
                    text store.seq_target[i].upper() color "#ffff00" size 45 bold True
                else:
                    text store.seq_target[i].upper() color "#ffffff" size 35
                    
        hbox:
            xalign 0.5
            spacing 20
            textbutton "CIMA" action Function(click_sequence, "up")
            textbutton "BAIXO" action Function(click_sequence, "down")
            textbutton "ESQUERDA" action Function(click_sequence, "left")
            textbutton "DIREITA" action Function(click_sequence, "right")

# 4. Katia - Clicker de Documentos
screen minigame_clicker():
    modal True
    zorder 200
    add Solid("#000000cc")
    
    timer 0.1 repeat True action SetVariable("clicker_timer", store.clicker_timer - 0.1)
    
    if store.clicker_done >= 10:
        timer 0.1 action Return("win")
    if store.clicker_timer <= 0:
        timer 0.1 action Return("lose")
        
    text "Limpe a mesa antes do colapso! Tempo: [store.clicker_timer:.1f]" size 40 color "#fff" xalign 0.5 ypos 50
    
    for i in range(10):
        if not store.clicker_docs[i]["clicked"]:
            button:
                xpos store.clicker_docs[i]["x"]
                ypos store.clicker_docs[i]["y"]
                xysize (80, 100)
                background Solid("#ffffff")
                action Function(click_document, i)
                text "Doc" color "#000" align (0.5, 0.5)

# 5. Nicole - Puzzle de Diplomacia
screen minigame_diplomacy():
    modal True
    zorder 200
    add Solid("#000000cc")
    
    timer 0.1 repeat True action Function(update_diplomacy)
    
    if store.diplomacy_timer <= 0 or store.diplomacy_patience <= 0:
        timer 0.1 action Return("lose")
        
    vbox:
        xalign 0.5 yalign 0.2
        spacing 20
        text "Acalme sua mãe pelo telefone! Rápido!" size 40 color "#fff" xalign 0.5
        
        hbox:
            spacing 10
            xalign 0.5
            text "Paciência da Mãe:" color "#ffaaaa" size 25
            bar value store.diplomacy_patience range 100.0 xsize 300 ysize 25
            
        text "O que você responde para não ser tirada da casa?" size 30 color "#fff" xalign 0.5
        
        null height 20
        
        vbox:
            spacing 15
            xalign 0.5
            
            button:
                xsize 700 ysize 60
                background Solid("#444")
                hover_background Solid("#666")
                action Return("lose")
                text "Mãe, eu odeio o flat, você só quer me controlar!" align (0.5, 0.5)
                
            button:
                xsize 700 ysize 60
                background Solid("#444")
                hover_background Solid("#666")
                action Return("lose")
                text "Eu arrumei um estágio aqui perto, e não vou pro flat." align (0.5, 0.5)
                
            button:
                xsize 700 ysize 60
                background Solid("#444")
                hover_background Solid("#666")
                action Return("win")
                text "Morar na república é vital para construir meu capital político." align (0.5, 0.5)

# 6. Huey - Simon Says
screen minigame_simon():
    modal True
    zorder 200
    add Solid("#000000cc")
    
    if store.simon_showing:
        timer 0.5 repeat True action [SetVariable("simon_tick", store.simon_tick + 1), 
                                      If(store.simon_tick >= 7, true=[SetVariable("simon_showing", False), SetVariable("simon_user_idx", 0)])]
    
    vbox:
        xalign 0.5 yalign 0.5
        spacing 30
        text "Estabilize os BPMs repetindo a sequência!" size 40 color "#fff" xalign 0.5
        
        if store.simon_showing:
            text "Preste Atenção..." size 30 color "#fff" xalign 0.5
            frame:
                xalign 0.5
                xysize (150, 150)
                background Solid(store.simon_sequence[store.simon_tick // 2] if (store.simon_tick % 2 == 0 and (store.simon_tick // 2) < 4) else "#333")
        else:
            text "Sua Vez!" size 30 color "#fff" xalign 0.5
            hbox:
                xalign 0.5 spacing 20
                for c in ["#ff0000", "#0000ff", "#00ff00", "#ffff00"]:
                    button:
                        xysize (100, 100)
                        background Solid(c)
                        action [
                            If(store.simon_user_idx < 4 and store.simon_sequence[store.simon_user_idx] == c,
                               true=[SetVariable("simon_user_idx", store.simon_user_idx + 1), If(store.simon_user_idx == 3, true=Return("win"))],
                               false=Return("lose")
                            )
                        ]

# 7. Harem - Gestão de Estresse
screen minigame_harem():
    modal True
    zorder 200
    add Solid("#000000cc")
    
    timer 0.1 repeat True action Function(update_harem_game)
    
    if store.harem_lost:
        timer 0.1 action Return("lose")
    if store.harem_timer <= 0:
        timer 0.1 action Return("win")
        
    vbox:
        xalign 0.5 yalign 0.1
        text "Acalme Todas! Sobreviva por: [store.harem_timer:.1f]s" size 40 color "#fff" xalign 0.5
        
    grid 3 2:
        xalign 0.5 yalign 0.6
        spacing 40
        for i in range(6):
            vbox:
                spacing 10
                text store.harem_names[i] color "#fff" xalign 0.5
                bar value store.harem_stress[i] range 100.0 xsize 150 ysize 20
                button:
                    xysize (150, 150)
                    background Solid("#666")
                    text "ACALMAR" align(0.5, 0.5)
                    action Function(click_harem, i)
