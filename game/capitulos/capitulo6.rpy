label capitulo6:
    if "capitulo6" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo6")
        
    scene black with fade
    play sound "spark.ogg"
    
    narrator "O calor era insuportável antes mesmo de eu abrir os olhos."
    
    scene bg quarto_protagonista with vpunch
    
    narrator "A fumaça entrava por debaixo da porta. O alarme de incêndio, velho de cinquenta anos, apitava fraco. A casa estava pegando fogo."
    
    mc "O segundo andar... as garotas!"
    
    scene bg casa_interior with hpunch
    
    narrator "Eu arrombei a minha porta. O corredor do segundo andar já estava tomado por chamas. As faíscas choviam do teto elétrico comprometido."
    
    show nicole angry at center
    
    nicole "SAIAM! TODO MUNDO PRA RUA AGORA!"
    
    narrator "Nicole estava coordenando a evacuação, empurrando Katia e Camille para a escada. Larissa vinha mancando na cadeira de rodas."
    
    mc "Estão todas aí?!"
    
    katia "A Samantha! Ela trancou a porta do quarto!"
    
    narrator "Eu não pensei. Corri pela fumaça até a porta da Samantha e chutei a maçaneta."
    
    scene bg casa_interior with hpunch
    
    narrator "Samantha estava encolhida debaixo da mesa do computador, catatônica."
    
    mc "Samantha! Vem!"
    
    narrator "Eu a puxei pelo braço. O teto começou a ceder atrás de nós."
    
    mc "O fogo está engolindo o corredor! Eu só tenho tempo de salvar uma coisa além da gente!"
    
