label capitulo2:
    if "capitulo2" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo2")
        
    scene bg sala_jantar with fade
    
    narrator "Acendi a luz do celular, apontando para o canto escuro."
    narrator "A garota cobriu o rosto com os braços, os cabelos longos e pretos caindo como uma cortina sobre os joelhos."
    narrator "Ao lado dela, no chão, óculos de grau caídos perto de uma mochila de rodinhas abarrotada."
    
    mc "Calma, calma... Ninguém te achou. Você está na Rua Aurora, 57. É a casa do edital."
    
    narrator "Ela espionou por entre os braços. Os olhos arregalados, a respiração curta."
    
    show samantha sad at center
    
    samantha "M-meu stealth falhou... A porta de trás estava destrancada, eu só queria entrar sem ativar nenhum evento de diálogo..."
    
    mc "Você é a terceira vaga remanescente? E tentou se mudar de madrugada como uma assaltante?"
    
    samantha "Nível baixo... minha defesa social é terrível. Eu tentei pegar um copo d'água, mas meu controle motor travou."
    
    menu:
        "Isso é ridículo. Vai dormir.":
            $ points_samantha -= 5
            mc "Olha, não tem monstros aqui. Pega seus óculos e vai dormir."
            narrator "Ela rapidamente recolheu os óculos, murmurando um pedido de desculpas robótico, e subiu as escadas correndo."
            hide samantha
            
        "Ajudá-la a recolher os cacos (Gastar 10 Energia)":
            if store.player_stats["energy"] >= 10:
                $ update_player_stat("energy", -10)
                $ points_samantha += 10
                mc "Cuidado com a mão."
                narrator "Abaixei-me e recolhi os óculos dela do chão antes que ela mesma se cortasse tentando pegá-los no escuro."
                narrator "Eu os entreguei. Ela os colocou tremendo."
                samantha "O-obrigada... Pelo suporte de cura..."
                mc "Bem-vinda à casa. Eu limpo o vidro. Vá dormir."
                narrator "Ela correu para o andar de cima como se a vida dependesse disso."
                hide samantha
            else:
                mc "Eu queria te ajudar, mas nem eu tô conseguindo ficar acordado."
                narrator "Ela apenas assentiu freneticamente, pegou os óculos e sumiu na escuridão do corredor."
                hide samantha
    
    # === A MANHÃ SEGUINTE ===
    scene bg quarto_protagonista with fade
    
    narrator "O resto da madrugada foi silencioso. Até que..."
    
    play sound "blender_noise.ogg"
    
    narrator "BZZZZZZZZZZZZT!"
    
    mc "Puta merda, estamos sendo atacados por abelhas gigantes?!"
    
    scene bg sala_jantar with dissolve
    
    narrator "Desci correndo as escadas. Eram seis da manhã."
    
    show nicole angry at right
    nicole "Desligue isso imediatamente! A cláusula 4.2 do meu regulamento proíbe ruídos industriais antes das oito!"
    
    show katia angry at left
    katia "Se isso for um ataque terrorista, eu quero morrer dormindo! Cale a boca!"
    
    hide nicole
    hide katia
    
    show larissa happy at center
    
    narrator "Uma garota loira incrivelmente atlética sorria enquanto segurava a tampa do liquidificador que parecia ter três hélices de trator."
    
    larissa "Bom diiiia! Eu sou a Larissa, vaga número quatro! Alguém quer um shake de hipertrofia com beterraba? Eu já corri o campus inteiro e o sol nem nasceu direito!"
    
    narrator "Nicole massageava as têmporas. Katia parecia prestes a cometer um crime violento."
    
    mc "E de três pulamos para cinco."
    
    larissa "Relaxem! Vamos ser uma equipe! Eu dou conta de motivar todos vocês, só preciso do meu shake primeiro!"
    
    hide larissa
    
    # === LOOP DO MAPA CAP 2 ===
    narrator "Foi uma manhã torturante. A dinâmica da casa tinha virado do avesso com a energia infinita de Larissa e a fobia da Samantha."
    
    $ dia_atual = 2
    $ periodo_atual = 1
    
    $ game_events.events = {}
    
    # Dia 1 (Cap 2)
    $ game_events.add_event("quadra", "evento_larissa_pista", 1, [1, 2, 3])
    $ game_events.add_event("sala", "evento_samantha_isolada", 1, [1, 2, 3])

    # Dia 2 (Cap 2)
    # Por enquanto, eventos temporários (você pode criar outros eventos depois)
    $ game_events.add_event("biblioteca", "evento_nicole_bolsa", 2, [1, 2, 3])
    $ game_events.add_event("cinema", "evento_katia_filme", 2, [1, 2, 3])

label loop_mapa_cap2:
    if dia_atual >= 3:
        mc "Foi um final de semana cheio. É melhor eu voltar pra casa pra tentar ter um minuto de paz."
        jump capitulo2_crise_conta

    call screen mapa_modal
    
    $ local_escolhido = _return
    
    if local_escolhido is None:
        jump loop_mapa_cap2
    
    $ evt_label = game_events.get_pending_event(local_escolhido, dia_atual, periodo_atual)
    
    if evt_label:
        if evt_label == "evento_samantha_isolada":
            $ add_shared_memory("samantha_room", ["samantha"], "Um momento de paz atrás de portas fechadas com a Samantha.")
        elif evt_label == "evento_larissa_pista":
            $ add_shared_memory("larissa_track", ["larissa"], "Vi Larissa ir além dos próprios limites físicos.")
            
        call expression evt_label
        
        $ game_events.mark_completed(evt_label)
        call avancar_tempo(15)
    else:
        call local_sem_evento(local_escolhido)
        call avancar_tempo(15)
        
    jump loop_mapa_cap2
