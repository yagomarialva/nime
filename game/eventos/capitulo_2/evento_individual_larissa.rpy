label evento_individual_larissa:
    scene bg park with fade
    show larissa happy at center

    narrator "Larissa me convidou para explorar o parque. Ela parecia animada, com um sorriso contagiante e uma energia que era difícil de ignorar."

    larissa "Que bom que você veio! Eu precisava de uma desculpa para sair e me mexer um pouco. Vamos aproveitar o dia!"

    narrator "Com Larissa liderando o caminho, eu sabia que seria uma tarde cheia de movimento e diversão."

    menu:
        "Perguntar o que ela gosta de fazer ao ar livre":
            $ points_larissa += 1
            larissa "Ah, qualquer coisa que envolva movimento! Caminhar, correr, jogar... Eu só preciso estar ativa."
            narrator "Larissa falou com entusiasmo, mostrando sua paixão por atividades físicas."

        "Comentar sobre a energia positiva dela":
            $ points_larissa += 1
            larissa "Obrigada! Acho que a energia vem de fazer o que eu amo. E estar ao ar livre ajuda muito."
            narrator "Larissa parecia feliz com o elogio, seu sorriso ficando ainda maior."

        "Sugerir que vocês explorem uma trilha juntos":
            $ points_larissa += 1
            larissa "Ótima ideia! Vamos ver o que encontramos por lá."
            narrator "Larissa parecia animada com a ideia de explorar o parque."

    # Cena 1: Caminhando pelo parque
    scene bg park_path with dissolve
    narrator "Começamos a caminhar pelo parque, conversando sobre esportes, vida e tudo mais."

    larissa "Esportes são mais do que apenas competição para mim. Eles são uma forma de me conectar com as pessoas e comigo mesma."

    menu:
        "Perguntar como ela começou a se interessar por esportes":
            $ points_larissa += 1
            larissa "Desde pequena! Eu sempre adorei correr e jogar com meus amigos. É algo que sempre fez parte de mim."
            narrator "Larissa falou com paixão sobre sua jornada no mundo dos esportes."

        "Discutir como esportes podem unir as pessoas":
            $ points_larissa += 1
            larissa "Exatamente! É incrível como um jogo pode quebrar barreiras e criar conexões."
            narrator "Larissa parecia animada com minha perspectiva."

        "Sugerir que ela organize um evento esportivo para o grupo":
            $ points_larissa += 1
            larissa "Isso seria incrível! Já estou pensando em algumas ideias."
            narrator "Larissa parecia empolgada com a ideia de reunir todos para uma atividade esportiva."

    # Cena 2: Jogando no parque
    scene bg park_field with dissolve
    narrator "Encontramos um campo aberto no parque, e Larissa sugeriu que jogássemos algo para nos divertir."

    larissa "Vamos jogar algo simples, só para nos mexermos um pouco. Que tal?"

    menu:
        "Aceitar e jogar com entusiasmo":
            $ points_larissa += 1
            larissa "Isso aí! É assim que se faz. Você tem talento!"
            narrator "Larissa parecia impressionada com minha disposição e habilidade."

        "Perguntar sobre sua rotina de treinos":
            $ points_larissa += 1
            larissa "Eu treino quase todos os dias. É uma mistura de força, resistência e diversão!"
            narrator "Larissa explicou sua rotina com entusiasmo, mostrando o quanto ela amava o que fazia."

        "Sugerir que vocês criem um jogo improvisado":
            $ points_larissa += 1
            larissa "Adorei a ideia! Vamos inventar algo divertido."
            narrator "Larissa parecia animada com a ideia de criar algo novo juntos."

    # Cena 3: Descanso no parque
    scene bg park_bench with dissolve
    narrator "Depois de nos movimentarmos bastante, decidimos descansar em um banco à sombra de uma árvore."

    larissa "Sabe, momentos como este me lembram por que eu amo tanto estar ativa. É uma sensação de liberdade."

    menu:
        "Elogiar sua paixão e dedicação":
            $ points_larissa += 1
            larissa "Obrigada! Isso significa muito para mim. Eu só quero inspirar as pessoas a se moverem também."
            narrator "Larissa parecia tocada pelo elogio, seu sorriso ficando ainda mais brilhante."

        "Perguntar como ela equilibra esportes e estudos":
            $ points_larissa += 1
            larissa "Não é fácil, mas quando você ama o que faz, encontra um jeito. Organização é a chave."
            narrator "Larissa explicou como conseguia equilibrar suas paixões com suas responsabilidades."

        "Sugerir que ela compartilhe sua paixão com mais pessoas":
            $ points_larissa += 1
            larissa "Eu adoraria! Talvez eu possa começar um clube ou algo assim."
            narrator "Larissa parecia animada com a ideia de inspirar mais pessoas a se envolverem com esportes."

    # Cena 4: Finalizando o encontro
    scene bg park_exit with dissolve
    narrator "Depois de algum tempo, Larissa olhou para o céu e respirou fundo, parecendo completamente em paz."

    larissa "Obrigada por passar esse tempo comigo. Foi ótimo ter alguém para compartilhar isso."

    menu:
        "Agradecer a Larissa pela tarde divertida":
            $ points_larissa += 1
            larissa "Ah, não precisa agradecer! Foi incrível ter você aqui."

        "Elogiar sua energia e entusiasmo":
            $ points_larissa += 1
            larissa "Obrigada! Eu tento sempre trazer energia positiva para tudo que faço."

        "Sugerir que vocês façam isso novamente no futuro":
            $ points_larissa += 1
            larissa "Com certeza! Já estou pensando em outras coisas que podemos fazer juntos."

    hide larissa
    narrator "Passei uma tarde cheia de energia e diversão com Larissa, aprendendo mais sobre sua paixão por esportes e sua visão positiva da vida. Foi uma experiência que certamente ficará na memória."
    return