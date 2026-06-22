init python:
    # Wallpapers
    current_wallpaper = "#1c1c1c"
    unlocked_wallpapers = [
        {"name": "Padrão (Escuro)", "color": "#1c1c1c", "price": 0},
        {"name": "Azul Neon", "color": "#0d1b2a", "price": 100},
        {"name": "Rosa Pastel", "color": "#ffb3c6", "price": 150},
        {"name": "Verde Matrix", "color": "#003300", "price": 200}
    ]
    
    # Store items
    store_items = [
        {"name": "Urso de Pelúcia", "price": 50, "affinity": 5, "target": "Nicole"},
        {"name": "Livro de Romance", "price": 50, "affinity": 5, "target": "Katia"},
        {"name": "Ingresso de Show", "price": 100, "affinity": 10, "target": "Samantha"}
    ]
    
    # Quests / Messages
    available_quests = [
        {"id": "q1", "sender": "Professor Alan", "title": "Me ajude com planilhas", "reward_money": 100, "cost_energy": 20, "completed": False},
        {"id": "d1", "sender": "Nicole", "title": "Convite: Tomar Sorvete", "cost_money": 50, "reward_affinity": 10, "completed": False}
    ]

screen hud_celular():
    zorder 90
    
    frame:
        background None
        xalign 0.98
        yalign 0.85
        
        imagebutton:
            idle Solid("#333333", xysize=(50, 80))
            hover Solid("#555555", xysize=(50, 80))
            action Show("celular_ui")
            tooltip "Abrir Celular"

        text "📱" align (0.5, 0.5) size 30

screen celular_ui():
    zorder 200
    modal True
    
    # Background para escurecer a tela e dar foco ao celular
    add Solid("#000000aa")
    
    # Corpo do Celular
    frame:
        xalign 0.5
        yalign 0.5
        xsize 400
        ysize 700
        background Solid(current_wallpaper)
        
        # Borda Superior (Câmera/Auto-falante)
        add Solid("#0a0a0a") xsize 400 ysize 40 yalign 0.0
        text "12:00" xalign 0.5 yalign 0.02 size 14 color "#ffffff"
        
        vbox:
            ypos 50
            xalign 0.5
            spacing 15
            
            # Cabeçalho
            text "📱 Meu Celular" size 28 color "#ffffff" xalign 0.5 bold True
            
            # Abas (Duas linhas de apps)
            grid 2 2:
                xalign 0.5
                spacing 20
                textbutton "Contatos" action Show("celular_contatos")
                textbutton "Notas" action Show("celular_memorias")
                textbutton "Loja" action Show("celular_loja")
                textbutton "Mensagens" action Show("celular_mensagens")
                
            null height 20
            
            # Aba de Wallpapers na tela inicial
            textbutton "Mudar Fundo":
                action Show("celular_wallpapers")
                xalign 0.5
            
            text "Bem-vindo ao NimeOS." size 16 color "#888888" xalign 0.5
            
        # Botão de Voltar / Fechar (Embaixo)
        textbutton "Home ⌂":
            action Hide("celular_ui"), Hide("celular_contatos"), Hide("celular_memorias"), Hide("celular_loja"), Hide("celular_mensagens"), Hide("celular_wallpapers")
            xalign 0.5
            yalign 0.95
            text_size 20
            text_color "#ffffff"

screen celular_contatos():
    zorder 201
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 380
        ysize 500
        yoffset 30
        background Solid("#252525")
        padding (20, 20)
        
        vbox:
            spacing 10
            
            text "👥 Relacionamentos" size 22 color "#ffcc00" bold True
            
            # Lista de Afinidades
            viewport:
                mousewheel True
                scrollbars "vertical"
                vbox:
                    spacing 15
                    
                    # Nicole
                    hbox:
                        spacing 10
                        text "Nicole:" size 18 color "#ffffff"
                        text "[points_nicole]/100" size 18 color "#4CAF50"
                        
                    # Katia
                    hbox:
                        spacing 10
                        text "Katia:" size 18 color "#ffffff"
                        text "[points_katia]/100" size 18 color "#4CAF50"
                        
                    # Samantha
                    hbox:
                        spacing 10
                        text "Samantha:" size 18 color "#ffffff"
                        text "[points_samantha]/100" size 18 color "#4CAF50"
                        
                    # Larissa
                    hbox:
                        spacing 10
                        text "Larissa:" size 18 color "#ffffff"
                        text "[points_larissa]/100" size 18 color "#4CAF50"
                        
                    # Huey
                    hbox:
                        spacing 10
                        text "Huey:" size 18 color "#ffffff"
                        text "[points_huey]/100" size 18 color "#4CAF50"
                        
                    # Camille
                    hbox:
                        spacing 10
                        text "Camille:" size 18 color "#ffffff"
                        text "[points_camille]/100" size 18 color "#4CAF50"

screen celular_memorias():
    zorder 201
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 380
        ysize 500
        yoffset 30
        background Solid("#252525")
        padding (20, 20)
        
        vbox:
            spacing 10
            
            text "📝 Notas Compartilhadas" size 22 color "#00ccff" bold True
            
            viewport:
                mousewheel True
                scrollbars "vertical"
                vbox:
                    spacing 15
                    if len(shared_memories) == 0:
                        text "Nenhuma memória registrada ainda..." size 14 color "#888888" italic True
                    else:
                        for memory in shared_memories:
                            frame:
                                xsize 320
                                background Solid("#333333")
                                padding (10, 10, 10, 10)
                                text memory size 14 color "#ffffff"

