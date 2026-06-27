init python:
    import random

    # 1. Larissa: Minijogo de Equilíbrio no Gelo
    def init_ice_skating():
        store.ice_balance = 50.0  # 0 to 100, 50 is perfectly balanced
        store.ice_momentum = random.choice([-1.0, 1.0])
        store.ice_timer = 15.0

    def update_ice_skating():
        store.ice_timer -= 0.1
        # Momentum gradually pushes the balance left or right, getting stronger
        store.ice_momentum += random.uniform(-0.5, 0.5)
        store.ice_balance += store.ice_momentum

    def ice_skate_lean(dir):
        if dir == "left":
            store.ice_balance -= 10.0
            store.ice_momentum -= 2.0
        elif dir == "right":
            store.ice_balance += 10.0
            store.ice_momentum += 2.0
            
    # 2. Camille: Minijogo de Constelações (Ligue os Pontos)
    def init_constellation():
        store.const_points = []
        for i in range(5):
            store.const_points.append({
                "x": random.uniform(0.2, 0.8),
                "y": random.uniform(0.2, 0.8),
                "active": False
            })
        store.const_current = 0
        store.const_timer = 10.0

    def click_constellation(idx):
        if idx == store.const_current:
            store.const_points[idx]["active"] = True
            store.const_current += 1
        else:
            # Reset on miss
            for p in store.const_points:
                p["active"] = False
            store.const_current = 0

    # 3. Samantha: Máquina de Garra
    def init_claw_machine():
        store.claw_x = 0.1
        store.claw_dir = 1
        store.claw_speed = 0.03
        store.claw_target_x = random.uniform(0.3, 0.7)
        store.claw_grabbed = False
        store.claw_win = False
        store.claw_timer = 10.0

    def update_claw_machine():
        if not store.claw_grabbed:
            store.claw_timer -= 0.1
            store.claw_x += store.claw_speed * store.claw_dir
            if store.claw_x > 0.9:
                store.claw_x = 0.9
                store.claw_dir = -1
            elif store.claw_x < 0.1:
                store.claw_x = 0.1
                store.claw_dir = 1

    def claw_grab():
        store.claw_grabbed = True
        if abs(store.claw_x - store.claw_target_x) < 0.05:
            store.claw_win = True
            
    # 4. Katia: Dividir Pipoca
    def init_popcorn():
        store.pop_katia = 50.0
        store.pop_mc = 50.0
        store.pop_timer = 15.0
        
    def update_popcorn():
        store.pop_timer -= 0.1
        store.pop_katia -= 0.5
        store.pop_mc -= 0.5
        
    def feed_popcorn(target):
        if target == "katia":
            store.pop_katia = min(100.0, store.pop_katia + 15.0)
        else:
            store.pop_mc = min(100.0, store.pop_mc + 15.0)

    # 5. Nicole: Etiqueta (Talheres)
    def init_etiquette():
        store.etiq_timer = 10.0
        store.etiq_target = random.choice(["Salada", "Peixe", "Carne", "Sobremesa"])
        
    def check_etiquette(choice):
        correct = False
        if store.etiq_target == "Salada" and choice == "Garfo Menor": correct = True
        if store.etiq_target == "Peixe" and choice == "Garfo Especial": correct = True
        if store.etiq_target == "Carne" and choice == "Garfo Maior": correct = True
        if store.etiq_target == "Sobremesa" and choice == "Garfinho de Cima": correct = True
        return correct

    # 6. Huey: Alinhamento de Órbitas
    def init_orbits():
        store.orbit1_ang = 0.0
        store.orbit2_ang = 180.0
        store.orbit1_speed = 5.0
        store.orbit2_speed = 3.0
        store.orbit_timer = 15.0
        store.orbit_aligned = False
        
    def update_orbits():
        if not store.orbit_aligned:
            store.orbit_timer -= 0.1
            store.orbit1_ang = (store.orbit1_ang + store.orbit1_speed) % 360
            store.orbit2_ang = (store.orbit2_ang + store.orbit2_speed) % 360
            
    def check_orbit_align():
        diff = abs(store.orbit1_ang - store.orbit2_ang)
        if diff < 15 or diff > 345:
            store.orbit_aligned = True
            return True
        return False

    # 7. Harem: Amigo Oculto
    def init_secret_santa():
        store.santa_timer = 20.0
        store.santa_girls = ["Larissa", "Camille", "Samantha", "Katia", "Nicole", "Huey"]
        store.santa_gifts = ["Bola de Vôlei", "Cristal", "Controle", "Caneta Tinteiro", "Joia", "Calculadora"]
        store.santa_matches = [0, 1, 2, 3, 4, 5] # Correct indices
        store.santa_current_girl = 0
        store.santa_mistake = False

    def check_santa_gift(gift_idx):
        if store.santa_matches[store.santa_current_girl] == gift_idx:
            store.santa_current_girl += 1
        else:
            store.santa_mistake = True


