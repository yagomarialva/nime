# Portuguese Translation - Chapter 1
# Tradução em português - Capítulo 1

translate portuguese capitulo1:
    if "capitulo1" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo1")
    
    # === INTRODUÇÃO COM MONÓLOGO DO PROFESSOR WENDELL ===
    # Tocar música de fundo do campus
    play music campus_ambient fadein 2.0
    
    scene bg auditorium with fade

    narrator "O auditório da Faculdade Solária estava repleto de expectativa. Dezenas de jovens, cada um carregando sonhos únicos, aguardavam o início de uma jornada que mudaria suas vidas para sempre."

    narrator "Entre eles, eu me sentava nas fileiras do meio, tentando absorver cada detalhe deste momento histórico. O ar estava carregado de possibilidades infinitas."

    # Professor Wendell - Monólogo sobre a faculdade e fase da vida
    show professor_wendell neutral at center
    professor_wendell "Bem-vindos à Faculdade Solária, jovens mentes brilhantes. Vocês estão prestes a embarcar em uma das jornadas mais transformadoras de suas vidas."
    professor_wendell "A universidade não é apenas um lugar de aprendizado acadêmico, mas um laboratório de descobertas pessoais, conexões humanas e crescimento interior."
    professor_wendell "Cada um de vocês traz consigo sonhos únicos, perspectivas distintas e potencial ilimitado. Aqui, vocês não apenas estudarão, mas descobrirão quem realmente são."
    professor_wendell "As amizades que vocês formarão aqui, os desafios que enfrentarão, as paixões que descobrirão... tudo isso moldará não apenas seus futuros profissionais, mas suas almas."
    professor_wendell "Não tenham medo de explorar, de questionar, de se conectar com pessoas diferentes de vocês. É na diversidade que encontramos nossa verdadeira força."
    professor_wendell "Agora, saiam e explorem este campus. Deixem que a vida os surpreenda com as pessoas incríveis que vocês estão prestes a conhecer."
    hide professor_wendell
    
    narrator "As palavras do Professor Wendell ecoaram em minha mente enquanto caminhava pelo campus. Sentia que algo especial estava prestes a acontecer."
    narrator "Cada corredor, cada jardim, cada prédio parecia pulsar com possibilidades infinitas. Era como se o próprio campus estivesse esperando para me revelar seus segredos."

    # === EXPLORAÇÃO DO CAMPUS ===
    narrator "Conforme explorava o campus, percebi que havia várias áreas interessantes para conhecer. Onde deveria começar minha jornada de descobertas?"
    
    # Inicializar variáveis de controle
    $ events_completed = []
    
    # === PRIMEIRA ESCOLHA - EXPLORAÇÃO DO CAMPUS ===
    menu:
        "Ir para a biblioteca e centro de estudos":
            $ add_shared_memory("library_exploration", [], "Primeira exploração da biblioteca do campus")
            call evento_nicole_camille
            $ events_completed.append("library")
            jump capitulo1_continue_exploration
            
        "Ir para o cinema da universidade":
            $ add_shared_memory("cinema_exploration", [], "Primeira exploração do cinema da universidade")
            call evento_katia_samantha
            $ events_completed.append("cinema")
            jump capitulo1_continue_exploration
            
        "Conhecer a quadra esportiva e áreas de lazer":
            $ add_shared_memory("sports_exploration", [], "Primeira exploração das áreas esportivas")
            call evento_larissa_huey
            $ events_completed.append("sports")
            jump capitulo1_continue_exploration

