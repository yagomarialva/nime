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
            call evento_nicole_camille
            jump capitulo1_segunda_escolha
            
        "Assistir a um filme com Katia e Samantha (Mergulhar na arte e criatividade)":
            $ add_shared_memory("cinema_first_meeting", ["katia", "samantha"], "Primeira experiência cinematográfica compartilhada")
            $ add_affinity_points("katia", 10, "Interesse em cinema independente")
            $ add_affinity_points("samantha", 10, "Interesse em suas atividades")
            
            # Reação tsundere da Katia
            show katia blush at left
            katia "E-eh?! Você quer vir comigo? N-não é como se eu estivesse esperando ou qualquer coisa assim..."
            katia "Mas... se você realmente quer, eu... eu não me importo. Só não venha reclamar se o filme for muito profundo para você!"
            hide katia
            
            call evento_katia_samantha
            jump capitulo1_segunda_escolha
            
        "Treinar na quadra com Larissa e Huey (Conectar corpo, mente e arte)":
            $ add_shared_memory("sports_first_meeting", ["larissa", "huey"], "Primeira atividade física e artística em grupo")
            $ add_affinity_points("larissa", 10, "Interesse em esportes")
            $ add_affinity_points("huey", 10, "Interesse em arte")
            call evento_larissa_huey
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
    show nicole happy at left
    show katia neutral at center_left
    show larissa happy at center_right
    show huey gentle at right
    show samantha happy at far_left
    show camille gentle at far_right
    
    narrator "E foi então que as vi... todas as seis pessoas incríveis que havia conhecido, reunidas em um só lugar."
    
    nicole "Nossa, que coincidência! Todas estamos aqui!"
    katia "Hmm... tanto faz."
    larissa "GENTE! Que energia incrível! Vamos aproveitar essa festa!"
    huey "É lindo ver todas vocês juntas... como uma obra de arte viva."
    samantha "Nossa, que legal! É tipo uma party épica com todas as personagens principais!"
    camille "Senti uma energia muito especial vindo daqui... como se o universo tivesse nos reunido."
    
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