# ==========================================
# SCREENS DOS MINIJOGOS DO CAPÍTULO 11
# ==========================================

# 1. Larissa - Patinação no Gelo
screen minigame_ice_skating():
    modal True
    zorder 200
    add Solid("#000000cc")
    
    timer 0.1 repeat True action Function(update_ice_skating)
    
    if store.ice_balance <= 0 or store.ice_balance >= 100:
        timer 0.1 action Return("lose")
    if store.ice_timer <= 0:
        timer 0.1 action Return("win")

    vbox:
        xalign 0.5 yalign 0.5
        spacing 30
        text "Mantenha o Equilíbrio! Tempo: [store.ice_timer:.1f]" size 40 color "#fff" xalign 0.5
        
        frame:
            xsize 600 ysize 50
            background Solid("#333")
            # Cursor
            frame:
                xsize 20 ysize 60
                yalign 0.5
                xpos (store.ice_balance / 100.0)
                background Solid("#00ffff" if 40 < store.ice_balance < 60 else "#ff0000")
                
        hbox:
            xalign 0.5 spacing 100
            textbutton "< INCLINAR ESQUERDA" action Function(ice_skate_lean, "left") text_size 30
            textbutton "INCLINAR DIREITA >" action Function(ice_skate_lean, "right") text_size 30


# 2. Camille - Constelações
screen minigame_constellation():
    modal True
    zorder 200
    add Solid("#000000cc")
    
    timer 0.1 repeat True action SetVariable("const_timer", store.const_timer - 0.1)
    
    if store.const_current >= 5:
        timer 0.1 action Return("win")
    if store.const_timer <= 0:
        timer 0.1 action Return("lose")
        
    text "Ligue as Estrelas em Ordem! Tempo: [store.const_timer:.1f]" size 40 color "#fff" xalign 0.5 ypos 50
    
    for i in range(5):
        button:
            xpos store.const_points[i]["x"]
            ypos store.const_points[i]["y"]
            xysize (60, 60)
            background Solid("#ffff00" if store.const_points[i]["active"] else "#555")
            action Function(click_constellation, i)
            text str(i+1) color "#000" align (0.5, 0.5) size 30


# 3. Samantha - Máquina de Garra
screen minigame_claw():
    modal True
    zorder 200
    add Solid("#000000cc")
    
    timer 0.1 repeat True action Function(update_claw_machine)
    
    if store.claw_grabbed:
        if store.claw_win:
            timer 1.0 action Return("win")
        else:
            timer 1.0 action Return("lose")
    if store.claw_timer <= 0 and not store.claw_grabbed:
        timer 0.1 action Return("lose")

    vbox:
        xalign 0.5 yalign 0.2
        spacing 30
        text "Pegue a Pelúcia Rara! Tempo: [store.claw_timer:.1f]" size 40 color "#fff" xalign 0.5
        
        frame:
            xsize 600 ysize 200
            background Solid("#333")
            
            # Pelúcia Alvo
            frame:
                xpos store.claw_target_x
                yalign 0.9
                xysize (40, 40)
                background Solid("#ff00ff")
                
            # Garra
            frame:
                xpos store.claw_x
                yalign (0.8 if store.claw_grabbed else 0.1)
                xysize (30, 30)
                background Solid("#aaaaaa")
                
        if not store.claw_grabbed:
            textbutton "PEGAR!" action Function(claw_grab) xalign 0.5 text_size 40


