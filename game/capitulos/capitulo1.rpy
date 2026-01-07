label capitulo1:
    # Desbloqueia o capítulo na galeria (se existir)
    if "capitulo1" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo1")
    
    # === ABERTURA: O DISCURSO DA COLISÃO ===
    play music campus_ambient fadein 2.0
    
    scene bg auditorium with fade

    # Imersão sensorial
    narrator "O zumbido do ar condicionado lutava contra o murmúrio de trezentos estudantes. O auditório cheirava a polímero novo e ansiedade adolescente."
    
    # MC com personalidade (Observador/Cínico)
    mc "Primeiro dia. Aquele momento em que todo mundo finge que sabe o que está fazendo, mas ninguém realmente sabe."
    
    narrator "Ajeitei-me na poltrona do meio. O palco estava iluminado, aguardando a 'autoridade' falar."

    # Foreshadowing das Heroínas (Visual apenas, sem interações ainda)
    narrator "Olhei ao redor. A fauna local era... diversa."
    
    # Katia e Samantha (Descrição visual corrigida)
    narrator "Duas fileiras à frente, uma garota de óculos lia um livro grosso, ignorando o mundo. Ao lado dela, outra garota tentava equilibrar três chaveiros de pelúcia na mochila."
    
    # Larissa e Huey
    narrator "Mais à direita, uma atleta girava uma bola de vôlei nos dedos, impaciente. Perto da janela, alguém desenhava no vidro embaçado com o dedo."
    
    mc "É... vai ser um semestre longo."

    # === O DISCURSO DO PROFESSOR WENDELL ===
    show professor_wendell neutral at center
    
    narrator "O microfone chiou. O homem no palco não parecia um reitor tradicional. Ele tinha um sorriso de quem sabia uma piada que ninguém mais ouviu."
    
    professor_wendell "Bom dia. Olhem para a pessoa ao seu lado."
    professor_wendell "Estatisticamente, um de vocês vai mudar o mundo. O outro... vai apenas pagar boletos."
    
    narrator "Risos nervosos na plateia."
    
    professor_wendell "Brincadeira. Ou não. Solária não é uma fábrica de diplomas. É um coliseu."
    professor_wendell "Vocês acham que vieram aprender fórmulas? Errado. Vocês vieram aprender a colidir."
    professor_wendell "Ideias colidem. Egos colidem. Sonhos colidem. E é nessa explosão que a gente descobre se vocês são feitos de vidro... ou de diamante."
    
    professor_wendell "O campus é de vocês. O laboratório, a quadra, o cinema. Não me importo com suas notas. Me importo com o que vocês farão quando ninguém estiver olhando."
    professor_wendell "Dispensados."
    
    hide professor_wendell
    
    # === A PRIMEIRA ESCOLHA: MOTIVAÇÃO ===
    narrator "O discurso foi curto, grosso e estranhamente motivador. A multidão começou a se dispersar."
    
    mc "Colidir, hein? Ok. Vamos ver onde essas colisões vão acontecer."
    
    # Inicializa variáveis de controle
    $ events_completed = []
    
# ... (Parte do discurso do Professor continua igual até o final) ...

    professor_wendell "O campus é de vocês... Dispensados."
    
    hide professor_wendell
    
    # === A PRIMEIRA ESCOLHA: INTERESSE GENUÍNO ===
    narrator "O discurso foi curto e grosso. A multidão começou a se dispersar, um fluxo caótico de estudantes indo para todas as direções."
    
    mc "Colidir, hein? O professor tem um jeito dramático de dizer 'façam amigos'."
    
    narrator "Olhei para o mapa do campus no meu celular. Eu tinha algumas horas livres antes da próxima aula obrigatória."
    narrator "Vi aquelas garotas do auditório seguindo caminhos diferentes. A 'leitora' e a 'animada' foram para o norte. A atleta correu para o sul."
    
    mc "Bom, não vou ficar aqui parado no auditório vazio. O que eu estou a fim de fazer agora?"
    
    # Inicializa variáveis de controle
    $ events_completed = []
    
    # Menu focado no INTERESSE DO MC (Sem stalkear!)
    menu:
        "Ir ao Cinema (Preciso relaxar um pouco)":
            mc "Aquele discurso me deu sono. Um filme parece a melhor forma de começar o semestre sem estresse."
            
            $ add_shared_memory("cinema_exploration", [], "Decidiu relaxar no cinema")
            call evento_katia_samantha from _call_evento_katia_samantha
            $ events_completed.append("cinema")
            jump capitulo1_continue_exploration
         
        "Ir à Quadra de Esportes (Preciso gastar energia)":
            mc "Ficar sentado me deixou travado. Aquela atleta girando a bola me lembrou que preciso me mexer."
            mc "Nada como um pouco de endorfina para processar esse discurso filosófico."
            
            $ add_shared_memory("sports_exploration", [], "Decidiu se exercitar na quadra")
            call evento_larissa_huey from _call_evento_larissa_huey
            $ events_completed.append("sports")
            jump capitulo1_continue_exploration

        "Ir à Biblioteca (Preciso de silêncio e foco)":
            mc "Muita gente, muito barulho, muito discurso motivacional. Minha bateria social já está no fim."
            mc "Preciso de um lugar quieto para organizar minha grade de horários."
            
            $ add_shared_memory("library_exploration", [], "Buscou refúgio na biblioteca")
            call evento_nicole_camille from _call_evento_nicole_camille
            $ events_completed.append("library")
            jump capitulo1_continue_exploration
