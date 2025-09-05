label capitulo1:
    if "capitulo1" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo1")
    
    # === INTRODUÇÃO MELHORADA ===
    scene bg auditorium with fade

    narrator "O auditório da Faculdade Solária estava repleto de expectativa. Dezenas de jovens, cada um carregando sonhos únicos, aguardavam o início de uma jornada que mudaria suas vidas para sempre."

    narrator "Entre eles, eu me sentava nas fileiras do meio, tentando absorver cada detalhe deste momento histórico. O ar estava carregado de possibilidades infinitas."

    # Professor Wendell - Diálogo mais impactante
    show professor_wendell neutral at center
    professor_wendell "Bem-vindos à Faculdade Solária, onde a arte encontra a alma humana."
    professor_wendell "Hoje, vocês não apenas iniciam um curso - vocês embarcam em uma jornada de autodescoberta através da criatividade."
    professor_wendell "Lembrem-se: as melhores histórias não são apenas contadas, são vividas. E vocês, queridos alunos, são os protagonistas de suas próprias narrativas."
    hide professor_wendell
    
    narrator "Suas palavras ecoaram em meu coração como uma profecia. Algo dentro de mim sabia que este dia seria especial."

    # === APRESENTAÇÕES MELHORADAS COM MECÂNICAS ===
    narrator "Após a apresentação, os alunos começaram a se dispersar. Foi então que percebi um grupo se formando naturalmente ao meu redor..."

    # Nicole - Apresentação mais profunda
    show nicole neutral at left
    nicole "Desculpem a interrupção, mas... vocês também sentiram que há algo diferente no ar hoje?"
    nicole "Sou Nicole. Especializo-me em comunicação estratégica, mas minha verdadeira paixão é entender como as pessoas se conectam através de suas histórias."
    nicole "Acredito que cada pessoa tem uma narrativa única esperando para ser descoberta."
    $ add_affinity_points("nicole", 5, "Primeira impressão positiva")
    hide nicole

    # Katia - Personalidade tsundere
    show katia neutral at left
    katia "Hmm... interessante perspectiva, Nicole. Mas vocês sabem o que realmente me intriga?"
    katia "Como as pessoas reagem quando suas expectativas são subvertidas. Sou Katia, cineasta em formação."
    katia "Especializo-me em filmes que fazem você questionar a realidade. A vida real, afinal, é o maior thriller de todos."
    katia "N-não que eu me importe com o que vocês pensam ou qualquer coisa assim..."
    $ add_affinity_points("katia", 5, "Primeira impressão positiva")
    hide katia

    # Larissa - Energia mais contagiante
    show larissa happy at left
    larissa "Nossa, que energia incrível vocês têm! Sou Larissa, mas podem me chamar de Lari."
    larissa "Sou apaixonada por esportes, especialmente vôlei. Acredito que o movimento do corpo liberta a mente, sabem?"
    larissa "E olha só essa quadra aqui! É como se estivesse chamando a gente para criar memórias incríveis juntos!"
    $ add_affinity_points("larissa", 5, "Primeira impressão positiva")
    hide larissa

    # Huey - Sensibilidade artística
    show huey gentle at left
    huey "Vocês... também sentiram que esta cidade respira arte? Cada esquina parece uma tela em branco esperando por uma pincelada de vida."
    huey "Sou Aline, mas muitos me chamam de Hu Wei. Sou artista visual, e acredito que a beleza está nos detalhes que a maioria das pessoas ignora."
    huey "Talvez... talvez tenhamos nos encontrado hoje por uma razão maior que o acaso."
    $ add_affinity_points("huey", 5, "Primeira impressão positiva")
    hide huey

    # Samantha - Entusiasmo genuíno
    show samantha happy at left
    samantha "GENTE! Vocês são demais! Sou Samantha, streamer de jogos e mestra de RPG!"
    samantha "Sabem o que é incrível? Cada um de vocês já parece ter uma personalidade única, como personagens de uma história épica!"
    samantha "Imaginem só... se fôssemos um grupo de aventureiros em uma jornada real! Seria a campanha mais incrível de todas!"
    $ add_affinity_points("samantha", 5, "Primeira impressão positiva")
    hide samantha

    # Camille - Espiritualidade sutil
    show camille gentle at left
    camille "Samantha... você disse exatamente o que eu estava sentindo. Sou Camille, e estudo as conexões energéticas entre as pessoas."
    camille "Hoje, quando entrei neste auditório, senti algo especial. Como se o universo tivesse alinhado as estrelas para nos reunir."
    camille "Cada um de vocês carrega uma energia única, mas juntos... juntos podemos criar algo verdadeiramente mágico."
    $ add_affinity_points("camille", 5, "Primeira impressão positiva")
    hide camille

    # === MOMENTO DE CONEXÃO PROFUNDA ===
    narrator "Por um instante, o tempo pareceu parar. Olhei ao redor e vi seis pessoas extraordinárias, cada uma com sua própria luz, mas todas conectadas por algo invisível e poderoso."

    # Momento emocional - estabelece o tom do jogo
    call emotional_moment("connection", None, "Reconhecimento de uma conexão especial entre o grupo") from _call_emotional_moment_1
    
    narrator "Meu coração se encheu de uma emoção indescritível. Esta não seria apenas mais uma faculdade - seria o início de uma família escolhida."

    # === PLANOS PARA A TARDE - MAIS ORGÂNICOS ===
    narrator "Conforme conversávamos, cada uma começou a compartilhar seus planos para a tarde..."

    show nicole happy at left
    nicole "Estava pensando em ir ao café da universidade para trabalhar em um projeto sobre storytelling em marketing."
    nicole "Se alguém quiser trocar ideias sobre como contar histórias que realmente tocam as pessoas... seria uma conversa fascinante."
    hide nicole

    show katia neutral at left
    katia "Eu tenho um filme independente em mente no cinema da cidade. Algo que desafia as convenções narrativas."
    katia "Se alguém quiser uma experiência cinematográfica que vai fazer vocês questionarem tudo... estou indo sozinha mesmo."
    katia "N-não é como se eu estivesse convidando ninguém ou algo assim! É só... se vocês quiserem, tanto faz."
    hide katia

    show larissa happy at left
    larissa "Eu vou treinar na quadra! Quem quiser se mexer e liberar endorfina, é só aparecer!"
    larissa "E depois podemos tomar um suco natural e conversar sobre como o movimento liberta a criatividade!"
    hide larissa

    show huey gentle at left
    huey "Ouvi falar de uma nova exposição de arte contemporânea na galeria do centro."
    huey "Se alguém quiser ver o mundo através de uma perspectiva diferente... seria uma experiência enriquecedora."
    hide huey

    show samantha happy at left
    samantha "Eu vou montar uma campanha de RPG épica! Quem quiser criar um personagem e embarcar numa aventura, é só falar!"
    samantha "E depois podemos assistir a um filme juntos para nos inspirar para as próximas sessões!"
    hide samantha

    show camille gentle at left
    camille "Vou meditar no jardim da universidade. É um lugar perfeito para conectar-se com a natureza e recarregar as energias."
    camille "Se alguém quiser aprender técnicas de mindfulness... seria um momento de paz compartilhado."
    hide camille

    # === ESCOLHA COM MAIS PESO EMOCIONAL ===
    narrator "Cada proposta parecia mais tentadora que a anterior. Como escolher entre tantas possibilidades incríveis?"

    narrator "Mas algo dentro de mim sabia que esta escolha seria importante. Não apenas para hoje, mas para toda a jornada que estava por vir."

    menu:
        "Ir ao café com Nicole e Camille (Explorar storytelling e espiritualidade)":
            $ add_shared_memory("cafe_first_meeting", ["nicole", "camille"], "Primeira conversa profunda sobre narrativas e conexões energéticas")
            $ add_affinity_points("nicole", 10, "Interesse em seus projetos")
            $ add_affinity_points("camille", 10, "Interesse em suas práticas")
            jump evento_nicole_camille
            
        "Assistir a um filme com Katia e Samantha (Mergulhar na arte e criatividade)":
            $ add_shared_memory("cinema_first_meeting", ["katia", "samantha"], "Primeira experiência cinematográfica compartilhada")
            $ add_affinity_points("katia", 10, "Interesse em cinema independente")
            $ add_affinity_points("samantha", 10, "Interesse em suas atividades")
            
            # Reação tsundere da Katia
            show katia blush at left
            katia "E-eh?! Você quer vir comigo? N-não é como se eu estivesse esperando ou qualquer coisa assim..."
            katia "Mas... se você realmente quer, eu... eu não me importo. Só não venha reclamar se o filme for muito profundo para você!"
            hide katia
            
            jump evento_katia_samantha
            
        "Treinar na quadra com Larissa e Huey (Conectar corpo, mente e arte)":
            $ add_shared_memory("sports_first_meeting", ["larissa", "huey"], "Primeira atividade física e artística em grupo")
            $ add_affinity_points("larissa", 10, "Interesse em esportes")
            $ add_affinity_points("huey", 10, "Interesse em arte")
            jump evento_larissa_huey

