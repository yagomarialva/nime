label capitulo1:
    # Desbloqueia o capítulo na galeria (se existir)
    if "capitulo1" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo1")
    
    # === ABERTURA: A PRIMAVERA DAS ILUSÕES ===
    play music campus_ambient fadein 2.0
    
    scene bg auditorium with fade

    narrator "O zumbido do ar condicionado era constante, quase como o som de uma respiração metálica tentando manter vivos trezentos estranhos."
    narrator "Poeira dançava no feixe denso de luz que cortava a sala. Tudo parecia suspenso. Efêmero. O cheiro de cadernos novos, o perfume barato, o nervosismo silencioso."
    
    mc "Primavera... a estação em que somos obrigados a fingir que nossos recomeços significam algo."
    
    narrator "Apoiei o rosto na mão, deixando meu olhar vagar pelas ilhas de isolamento ao meu redor."
    narrator "Não éramos uma turma. Éramos estilhaços esperando por uma desculpa para quebrar."
    
    # Foreshadowing com subtexto e atmosfera
    narrator "Duas fileiras à frente, uma garota de óculos lia um livro com uma postura tão rígida que parecia usar as páginas como um escudo contra o mundo."
    narrator "Ao lado dela, quase invisível, alguém murmurava debaixo de fones de ouvido gigantes, a luz de uma tela refletindo em seus olhos cansados."
    narrator "Perto da janela, o tamborilar frenético de tênis esportivos batendo no linóleo. Pura ansiedade disfarçada de energia."
    
    mc "Todos nós tão desesperados para sermos vistos... e tão apavorados de que alguém realmente olhe."

    # === O DISCURSO DO PROFESSOR WENDELL ===
    show professor_wendell neutral at center
    
    narrator "O homem que subiu ao palco não possuía a aura de um educador. Ele caminhava com o equilíbrio de quem pendia sobre a beirada de um precipício."
    narrator "O microfone chiou em uma microfonia aguda. Ele sorriu, como se o som o agradasse."
    
    professor_wendell "Os humanos são criaturas patéticas, não acham?"
    
    narrator "O silêncio no auditório foi instantâneo. Gélido."
    
    professor_wendell "Nós passamos a vida inteira tateando no escuro, construindo muros de sarcasmo, de arrogância, de notas altas... tudo para evitar o atrito."
    professor_wendell "Vocês acham que a Faculdade Solária vai ensinar a vocês como serem bem-sucedidos? Tolice."
    
    narrator "Ele deu um passo à frente, quase caindo do palco. Os olhos dele eram selvagens."
    
    professor_wendell "Eu quero que vocês colidam. Quero que vocês quebrem as fachadas uns dos outros. Suas carreiras não importam se, no fim do dia, vocês ainda forem covardes emocionais."
    professor_wendell "Rejeitem o silêncio. Entrem em combustão. Mas acima de tudo..."
    professor_wendell "Parem de fingir que não precisam uns dos outros. Estão dispensados."
    
    hide professor_wendell
    
    # === A PRIMEIRA ESCOLHA: MOTIVAÇÃO ===
    narrator "O discurso foi curto, grosso e estranhamente motivador. A multidão começou a se dispersar."
    
    mc "Colidir, hein? Ok. Vamos ver onde essas colisões vão acontecer."
    
    # Inicializa variáveis de controle
    $ events_completed = []
    
# ... (Parte do discurso do Professor continua igual até o final) ...

    professor_wendell "O campus é de vocês... Dispensados."
    
    hide professor_wendell
    
    # === PREPARAÇÃO DO MAPA E EVENTOS ===
    narrator "O discurso foi curto e grosso. A multidão começou a se dispersar, um fluxo caótico de estudantes indo para todas as direções."
    
    mc "Colidir, hein? O professor tem um jeito dramático de dizer 'façam amigos'."
    
    narrator "Olhei para o mapa do campus no meu celular. Eu tinha algumas horas livres antes da próxima aula."
    
    # Resetando/Iniciando tempo e tracker
    $ dia_atual = 1
    $ periodo_atual = 1
    
    # Registrando eventos do Capítulo 1 no EventManager
    # Evitamos duplicidade se o script rodar de novo
    $ game_events.events = {}
    
    # Dia 1
    $ game_events.add_event("cinema", "evento_katia_samantha", 1, [1, 2, 3])
    $ game_events.add_event("quadra", "evento_larissa_huey", 1, [1, 2, 3])
    $ game_events.add_event("biblioteca", "evento_nicole_camille", 1, [1, 2, 3])

    # Dia 2
    $ game_events.add_event("laboratorio", "evento_katia_nicole", 2, [1, 2, 3])
    $ game_events.add_event("galeria", "evento_huey_camille", 2, [1, 2, 3])
    $ game_events.add_event("jogos", "evento_samantha_larissa", 2, [1, 2, 3])

