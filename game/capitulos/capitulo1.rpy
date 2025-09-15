label capitulo1:
    if "capitulo1" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo1")
    
    # === INTRODUÇÃO COM MONÓLOGO DO PROFESSOR WENDELL ===
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
label capitulo1_continue_exploration:
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
label capitulo1_segunda_escolha:
    scene bg campus_morning with fade
    
    narrator "O sol da manhã iluminava o campus com uma luz dourada. O segundo dia na Faculdade Solária havia começado."
    narrator "Após a experiência incrível do dia anterior, eu mal podia esperar para ver o que mais esta jornada me reservava."
    
    narrator "Conforme caminhava pelo campus, encontrei todas as pessoas que havia conhecido no dia anterior, cada uma explorando suas paixões..."
    
    # Apresentação de todas as 6 personagens
    show nicole neutral at left
    nicole "Bom dia! Estava pensando em continuar nossa conversa sobre metodologia e análise de dados..."
    nicole "Se alguém quiser trocar ideias sobre como estruturar projetos de forma eficiente... seria uma discussão fascinante."
    hide nicole
    
    show katia neutral at left
    katia "Hmm... interessante perspectiva, Nicole. Mas vocês sabem o que realmente me intriga?"
    katia "Como as pessoas reagem quando suas expectativas são subvertidas. Tenho alguns filmes em mente que desafiam convenções."
    katia "N-não é como se eu estivesse convidando ninguém ou qualquer coisa assim... mas se vocês quiserem, tanto faz."
    hide katia
    
    show larissa happy at left
    larissa "Nossa, que energia incrível vocês têm! Eu vou treinar na quadra hoje!"
    larissa "Quem quiser se mexer e liberar endorfina, é só aparecer! E depois podemos tomar um suco natural!"
    hide larissa
    
    show huey gentle at left
    huey "Ouvi falar de uma nova exposição de arte contemporânea na galeria do centro."
    huey "Se alguém quiser explorar a conexão entre técnica artística e energia criativa... seria uma experiência enriquecedora."
    hide huey
    
    show samantha happy at left
    samantha "GENTE! Vamos fazer uma sessão épica de RPG na quadra!"
    samantha "Imaginem só... uma aventura onde vocês são aventureiros em uma arena mágica! É tipo esporte, mas com mais imaginação!"
    hide samantha
    
    show camille gentle at left
    camille "Samantha... você disse exatamente o que eu estava sentindo. Vou meditar no jardim da universidade."
    camille "É um lugar perfeito para conectar-se com a natureza e recarregar as energias."
    camille "Se alguém quiser aprender técnicas de mindfulness... seria um momento de paz compartilhado."
    hide camille
    
    narrator "Cada proposta parecia mais interessante que a anterior. Como escolher entre tantas possibilidades incríveis?"
    
    menu:
        "Debater metodologia com Katia e Nicole (Análise vs. Intuição criativa)":
            $ add_shared_memory("methodology_debate_meeting", ["katia", "nicole"], "Primeira discussão sobre metodologia e criatividade")
            $ add_affinity_points("katia", 10, "Interesse em análise criativa")
            $ add_affinity_points("nicole", 10, "Interesse em metodologia")
            call evento_katia_nicole
            jump capitulo1_final
            
        "Explorar arte espiritual com Huey e Camille (Técnica vs. Energia)":
            $ add_shared_memory("art_spirituality_meeting", ["huey", "camille"], "Primeira exploração da conexão entre arte e espiritualidade")
            $ add_affinity_points("huey", 10, "Interesse em técnica artística")
            $ add_affinity_points("camille", 10, "Interesse em energia criativa")
            call evento_huey_camille
            jump capitulo1_final
            
        "Jogar RPG esportivo com Samantha e Larissa (Fantasia vs. Realidade)":
            $ add_shared_memory("gaming_sports_meeting", ["samantha", "larissa"], "Primeira atividade combinando jogos e esportes")
            $ add_affinity_points("samantha", 10, "Interesse em RPG e criatividade")
            $ add_affinity_points("larissa", 10, "Interesse em competição e superação")
            call evento_samantha_larissa
            jump capitulo1_terceira_escolha