# === CONTINUAÇÃO DA EXPLORAÇÃO ===
translate portuguese capitulo1_continue_exploration:
    narrator "Após essa primeira experiência, senti que havia muito mais para descobrir no campus. Onde deveria explorar a seguir?"
    
    menu:
        "Ir para a biblioteca e centro de estudos" if "library" not in events_completed:
            $ add_shared_memory("library_exploration", [], "Exploração da biblioteca do campus")
            call evento_nicole_camille
            $ events_completed.append("library")
            jump capitulo1_continue_exploration
            
        "Ir para o cinema da universidade" if "cinema" not in events_completed:
            $ add_shared_memory("cinema_exploration", [], "Exploração do cinema da universidade")
            call evento_katia_samantha
            $ events_completed.append("cinema")
            jump capitulo1_continue_exploration
            
        "Conhecer a quadra esportiva e áreas de lazer" if "sports" not in events_completed:
            $ add_shared_memory("sports_exploration", [], "Exploração das áreas esportivas")
            call evento_larissa_huey
            $ events_completed.append("sports")
            jump capitulo1_continue_exploration
            
        "Continuar para o próximo dia" if len(events_completed) >= 3:
            jump capitulo1_segunda_escolha

# === SEGUNDA ESCOLHA - NOVO DIA ===
translate portuguese capitulo1_segunda_escolha:
    scene bg campus_morning with fade
    
    narrator "O sol da manhã iluminava o campus com uma luz dourada. O segundo dia na Faculdade Solária havia começado."
    narrator "Após as experiências incríveis do dia anterior, eu mal podia esperar para continuar explorando o campus e conhecendo novas pessoas."
    
    narrator "Conforme caminhava pelo campus, percebi que havia muito mais para descobrir. Onde deveria explorar a seguir?"
    
    # Mostrar apenas as personagens que o jogador ainda não conheceu
    narrator "Lembrei-me das pessoas incríveis que havia conhecido no dia anterior, mas sabia que havia muito mais para descobrir neste campus."
    narrator "Cada área do campus parecia pulsar com possibilidades de novos encontros e descobertas."
    
    # Inicializar lista de eventos da segunda escolha se não existir
    if "second_choice_events" not in globals():
        $ second_choice_events = []
    
    jump capitulo1_continue_second_choice

# === CONTINUAÇÃO DA SEGUNDA ESCOLHA ===
translate portuguese capitulo1_continue_second_choice:
    narrator "Após essa experiência, senti que havia muito mais para descobrir no campus. Onde deveria explorar a seguir?"
    
    menu:
        "Ir para o laboratório de comunicação e análise de dados" if "lab" not in second_choice_events:
            $ add_shared_memory("methodology_debate_meeting", ["katia", "nicole"], "Primeira discussão sobre metodologia e criatividade")
            $ add_affinity_points("katia", 10, "Interesse em análise criativa")
            $ add_affinity_points("nicole", 10, "Interesse em metodologia")
            call evento_katia_nicole
            $ second_choice_events.append("lab")
            jump capitulo1_continue_second_choice
            
        "Explorar a galeria de arte e espaços criativos" if "gallery" not in second_choice_events:
            $ add_shared_memory("art_spirituality_meeting", ["huey", "camille"], "Primeira exploração da conexão entre arte e espiritualidade")
            $ add_affinity_points("huey", 10, "Interesse em técnica artística")
            $ add_affinity_points("camille", 10, "Interesse em energia criativa")
            call evento_huey_camille
            $ second_choice_events.append("gallery")
            jump capitulo1_continue_second_choice
            
        "Conhecer o centro de jogos e atividades recreativas" if "games" not in second_choice_events:
            $ add_shared_memory("gaming_sports_meeting", ["samantha", "larissa"], "Primeira atividade combinando jogos e esportes")
            $ add_affinity_points("samantha", 10, "Interesse em RPG e criatividade")
            $ add_affinity_points("larissa", 10, "Interesse em competição e superação")
            call evento_samantha_larissa
            $ second_choice_events.append("games")
            jump capitulo1_continue_second_choice
            
        "Continuar para a aula com o Professor Wendell" if len(second_choice_events) >= 3:
            call capitulo1_aula_professor_wendell

    # Após a aula, continuar para a festa
    call capitulo1_terceira_escolha

    # Chamar o questionário de conexões futuras
    call capitulo1_quarta_escolha


