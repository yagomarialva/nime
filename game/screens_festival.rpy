screen hud_convite_fogos():
    zorder 200
    modal True
    
    add Solid("#000000cc")
    
    frame:
        background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)
        xalign 0.5
        yalign 0.5
        xsize 700
        padding (30, 30)
        
        vbox:
            spacing 15
            xalign 0.5
            
            text "Para quem você vai mandar mensagem convidando para ver os fogos?" size 30 color "#ffffff" bold True text_align 0.5 xalign 0.5
            
            null height 10
            
            # Opção Harém / Amizade Colorida
            textbutton "Mandar no Grupo da Casa (Ir com todas)":
                action Return("grupo")
                xalign 0.5
                text_size 24
            
            null height 10
            
            # Botões das rotas individuais (Requer afinidade >= 30)
            if getattr(store, "points_larissa", 0) >= 30:
                textbutton "Convidar Larissa (Rota Larissa)":
                    action Return("larissa")
                    xalign 0.5
                    text_size 24
            else:
                textbutton "Convidar Larissa (Afinidade insuficiente)":
                    action NullAction()
                    xalign 0.5
                    text_color "#555555"
                    text_size 24
                    
            if getattr(store, "points_camille", 0) >= 30:
                textbutton "Convidar Camille (Rota Camille)":
                    action Return("camille")
                    xalign 0.5
                    text_size 24
            else:
                textbutton "Convidar Camille (Afinidade insuficiente)":
                    action NullAction()
                    xalign 0.5
                    text_color "#555555"
                    text_size 24
                    
            if getattr(store, "points_samantha", 0) >= 30:
                textbutton "Convidar Samantha (Rota Samantha)":
                    action Return("samantha")
                    xalign 0.5
                    text_size 24
            else:
                textbutton "Convidar Samantha (Afinidade insuficiente)":
                    action NullAction()
                    xalign 0.5
                    text_color "#555555"
                    text_size 24
                    
            if getattr(store, "points_katia", 0) >= 30:
                textbutton "Convidar Katia (Rota Katia)":
                    action Return("katia")
                    xalign 0.5
                    text_size 24
            else:
                textbutton "Convidar Katia (Afinidade insuficiente)":
                    action NullAction()
                    xalign 0.5
                    text_color "#555555"
                    text_size 24
                    
            if getattr(store, "points_nicole", 0) >= 30:
                textbutton "Convidar Nicole (Rota Nicole)":
                    action Return("nicole")
                    xalign 0.5
                    text_size 24
            else:
                textbutton "Convidar Nicole (Afinidade insuficiente)":
                    action NullAction()
                    xalign 0.5
                    text_color "#555555"
                    text_size 24
                    
            if getattr(store, "points_huey", 0) >= 30:
                textbutton "Convidar Huey (Rota Huey)":
                    action Return("huey")
                    xalign 0.5
                    text_size 24
            else:
                textbutton "Convidar Huey (Afinidade insuficiente)":
                    action NullAction()
                    xalign 0.5
                    text_color "#555555"
                    text_size 24