# === TERCEIRA ESCOLHA - FESTA DE BOAS-VINDAS ===
label capitulo1_terceira_escolha:
    scene bg campus_evening with fade
    
    narrator "O terceiro dia na Faculdade Solária havia chegado ao fim. O sol se punha sobre o campus, pintando o céu com tons alaranjados e rosa."
    narrator "Mas a noite ainda estava apenas começando..."
    
    scene bg campus_night with fade
    narrator "Conforme caminhava pelo campus, ouvi música e risadas vindas do centro estudantil. Uma festa de boas-vindas estava acontecendo!"
    narrator "Era a oportunidade perfeita para conhecer melhor todas as pessoas incríveis que havia encontrado nos últimos dias."
    
    scene bg festa_boas_vindas with fade
    narrator "O ambiente estava animado, com música, luzes coloridas e estudantes conversando em grupos. O ar estava carregado de energia e possibilidades."
    
    # Apresentação do grupo reunido
    narrator "E foi então que as vi... todas as seis pessoas incríveis que havia conhecido, reunidas em um só lugar."
    
    show nicole happy at center
    nicole "Nossa, que coincidência! Todas estamos aqui!"
    hide nicole with dissolve
    
    show katia neutral at center
    katia "Hmm... tanto faz."
    hide katia with dissolve
    
    show larissa happy at center
    larissa "GENTE! Que energia incrível! Vamos aproveitar essa festa!"
    hide larissa with dissolve
    
    show huey gentle at center
    huey "É lindo ver todas vocês juntas... como uma obra de arte viva."
    hide huey with dissolve
    
    show samantha happy at center
    samantha "Nossa, que legal! É tipo uma party épica com todas as personagens principais!"
    hide samantha with dissolve
    
    show camille gentle at center
    camille "Senti uma energia muito especial vindo daqui... como se o universo tivesse nos reunido."
    hide camille with dissolve
    
    narrator "Por um momento, todas ficaram em silêncio, observando uma à outra. Era como se houvesse uma conexão invisível entre todas elas."
    
    # Momento especial com cada personagem
    narrator "Conforme a festa continuava, cada uma se dispersou para explorar o ambiente. Foi então que tive a oportunidade de conversar individualmente com cada uma..."
    
    # === MOMENTO ESPECIAL COM NICOLE ===
    scene bg festa_boas_vindas with fade
    show nicole neutral at center
    
    narrator "Encontrei Nicole em um canto mais silencioso da festa, organizando seus materiais em uma mesa."
    
    nicole "Ah, você! Estava esperando uma oportunidade para conversar com você em particular."
    nicole "Estes últimos dias foram... transformadores. Nunca pensei que encontraria pessoas que entendessem minha paixão por metodologia e análise."
    
    menu:
        "Perguntar sobre seus projetos futuros":
            $ points_nicole += 3
            narrator "Perguntei sobre os projetos que Nicole estava desenvolvendo."
            nicole "Bem... tenho várias ideias em mente. Mas o mais importante é que agora tenho pessoas incríveis para colaborar."
            nicole "Katia, por exemplo... ela me mostrou que há mais na narrativa do que apenas estrutura. É fascinante como nos complementamos."
            
        "Comentar sobre a conexão do grupo":
            $ points_nicole += 2
            narrator "Comentei sobre a conexão especial que parecia existir entre todas."
            nicole "É verdade... há algo especial aqui. Como se cada uma de nós trouxesse uma peça única de um quebra-cabeça maior."
            nicole "E você... você parece ser a peça que conecta todas as outras."
            
        "Refletir sobre os últimos dias":
            $ points_nicole += 1
            narrator "Refletimos juntos sobre tudo que havia acontecido nos últimos dias."
            nicole "Nunca pensei que a faculdade seria assim... cheia de descobertas e conexões genuínas."
            nicole "Você fez parte disso. Obrigada por estar aqui."
    
    # === MOMENTO ESPECIAL COM KATIA ===
    scene bg festa_boas_vindas with fade
    show katia neutral at center
    
    narrator "Katia estava em pé perto de uma janela, observando a festa com um ar pensativo."
    
    katia "Hmm... você apareceu. Estava pensando em algo importante."
    katia "Estes últimos dias... foram diferentes do que eu esperava. Encontrei pessoas que realmente entendem de cinema e narrativa."
    
    menu:
        "Perguntar sobre seus filmes favoritos":
            $ points_katia += 3
            narrator "Perguntei sobre os filmes que Katia mais gostava."
            katia "Hmm... tenho vários. Mas o mais especial é quando encontro alguém que realmente entende a profundidade do cinema."
            katia "Nicole, por exemplo... ela me mostrou que há mais na análise do que apenas intuição. É fascinante como nos complementamos."
            katia "N-não é como se eu estivesse impressionada ou qualquer coisa assim... mas é raro encontrar alguém assim."
            
        "Comentar sobre sua personalidade única":
            $ points_katia += 2
            narrator "Comentei sobre a personalidade única de Katia."
            katia "Hmpf... você realmente me observa, não é? É... reconfortante saber que alguém entende minha forma de ser."
            katia "Às vezes sinto que sou muito diferente das outras pessoas... mas aqui, com vocês, me sinto... aceita."
            
        "Refletir sobre o crescimento do grupo":
            $ points_katia += 1
            narrator "Refletimos sobre como o grupo havia crescido e se conectado."
            katia "Nunca pensei que encontraria pessoas que me aceitassem como sou... com todas as minhas peculiaridades."
            katia "E você... você parece entender cada uma de nós de uma forma única."
    
    # === MOMENTO ESPECIAL COM LARISSA ===
    scene bg festa_boas_vindas with fade
    show larissa happy at center
    
    narrator "Larissa estava dançando sozinha em um canto da festa, com um sorriso contagiante no rosto."
    
    larissa "Oi! Que bom te ver! Estava esperando uma oportunidade para conversar com você!"
    larissa "Nossa, que energia incrível esta festa tem! E olha só, todas as pessoas incríveis que conhecemos estão aqui!"
    
    menu:
        "Perguntar sobre seus treinos":
            $ points_larissa += 3
            narrator "Perguntei sobre os treinos e atividades esportivas de Larissa."
            larissa "Nossa, que legal que você perguntou! Tenho treinado muito, e agora tenho pessoas incríveis para treinar junto!"
            larissa "Samantha, por exemplo... ela me mostrou que há mais no esporte do que apenas competição. É fascinante como nos complementamos!"
            
        "Comentar sobre sua energia contagiante":
            $ points_larissa += 2
            narrator "Comentei sobre a energia positiva e contagiante de Larissa."
            larissa "Nossa, obrigada! É que eu realmente amo estar com pessoas e criar memórias incríveis!"
            larissa "E você... você tem uma energia muito especial. É como se você conseguisse conectar todas as pessoas!"
            
        "Refletir sobre as amizades formadas":
            $ points_larissa += 1
            narrator "Refletimos sobre as amizades que haviam se formado."
            larissa "Nunca pensei que encontraria pessoas tão incríveis! Cada uma tem algo especial para oferecer!"
            larissa "E você... você é como a cola que mantém todo mundo junto!"
    
    # === MOMENTO ESPECIAL COM HUEY ===
    scene bg festa_boas_vindas with fade
    show huey gentle at center
    
    narrator "Huey estava sentada em um sofá, observando as pessoas dançarem com um olhar contemplativo."
    
    huey "Ah, você... que sincronia. Estava pensando em algo especial."
    huey "Esta festa... é como uma obra de arte viva. Cada pessoa, cada movimento, cada emoção... tudo se conecta de forma única."
    
    menu:
        "Perguntar sobre sua arte":
            $ points_huey += 3
            narrator "Perguntei sobre os projetos artísticos de Huey."
            huey "Bem... tenho várias ideias em mente. Mas o mais especial é que agora tenho pessoas que realmente entendem a arte."
            huey "Camille, por exemplo... ela me mostrou que há mais na criação do que apenas técnica. É fascinante como nos complementamos."
            
        "Comentar sobre sua sensibilidade artística":
            $ points_huey += 2
            narrator "Comentei sobre a sensibilidade artística única de Huey."
            huey "Você realmente me vê, não é? É... reconfortante saber que alguém entende minha forma de perceber o mundo."
            huey "Às vezes sinto que vejo as coisas de forma diferente... mas aqui, com vocês, me sinto... compreendida."
            
        "Refletir sobre a beleza do momento":
            $ points_huey += 1
            narrator "Refletimos sobre a beleza do momento presente."
            huey "Nunca pensei que encontraria pessoas que vissem a beleza nas mesmas coisas que eu..."
            huey "E você... você parece conseguir ver a beleza em cada uma de nós de uma forma única."
    
    # === MOMENTO ESPECIAL COM SAMANTHA ===
    scene bg festa_boas_vindas with fade
    show samantha happy at center
    
    narrator "Samantha estava em pé perto da mesa de jogos, organizando cartas e dados com entusiasmo."
    
    samantha "GENTE! Que legal te ver! Estava esperando uma oportunidade para conversar com você!"
    samantha "Nossa, que festa épica! É tipo uma party de RPG com todas as personagens principais reunidas!"
    
    menu:
        "Perguntar sobre suas campanhas de RPG":
            $ points_samantha += 3
            narrator "Perguntei sobre as campanhas de RPG que Samantha estava organizando."
            samantha "Nossa, que legal que você perguntou! Tenho várias ideias épicas, e agora tenho pessoas incríveis para jogar!"
            samantha "Larissa, por exemplo... ela me mostrou que há mais nos jogos do que apenas fantasia. É fascinante como nos complementamos!"
            
        "Comentar sobre seu entusiasmo contagiante":
            $ points_samantha += 2
            narrator "Comentei sobre o entusiasmo contagiante de Samantha."
            samantha "Nossa, obrigada! É que eu realmente amo estar com pessoas e criar aventuras incríveis!"
            samantha "E você... você tem uma energia muito especial. É como se você conseguisse conectar todas as pessoas!"
            
        "Refletir sobre as aventuras compartilhadas":
            $ points_samantha += 1
            narrator "Refletimos sobre as aventuras que haviam sido compartilhadas."
            samantha "Nunca pensei que encontraria pessoas tão incríveis para jogar! Cada uma tem algo especial para oferecer!"
            samantha "E você... você é como o mestre de RPG que conecta todas as histórias!"
    
    # === MOMENTO ESPECIAL COM CAMILLE ===
    scene bg festa_boas_vindas with fade
    show camille gentle at center
    
    narrator "Camille estava sentada em um canto mais tranquilo, meditando suavemente enquanto observava a festa."
    
    camille "Ah, você... que sincronia perfeita. Estava esperando por este momento."
    camille "Esta festa... sinto uma energia muito especial aqui. Como se todas as pessoas estivessem conectadas por algo maior."
    
    menu:
        "Perguntar sobre suas práticas espirituais":
            $ points_camille += 3
            narrator "Perguntei sobre as práticas espirituais e de meditação de Camille."
            camille "Bem... tenho várias práticas que me ajudam a me conectar com a energia universal."
            camille "Huey, por exemplo... ela me mostrou que há mais na arte do que apenas técnica. É fascinante como nos complementamos."
            
        "Comentar sobre sua energia serena":
            $ points_camille += 2
            narrator "Comentei sobre a energia serena e espiritual de Camille."
            camille "Você realmente sente a energia, não é? É... reconfortante saber que alguém entende minha conexão com o universo."
            camille "Às vezes sinto que percebo as coisas de forma diferente... mas aqui, com vocês, me sinto... acolhida."
            
        "Refletir sobre a conexão espiritual do grupo":
            $ points_camille += 1
            narrator "Refletimos sobre a conexão espiritual que parecia existir entre todas."
            camille "Nunca pensei que encontraria pessoas que sentissem a energia da mesma forma que eu..."
            camille "E você... você parece conseguir sentir a energia única de cada uma de nós."
    
    # === MOMENTO DE DECISÃO ===
    scene bg festa_boas_vindas with fade
    
    narrator "Conforme a festa chegava ao fim, senti que era hora de escolher alguém para acompanhar até sua república."
    narrator "Cada uma das pessoas incríveis que havia conhecido parecia ter algo especial para compartilhar..."
    
    menu:
        "Acompanhar Nicole até sua república":
            $ add_shared_memory("evening_walk_nicole", ["nicole"], "Caminhada noturna especial com Nicole até sua república")
            $ add_affinity_points("nicole", 15, "Momento íntimo especial")
            jump capitulo1_caminhada_nicole
            
        "Acompanhar Katia até sua república":
            $ add_shared_memory("evening_walk_katia", ["katia"], "Caminhada noturna especial com Katia até sua república")
            $ add_affinity_points("katia", 15, "Momento íntimo especial")
            jump capitulo1_caminhada_katia
            
        "Acompanhar Larissa até sua república":
            $ add_shared_memory("evening_walk_larissa", ["larissa"], "Caminhada noturna especial com Larissa até sua república")
            $ add_affinity_points("larissa", 15, "Momento íntimo especial")
            jump capitulo1_caminhada_larissa
            
        "Acompanhar Huey até sua república":
            $ add_shared_memory("evening_walk_huey", ["huey"], "Caminhada noturna especial com Huey até sua república")
            $ add_affinity_points("huey", 15, "Momento íntimo especial")
            jump capitulo1_caminhada_huey
            
        "Acompanhar Samantha até sua república":
            $ add_shared_memory("evening_walk_samantha", ["samantha"], "Caminhada noturna especial com Samantha até sua república")
            $ add_affinity_points("samantha", 15, "Momento íntimo especial")
            jump capitulo1_caminhada_samantha
            
        "Acompanhar Camille até sua república":
            $ add_shared_memory("evening_walk_camille", ["camille"], "Caminhada noturna especial com Camille até sua república")
            $ add_affinity_points("camille", 15, "Momento íntimo especial")
            jump capitulo1_caminhada_camille