# === CONTINUAÇÃO DA EXPLORAÇÃO (LOOP) ===
label capitulo1_continue_exploration:
    
    # Se já fez 3 eventos, avança para o dia seguinte
    if len(events_completed) >= 3:
        jump capitulo1_segunda_escolha

    narrator "Ainda havia tempo para explorar mais o campus antes do dia terminar. Para onde eu deveria ir agora?"
    
    menu:
        "Ir para a biblioteca e centro de estudos" if "library" not in events_completed:
            $ add_shared_memory("library_exploration", [], "Exploração da biblioteca")
            call evento_nicole_camille from _call_evento_nicole_camille_1
            $ events_completed.append("library")
            jump capitulo1_continue_exploration
            
        "Ir para o cinema universitário" if "cinema" not in events_completed:
            $ add_shared_memory("cinema_exploration", [], "Exploração do cinema")
            call evento_katia_samantha from _call_evento_katia_samantha_1
            $ events_completed.append("cinema")
            jump capitulo1_continue_exploration
            
        "Visitar a quadra de esportes" if "sports" not in events_completed:
            $ add_shared_memory("sports_exploration", [], "Exploração da quadra")
            call evento_larissa_huey from _call_evento_larissa_huey_1
            $ events_completed.append("sports")
            jump capitulo1_continue_exploration

# === SEGUNDA ESCOLHA - NOVO DIA ===
label capitulo1_segunda_escolha:
    scene bg campus_morning with fade
    
    narrator "O sol da manhã iluminava o campus com uma luz dourada. O segundo dia na Solária College havia começado."
    mc "Certo. Sobrevivi ao primeiro dia. Agora é hora de aprofundar."
    
    narrator "Lembrei das pessoas incríveis que conheci ontem, mas sabia que havia cantos do campus que eu ainda não tinha visto."
    
    # Inicializa lista de eventos do segundo dia se não existir
    if "second_choice_events" not in globals():
        $ second_choice_events = []
    
    jump capitulo1_continue_second_choice

# === CONTINUAÇÃO DA SEGUNDA ESCOLHA ===
label capitulo1_continue_second_choice:
    
    # Se já fez eventos suficientes, vai para a aula
    if len(second_choice_events) >= 3:
        call capitulo1_aula_professor_wendell from _call_capitulo1_aula_professor_wendell
        # Depois da aula, continua para a festa
        call capitulo1_terceira_escolha from _call_capitulo1_terceira_escolha
        # Questionário de conexões futuras
        call capitulo1_quarta_escolha from _call_capitulo1_quarta_escolha
        jump capitulo1_final

    narrator "Para onde devo ir agora?"
    
    menu:
        "Ir ao laboratório de comunicação e dados" if "lab" not in second_choice_events:
            $ add_shared_memory("methodology_debate_meeting", ["katia", "nicole"], "Primeira discussão sobre metodologia e criatividade")
            $ add_affinity_points("katia", 10, "Interesse em análise criativa")
            $ add_affinity_points("nicole", 10, "Interesse em metodologia")
            
            call evento_katia_nicole from _call_evento_katia_nicole
            $ second_choice_events.append("lab")
            jump capitulo1_continue_second_choice
            
        "Explorar a galeria de arte" if "gallery" not in second_choice_events:
            $ add_shared_memory("art_spirituality_meeting", ["huey", "camille"], "Exploração da conexão entre arte e espiritualidade")
            $ add_affinity_points("huey", 10, "Interesse em técnica artística")
            $ add_affinity_points("camille", 10, "Interesse em energia criativa")
            
            call evento_huey_camille from _call_evento_huey_camille
            $ second_choice_events.append("gallery")
            jump capitulo1_continue_second_choice
            
        "Visitar o centro de jogos e recreação" if "games" not in second_choice_events:
            $ add_shared_memory("gaming_sports_meeting", ["samantha", "larissa"], "Primeira atividade combinando jogos e esportes")
            $ add_affinity_points("samantha", 10, "Interesse em RPG e criatividade")
            $ add_affinity_points("larissa", 10, "Interesse em competição e superação")
            
            call evento_samantha_larissa from _call_evento_samantha_larissa
            $ second_choice_events.append("games")
            jump capitulo1_continue_second_choice

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
        
        # Transição para próximo capítulo
        scene bg city with fade
        narrator "O Capítulo 1 chegou ao fim, mas nossa história estava apenas começando..."
        
        # Desbloqueia próximo
        if "capitulo2" not in persistent.unlocked_chapters:
            $ persistent.unlocked_chapters.append("capitulo2")
        
        # Redireciona para onde o jogo deve seguir (ex: atualização ou menu)
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