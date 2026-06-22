# === HUD (Heads Up Display) ===
# Exibe os status do jogador, tempo atual e botão do inventário.

screen player_hud():
    zorder 100

    frame:
        xalign 1.0
        yalign 0.0
        xmargin 20
        ymargin 20
        padding (15, 10, 15, 10)
        background Solid("#16213ecc")
        
        hbox:
            spacing 20
            yalign 0.5

            # Tempo e Dia
            vbox:
                spacing 2
                text _("Dia [dia_atual]") size 16 color "#ffffff" bold True
                text get_nome_periodo(periodo_atual) size 14 color "#66c1e0"

            # Separador
            add Solid("#aaaaaa") xsize 1 ysize 30 yalign 0.5

            # Energia
            vbox:
                spacing 2
                text _("Energia") size 12 color "#aaaaaa"
                hbox:
                    spacing 5
                    text "⚡" size 16 yalign 0.5 color "#ffcc00"
                    text str(store.player_stats["energy"]) size 16 color "#ffffff" bold True yalign 0.5

            # Dinheiro
            vbox:
                spacing 2
                text _("Dinheiro") size 12 color "#aaaaaa"
                hbox:
                    spacing 5
                    text "💵" size 16 yalign 0.5 color "#85bb65"
                    text str(store.player_stats["money"]) size 16 color "#ffffff" bold True yalign 0.5
                    
            # Inteligência
            vbox:
                spacing 2
                text _("Intelecto") size 12 color "#aaaaaa"
                hbox:
                    spacing 5
                    text "🧠" size 16 yalign 0.5 color "#ff66cc"
                    text str(store.player_stats["intelligence"]) size 16 color "#ffffff" bold True yalign 0.5

            # Físico
            vbox:
                spacing 2
                text _("Físico") size 12 color "#aaaaaa"
                hbox:
                    spacing 5
                    text "💪" size 16 yalign 0.5 color "#ff9933"
                    text str(store.player_stats["fitness"]) size 16 color "#ffffff" bold True yalign 0.5

            # Carisma
            vbox:
                spacing 2
                text _("Carisma") size 12 color "#aaaaaa"
                hbox:
                    spacing 5
                    text "🗣️" size 16 yalign 0.5 color "#33ccff"
                    text str(store.player_stats["charisma"]) size 16 color "#ffffff" bold True yalign 0.5

            # Criatividade
            vbox:
                spacing 2
                text _("Criatividade") size 12 color "#aaaaaa"
                hbox:
                    spacing 5
                    text "🎨" size 16 yalign 0.5 color "#cc33ff"
                    text str(store.player_stats["creativity"]) size 16 color "#ffffff" bold True yalign 0.5

            # Separador
            add Solid("#aaaaaa") xsize 1 ysize 30 yalign 0.5

            # Botões (Inventário e Celular)
            hbox:
                spacing 10
                
                # Inventário
                textbutton "🎒":
                    text_size 24
                    action Show("inventory_ui")
                    yalign 0.5
                    
                # Celular
                textbutton "📱":
                    text_size 24
                    action Show("celular_ui")
                    yalign 0.5
