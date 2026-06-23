label capitulo5:
    if "capitulo5" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo5")
        
    scene bg casa_interior with fade
    
    narrator "A sala da Rua Aurora nunca pareceu tão pequena."
    
    show nicole sad at center
    
    narrator "A mãe da Nicole não gritou. Mulheres daquele círculo social não gritam. A crueldade dela estava no tom de voz, baixo, calculado, e frio como lâminas."
    
    "Mãe da Nicole" "Eu não vou repetir, Nicole. Arruma suas malas. O seu pai já falou com o Reitor. O nosso motorista está esperando."
    
    nicole "Mãe, por favor... Eu passei no edital por mérito..."
    
    "Mãe da Nicole" "Mérito? Ficar morando de favor em uma espelunca insalubre com viciados e desajustadas é mérito?"
    
    show katia angry at right
    
    katia "Olha aqui, Madame Botox. Essa espelunca insalubre não tem porta giratória. Ninguém te chamou."
    
    narrator "Nicole engasgou. O choque na sala era palpável. Katia, a arqui-inimiga da Nicole, tinha acabado de se enfiar entre a herdeira rica e a mãe dela."
    
    "Mãe da Nicole" "Não ouse se dirigir a mim."
    
    katia "A porta da rua é a serventia da casa. Vai pela sombra antes que o meu chiclete caia nesse seu casaco de dálmata."
    
    narrator "A mãe de Nicole olhou de Katia para a filha, com nojo absoluto."
    
    "Mãe da Nicole" "Eu não vou ser humilhada por plebeus. Se você escolher ficar nesta pocilga amanhã, Nicole, os seus cartões de crédito serão todos cancelados às oito da manhã. E os advogados da família darão um jeito de 'provar' que a sua estadia aqui fere as regras do edital financeiro."
    
    narrator "Ela se virou, os saltos batendo como martelos no chão de madeira, e sumiu na noite."
    
    hide katia
    show nicole sad at center
    
    narrator "Assim que o barulho do carro de luxo sumiu na rua, Nicole caiu de joelhos. Não houve choro. Apenas um tremor silencioso e incontrolável."
    
    mc "Nicole..."
    
    nicole "Eles vão tirar... eles vão tirar a casa de nós. Meus cartões estão bloqueados e se os advogados provarem renda alta, o professor Wendell tem que me expulsar."
    
    narrator "A muralha de gelo caiu. A síndica perfeita era apenas uma garota aterrorizada."
    
    # === LOOP DO MAPA CAP 5 ===
    $ dia_atual = 5
    $ periodo_atual = 1
    
    $ game_events.events = {}
    
    # Dia 1 (Cap 5)
    $ game_events.add_event("biblioteca", "evento_nicole_biblioteca", 5, [1, 2, 3])
    $ game_events.add_event("cozinha_escura", "evento_katia_alianca", 5, [1, 2, 3])

label loop_mapa_cap5:
    if dia_atual >= 6:
        mc "Chegou a hora. Hoje a mãe da Nicole volta. Eu preciso estar pronto para a guerra no tribunal da nossa sala."
        jump capitulo5_confronto

    call screen mapa_modal
    
    $ local_escolhido = _return
    
    if local_escolhido is None:
        jump loop_mapa_cap5
    
    $ evt_label = game_events.get_pending_event(local_escolhido, dia_atual, periodo_atual)
    
    if evt_label:
        if evt_label == "evento_nicole_biblioteca":
            $ add_shared_memory("nicole_defesa", ["nicole"], "Pesquisei até os olhos sangrarem para encontrar uma brecha na lei de emancipação para salvar Nicole.")
        elif evt_label == "evento_katia_alianca":
            $ add_shared_memory("katia_cozinha", ["katia"], "Katia quase botou fogo na cozinha tentando fazer conforto pra Nicole. Ela se importa.")
            
        call expression evt_label
        
        $ game_events.mark_completed(evt_label)
        call avancar_tempo(15)
    else:
        call local_sem_evento(local_escolhido)
        call avancar_tempo(15)
        
    jump loop_mapa_cap5