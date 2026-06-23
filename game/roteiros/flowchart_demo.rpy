# ==============================================================================
# DEMONSTRAÇÃO DO SISTEMA DE FLOWCHART E GATING DE CAPÍTULO
# ==============================================================================

label flowchart_demo:
    # Cenário de fundo provisório
    scene black
    with dissolve
    
    narrator "Iniciando a demonstração do Sistema de Flowchart e Gating."
    narrator "Abra o menu para selecionar seu próximo capítulo."
    
    # Chama a interface (tela de árvore de seleção)
    call screen chapter_select
    
    # O resultado retornado pela screen (via action Return)
    $ selected_node = _return
    
    if selected_node == "back":
        narrator "Saindo da demonstração."
        return
        
    # Tenta transicionar para o capítulo clicado
    call chapter_transition(selected_node) from _call_chapter_transition
    
    # Fica em loop na demo para o usuário testar várias vezes
    jump flowchart_demo

# ==============================================================================
# LÓGICA DE VALIDAÇÃO (GATING)
# ==============================================================================
label chapter_transition(target_node_id):
    # Puxa o objeto do node para usarmos na narrativa
    $ node_obj = flowchart_system.nodes.get(target_node_id)
    
    # O jogo base usa persistent.unlocked_chapters
    if not hasattr(persistent, "unlocked_chapters") or persistent.unlocked_chapters is None:
        $ persistent.unlocked_chapters = ["intro", "capitulo1"]

    # Se o nó já estiver desbloqueado, o jogador pode acessá-lo.
    if target_node_id in persistent.unlocked_chapters:
        narrator "Acessando capítulo: [node_obj.name]..."
        
        # O usuário solicitou que, se iniciar direto de um cap desbloqueado, receba 70% dos status
        python:
            for stat, max_val in node_obj.required_stats.items():
                req_val = int(max_val * 0.70)
                if store.player_stats.get(stat, 0) < req_val:
                    store.player_stats[stat] = req_val
                    
            if node_obj.required_affinity:
                for char, max_pts in node_obj.required_affinity.items():
                    req_val = int(max_pts * 0.70)
                    current_pts = getattr(store, f"points_{char}", 0)
                    if current_pts < req_val:
                        # Injeta o valor exigido
                        globals()[f"points_{char}"] = req_val
                        # Chama a função de atualização de nível existente no sistemas_melhorados.rpy
                        if "update_relationship_level" in globals():
                            update_relationship_level(char)

        # Marca como jogado para a barra de progresso encher
        $ played_chapters.add(target_node_id)
        # Pula para o label correspondente ao id do nó
        jump expression target_node_id

    # --- TRAVA SEQUENCIAL ---
    # Verifica se o jogador está tentando pular capítulos.
    # Obtém a lista de todos os nós em ordem para descobrir qual é o anterior.
    python:
        nodes_list = list(flowchart_system.nodes.keys())
        target_idx = nodes_list.index(target_node_id)
        prev_node_id = nodes_list[target_idx - 1] if target_idx > 0 else None

    if prev_node_id and prev_node_id not in persistent.unlocked_chapters:
        $ prev_node_name = flowchart_system.nodes[prev_node_id].name
        narrator "Você não pode acessar este capítulo ainda. É necessário concluir o [prev_node_name] primeiro!"
        jump flowchart_demo

    # Se a ordem estiver correta (tentando abrir o próximo cap legítimo), iniciamos a validação de atributos
    narrator "O [node_obj.name] exige 70%% do teto das atividades internas dele."
    narrator "Calculando seus status..."
    
    python:
        # Chama a matemática da classe no arquivo systems_flowchart.rpy
        sucesso, mensagem_falha = flowchart_system.calculate_gating(target_node_id)
        
    if sucesso:
        # Passou na checagem! Destranca o capítulo e marca como aberto no persistent
        if target_node_id not in persistent.unlocked_chapters:
            $ persistent.unlocked_chapters.append(target_node_id)
        
        # Opcional: Feedback Visual (sons/telas)
        narrator "Validação Concluída! Você passou nos testes matemáticos."
        narrator "Iniciando o capítulo!"
        # Marca como jogado para a barra de progresso encher
        $ played_chapters.add(target_node_id)
        # Pula para o label
        jump expression target_node_id
    else:
        # Falhou na checagem de 70%
        narrator "Validação Falhou! Você não está pronto para essa fase."
        
        # Mostra o motivo exato retornado pelo sistema
        narrator "[mensagem_falha]"
        narrator "Você retornará para a rotina de evolução de status."
        
    return
