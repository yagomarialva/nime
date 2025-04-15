label capitulo1:
    
    scene bg auditorium with fade

    # Narrador
    narrator "Ao chegar ao auditório onde a aula inaugural aconteceria, sentei-me nas fileiras do meio. O espaço logo foi preenchido com dezenas de alunos."

    narrator "Um homem de meia-idade, de postura serena e olhar atento, subiu ao palco improvisado. Seu nome era Professor Wendell Garcez, coordenador do curso de Arte e Comunicação."

    # Professor Wendell
    "Professor Wendell" "Sejam bem-vindos à faculdade Solária. Hoje começa uma jornada de criatividade, expressão pessoal e a beleza de contar histórias com emoção."
    "Professor Wendell" "Explorem diferentes linguagens artísticas, expressem-se com autenticidade e nunca subestimem o poder de uma boa narrativa."

    narrator "Após o término da apresentação, os alunos começaram a se dispersar. Eu ainda absorvia as palavras do professor quando uma voz próxima se fez ouvir."

    # Nicole
    show nicole neutral at left
    nicole "Vocês já estão reclamando? Nem começou o semestre."
    nicole "Olá, sou Nicole. Comunicação estratégica e planejamento financeiro são minha praia."
    hide nicole

    # Katia
    show katia neutral at left
    katia "Que coisa mais motivacional de filme B..."
    katia "Se fosse o roteiro de um longa, eu teria abandonado na metade."
    katia "Katia. Cineasta em formação. Especialidade: filmes que fazem você dormir com a luz acesa."
    hide katia

    # Larissa
    show larissa happy at left
    larissa "Cara! A quadra de vôlei aqui é ENORME. Já quero marcar um amistoso com a turma!"
    larissa "Oi, sou Larissa, mas pode chamar de Lari."
    hide larissa

    # Aline (Huey)
    show huey neutral at left
    huey "Vocês... também sentiram que essa cidade tem uma energia especial?"
    huey "Sou Aline. Mas muita gente me chama de Huey."
    hide huey

    # Samantha
    show samantha happy at left
    samantha "ALGUÉM AQUI CURTE RPG DE MESA?!"
    samantha "Meu nome é Samantha! Faço lives de jogos e tô montando uma campanha de D&D pra esse fim de semana! Quem topa?!"
    hide samantha

    # Camille
    show camille neutral at left
    camille "Com licença... vocês também sentiram que hoje o ar está diferente?"
    camille "Sou Camille. Estava meditando ali perto e senti... uma conexão entre vocês. As energias estão pulsando."
    hide camille

    narrator "O grupo começou a se formar de forma involuntária, como se o universo estivesse alinhando as peças de um tabuleiro invisível."

    # Personagens falam sobre seus planos
    show nicole neutral at left
    nicole "Mais tarde, vou ao café da universidade para planejar um projeto sobre monetização de arte. Se alguém quiser trocar ideias, será bem-vindo."
    hide nicole

    show katia neutral at left
    katia "Eu estava pensando em assistir a um filme cult no cinema da cidade. Nada muito popular, mas algo que faz você pensar. Se alguém quiser ir, tanto faz."
    hide katia

    show larissa happy at left
    larissa "Eu vou treinar na quadra de vôlei mais tarde. Quem quiser se mexer um pouco e se divertir, pode aparecer por lá!"
    hide larissa

    show huey neutral at left
    huey "Eu ouvi falar de uma galeria de arte contemporânea que abriu recentemente. Acho que vou dar uma passada para me inspirar. Se alguém quiser vir, será interessante."
    hide huey

    show samantha happy at left
    samantha "Eu vou montar uma campanha de RPG de mesa mais tarde. Se alguém quiser criar um personagem e se juntar, vai ser épico!"
    hide samantha

    show camille neutral at left
    camille "Eu estava pensando em meditar no jardim da universidade mais tarde. É um ótimo lugar para recarregar as energias. Se alguém quiser, pode vir comigo."
    hide camille

    # Samantha
    show samantha happy at left
    samantha "Eu estava pensando em assistir a um filme no cinema mais tarde. Parece que é cheio de mistério e simbolismo."
    samantha "Pode ser uma ótima inspiração para criar novas histórias para minhas campanhas de RPG. Se alguém quiser ir, será divertido!"
    hide samantha

    narrator "Cada um parecia ter planos interessantes para o resto do dia. Eu precisava decidir com quem passaria a tarde."

    # Escolha de evento
    menu:
        "Ir ao café com Nicole e Camille":
            jump evento_nicole
        "Assistir a um filme com Katia e Samantha":
            jump evento_katia_samantha
        "Treinar na quadra com Larissa e Huey":
            jump evento_larissa
        "Visitar a galeria de arte com Huey e Katia":
            jump evento_huey

