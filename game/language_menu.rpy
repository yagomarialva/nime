# Menu de Seleção de Idiomas
# Interface para escolher entre português e inglês

screen language_selection():
    modal True
    
    # Fundo escuro
    add "#000000" alpha 0.8
    
    # Container principal
    frame:
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 400
        background "#2c2c2c"
        padding (40, 40)
        
        vbox:
            spacing 20
            
            # Título
            text _("Selecionar Idioma / Select Language"):
                xalign 0.5
                size 32
                color "#ffffff"
                font gui.interface_text_font
                bold True
            
            # Espaçador
            null height 20
            
            # Botões de idiomas
            vbox:
                spacing 15
                xalign 0.5
                
                # Português
                button:
                    xsize 400
                    ysize 60
                    background "#4a4a4a"
                    hover_background "#6a6a6a"
                    action Function(change_language_and_close, "pt")
                    
                    text "🇧🇷 Português":
                        xalign 0.5
                        yalign 0.5
                        size 24
                        color "#ffffff"
                        font gui.interface_text_font
                
                # Inglês
                button:
                    xsize 400
                    ysize 60
                    background "#4a4a4a"
                    hover_background "#6a6a6a"
                    action Function(change_language_and_close, "en")
                    
                    text "🇺🇸 English":
                        xalign 0.5
                        yalign 0.5
                        size 24
                        color "#ffffff"
                        font gui.interface_text_font
            
            # Espaçador
            null height 30
            
            # Botão de fechar
            button:
                xsize 200
                ysize 40
                xalign 0.5
                background "#666666"
                hover_background "#888888"
                action Hide("language_selection")
                
                text _("Fechar / Close"):
                    xalign 0.5
                    yalign 0.5
                    size 18
                    color "#ffffff"
                    font gui.interface_text_font

# Função para mostrar o menu de idiomas
label show_language_menu:
    call screen language_selection
    return