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
                    narrator "Você ganhou 50 de dinheiro!"
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
                    narrator "Você ganhou 60 de dinheiro!"
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
                    narrator "Você ganhou 50 de dinheiro!"
                else:
                    mc "Estou muito cansado, perdi muito tempo e não terminei."
                    narrator "Você falhou no trabalho e não recebeu nada."
            else:
                mc "Não consigo correr atrás dessas bolas agora..."
        "Voltar":
            pass
            
    return