# --- Evento Nicole e Camille ---
label evento_nicole:
    $ points_nicole += 1
    scene bg cafe with dissolve
    show nicole neutral at left
    show camille neutral at right

    narrator "Nicole me convidou para continuar a conversa no café da universidade. Camille também se juntou, atraída pelo tema de sustentabilidade."

    nicole "Estou organizando um projeto para ajudar artistas a entender melhor como monetizar sua arte sem perder a essência."

    camille "A conexão entre arte e energia é mais profunda do que parece. Sustentabilidade também é espiritualidade."

    menu:
        "Perguntar a Nicole sobre investimento em arte":
            $ points_nicole += 1
            nicole "Excelente pergunta! Muitos ignoram o valor patrimonial da arte. Podemos discutir isso em uma oficina!"

        "Falar com Camille sobre chakras e criatividade":
            $ points_camille += 1
            camille "Ah, sim. Cada chakra influencia um aspecto criativo. O plexo solar, por exemplo, está ligado à autoconfiança na expressão."

        "Sugerir unir espiritualidade e planejamento no mesmo projeto":
            $ points_nicole += 1
            $ points_camille += 1
            nicole "Gostei disso. Estratégia e intuição. Talvez possamos criar algo juntos."
            camille "Isso parece harmonioso. Gosto da ideia."

        "Contar uma ideia sua para um aplicativo de meditação com monetização criativa":
            $ points_camille += 1
            camille "Genial. Isso ajudaria muitos artistas sensíveis a manterem equilíbrio e renda ao mesmo tempo."

        "Perguntar como manter autenticidade artística sem se perder no mercado":
            $ points_nicole += 1
            nicole "É o dilema de todo criador. Podemos conversar mais sobre branding pessoal e valores."

    hide nicole
    hide camille
    narrator "Após a conversa inspiradora, o trio se despediu com novas ideias na mente. Nicole já fazia planos, e Camille parecia ter captado boas vibrações."
    jump capitulo2

# --- Evento Larissa e Huey ---
label evento_larissa:
    $ points_larissa += 1
    scene bg quadra with dissolve
    show larissa happy at left
    show huey neutral at right

    narrator "Larissa me convidou para uma partida de vôlei na quadra da universidade. Huey apareceu para assistir e torcer."

    larissa "Vamos aquecer antes do jogo. Preparado para suar a camisa?"

    huey "A energia aqui é contagiante. Esportes realmente elevam o espírito."

    menu:
        "Treinar saques com Larissa":
            $ points_larissa += 1
            larissa "Ótimo saque! Com prática, você vai dominar essa técnica."

        "Conversar com Huey sobre esportes e bem-estar":
            $ points_huey += 1
            huey "Atividades físicas equilibram corpo e mente. É essencial para a saúde."

        "Propor um jogo amistoso com todos":
            $ points_larissa += 1
            $ points_huey += 1
            larissa "Adoro a ideia! Vamos formar times mistos."
            huey "Será divertido e revigorante."

        "Perguntar a Larissa sobre sua rotina de treinos":
            $ points_larissa += 1
            larissa "Treino diariamente, focando em resistência e agilidade. Posso te passar algumas dicas."

        "Discutir com Huey sobre a importância da respiração durante exercícios":
            $ points_huey += 1
            huey "A respiração correta melhora o desempenho e previne lesões. É fundamental."

    hide larissa
    hide huey
    narrator "Após o jogo, nos sentamos para recuperar o fôlego e conversar. Uma tarde energizante e cheia de aprendizado."
    jump capitulo2

# --- Evento Huey e Katia ---
label evento_huey:
    $ points_huey += 1
    scene bg galeria with dissolve
    show huey neutral at left
    show katia neutral at right

    narrator "Huey me convidou para visitar uma galeria de arte contemporânea. Katia também apareceu, interessada nas exposições."

    huey "As obras aqui são provocativas, desafiando nossas percepções."

    katia "Algumas peças realmente mexem com a mente. Arte que instiga é sempre bem-vinda."

    menu:
        "Discutir interpretações das obras com Huey":
            $ points_huey += 1
            huey "Cada pessoa vê algo diferente. Essa é a beleza da arte abstrata."

        "Conversar com Katia sobre técnicas artísticas":
            $ points_katia += 1
            katia "A mistura de mídias aqui é fascinante. Inspira novas ideias para meus projetos."

        "Propor uma obra conjunta entre você, Huey e Katia":
            $ points_huey += 1
            $ points_katia += 1
            huey "Uma colaboração? Isso seria incrível."
            katia "Estou curiosa para ver no que isso daria."

        "Pedir recomendações de artistas para estudar":
            $ points_huey += 1
            huey "Te passo uma lista depois. Tem alguns que mudaram minha visão de arte."

        "Falar com Katia sobre o uso de horror e surrealismo nas obras":
            $ points_katia += 1
            katia "A tensão e o desconforto são ferramentas poderosas na narrativa visual."

    hide huey
    hide katia
    narrator "A visita terminou com boas ideias e novos olhares. A arte cumpriu seu papel: provocar, inspirar e unir."
    return

