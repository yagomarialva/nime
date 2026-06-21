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
        background Solid("#1c1c1c")
        
        # Borda Superior (Câmera/Auto-falante)
        add Solid("#0a0a0a") xsize 400 ysize 40 yalign 0.0
        text "12:00" xalign 0.5 yalign 0.02 size 14 color "#ffffff"
        
        vbox:
            ypos 50
            xalign 0.5
            spacing 15
            
            # Cabeçalho
            text "📱 Meu Celular" size 28 color "#ffffff" xalign 0.5 bold True
            
            # Abas
            hbox:
                xalign 0.5
                spacing 20
                textbutton "Contatos" action Show("celular_contatos")
                textbutton "Notas/Memórias" action Show("celular_memorias")
                
            null height 20
            
            # Tela Inicial Padrão (Pode mostrar um resumo ou logo)
            text "Bem-vindo ao NimeOS." size 16 color "#888888" xalign 0.5
            text "Selecione um app acima." size 14 color "#888888" xalign 0.5
            
        # Botão de Voltar / Fechar (Embaixo)
        textbutton "Home ⌂":
            action Hide("celular_ui"), Hide("celular_contatos"), Hide("celular_memorias")
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
