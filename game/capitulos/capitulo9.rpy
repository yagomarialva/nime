label capitulo9:
    if "capitulo9" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo9")
        
    scene bg casa_interior with fade
    
    narrator "Uma semana após a nossa vitória burocrática, a paz finalmente reinava na Rua Aurora, 57."
    
    narrator "A sala de estar tinha cheiro de tinta fresca. Camille meditava no tapete, Nicole lia uma revista de moda europeia, e Samantha destruía adolescentes num jogo de tiro online."
    
    play sound "cellphone_vibrate.ogg"
    
    narrator "Meu celular vibrou no bolso."
    
    mc "Mensagem do Professor Wendell."
    
    show katia sad at left
    
    katia "Lá vem. O que a gente quebrou agora?"
    
    mc "Ele disse: 'O orçamento de emergência que aprovei pra vocês deixou um rombo no departamento de contabilidade. Vocês vão pagar essa dívida trabalhando no Festival de Primavera. Vejo vocês no campus amanhã.'"
    
    show larissa angry at right
    
    larissa "Trabalhar de graça?! Isso é exploração estudantil!"
    
    show huey neutral at center
    
    huey "Do ponto de vista contratual, é uma permuta justa. Materiais de construção por mão de obra em eventos universitários."
    
    mc "Pelo menos o Festival de Primavera é divertido. O que vocês querem fazer nas barracas?"
    
    nicole "Eu vou organizar um desfile de moda customizada. Preciso de assistentes pra maquiagem e tecidos."
    
    samantha "Eu vou ligar uns monitores CRT velhos e fazer um campeonato de fliperama retrô."
    
    larissa "Torneio de Luta de Braço! Quem me derrotar ganha um algodão doce."
    
    camille "Uma tenda de Tarô místico. As energias da primavera são propícias para leituras de futuro."
    
    katia "O Grêmio me forçou a cuidar do Correio Elegante. Alguém me tira dessa tortura, por favor."
    
    huey "Exposição de arte isométrica usando palitos de picolé."
    
    narrator "Seis barracas completamente diferentes."
    
    mc "E eu?"
    
    katia "Você vai ser o nosso assistente geral, óbvio. Ajuda quem precisar de ajuda."
    
    narrator "O Festival começa amanhã. Eu tenho apenas alguns 'Tickets de Ação' por dia para dividir entre elas. É melhor eu escolher com sabedoria quem eu quero ajudar."
    
    # Configuração do Loop do Festival
    $ dia_atual = 15
    $ periodo_atual = 1
    
    $ game_events.events = {}
    
    # Registrando eventos do festival no campus
    $ game_events.add_event("ginasio", "evento_cap9_larissa", 15, [1, 2, 3])
    $ game_events.add_event("predio_adm", "evento_cap9_katia", 15, [1, 2, 3])
    $ game_events.add_event("jardim_campus", "evento_cap9_camille", 15, [1, 2, 3])
    $ game_events.add_event("biblioteca", "evento_cap9_samantha", 15, [1, 2, 3])
    $ game_events.add_event("estacionamento", "evento_cap9_nicole", 15, [1, 2, 3])
    $ game_events.add_event("corredor_salas", "evento_cap9_huey", 15, [1, 2, 3])

label loop_mapa_cap9:
    # 2 dias de festival (dia 15 e 16), com 3 periodos cada = 6 turnos para interagir com as meninas.
    if dia_atual >= 17:
        jump capitulo9_fogos_pre

    scene bg campus_principal
    show screen hud_celular
    show screen player_hud
    
    $ ui_message = "Festival de Primavera - Dia " + str(dia_atual)
    
    call screen mapa_modal

    $ local_escolhido = _return
    
    if local_escolhido is None:
        jump loop_mapa_cap9
    
    $ evt_label = game_events.get_pending_event(local_escolhido, 15, 1) # Sempre usa o mesmo evento ignorando o dia, mas a mecânica marca como completado.
    
    hide screen mapa_modal
    hide screen hud_celular
    hide screen player_hud
    
    if evt_label:
        call expression evt_label
        $ game_events.mark_completed(evt_label)
    else:
        narrator "A barraca de [local_escolhido] está cheia de gente. Fiquei um tempo ajudando na organização geral do festival."
        $ update_player_stat("energy", -5)
        
    call avancar_tempo(10)
    jump loop_mapa_cap9