# === FINAL DO CAPÍTULO 1 - RETROSPECTIVA E PROGRESSÃO ===
translate portuguese capitulo1_final:
    scene bg campus_sunset with fade
    
    narrator "O sol começava a se pôr sobre o campus, pintando o céu com tons dourados e rosa. Os primeiros dias na Faculdade Solária estavam chegando ao fim."
    
    narrator "Mas antes de voltar para casa, algo dentro de mim pedia uma pausa para refletir sobre tudo que havia acontecido..."

    # === RETROSPECTIVA DOS RELACIONAMENTOS ===
    narrator "Olhando para trás, percebi como cada encontro havia deixado uma marca única em meu coração."

    # Mostra o resumo dos relacionamentos
    $ relationship_summary = get_relationship_summary()
    
    narrator "📊 RESUMO DOS RELACIONAMENTOS:"
    python:
        for summary in relationship_summary:
            narrator(summary)
    
    # Momento emocional de reflexão
    call emotional_moment("reflection", None, "Reflexão sobre as conexões formadas no primeiro dia")
    
    narrator "Cada sorriso, cada conversa, cada momento compartilhado... tudo isso havia criado laços invisíveis mas poderosos entre nós."
    
    narrator "Mas uma pergunta ecoava em minha mente: seria suficiente para continuar esta jornada?"

    # === VERIFICAÇÃO DE PROGRESSÃO ===
    $ can_progress, progress_message = check_chapter_progression_requirement(1)
    
    narrator "[progress_message]"
    
    if can_progress:
        narrator "Meu coração se encheu de alegria ao perceber que havia criado conexões verdadeiras com todas essas pessoas incríveis."
        
        # Momento especial de realização
        call emotional_moment("achievement", None, "Realização de ter criado conexões suficientes para continuar")
        
        narrator "Esta jornada estava apenas começando, e eu mal podia esperar para ver o que o futuro nos reservava."
        
        narrator "Com um sorriso no rosto e esperança no coração, me preparei para o que estava por vir..."
        
        # Transição para o próximo capítulo
        scene bg city with fade
        narrator "O Capítulo 1 chegou ao fim, mas nossa história estava apenas começando..."
        
        # Desbloqueia o próximo capítulo
        if "capitulo2" not in persistent.unlocked_chapters:
            $ persistent.unlocked_chapters.append("capitulo2")
        
        # Por enquanto, direcionar para a última atualização
        jump ultima_atualizacao
        
    else:
        narrator "Uma sensação de inquietação tomou conta de mim. Talvez eu não tivesse me conectado o suficiente com todas as pessoas."
        
        narrator "Mas isso não significava que eu deveria desistir. Talvez fosse necessário mais tempo para construir essas conexões..."
        
        # Opção de revisitar eventos ou tentar novamente
        menu:
            "Refletir sobre as conexões perdidas":
                narrator "Talvez eu devesse ter escolhido diferentes caminhos, conhecido outras pessoas..."
                narrator "Mas cada escolha que fiz me trouxe até aqui, e isso também tinha seu valor."
                
            "Aceitar que algumas conexões levam tempo":
                narrator "Nem todas as amizades nascem no primeiro dia. Algumas precisam de tempo para florescer."
                narrator "O importante era que eu havia dado o primeiro passo."
        
        # Momento de crescimento pessoal
        call emotional_moment("growth", None, "Crescimento pessoal através da reflexão")
        
        narrator "Mesmo sem ter atingido o objetivo, este dia havia me ensinado muito sobre mim mesmo e sobre como me conectar com os outros."
        
        narrator "Talvez fosse hora de tentar uma abordagem diferente, ou simplesmente dar tempo para que as conexões se desenvolvessem naturalmente..."
        
        # Retorna para o menu principal ou oferece opção de rejogar
        scene bg city with fade
        narrator "O Capítulo 1 chegou ao fim. Talvez seja hora de refletir sobre suas escolhas e tentar novamente..."
        
        return
