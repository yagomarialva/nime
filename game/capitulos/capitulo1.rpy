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

    menu:
        "Conversar com Nicole sobre planejamento financeiro":
            $ points_nicole += 1
            show nicole neutral at left
            nicole "Ah, então você também se interessa por estratégias? Podemos trocar ideias depois!"
            narrator "Nicole pareceu animada com a conversa."
            hide nicole

        "Perguntar a Katia sobre filmes de terror":
            $ points_katia += 1
            show katia neutral at left
            katia "Finalmente alguém com bom gosto. Vou te mostrar uns filmes que vão te deixar sem dormir por uma semana."
            narrator "Katia sorriu de canto, mas parecia genuinamente interessada."
            hide katia

        "Falar com Larissa sobre esportes":
            $ points_larissa += 1
            show larissa happy at left
            larissa "Você joga vôlei? Se não, eu posso te ensinar! Vai ser divertido!"
            narrator "Larissa parecia cheia de energia e pronta para qualquer coisa."
            hide larissa

        "Discutir arte com Aline":
            $ points_huey += 1
            show huey neutral at left
            huey "Você também gosta de arte expressionista? Que incrível! Precisamos explorar isso juntos."
            narrator "Aline começou a rabiscar algo no caderno enquanto conversávamos."
            hide huey

        "Aceitar o convite de Samantha para jogar RPG":
            $ points_samantha += 1
            show samantha happy at left
            samantha "Sério?! Isso vai ser épico! Já tenho algumas ideias para o seu personagem."
            narrator "Samantha parecia radiante com a ideia de ter mais alguém no grupo."
            hide samantha

        "Perguntar a Camille sobre energias e meditação":
            $ points_camille += 1
            show camille neutral at left
            camille "Ah, você também sente isso? Podemos meditar juntos algum dia. Vai ser uma experiência única."
            narrator "Camille parecia tranquila e conectada com o ambiente ao redor."
            hide camille

    narrator "Após as conversas, decidimos ir até o café da universidade. As interações fluíam naturalmente, e eu sentia que algo especial estava começando a se formar."

    return
