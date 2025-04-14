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
    narrator "Com quem você passará a tarde?"
    # Escolha de evento
    menu:
        "Nicole e Camille no café":
            jump evento_nicole
        "Katia e Samantha no cinema":
            jump evento_katia
        "Larissa e Huey na quadra":
            jump evento_larissa
        "Huey e Katia na galeria de arte":
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

# --- Evento Katia e Samantha ---
label evento_katia:
    $ points_katia += 1
    scene bg cinema with dissolve
    show katia neutral at left
    show samantha happy at right

    narrator "Katia me convidou para assistir a um filme cult no cinema da cidade. Samantha apareceu de surpresa, curiosa sobre o evento."

    katia "Este é um clássico do terror psicológico. Prepare-se para uma experiência intensa."

    samantha "Uau, adoro filmes que mexem com a mente! Posso me juntar a vocês?"

    menu:
        "Discutir simbolismos do filme com Katia":
            $ points_katia += 1
            katia "Você percebeu a metáfora sobre a perda da identidade? Poucos notam isso."

        "Conversar com Samantha sobre trilhas sonoras de filmes":
            $ points_samantha += 1
            samantha "A música realmente amplifica as emoções. Tenho algumas playlists que combinam com esse clima."

        "Comparar o filme com jogos de terror com Samantha":
            $ points_samantha += 1
            samantha "Sim! Muitos jogos se inspiram nesse estilo cinematográfico. Podemos jogar algo parecido depois."

        "Perguntar a Katia sobre diretores independentes":
            $ points_katia += 1
            katia "Há muitos talentos emergentes que merecem reconhecimento. Posso te indicar alguns."

        "Sugerir uma maratona de filmes com ambas":
            $ points_katia += 1
            $ points_samantha += 1
            katia "Uma ótima ideia. Podemos selecionar uma temática específica."
            samantha "Estou dentro! Vai ser divertido."

    # Cena adicional 1
    scene bg cinema_lobby with dissolve
    narrator "Após o filme, fomos para o lobby do cinema, onde começamos a discutir nossas impressões."
    show katia neutral at left
    show samantha happy at right
    menu:
        "Perguntar a Katia sobre a direção do filme":
            $ points_katia += 1
            katia "A direção foi impecável. Cada cena parecia uma pintura cuidadosamente composta."
        "Perguntar a Samantha sobre a trilha sonora":
            $ points_samantha += 1
            samantha "A trilha sonora foi incrível! Ela realmente intensificou as emoções do filme."
        "Compartilhar sua interpretação do final":
            $ points_katia += 1
            $ points_samantha += 1
            katia "Interessante... nunca tinha pensado por esse ângulo."
            samantha "Adorei sua perspectiva! Faz muito sentido."

    # Cena adicional 2
    scene bg cinema_cafe with dissolve
    narrator "Decidimos tomar um café no cinema enquanto continuávamos a conversa."
    show katia neutral at left
    show samantha happy at right
    menu:
        "Perguntar a Katia sobre seus filmes favoritos":
            $ points_katia += 1
            katia "Eu adoro filmes que desafiam a mente, como os de David Lynch."
        "Perguntar a Samantha sobre jogos baseados em filmes":
            $ points_samantha += 1
            samantha "Existem alguns jogos incríveis inspirados em filmes. Posso te mostrar depois!"
        "Sugerir criar um curta-metragem juntos":
            $ points_katia += 1
            $ points_samantha += 1
            katia "Isso seria incrível! Já estou cheia de ideias."
            samantha "Eu adoraria ajudar com a trilha sonora ou até mesmo atuar!"

    # Cena adicional 3
    scene bg cinema_exhibition with dissolve
    narrator "Exploramos uma pequena exposição de pôsteres de filmes clássicos no cinema."
    show katia neutral at left
    show samantha happy at right
    menu:
        "Perguntar a Katia sobre o design dos pôsteres":
            $ points_katia += 1
            katia "Os pôsteres antigos têm uma estética única. Eles realmente capturam a essência do filme."
        "Perguntar a Samantha sobre a evolução do marketing de filmes":
            $ points_samantha += 1
            samantha "Hoje em dia, o marketing é tão importante quanto o próprio filme. É fascinante!"
        "Comentar sobre como os pôsteres influenciam a percepção do público":
            $ points_katia += 1
            $ points_samantha += 1
            katia "Exatamente! Um bom pôster pode fazer toda a diferença."
            samantha "Concordo! É como a capa de um livro, só que para filmes."

    # Cena adicional 4
    scene bg cinema_arcade with dissolve
    narrator "Passamos por uma área de fliperamas no cinema, e Samantha ficou animada."
    show katia neutral at left
    show samantha happy at right
    menu:
        "Desafiar Samantha para um jogo de terror no fliperama":
            $ points_samantha += 1
            samantha "Você vai se arrepender de me desafiar! Eu sou ótima nesses jogos."
        "Perguntar a Katia se ela gosta de jogos antigos":
            $ points_katia += 1
            katia "Não sou muito de jogar, mas adoro a estética dos jogos retrô."
        "Sugerir um torneio entre os três":
            $ points_katia += 1
            $ points_samantha += 1
            katia "Por que não? Pode ser divertido."
            samantha "Estou dentro! Prepare-se para perder."

    # Cena adicional 5
    scene bg cinema_exit with dissolve
    narrator "Ao final da noite, saímos do cinema e nos despedimos."
    show katia neutral at left
    show samantha happy at right
    menu:
        "Agradecer a Katia pelo convite":
            $ points_katia += 1
            katia "Foi um prazer. Espero que possamos fazer isso de novo."
        "Agradecer a Samantha por se juntar a vocês":
            $ points_samantha += 1
            samantha "Eu adorei! Vamos repetir isso em breve."
        "Sugerir um próximo encontro para assistir outro filme":
            $ points_katia += 1
            $ points_samantha += 1
            katia "Ótima ideia. Já tenho alguns filmes em mente."
            samantha "Com certeza! Mal posso esperar."

    hide katia
    hide samantha
    narrator "A noite foi cheia de conversas interessantes e momentos divertidos. Uma experiência que ficará na memória."
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