# === FINAL DO CAPÍTULO 1 - RETROSPECTIVA E PROGRESSÃO ===
label capitulo1_final:
    scene bg campus_sunset with fade
    
    narrator "O sol começava a se pôr sobre o campus, pintando o céu com tons dourados e rosa. O primeiro dia na Faculdade Solária estava chegando ao fim."
    
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
    call emotional_moment("reflection", None, "Reflexão sobre as conexões formadas no primeiro dia") from _call_emotional_moment_cap1_2
    
    narrator "Cada sorriso, cada conversa, cada momento compartilhado... tudo isso havia criado laços invisíveis mas poderosos entre nós."
    
    narrator "Mas uma pergunta ecoava em minha mente: seria suficiente para continuar esta jornada?"

    # === VERIFICAÇÃO DE PROGRESSÃO ===
    $ can_progress, progress_message = check_chapter_progression_requirement(1)
    
    narrator "[progress_message]"
    
    if can_progress:
        narrator "Meu coração se encheu de alegria ao perceber que havia criado conexões verdadeiras com todas essas pessoas incríveis."
        
        # Momento especial de realização
        call emotional_moment("achievement", None, "Realização de ter criado conexões suficientes para continuar") from _call_emotional_moment_cap1_3
        
        narrator "Esta jornada estava apenas começando, e eu mal podia esperar para ver o que o futuro nos reservava."
        
        narrator "Com um sorriso no rosto e esperança no coração, me preparei para o que estava por vir..."
        
        # Transição para o próximo capítulo
        scene bg city with fade
        narrator "O Capítulo 1 chegou ao fim, mas nossa história estava apenas começando..."
        
        # Desbloqueia o próximo capítulo
        if "capitulo2" not in persistent.unlocked_chapters:
            $ persistent.unlocked_chapters.append("capitulo2")
        
        jump capitulo2
        
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
        call emotional_moment("growth", None, "Crescimento pessoal através da reflexão") from _call_emotional_moment_cap1_4
        
        narrator "Mesmo sem ter atingido o objetivo, este dia havia me ensinado muito sobre mim mesmo e sobre como me conectar com os outros."
        
        narrator "Talvez fosse hora de tentar uma abordagem diferente, ou simplesmente dar tempo para que as conexões se desenvolvessem naturalmente..."
        
        # Retorna para o menu principal ou oferece opção de rejogar
        scene bg city with fade
        narrator "O Capítulo 1 chegou ao fim. Talvez seja hora de refletir sobre suas escolhas e tentar novamente..."
        
        menu:
            "Voltar ao menu principal":
                return
            "Tentar o Capítulo 1 novamente":
                jump capitulo1

