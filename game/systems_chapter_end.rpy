# systems_chapter_end.rpy

init python:
    # Função para pegar nomes traduzidos de atributos
    def get_stat_name_pt(stat):
        names = {
            "energy": "Energia",
            "money": "Dinheiro",
            "intelligence": "Intelecto",
            "charisma": "Carisma",
            "fitness": "Físico",
            "creativity": "Criatividade"
        }
        return names.get(stat, stat.capitalize())

screen chapter_results(next_node_id):
    zorder 100
    modal True
    
    # Fundo semi-transparente escurecido
    add Solid("#000000dd")
    
    python:
        node = flowchart_system.nodes.get(next_node_id)
        if node is None:
            # Fallback seguro caso tentem chamar o fim no último epílogo
            stats_to_check = {}
            char_to_check = None
            affinity_to_check = {}
            node_name = "Conclusão"
        else:
            stats_to_check = node.required_stats
            affinity_to_check = node.required_affinity
            node_name = node.name

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 40
        background Solid("#1a1a1a")
        
        vbox:
            spacing 20
            xalign 0.5
            
            text "Capítulo Concluído!" size 60 color "#ffaa00" bold True xalign 0.5
            text "Calculando Progresso para: [node_name]" size 30 color "#cccccc" xalign 0.5
            
            null height 20
            
            # Barras de Atributos
            if stats_to_check:
                text "Requisitos de Atributos (70% do Teto)" size 24 color "#ffffff" xalign 0.0
                for stat, max_val in stats_to_check.items():
                    $ req_val = int(max_val * 0.70)
                    $ cur_val = store.player_stats.get(stat, 0)
                    $ pct = float(cur_val) / float(req_val) if req_val > 0 else 1.0
                    $ pct = min(pct, 1.0)
                    $ is_pass = cur_val >= req_val
                    $ color_bar = "#00ff00" if is_pass else "#ff3333"
                    $ stat_pt = get_stat_name_pt(stat)
                    
                    hbox:
                        spacing 20
                        xsize 600
                        text "[stat_pt]" size 24 color "#ffffff" xalign 0.0 min_width 150
                        
                        # Barra manual via ui ou frame
                        frame:
                            xsize 300
                            ysize 25
                            yalign 0.5
                            background Solid("#333333")
                            
                            frame:
                                xsize int(300 * pct)
                                ysize 25
                                background Solid(color_bar)
                                
                        text "[cur_val] / [req_val]" size 24 color color_bar xalign 1.0
            
            # Barras de Afinidade (se houver)
            if affinity_to_check:
                null height 10
                text "Requisitos de Afinidade (70% do Teto)" size 24 color "#ffffff" xalign 0.0
                
                for char, max_pts in affinity_to_check.items():
                    $ char_pts_req = int(max_pts * 0.70)
                    $ cur_pts = getattr(store, "points_" + char, 0)
                    $ pct_char = float(cur_pts) / float(char_pts_req) if char_pts_req > 0 else 1.0
                    $ pct_char = min(pct_char, 1.0)
                    $ is_pass_char = cur_pts >= char_pts_req
                    $ color_bar_char = "#00ff00" if is_pass_char else "#ff3333"
                    $ char_name = char.capitalize()
                    
                    hbox:
                        spacing 20
                        xsize 600
                        text "[char_name]" size 24 color "#ffffff" xalign 0.0 min_width 150
                        
                        frame:
                            xsize 300
                            ysize 25
                            yalign 0.5
                            background Solid("#333333")
                            
                            frame:
                                xsize int(300 * pct_char)
                                ysize 25
                                background Solid(color_bar_char)
                                
                        text "[cur_pts] / [char_pts_req]" size 24 color color_bar_char xalign 1.0

            null height 30
            
            # Botão de Continuar
            textbutton "Avançar" action Return(True) xalign 0.5 text_size 30 text_color "#ffffff" text_hover_color "#ffaa00"

label end_of_chapter_validation(next_chapter_id):
    # Exibe a tela de resultados
    show screen chapter_results(next_chapter_id) with dissolve
    
    # Pausa o jogo até o jogador clicar no botão Avançar
    $ ui.interact()
    
    hide screen chapter_results with dissolve
    
    # Valida usando a função do FlowchartSystem
    python:
        # Puxa o nó atual (último capítulo jogado) baseado no next_chapter_id
        nodes_list = list(flowchart_system.nodes.keys())
        if next_chapter_id in nodes_list:
            next_idx = nodes_list.index(next_chapter_id)
            current_chapter_id = nodes_list[next_idx - 1] if next_idx > 0 else next_chapter_id
        else:
            current_chapter_id = next_chapter_id
            
        sucesso, mensagem = flowchart_system.calculate_gating(next_chapter_id)
        
    if sucesso:
        narrator "Avaliação concluída. Você atende aos requisitos!"
        
        # Adiciona o próximo capítulo aos destrancados globais
        if next_chapter_id not in persistent.unlocked_chapters:
            $ persistent.unlocked_chapters.append(next_chapter_id)
            
        narrator "O [flowchart_system.nodes[next_chapter_id].name] foi desbloqueado."
        jump expression next_chapter_id
    else:
        narrator "Você não atinge os requisitos mínimos para prosseguir para o próximo capítulo."
        narrator "[mensagem]"
        narrator "Retornando à Árvore de Seleção de Capítulos. Jogue capítulos anteriores novamente para acumular os atributos e pontos necessários!"
        
        # Volta para o Flowchart
        jump flowchart_demo
