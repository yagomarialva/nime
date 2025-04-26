label evento_larissa_huey_esporte:
    scene bg quadra_volei with fade
    show larissa voley at left
    show huey neutral at right

    narrator "Larissa me convidou para participar de uma atividade esportiva criativa na quadra de vôlei. Huey também apareceu, curioso para ver como seria."

    larissa "Ei! Pensei em algo diferente hoje. Que tal um jogo de vôlei com algumas regras criativas? Vai ser divertido!"

    huey "Eu não sou muito bom em esportes, mas estou curioso para ver como isso vai funcionar."

    narrator "Larissa parecia animada para liderar a atividade, enquanto Huey estava mais interessado em observar e participar de forma descontraída."

    menu:
        "Aceitar a ideia de Larissa e jogar com entusiasmo":
            $ points_larissa += 1
            larissa "Isso aí! Vamos nos divertir e nos mexer um pouco!"
            narrator "Larissa ficou animada com minha disposição e começou a explicar as regras criativas do jogo."

        "Perguntar a Huey o que ele acha da ideia":
            $ points_huey += 1
            huey "Eu acho interessante. É uma forma de tornar o esporte mais acessível para todos."
            narrator "Huey parecia gostar da ideia de um jogo mais inclusivo e criativo."

        "Sugerir uma abordagem mais colaborativa para o jogo":
            $ points_larissa += 1
            $ points_huey += 1
            larissa "Boa ideia! Podemos trabalhar em equipe para criar algo único."
            huey "Isso soa ótimo. Vamos tentar!"

    # Cena 1: Início do jogo
    scene bg quadra_volei with dissolve
    narrator "Começamos o jogo com as regras criativas de Larissa. Era uma mistura de vôlei tradicional com desafios inesperados, como acertar alvos no chão ou passar a bola de formas inusitadas."

    menu:
        "Tentar acertar os alvos com precisão":
            $ points_larissa += 1
            larissa "Uau! Você tem uma boa mira. Continue assim!"
            narrator "Larissa ficou impressionada com minha habilidade e me incentivou a continuar."

        "Ajudar Huey a se sentir mais confortável no jogo":
            $ points_huey += 1
            huey "Obrigado por me ajudar. Isso está sendo mais divertido do que eu esperava."
            narrator "Huey parecia mais à vontade e começou a se envolver mais no jogo."

        "Sugerir uma nova regra criativa para o jogo":
            $ points_larissa += 1
            $ points_huey += 1
            larissa "Adorei sua ideia! Vamos adicionar isso ao jogo."
            huey "Isso torna tudo ainda mais interessante. Boa sugestão!"

    # Cena 2: Intervalo
    scene bg quadra_volei with dissolve
    narrator "Fizemos uma pausa para descansar e conversar sobre a atividade."

    menu:
        "Perguntar a Larissa sobre sua paixão por esportes":
            $ points_larissa += 1
            larissa "Esportes sempre foram minha forma de me expressar e me conectar com as pessoas. É algo que amo fazer."
            narrator "Larissa falou com entusiasmo sobre sua paixão, e foi inspirador ouvir."

        "Conversar com Huey sobre a energia do ambiente":
            $ points_huey += 1
            huey "A energia aqui é incrível. É como se todos estivessem conectados de alguma forma."
            narrator "Huey parecia estar em sintonia com o ambiente e apreciava a experiência."

        "Sugerir uma reflexão sobre como o esporte une as pessoas":
            $ points_larissa += 1
            $ points_huey += 1
            larissa "Com certeza! Esportes têm esse poder de unir as pessoas."
            huey "É verdade. É uma forma de criar conexões de maneira natural."

    # Cena 3: Final do jogo
    scene bg quadra_volei with dissolve
    narrator "Terminamos o jogo com risadas e um sentimento de realização. Larissa parecia satisfeita com a atividade, e Huey estava mais relaxado e envolvido."

    menu:
        "Agradecer a Larissa pela ideia criativa":
            $ points_larissa += 1
            larissa "Fico feliz que você tenha gostado! Vamos fazer isso mais vezes."
            narrator "Larissa parecia animada para organizar mais atividades no futuro."

        "Agradecer a Huey por participar e compartilhar suas reflexões":
            $ points_huey += 1
            huey "Obrigado por me incluir. Foi uma experiência única e divertida."
            narrator "Huey parecia grato por ter participado e se conectado mais com o grupo."

        "Sugerir uma próxima atividade para o grupo":
            $ points_larissa += 1
            $ points_huey += 1
            larissa "Ótima ideia! Podemos planejar algo ainda mais criativo."
            huey "Estou dentro. Mal posso esperar para ver o que vamos fazer."

    hide larissa
    hide huey
    narrator "A atividade esportiva foi um sucesso, fortalecendo os laços entre nós e criando memórias divertidas. Mal posso esperar para a próxima aventura com Larissa e Huey."
    jump terceiro_dia_escolha