screen celular_loja():
    zorder 201
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 380
        ysize 500
        yoffset 30
        background Solid("#252525")
        padding (20, 20)
        
        vbox:
            spacing 10
            text "🛒 NimeStore" size 22 color "#ff4444" bold True
            text "Seu dinheiro: [store.player_stats['money']]" size 16 color "#85bb65"
            
            viewport:
                mousewheel True
                scrollbars "vertical"
                vbox:
                    spacing 15
                    for item in store_items:
                        frame:
                            xsize 320
                            background Solid("#333333")
                            padding (10, 10, 10, 10)
                            vbox:
                                text item["name"] size 16 color "#fff"
                                text "Presente para: [item['target']] (+[item['affinity']] Afinidade)" size 12 color "#888"
                                textbutton "Comprar ($" + str(item["price"]) + ")":
                                    action If(store.player_stats["money"] >= item["price"],
                                        true=[
                                            Function(update_player_stat, "money", -item["price"]),
                                            If(item["target"] == "Nicole", true=SetVariable("points_nicole", points_nicole + item["affinity"])),
                                            If(item["target"] == "Katia", true=SetVariable("points_katia", points_katia + item["affinity"])),
                                            If(item["target"] == "Samantha", true=SetVariable("points_samantha", points_samantha + item["affinity"])),
                                            Notify("Comprado! Afinidade com " + item["target"] + " subiu.")
                                        ],
                                        false=Notify("Dinheiro insuficiente!")
                                    )

screen celular_mensagens():
    zorder 201
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 380
        ysize 500
        yoffset 30
        background Solid("#252525")
        padding (20, 20)
        
        vbox:
            spacing 10
            text "💬 Mensagens & Quests" size 22 color "#33ccff" bold True
            
            viewport:
                mousewheel True
                scrollbars "vertical"
                vbox:
                    spacing 15
                    for q in available_quests:
                        if not q["completed"]:
                            frame:
                                xsize 320
                                background Solid("#333333")
                                padding (10, 10, 10, 10)
                                vbox:
                                    text q["sender"] size 16 color "#ffcc00" bold True
                                    text q["title"] size 14 color "#fff"
                                    
                                    if "reward_money" in q:
                                        text "Recompensa: $" + str(q["reward_money"]) + " | Custo: " + str(q["cost_energy"]) + " Energia" size 12 color "#aaa"
                                        textbutton "Aceitar Trabalho":
                                            action If(store.player_stats["energy"] >= q["cost_energy"],
                                                true=[
                                                    Function(update_player_stat, "energy", -q["cost_energy"]),
                                                    Function(update_player_stat, "money", q["reward_money"]),
                                                    SetDict(q, "completed", True),
                                                    Notify("Trabalho concluído!")
                                                ],
                                                false=Notify("Energia insuficiente!")
                                            )
                                            
                                    elif "reward_affinity" in q:
                                        text "Custo do Encontro: $" + str(q["cost_money"]) size 12 color "#aaa"
                                        textbutton "Sair em Encontro":
                                            action If(store.player_stats["money"] >= q["cost_money"],
                                                true=[
                                                    Function(update_player_stat, "money", -q["cost_money"]),
                                                    SetVariable("points_nicole", points_nicole + q["reward_affinity"]),
                                                    SetDict(q, "completed", True),
                                                    Notify("Encontro incrível! Afinidade subiu.")
                                                ],
                                                false=Notify("Dinheiro insuficiente!")
                                            )

screen celular_wallpapers():
    zorder 201
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 380
        ysize 500
        yoffset 30
        background Solid("#252525")
        padding (20, 20)
        
        vbox:
            spacing 10
            text "🖼️ Wallpapers" size 22 color "#cc33ff" bold True
            text "Dinheiro: [store.player_stats['money']]" size 14 color "#85bb65"
            
            viewport:
                mousewheel True
                scrollbars "vertical"
                vbox:
                    spacing 15
                    for w in unlocked_wallpapers:
                        frame:
                            xsize 320
                            background Solid(w["color"])
                            padding (10, 10, 10, 10)
                            vbox:
                                text w["name"] size 16 color "#fff" outlines [(2, "#000")]
                                if current_wallpaper == w["color"]:
                                    text "Ativo" size 14 color "#0f0" outlines [(2, "#000")]
                                else:
                                    if w["price"] == 0:
                                        textbutton "Aplicar":
                                            action SetVariable("current_wallpaper", w["color"])
                                    else:
                                        textbutton "Comprar ($" + str(w["price"]) + ") e Aplicar":
                                            action If(store.player_stats["money"] >= w["price"],
                                                true=[
                                                    Function(update_player_stat, "money", -w["price"]),
                                                    SetDict(w, "price", 0),
                                                    SetVariable("current_wallpaper", w["color"])
                                                ],
                                                false=Notify("Dinheiro insuficiente!")
                                            )
