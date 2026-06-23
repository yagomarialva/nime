# ==============================================================================
# QUARTO DO PROTAGONISTA
# ==============================================================================

label quarto_protagonista:
    scene expression "images/cenarios/casa_interior.png" with dissolve
    
    menu:
        "Você está no seu quarto. O que deseja fazer?"
        "Dormir":
            mc "Vou descansar um pouco."
            # Avançar tempo e restaurar energia
            $ periodo_atual = 3 # Força a ser noite para dormir virar o dia
            call avancar_tempo(0)
            jump quarto_protagonista
            
        "Usar Computador":
            call screen computador_ui
            jump quarto_protagonista
            
        "Sair":
            return

# ==============================================================================
# INTERFACE DO COMPUTADOR
# ==============================================================================

screen computador_ui():
    zorder 200
    modal True
    
    add Solid("#000000aa")
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1000
        ysize 650
        background Solid("#1c1c1c")
        
        # Monitor bezel
        add Solid("#0a0a0a") xsize 1000 ysize 30 yalign 1.0
        
        vbox:
            ypos 20
            xalign 0.5
            spacing 20
            
            text "🖥️ NimeOS Desktop" size 30 color "#ffffff" xalign 0.5 bold True
            
            hbox:
                xalign 0.5
                spacing 40
                
                # Apps de Celular Espelhados
                textbutton "📱 Abrir Emulador de Celular" action Show("celular_ui")
                
                # Aba de Dicas
                textbutton "💡 Dicas do Jogo" action Show("computador_dicas")
                
        textbutton "Desligar Computador":
            action Hide("computador_ui"), Hide("computador_dicas"), Return()
            xalign 0.5
            yalign 0.95
            text_size 20

screen computador_dicas():
    zorder 201
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 400
        background Solid("#223344")
        padding (20, 20)
        
        vbox:
            spacing 10
            text "💡 Central de Dicas" size 25 color "#ffcc00" bold True
            
            viewport:
                mousewheel True
                scrollbars "vertical"
                vbox:
                    spacing 15
                    
                    text "1. Energia e Tempo:" size 18 color "#00ccff" bold True
                    text "Trabalhar nos locais consome Energia. Visitar novos locais não consome se não tiver evento. Se a energia acabar, venha dormir." size 16
                    
                    text "2. Status:" size 18 color "#00ccff" bold True
                    text "Use o dinheiro ganho nos trabalhos para comprar presentes para as garotas ou fazer melhorias na Loja pelo celular." size 16
                    
                    text "3. Afinidade:" size 18 color "#00ccff" bold True
                    text "Os presentes comprados aumentam a sua afinidade instantaneamente." size 16
                    
                    text "4. Encontros e Side-Quests:" size 18 color "#00ccff" bold True
                    text "Acesse o app 'Mensagens' no celular para aceitar side-quests de outros personagens e ganhar recompensas!" size 16
