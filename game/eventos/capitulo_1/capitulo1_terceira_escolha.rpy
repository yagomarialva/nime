# === TERCEIRA ESCOLHA - FESTA DE BOAS-VINDAS ===
label capitulo1_terceira_escolha:
    # Tocar música da festa
    play music party fadein 2.0
    
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
