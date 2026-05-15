screen mapa_interativo():
    # Impede do jogador interagir com o que estiver atrás
    modal True
    
    # Background temporário genérico
    add Solid("#333333")
    
    # Lógica do HUD de Tempo
    python:
        txt_hud = _("Dia ") + str(dia_atual) + " - " + get_nome_periodo(periodo_atual)
        
    # HUD Superior: Dia e Período
    frame:
        xalign 0.5 ypos 30
        padding (20, 10)
        background Solid("#00000088")
        text txt_hud size 30 color "#FFFFFF"

    # Define o tooltip global para podermos capturar o hover
    $ tooltip = GetTooltip()
    if tooltip:
        frame:
            xalign 0.5 ypos 90
            padding (15, 10)
            background Solid("#ffffffEE")
            text tooltip size 20 color "#000000" bold True

    # ==============================
    # BOTÕES DO MAPA (xpos, ypos genéricos)
    # ==============================
    
    # 1. Biblioteca
    python:
        evt_lib = game_events.get_pending_event("biblioteca", dia_atual, periodo_atual)
        lib_tooltip = _("Biblioteca") + (" (!)" if evt_lib else "")
    textbutton _("Biblioteca"):
        xpos 200 ypos 300
        text_size 25
        action Return("biblioteca")
        tooltip lib_tooltip
        
    # 2. Quadra
    python:
        evt_quadra = game_events.get_pending_event("quadra", dia_atual, periodo_atual)
        quadra_tooltip = _("Quadra de Esportes") + (" (!)" if evt_quadra else "")
    textbutton _("Quadra"):
        xpos 800 ypos 200
        text_size 25
        action Return("quadra")
        tooltip quadra_tooltip
        
    # 3. Cinema
    python:
        evt_cinema = game_events.get_pending_event("cinema", dia_atual, periodo_atual)
        cinema_tooltip = _("Cinema Universitário") + (" (!)" if evt_cinema else "")
    textbutton _("Cinema"):
        xpos 400 ypos 500
        text_size 25
        action Return("cinema")
        tooltip cinema_tooltip
        
    # 4. Galeria
    python:
        evt_galeria = game_events.get_pending_event("galeria", dia_atual, periodo_atual)
        galeria_tooltip = _("Galeria de Arte") + (" (!)" if evt_galeria else "")
    textbutton _("Galeria"):
        xpos 900 ypos 550
        text_size 25
        action Return("galeria")
        tooltip galeria_tooltip
        
    # 5. Laboratório
    python:
        evt_lab = game_events.get_pending_event("laboratorio", dia_atual, periodo_atual)
        lab_tooltip = _("Laboratório de Dados") + (" (!)" if evt_lab else "")
    textbutton _("Laboratório"):
        xpos 200 ypos 650
        text_size 25
        action Return("laboratorio")
        tooltip lab_tooltip
        
    # 6. Centro de Jogos
    python:
        evt_jogos = game_events.get_pending_event("jogos", dia_atual, periodo_atual)
        jogos_tooltip = _("Centro de Jogos") + (" (!)" if evt_jogos else "")
    textbutton _("Centro de Jogos"):
        xpos 600 ypos 700
        text_size 25
        action Return("jogos")
        tooltip jogos_tooltip