# 4. Katia - Dividir Pipoca
screen minigame_popcorn():
    modal True
    zorder 200
    add Solid("#000000cc")
    
    timer 0.1 repeat True action Function(update_popcorn)
    
    if store.pop_katia <= 0 or store.pop_mc <= 0:
        timer 0.1 action Return("lose")
    if store.pop_timer <= 0:
        timer 0.1 action Return("win")

    vbox:
        xalign 0.5 yalign 0.5
        spacing 30
        text "Mantenha ambos alimentados sem tirar o olho da tela!" size 40 color "#fff" xalign 0.5
        text "Tempo Restante: [store.pop_timer:.1f]" size 30 color "#fff" xalign 0.5
        
        hbox:
            xalign 0.5 spacing 100
            vbox:
                spacing 10
                text "Sua Fome" color "#fff" xalign 0.5
                bar value store.pop_mc range 100.0 xsize 150 ysize 20
                textbutton "COMER PIPOCA" action Function(feed_popcorn, "mc")
                
            vbox:
                spacing 10
                text "Fome da Katia" color "#fff" xalign 0.5
                bar value store.pop_katia range 100.0 xsize 150 ysize 20
                textbutton "DAR PIPOCA PRA ELA" action Function(feed_popcorn, "katia")


# 5. Nicole - Etiqueta
screen minigame_etiquette():
    modal True
    zorder 200
    add Solid("#000000cc")
    
    timer 0.1 repeat True action SetVariable("etiq_timer", store.etiq_timer - 0.1)
    
    if store.etiq_timer <= 0:
        timer 0.1 action Return("lose")
        
    vbox:
        xalign 0.5 yalign 0.2
        spacing 20
        text "O Garçom trouxe o prato: [store.etiq_target]" size 40 color "#fff" xalign 0.5
        text "Qual talher você pega?! Tempo: [store.etiq_timer:.1f]" size 30 color "#ffaaaa" xalign 0.5
        
        null height 40
        
        hbox:
            spacing 20 xalign 0.5
            for fork in ["Garfo Menor", "Garfo Especial", "Garfo Maior", "Garfinho de Cima"]:
                button:
                    xysize (150, 150)
                    background Solid("#aaa")
                    text fork align (0.5, 0.5) text_align 0.5
                    action [If(check_etiquette(fork), true=Return("win"), false=Return("lose"))]


# 6. Huey - Alinhamento de Órbitas
screen minigame_orbits():
    modal True
    zorder 200
    add Solid("#000000cc")
    
    timer 0.1 repeat True action Function(update_orbits)
    
    if store.orbit_aligned:
        timer 0.5 action Return("win")
    if store.orbit_timer <= 0:
        timer 0.1 action Return("lose")
        
    vbox:
        xalign 0.5 yalign 0.2
        spacing 20
        text "Alinhe as Órbitas! Tempo: [store.orbit_timer:.1f]" size 40 color "#fff" xalign 0.5
        text "Clique em ALINHAR quando as barras se cruzarem no centro!" size 25 color "#aaa" xalign 0.5
        
        frame:
            xalign 0.5 yalign 0.5
            xsize 400 ysize 400
            background Solid("#333")
            
            # Orbit 1
            frame:
                xysize (20, 20)
                background Solid("#00ff00")
                yalign 0.5 xanchor 0.5
                # Simple linear representation for engine constraints
                xpos (store.orbit1_ang / 360.0)
                
            # Orbit 2
            frame:
                xysize (20, 20)
                background Solid("#ff0000")
                yalign 0.5 xanchor 0.5
                xpos (store.orbit2_ang / 360.0)
                
        textbutton "ALINHAR!" action [If(check_orbit_align(), true=Return("win"), false=Return("lose"))] xalign 0.5 text_size 40


# 7. Harem - Amigo Oculto
screen minigame_secret_santa():
    modal True
    zorder 200
    add Solid("#000000cc")
    
    timer 0.1 repeat True action SetVariable("santa_timer", store.santa_timer - 0.1)
    
    if store.santa_current_girl >= 6:
        timer 0.5 action Return("win")
    if store.santa_mistake or store.santa_timer <= 0:
        timer 0.1 action Return("lose")
        
    vbox:
        xalign 0.5 yalign 0.1
        spacing 20
        text "Distribua os Presentes! Tempo: [store.santa_timer:.1f]" size 40 color "#fff" xalign 0.5
        if store.santa_current_girl < 6:
            text "Para quem vai: [store.santa_gifts[store.santa_current_girl]]?" size 35 color "#ffff00" xalign 0.5
        
        grid 3 2:
            spacing 20 xalign 0.5
            for i in range(6):
                button:
                    xysize (200, 100)
                    background Solid("#444")
                    text store.santa_girls[i] align (0.5, 0.5)
                    action Function(check_santa_gift, i)