# === QUARTA ESCOLHA - ENTREVISTA DE TRABALHO ===
label capitulo1_quarta_escolha:
    scene bg campus_morning with fade
    
    # Inicializar variáveis do sistema de trabalho
    $ work_interests = {"analytical": False, "creative": False, "social": False}
    $ work_style = {"independent": False, "collaborative": False, "leadership": False}
    $ work_environment = {"quiet": False, "dynamic": False, "creative": False}
    $ work_approach = {"analytical": False, "intuitive": False, "adaptive": False}
    $ work_impact = {"efficiency": False, "community": False, "innovation": False}
    $ chosen_work = ""
    $ work_team = []
    $ work_description = ""
    $ work_benefits = ""
    
    narrator "O quarto dia na Faculdade Solária havia começado. Após as experiências incríveis dos dias anteriores, senti que era hora de pensar no futuro prático."
    narrator "Precisava de um trabalho de meio período para me sustentar durante os estudos, e ouvi que o Professor Wendell poderia ter algumas orientações valiosas."
    
    scene bg professor_office with fade
    show professor_wendell neutral at center
    
    narrator "Encontrei o Professor Wendell em seu escritório, organizando alguns documentos. Ele parecia estar esperando por alguém."
    
    professor_wendell "Ah, você! Estava esperando sua visita. Ouvi que você está procurando oportunidades de trabalho no campus."
    professor_wendell "Tenho algumas posições interessantes disponíveis, mas antes preciso entender melhor seu perfil e interesses."
    professor_wendell "Vamos fazer uma pequena entrevista para encontrar a posição ideal para você."
    
    narrator "O Professor Wendell se acomodou em sua cadeira e pegou um formulário. Sua expressão era séria, mas acolhedora."
    
    professor_wendell "Primeiro, me conte sobre seus interesses acadêmicos. O que mais te motiva nos estudos?"
    
    menu:
        "Análise de dados e metodologia":
            $ work_interests["analytical"] = True
            $ work_interests["creative"] = False
            $ work_interests["social"] = False
            narrator "Mencionei minha paixão por análise de dados, metodologia e estruturas organizacionais."
            professor_wendell "Interessante... uma mente analítica. Isso pode ser muito útil em várias áreas do campus."
            
        "Arte e expressão criativa":
            $ work_interests["analytical"] = False
            $ work_interests["creative"] = True
            $ work_interests["social"] = False
            narrator "Falei sobre meu interesse em arte, criatividade e expressão visual."
            professor_wendell "Fascinante... a criatividade é essencial para o crescimento da universidade."
            
        "Interação social e comunicação":
            $ work_interests["analytical"] = False
            $ work_interests["creative"] = False
            $ work_interests["social"] = True
            narrator "Comentei sobre minha paixão por interação social, comunicação e trabalho em equipe."
            professor_wendell "Excelente... as conexões humanas são o coração de qualquer instituição."
    
    professor_wendell "Agora, me conte sobre seu estilo de trabalho preferido. Como você gosta de trabalhar?"
    
    menu:
        "Trabalho independente e focado":
            $ work_style["independent"] = True
            $ work_style["collaborative"] = False
            $ work_style["leadership"] = False
            narrator "Mencionei que prefiro trabalhar de forma independente, com foco e concentração."
            professor_wendell "Entendo... autonomia e responsabilidade individual. Muito valioso."
            
        "Trabalho em equipe e colaborativo":
            $ work_style["independent"] = False
            $ work_style["collaborative"] = True
            $ work_style["leadership"] = False
            narrator "Falei sobre minha preferência por trabalho em equipe e colaboração."
            professor_wendell "Perfeito... o trabalho em equipe é fundamental para o sucesso."
            
        "Liderança e coordenação de projetos":
            $ work_style["independent"] = False
            $ work_style["collaborative"] = False
            $ work_style["leadership"] = True
            narrator "Comentei sobre minha paixão por liderança e coordenação de projetos."
            professor_wendell "Impressionante... líderes natos são raros e valiosos."
    
    professor_wendell "Qual ambiente de trabalho você considera mais produtivo para você?"
    
    menu:
        "Ambiente silencioso e organizado":
            $ work_environment["quiet"] = True
            $ work_environment["dynamic"] = False
            $ work_environment["creative"] = False
            narrator "Mencionei que prefiro ambientes silenciosos e bem organizados."
            professor_wendell "Compreensível... a concentração é essencial para certas tarefas."
            
        "Ambiente dinâmico e movimentado":
            $ work_environment["quiet"] = False
            $ work_environment["dynamic"] = True
            $ work_environment["creative"] = False
            narrator "Falei sobre minha preferência por ambientes dinâmicos e movimentados."
            professor_wendell "Excelente... a energia é contagiante e produtiva."
            
        "Ambiente criativo e inspirador":
            $ work_environment["quiet"] = False
            $ work_environment["dynamic"] = False
            $ work_environment["creative"] = True
            narrator "Comentei sobre minha paixão por ambientes criativos e inspiradores."
            professor_wendell "Maravilhoso... a inspiração é o motor da inovação."
    
    professor_wendell "Como você lida com desafios e pressão no trabalho?"
    
    menu:
        "Análise sistemática e planejamento":
            $ work_approach["analytical"] = True
            $ work_approach["intuitive"] = False
            $ work_approach["adaptive"] = False
            narrator "Mencionei que prefiro analisar sistematicamente e planejar antes de agir."
            professor_wendell "Muito bom... a abordagem metódica evita muitos problemas."
            
        "Intuição e criatividade":
            $ work_approach["analytical"] = False
            $ work_approach["intuitive"] = True
            $ work_approach["adaptive"] = False
            narrator "Falei sobre minha confiança na intuição e criatividade para resolver problemas."
            professor_wendell "Interessante... a intuição pode ser uma ferramenta poderosa."
            
        "Adaptação rápida e flexibilidade":
            $ work_approach["analytical"] = False
            $ work_approach["intuitive"] = False
            $ work_approach["adaptive"] = True
            narrator "Comentei sobre minha capacidade de adaptação rápida e flexibilidade."
            professor_wendell "Excelente... a adaptabilidade é crucial no mundo atual."
    
    professor_wendell "Por fim, qual tipo de impacto você gostaria de ter na universidade?"
    
    menu:
        "Melhorar processos e eficiência":
            $ work_impact["efficiency"] = True
            $ work_impact["community"] = False
            $ work_impact["innovation"] = False
            narrator "Mencionei meu interesse em melhorar processos e eficiência da universidade."
            professor_wendell "Muito nobre... a eficiência beneficia todos."
            
        "Fortalecer a comunidade estudantil":
            $ work_impact["efficiency"] = False
            $ work_impact["community"] = True
            $ work_impact["innovation"] = False
            narrator "Falei sobre meu desejo de fortalecer a comunidade estudantil."
            professor_wendell "Admirável... a comunidade é o coração da universidade."
            
        "Promover inovação e criatividade":
            $ work_impact["efficiency"] = False
            $ work_impact["community"] = False
            $ work_impact["innovation"] = True
            narrator "Comentei sobre minha paixão por promover inovação e criatividade."
            professor_wendell "Inspirador... a inovação é o futuro da educação."
    
    # === ANÁLISE DAS RESPOSTAS E DETERMINAÇÃO DO TRABALHO ===
    narrator "O Professor Wendell analisou minhas respostas cuidadosamente, fazendo algumas anotações em seu formulário."
    
    professor_wendell "Baseado em suas respostas, identifiquei a posição ideal para você. Vou apresentar três opções que se alinham com seu perfil."
    
    # Calcular pontuações para determinar o trabalho
    $ analytical_score = 0
    $ creative_score = 0
    $ social_score = 0
    
    if work_interests["analytical"]:
        $ analytical_score += 2
    if work_interests["creative"]:
        $ creative_score += 2
    if work_interests["social"]:
        $ social_score += 2
    
    if work_style["independent"]:
        $ analytical_score += 1
    if work_style["collaborative"]:
        $ social_score += 1
    if work_style["leadership"]:
        $ social_score += 1
    
    if work_environment["quiet"]:
        $ analytical_score += 1
    if work_environment["dynamic"]:
        $ social_score += 1
    if work_environment["creative"]:
        $ creative_score += 1
    
    if work_approach["analytical"]:
        $ analytical_score += 1
    if work_approach["intuitive"]:
        $ creative_score += 1
    if work_approach["adaptive"]:
        $ social_score += 1
    
    if work_impact["efficiency"]:
        $ analytical_score += 1
    if work_impact["community"]:
        $ social_score += 1
    if work_impact["innovation"]:
        $ creative_score += 1
    
    # Determinar o trabalho baseado nas pontuações
    if analytical_score >= creative_score and analytical_score >= social_score:
        $ chosen_work = "library"
        $ work_team = ["nicole", "katia", "huey"]
        $ work_description = "Biblioteca e Centro de Pesquisa"
        $ work_benefits = "Trabalhar com Nicole na organização de dados, Katia na análise de narrativas e Huey na curadoria artística"
    elif creative_score >= social_score:
        $ chosen_work = "arts_center"
        $ work_team = ["huey", "camille", "samantha"]
        $ work_description = "Centro de Artes e Criatividade"
        $ work_benefits = "Colaborar com Huey em projetos artísticos, Camille em eventos espirituais e Samantha em atividades criativas"
    else:
        $ chosen_work = "student_center"
        $ work_team = ["larissa", "samantha", "camille"]
        $ work_description = "Centro Estudantil e Atividades"
        $ work_benefits = "Trabalhar com Larissa em eventos esportivos, Samantha em atividades de entretenimento e Camille em eventos comunitários"
    
    professor_wendell "Perfeito! Baseado em seu perfil, recomendo que você trabalhe no [work_description]."
    professor_wendell "[work_benefits]."
    professor_wendell "Esta posição permitirá que você desenvolva suas habilidades enquanto contribui significativamente para a universidade."
    
    narrator "O Professor Wendell me entregou um documento com os detalhes da posição e os contatos das pessoas com quem trabalharia."
    
    # Adicionar memória compartilhada sobre o trabalho
    $ add_shared_memory("work_assignment", work_team, f"Atribuição de trabalho no {work_description} com foco em {work_benefits}")
    
    # Adicionar pontos de afinidade com a equipe de trabalho
    python:
        for character in work_team:
            add_affinity_points(character, 10, "Colega de trabalho")
    
    professor_wendell "Agora, você gostaria de conhecer melhor sua equipe de trabalho? Posso apresentá-lo às pessoas com quem você colaborará."
    
    menu:
        "Sim, gostaria de conhecer a equipe":
            $ add_affinity_points(work_team[0], 5, "Interesse em colaboração")
            $ add_affinity_points(work_team[1], 5, "Interesse em colaboração")
            $ add_affinity_points(work_team[2], 5, "Interesse em colaboração")
            narrator "Concordei em conhecer a equipe de trabalho."
            professor_wendell "Excelente! Vou organizar um encontro para vocês se conhecerem melhor."
            jump capitulo1_final
            
        "Prefiro começar o trabalho diretamente":
            narrator "Agradeci a oferta, mas preferi começar o trabalho diretamente."
            professor_wendell "Entendo perfeitamente. Boa sorte em sua nova posição!"
            jump capitulo1_final


# === FINAL DO CAPÍTULO 1 - RETROSPECTIVA E PROGRESSÃO ===
label capitulo1_final:
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