label menu_resgate_incendio:
    menu:
        "Pegar a CPU do PC da Samantha":
            narrator "Eu arranquei os cabos da parede e abracei a pesada caixa de metal do computador dela."
            samantha "Meu... meu setup!"
            $ add_affinity_points("samantha", 30)
            
        "Correr pro quarto da Larissa e salvar as medalhas":
            narrator "Joguei Samantha para fora e mergulhei no quarto ao lado. Arranquei o quadro de medalhas da Larissa da parede antes que a cama pegasse fogo."
            $ add_affinity_points("larissa", 30)
            
        "Chutar a gaveta da Katia e salvar a caixa secreta":
            narrator "Joguei Samantha para fora. Vi a caixa trancada que Katia sempre esconde debaixo da cama quase derretendo. Agarrei e corri."
            $ add_affinity_points("katia", 30)
            
        "Salvar o Casaco de Grife da Nicole":
            narrator "Nicole gritou que a última peça da avó dela estava no armário. Eu abri a porta fumegante e puxei o casaco italiano."
            $ add_affinity_points("nicole", 30)
            
        "Salvar o Caderno de Rascunhos da Huey":
            narrator "Huey estava em choque, olhando o papel virar cinzas. Eu agarrei a mochila dela, cheia de todas as plantas e desenhos dos últimos anos."
            $ add_affinity_points("huey", 30)
            
        "Salvar o Altar de Incensos da Camille":
            narrator "Corri pelo corredor e peguei o altar de madeira sagrada da Camille que ela deixou para trás. Queimou minha mão, mas consegui."
            $ add_affinity_points("camille", 30)
            
        "Mergulhar nas chamas e salvar TUDO (Requer 10 Físico)":
            if store.player_stats["fitness"] >= 10:
                narrator "Eu não ia deixar a casa engolir a história delas. Puxei o ar com força, meus pulmões arderam."
                mc "VÃO PRA FORA, EU CUBRO VOCÊS!"
                narrator "Usando todo o meu vigor físico treinado, mergulhei nos escombros. Chutei portas pesadas, arrastei a mesa da Samantha, joguei a mala da Nicole pela janela e trouxe a caixa da Katia num braço enquanto segurava as medalhas e os cadernos no outro."
                narrator "Quando caí no gramado com os braços cheios de fuligem e tesouros, as seis me olharam como se eu fosse um deus."
                $ update_player_stat("energy", -50)
                $ add_affinity_points("samantha", 20)
                $ add_affinity_points("larissa", 20)
                $ add_affinity_points("katia", 20)
                $ add_affinity_points("nicole", 20)
                $ add_affinity_points("huey", 20)
                $ add_affinity_points("camille", 20)
            else:
                narrator "Eu tentei dar um passo a mais nas chamas, mas a fumaça invadiu meus pulmões. Meu corpo não tinha preparo físico pra correr carregando tanto peso."
                narrator "Fui jogado pra trás tossindo violentamente. O fogo bloqueou parte da passagem."
                mc "Droga! Não tenho força suficiente... Eu só tenho tempo pra pegar uma coisa!"
                $ update_player_stat("energy", -10)
                jump menu_resgate_incendio
            
    scene bg quintal with fade
    
    narrator "Nós tossíamos no gramado. O caminhão dos bombeiros já soava na rua de baixo."
    narrator "O fogo foi contido no segundo andar. A estrutura não desabou. Mas o estrago estava feito."
    
    scene bg sala_jantar with dissolve
    
    narrator "Na manhã seguinte, o cheiro de queimado era a nossa nova realidade."
    
    show nicole sad at left
    show katia neutral at right
    
    nicole "O bombeiro disse que a fiação do segundo andar tem que ser inteira refeita. E que a laje precisa de escoras."
    
    katia "O Wendell já mandou e-mail. 'Risco estrutural severo'. Ele quer cancelar o edital, interditar a casa e nos mandar para alojamentos temporários diferentes."
    
    mc "Diferentes? Separar a gente?"
    
    katia "Sim. Fim da linha, herói. A casa morreu."
    
    narrator "Um silêncio pesado tomou a sala. Mas dessa vez, a derrota não vinha da falta de dinheiro. Vinha da fumaça."
    
    show larissa happy at center
    
    larissa "E desde quando a gente obedece a e-mails de velhos engravatados?"
    
    nicole "O que você está sugerindo, Larissa?"
    
    larissa "O edital diz que a casa deve ser mantida pelos bolsistas. Nós somos bolsistas. Nós podemos fazer as reformas emergenciais até a reitoria aprovar."
    
    camille "A fênix só voa se você permitir que as cinzas se assentem."
    
    mc "Vocês tão malucas. Nós não somos pedreiros."
    
    katia "Você que é nerd de RPG, pensa nisso como *crafting*. Ou a gente reforma o teto e convence o inspetor, ou vamos cada um pra um canto."
    
    narrator "Eu olhei para as cinco garotas na sala. Sujas de fuligem, cansadas, mas juntas."
    
    mc "Ok. Peguem as vassouras. Nós temos uma casa pra reconstruir."
    
    if store.player_stats["energy"] >= 30:
        $ update_player_stat("energy", -30)
    else:
        $ store.player_stats["energy"] = 0
        
    call screen minigame_clicker("🧹", 10, "images/cenarios/casa_interior.png")
    
    if _return:
        mc "Ufa... Conseguimos tirar o pior da fuligem."
    else:
        mc "O estrago foi grande, a gente não deu conta de tudo, mas já dá pra andar sem tropeçar."
    
    # === LOOP DO MAPA CAP 6 ===
    $ dia_atual = 6
    $ periodo_atual = 1
    
    $ game_events.events = {}
    
    # Dia 1 (Cap 6)
    # Eventos de narrativa focado nas reformas na casa
    $ game_events.add_event("quintal", "evento_reforma_criatividade", 6, [1, 2, 3])
    $ game_events.add_event("sala_jantar", "evento_samantha_trauma", 6, [1, 2, 3])

label loop_mapa_cap6:
    if dia_atual >= 7:
        mc "Chegou a hora. O inspetor da prefeitura universitária chegou. Eu preciso usar tudo o que tenho de conversa para não sermos despejados."
        jump capitulo6_inspecao

    call screen mapa_modal
    
    $ local_escolhido = _return
    
    if local_escolhido is None:
        jump loop_mapa_cap6
        
    # Impedir acesso ao quarto porque está destruído
    if local_escolhido == "quarto":
        mc "O segundo andar tá isolado e destruído. Não posso subir lá."
        jump loop_mapa_cap6

    # Podemos desencorajar a ida ao campus, já que a casa precisa ser consertada.
    # Mas deixamos ir para minigames de dinheiro se precisarem.
    
    $ evt_label = game_events.get_pending_event(local_escolhido, dia_atual, periodo_atual)
    
    if evt_label:
        if evt_label == "evento_reforma_criatividade":
            $ add_shared_memory("reforma_casa", ["huey", "larissa"], "Usei gambiarras artísticas para escorar o teto queimado.")
        elif evt_label == "evento_samantha_trauma":
            $ add_shared_memory("samantha_chao", ["samantha"], "O verdadeiro santuário da Samantha nunca foi o PC, e sim não estar sozinha.")
            
        call expression evt_label
        
        $ game_events.mark_completed(evt_label)
        call avancar_tempo(15)
    else:
        call local_sem_evento(local_escolhido)
        call avancar_tempo(15)
        
    jump loop_mapa_cap6