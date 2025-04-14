label capitulo1:
    
    scene bg room with fade
    show p happy at center

    # play music "audio/intro_theme.mp3" fadein 1.0

    p "Olá, seja bem-vindo à Cidade de Trindex."
    p "Esta é a faculdade Solária. Você quer conhecer alguns pontos dela comigo, cara?!"

    menu:
        "Vamos ao parque!":
            p "Ótimo! Vamos ao parque! Preciso de um lugar para inspirar meus cenários de RPG."
            # jump park, ganha nenhum ponto 
            jump capitulo2

        "Vamos à praia":
            p "Estava precisando pegar um sol. Estou precisando de um pouco de vitamina D."
            # jump Praia, ganha nenhum ponto 
            jump capitulo2

        "Vamos à cafeteria!":
            p "Um cafezinho seria bom agora. Preciso ficar ligada, estou com um pouco de sono."
            # jump Cafeteria, ganha nenhum ponto 
            jump capitulo2

        "Vamos ao fliperama!":
            # p "Adoro fliperamas!!! Tem um jogo novo lá chamado Flinka. É muito divertido, você vai adorar."
            # jump Fliperama, ganha muito ponto aqui com ela 
            $ points_samantha += 3
            p "Adoro fliperamas!!! Tem um jogo novo lá chamado Flinka. É muito divertido, você vai adorar."
            if points_samantha >= 3:
                p "Samantha sorri para você como se quisesse dizer algo mais."
                # jump cena_romantica_samantha
            else:
                p "Samantha fala de forma amigável, mas mantém certa distância."
            # jump biblioteca, aqui ganha poucos pontos
            jump capitulo2

        "Vamos à biblioteca!!":
            $ points_samantha += 1
            p "Vamos!! Preciso pegar uns livros emprestados lá."
            if points_samantha >= 3:
                p "Samantha sorri para você como se quisesse dizer algo mais."
                # jump cena_romantica_samantha
            else:
                p "Samantha fala de forma amigável, mas mantém certa distância."
            # jump biblioteca, aqui ganha poucos pontos
            jump capitulo2
