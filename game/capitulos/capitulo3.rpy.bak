label capitulo3:
    if "capitulo3" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo3")
        
    scene bg sala_jantar with fade
    
    narrator "Manhã seguinte à Crise da Conta de Luz. A tensão na casa havia mudado de 'vamos ser despejados' para 'nós precisamos criar a Capela Sistina em três dias'."
    
    narrator "O professor Wendell foi bem claro: se não provássemos o valor cultural da casa com um Projeto Artístico Comunitário, a bolsa já era."
    
    show nicole neutral at right
    
    nicole "Muito bem. O plano de ação é simples. Precisamos de uma obra que comunique 'jovens acadêmicos revitalizando o patrimônio'."
    
    narrator "No centro da sala, a nossa suposta salvação parecia estar em curto-circuito. Huey encarava a parede descascada da sala com a intensidade de quem tenta ler mentes."
    
    # Não existe um sprite exato chamado huey_neutral ou algo assim, o user só falou 'huey sad' antes, mas vamos tentar neutral e lidar com a imagem dps
    show huey neutral at left
    
    huey "...Ocre. Tem um subtexto de ocre nessa parede. Um eco de... desespero de 1970."
    
    mc "Huey, a gente não vai restaurar a parede. A gente precisa criar uma arte nova em cima dela. Um mural."
    
    huey "Mas como eu posso impor minhas cores sobre uma parede que ainda está chorando o seu passado? As texturas estão gritando comigo."
    
    narrator "Ao contrário da Samantha, que se escondia das pessoas por medo, a Huey simplesmente não estava na mesma frequência de rádio que o resto da humanidade. Para ela, o mundo era um quadro abstrato constante."
    
    katia "Ótimo. Nossa artista fuma as tintas em vez de pintar com elas."
    
    nicole "Concentre-se, Huey! Precisamos de um rascunho até o meio-dia!"
    
    huey "O meio-dia tem uma luz muito agressiva... o amarelo queima as ideias..."
    
    narrator "Antes que Nicole pudesse gritar, a campainha tocou."
    narrator "Na verdade, não foi a campainha. Foi um sino de vento batendo contra a madeira da porta."
    
    scene bg casa_interior with dissolve
    
    narrator "Fui abrir a porta. A fumaça de um incenso de sândalo me atingiu em cheio no rosto."
    
    show camille neutral at center
    
    narrator "Uma garota de cabelos escuros e olhar sereno estava parada na varanda. Ela usava roupas leves e carregava duas malas imensas e um vaso gigantesco de espada-de-são-jorge."
    
    "???" "As correntes de energia desta casa estão completamente obstruídas. A madeira daqui respira raiva."
    
    mc "E você é... o controle de pragas astrais?"
    
    camille "Sou Camille. A sexta moradora."
    
    narrator "Ela passou por mim com uma naturalidade assustadora, deixando as malas pesadíssimas no chão como se não pesassem nada."
    
    scene bg sala_jantar with dissolve
    
    show camille neutral at center
    show nicole angry at right
    show huey neutral at left
    
    camille "Paz profunda a todas. Eu sinto muito a vibração de controle vindo de você, loirinha. E você..."
    narrator "Camille olhou para Huey."
    camille "Sua aura é completamente magenta. Brilhante, porém dispersa."
    
    huey "Magenta... é uma boa cor para o desespero de 1970."
    
    nicole "Mas que loucura é essa?! A casa já está um caos e mandam uma mística no meio do prazo do edital?"
    
    camille "Não se preocupe com o prazo. O tempo é uma construção ilusória. Aceite um chá de erva-cidreira e o mural vai fluir."
    
    hide nicole
    hide huey
    hide camille
    
    mc "E assim, nossa formação estava completa. Seis personalidades presas numa casa velha, tentando pintar um mural para salvar a própria pele."
    
    # === LOOP DO MAPA CAP 3 ===
    $ dia_atual = 3
    $ periodo_atual = 1
    
    $ game_events.events = {}
    
    # Dia 1 (Cap 3)
    $ game_events.add_event("quintal", "evento_huey_bloqueio", 3, [1, 2, 3])
    $ game_events.add_event("cozinha_escura", "evento_camille_cha", 3, [1, 2, 3])

    # Podemos colocar mais coisas no mapa se quiser
    # $ game_events.add_event("quadra", "evento_larissa_treino_leve", 3, [1, 2, 3]) # Removido temporariamente para o minigame da quadra rodar

label loop_mapa_cap3:
    if dia_atual >= 4:
        mc "Chega. O mural precisa ser terminado hoje à noite. Todo mundo pra sala."
        jump capitulo3_mural

    call screen mapa_modal
    
    $ local_escolhido = _return
    
    if local_escolhido is None:
        jump loop_mapa_cap3
    
    $ evt_label = game_events.get_pending_event(local_escolhido, dia_atual, periodo_atual)
    
    if evt_label:
        if evt_label == "evento_huey_bloqueio":
            $ add_shared_memory("huey_cores", ["huey"], "Descobri que o silêncio da Huey é porque o cérebro dela é barulhento demais.")
        elif evt_label == "evento_camille_cha":
            $ add_shared_memory("camille_peso", ["camille"], "Camille confessou que ser a âncora espiritual de todo mundo é exaustivo.")
            
        call expression evt_label
        
        $ game_events.mark_completed(evt_label)
        call avancar_tempo(15)
    else:
        call local_sem_evento(local_escolhido)
        call avancar_tempo(15)
        
    jump loop_mapa_cap3