# === LOOP PRINCIPAL DO MAPA ===
label loop_mapa_cap1:
    # Transição visual caso o dia tenha virado (exemplo básico)
    if dia_atual == 2 and periodo_atual == 1 and game_events.completed_events:
        scene bg campus_morning with dissolve
        narrator "O sol da manhã iluminava o campus. O segundo dia na Solária College havia começado."
        
    # Condição de avanço da narrativa
    if dia_atual >= 3:
        mc "Acho que por enquanto chega de exploração livre. A aula do Professor Wendell vai começar em breve."
        
        call capitulo1_aula_professor_wendell from _call_capitulo1_aula_wendell_map
        
        # Depois da aula, continua para a festa
        narrator "A aula foi intensa, mas a noite prometia mais."
        call capitulo1_terceira_escolha from _call_capitulo1_terceira_map
        
        # Questionário de conexões futuras
        call capitulo1_quarta_escolha from _call_capitulo1_quarta_map
        
        jump capitulo1_final

    # Chamada da tela do mapa interativo. O jogador escolhe um local.
    call screen mapa_modal
    
    $ local_escolhido = _return
    
    # Se o jogador fechou o modal sem escolher (botão X), volta ao mapa
    if local_escolhido is None:
        jump loop_mapa_cap1
    
    # Pede ao EventManager o evento pendente
    $ evt_label = game_events.get_pending_event(local_escolhido, dia_atual, periodo_atual)
    
    if evt_label:
        # Prepara a memória / status se necessário
        if evt_label == "evento_katia_samantha":
            $ add_shared_memory("cinema_exploration", [], "Decidiu relaxar no cinema")
        elif evt_label == "evento_larissa_huey":
            $ add_shared_memory("sports_exploration", [], "Decidiu se exercitar na quadra")
        elif evt_label == "evento_nicole_camille":
            $ add_shared_memory("library_exploration", [], "Buscou refúgio na biblioteca")
        elif evt_label == "evento_katia_nicole":
            $ add_shared_memory("methodology_debate_meeting", ["katia", "nicole"], "Primeira discussão sobre metodologia e criatividade")
            $ add_affinity_points("katia", 10, "Interesse em análise criativa")
            $ add_affinity_points("nicole", 10, "Interesse em metodologia")
        elif evt_label == "evento_huey_camille":
            $ add_shared_memory("art_spirituality_meeting", ["huey", "camille"], "Exploração da conexão entre arte e espiritualidade")
            $ add_affinity_points("huey", 10, "Interesse em técnica artística")
            $ add_affinity_points("camille", 10, "Interesse em energia criativa")
        elif evt_label == "evento_samantha_larissa":
            $ add_shared_memory("gaming_sports_meeting", ["samantha", "larissa"], "Primeira atividade combinando jogos e esportes")
            $ add_affinity_points("samantha", 10, "Interesse em RPG e criatividade")
            $ add_affinity_points("larissa", 10, "Interesse em competição e superação")
            
        # Executa o evento dinamicamente
        call expression evt_label
        
        # Finaliza e marca evento
        $ game_events.mark_completed(evt_label)
        call avancar_tempo
        
    else:
        # Não há evento.
        call local_sem_evento(local_escolhido)
        
    jump loop_mapa_cap1
            
# === FINAL DO CAPÍTULO 1 - RETROSPECTIVA ===
label capitulo1_final:
    scene bg campus_sunset with fade
    
    narrator "O sol começava a se pôr sobre o campus, pintando o céu com tons de dourado e rosa. Os primeiros dias na Solária estavam chegando ao fim."
    
    mc "Parece que foi ontem que cheguei... bom, tecnicamente foi anteontem."
    narrator "Mas antes de voltar para casa, algo dentro de mim pedia uma pausa para refletir sobre tudo o que aconteceu..."
    
    # === RETROSPECTIVA DE RELACIONAMENTOS ===
    narrator "Olhando para trás, percebi como cada encontro deixou uma marca única."
    
    # Mostra resumo (assumindo que esta função existe no seu jogo)
    $ relationship_summary = get_relationship_summary()
    
    narrator "📊 RESUMO DOS RELACIONAMENTOS:"
    
    python:
        for summary in relationship_summary:
            narrator(summary)
    
    # Momento emocional
    call emotional_moment("reflection", None, "Reflexão sobre as conexões formadas") from _call_emotional_moment_cap1_2
    
    narrator "Cada sorriso, cada discussão, cada momento compartilhado... tudo isso criou laços invisíveis."
    
    # === CHECAGEM DE PROGRESSÃO ===
    $ can_progress, progress_message = check_chapter_progression_requirement(1)
    
    narrator "[progress_message]"
    
    if can_progress:
        mc "Acho que fiz a escolha certa em vir para cá. Essas pessoas... elas são reais."
        
        # Conquista
        call emotional_moment("achievement", None, "Conexões suficientes para continuar") from _call_emotional_moment_cap1_3
        
        narrator "Essa jornada estava apenas começando, e eu mal podia esperar para ver o que o futuro nos reservava."
        
        # Transição para tela de fim de demo
        scene black with fade
        narrator "O Capítulo 1 chegou ao fim. Mas essas peças mal ajustadas ainda têm muitas colisões pela frente..."
        
        narrator "Muito obrigado por jogar a introdução de {i}NIME: Crossed Hearts - Master Edition{/i}."
        narrator "Os próximos capítulos, explorando cada fundo do poço e faísca de conexão dessas personagens, serão lançados em breve em novas atualizações."
        narrator "Até a próxima estação."
        
        # Desbloqueia próximo
        if "capitulo2" not in persistent.unlocked_chapters:
            $ persistent.unlocked_chapters.append("capitulo2")
        
        return
        
    else:
        mc "Sinto que deixei algo passar... Talvez eu devesse ter me aberto mais."
        
        # Opção de tentar novamente
        menu:
            "Refletir sobre conexões perdidas (Reiniciar Capítulo)":
                mc "Preciso tentar de novo. Fazer diferente."
                jump capitulo1
                
            "Aceitar que algumas conexões levam tempo (Retornar ao Menu)":
                mc "Nem toda amizade nasce no primeiro dia. Vou dar tempo ao tempo."
                return