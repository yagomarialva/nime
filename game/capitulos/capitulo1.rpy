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
            jump evento_nicole_camille
        "Assistir a um filme com Katia e Samantha":
            jump evento_katia_samantha
        "Treinar na quadra com Larissa e Huey":
            jump evento_larissa_huey

