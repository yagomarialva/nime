label capitulo4:
    if "capitulo4" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo4")
        
    scene bg quarto_protagonista with fade
    
    narrator "Oito da manhã. Silêncio."
    
    narrator "Desde que Larissa se mudou para cá, as manhãs da Rua Aurora eram marcadas pelo som de passos pesados de corrida e do liquidificador industrial dela às 6h."
    narrator "Mas hoje, o silêncio era tão espesso que quase sufocava."
    
    scene bg sala_jantar with dissolve
    
    narrator "Desci para a cozinha. A atmosfera estava fúnebre."
    
    show nicole neutral at right
    show katia neutral at left
    
    narrator "Nicole olhava para uma xícara de café intocada. Katia estava encostada na parede, estourando uma bola de chiclete sem nenhum entusiasmo."
    
    mc "Ninguém foi ver como ela está?"
    
    nicole "Ela trancou a porta. O médico ligou ontem à noite... eu ouvi parte da conversa. Rompimento total do ligamento cruzado."
    
    katia "Fim da linha para a Usain Bolt loira. Sem ligamento, sem corrida. Sem corrida, sem bolsa de estudos atlética."
    
    nicole "A Katia pode ser insensível, mas está certa. A identidade inteira da Larissa girava em torno do esporte. Como ela vai justificar a permanência dela na universidade agora?"
    
    mc "A gente não tá num quartel general. Ela acabou de perder o sonho dela. A gente devia apoiar."
    
    katia "E dizer o quê? 'Sinto muito que você vai mancar pelo resto da vida'? Sinceramente, a pior coisa que você pode fazer por alguém no buraco é sentir pena."
    
    narrator "Katia desencostou da parede, jogando o chiclete no lixo."
    
    katia "Se quiser ir lá bancar o herói, a porta dela é a segunda à esquerda."
    
    hide nicole
    hide katia
    
    # === LOOP DO MAPA CAP 4 ===
    narrator "O clima da casa despencou. O peso da depressão da Larissa era sentido por todas nós. Eu tinha que dar um jeito nisso."
    
    $ dia_atual = 4
    $ periodo_atual = 1
    
    $ game_events.events = {}
    
    # Dia 1 (Cap 4)
    $ game_events.add_event("quarto_larissa", "evento_larissa_depressao", 4, [1, 2, 3])
    $ game_events.add_event("sala_jantar", "evento_nicole_sobrecarga", 4, [1, 2, 3])

label loop_mapa_cap4:
    if dia_atual >= 5:
        mc "A depressão dela está corroendo a casa inteira. Eu não aguento mais ver ela assim. É hoje."
        jump capitulo4_quadra

    call screen mapa_modal
    
    $ local_escolhido = _return
    
    if local_escolhido is None:
        jump loop_mapa_cap4
    
    $ evt_label = game_events.get_pending_event(local_escolhido, dia_atual, periodo_atual)
    
    if evt_label:
        if evt_label == "evento_larissa_depressao":
            $ add_shared_memory("larissa_quarto", ["larissa"], "Vi Larissa vulnerável e sem seu escudo de energia pela primeira vez.")
        elif evt_label == "evento_nicole_sobrecarga":
            $ add_shared_memory("nicole_colapso", ["nicole"], "Ajudei Nicole a não enlouquecer com o acúmulo de tarefas domésticas.")
            
        call expression evt_label
        
        $ game_events.mark_completed(evt_label)
        call avancar_tempo(15)
    else:
        call local_sem_evento(local_escolhido)
        call avancar_tempo(15)
        
    jump loop_mapa_cap4
