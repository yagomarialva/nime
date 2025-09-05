# --- Evento Katia e Samantha ---
label evento_katia_samantha:
    $ points_katia += 1
    scene bg cinema with dissolve
    show katia angry at left
    show samantha neutral at right

    narrator "Katia me convidou para assistir a um filme cult no cinema da cidade. Samantha apareceu de surpresa, curiosa sobre o evento."

    katia "E-ei! Eu te convidei... não esperava que virasse um encontro em grupo." 
    katia "Hmpf. Mas tanto faz. Só não atrapalha."
    katia "N-não é como se eu estivesse esperando um encontro a dois ou qualquer coisa assim!"

    samantha "Relaxa, Katia. Eu só fiquei curiosa! Esse filme tem um enredo tão interessante... cheio de camadas filosóficas!"

    katia "Tsc... é só um filme, não precisa fazer uma tese."

    samantha "Claro que precisa! O diretor usa simbolismo freudiano o tempo inteiro!"

    narrator "O clima entre elas era... intenso, mas divertido."
    scene bg cinema_katia_samantha with dissolve
    menu:
        "Discutir simbolismos do filme com Katia":
            $ points_katia += 3
            show katia blush at left
            katia "Você percebeu a metáfora sobre a perda da identidade? Pff... não achei que você fosse notar algo assim."
            katia "Quer dizer, não que eu esteja impressionada nem nada! Hmpf."
            katia "É só que... é raro encontrar alguém que realmente entende de cinema. N-não que eu me importe com sua opinião!"

        "Conversar com Samantha sobre trilhas sonoras de filmes":
            $ points_samantha += 3
            samantha "A música realmente amplifica as emoções. Tenho uma playlist inteira só de trilhas sonoras marcantes."
            samantha "Quer que eu te envie depois? Posso até organizar por gênero!"

        "Comparar o filme com jogos de terror com Samantha":
            $ points_samantha += 3
            samantha "Sim! Muitos jogos se inspiram nesse estilo cinematográfico. Podemos jogar algo parecido depois, tipo Silent Hill 2!"
            samantha "Aliás, você sabia que esse diretor foi consultor num game japonês obscuro?"

        "Perguntar a Katia sobre diretores independentes":
            $ points_katia += 3
            show katia neutral at left
            katia "Há muitos talentos emergentes que merecem reconhecimento. Não que você conheça, mas posso te indicar alguns... se quiser."
            katia "Mas só porque eu odeio quando bons diretores passam despercebidos! Não é por sua causa ou algo assim."
            katia "É só que... você parece ter um gosto decente. N-não que eu me importe com sua opinião ou qualquer coisa!"

        "Sugerir uma maratona de filmes com ambas":
            $ points_katia += 1
            $ points_samantha += 1
            show katia blush at left
            katia "Uma maratona, hein? Só se for com filmes decentes."
            katia "N-não é como se eu estivesse animada ou qualquer coisa assim! É só que... seria interessante."
            samantha "Estou dentro! Podemos até fazer um cronograma por décadas!"

    # Cena adicional 1 – Debate no lobby
    
    narrator "Após o filme, fomos para o lobby do cinema, onde começamos a discutir nossas impressões."
    scene bg cinema_lobby_empty with dissolve
    show katia neutral at left
    show samantha neutral at right

    menu:
        "Perguntar a Katia sobre a direção do filme":
            $ points_katia += 3
            katia  "A direção foi impecável. Cada cena parecia uma pintura cuidadosamente composta..."
            katia  "Mas... acho que só eu reparei nisso. Não que eu me importe."

        "Perguntar a Samantha sobre a trilha sonora":
            $ points_samantha += 3
            samantha "A trilha foi incrível! Eu fiquei arrepiada em várias cenas."
            samantha "Tenho até a versão em vinil desse compositor. Posso te mostrar depois!"

        "Compartilhar sua interpretação do final":
            $ points_katia += 1
            $ points_samantha += 1
            katia "Huh... não é uma leitura ruim. Meio... ousada, talvez. Mas interessante."
            samantha "Amei sua análise! Posso até escrever sobre isso no meu blog!"

    # Cena adicional 2 – Café
    scene bg cinema_cafe with dissolve
    narrator "Decidimos tomar um café no cinema enquanto continuávamos a conversa."
    scene bg cinema_cafeteria with dissolve
    show katia neutral at left
    show samantha neutral at right

    menu:
        "Perguntar a Katia sobre seus filmes favoritos":
            $ points_katia += 3
            katia "Eu adoro filmes que desafiam a mente... tipo os do David Lynch."
            katia "Mas não é como se eu fosse fã de carteirinha ou algo assim. Só... gosto deles."

        "Perguntar a Samantha sobre jogos baseados em filmes":
            $ points_samantha += 3
            samantha "A maioria é ruim, mas alguns são pérolas escondidas!"
            samantha "Quer jogar comigo qualquer dia desses? Eu faço um ranking dos melhores."

        "Sugerir criar um curta-metragem juntos":
            $ points_katia += 1
            $ points_samantha += 1
            katia "Isso seria... legal. Desde que não vire uma comédia boba, claro!"
            samantha "Eu posso cuidar da trilha e da edição! Já tô animada!"

    # Cena adicional 3 – Exposição
    hide katia
    hide samantha
    scene bg cinema_exhibition with dissolve
    narrator "Exploramos uma pequena exposição de pôsteres de filmes clássicos no cinema."
    scene bg cinema_lobby_empty with dissolve
    show katia neutral at left
    show samantha neutral at right

    menu:
        "Perguntar a Katia sobre o design dos pôsteres":
            $ points_katia += 3
            katia "Eles têm personalidade, sabe? Minimalistas, mas intensos. Como deveria ser."
            katia "Hoje em dia tudo parece feito no piloto automático..."

        "Perguntar a Samantha sobre a evolução do marketing de filmes":
            $ points_samantha += 3
            samantha "Hoje o marketing é quase uma ciência! Adoro estudar isso. É tipo manipulação social, mas artística!"
            samantha "Já viu os trailers dos anos 70? São uma viagem."

        "Comentar sobre como os pôsteres influenciam a percepção do público":
            $ points_katia += 1
            $ points_samantha += 1
            katia "Sim, um pôster bem feito já te prepara pro tipo de experiência que vem."
            samantha "É como um teaser visual. Eu tenho até uma coleção digital deles!"

    # Cena adicional 4 – Fliperama
    scene bg cinema_arcade with dissolve
    narrator "Passamos por uma área de fliperamas no cinema, e Samantha ficou animada."
    show katia neutral at left
    show samantha neutral at right

    menu:
        "Desafiar Samantha para um jogo de terror no fliperama":
            $ points_samantha += 3
            samantha "Você vai se arrepender! Eu platinei todos os Resident Evil."
            samantha "Prepare-se pra levar susto e perder feio."

        "Perguntar a Katia se ela gosta de jogos antigos":
            $ points_katia += 3
            katia "Não sou de jogar, mas esses jogos têm... charme. Meio nostálgico."
            katia "Além disso, ver você se empolgando tanto é... engraçado."

        "Sugerir um torneio entre os três":
            $ points_katia += 1
            $ points_samantha += 1
            katia "Sério? Aposto que vou te vencer só com sorte."
            samantha "Mal posso esperar. Já me sinto no modo competitivo!"

    # Cena adicional 5 – Saída
    scene bg cinema with dissolve
    narrator "Ao final da noite, saímos do cinema e nos despedimos."
    show katia neutral at left
    show samantha neutral at right

    menu:
        "Agradecer a Katia pelo convite":
            $ points_katia += 3
            show katia blush at left
            katia  "Tsc... eu que agradeço por ter vindo. Mas não se acostuma, tá?"
            katia "N-não é como se eu tivesse gostado da sua companhia ou qualquer coisa assim!"
            katia "É só que... foi menos chato do que eu esperava. Nada mais que isso!"

        "Agradecer a Samantha por se juntar a vocês":
            $ points_samantha += 3
            samantha "Foi ótimo! Obrigada por me incluir. Vocês são divertidos."

        "Sugerir um próximo encontro para assistir outro filme":
            $ points_katia += 1
            $ points_samantha += 1
            show katia blush at left
            katia "Se for um filme decente... talvez eu aceite."
            katia "N-não é como se eu estivesse ansiosa para sair com você novamente ou qualquer coisa assim!"
            katia "É só que... você tem um gosto razoável. Nada mais que isso!"
            samantha "Vamos sim! Já quero montar um cronograma de filmes cult."

    hide katia
    hide samantha
    narrator "A noite foi cheia de conversas, provocações e risadas. O tipo de encontro que deixa saudade — e vontade de repetir."
    jump capitulo1_final