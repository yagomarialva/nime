label capitulo1:
    scene bg room with fade
    show p happy at center

    # scene bg room_day with fade
    # play music "audio/intro_theme.mp3" fadein 1.0

    p "Olá, seja bem-vindo a Cidade de Trindex "
    p "Está é a faculdade Solária , você quer conhecer alguns pontos dela comigo cara ?!"
    menu:
            "Vamos ao parque!":
                p "Ótimo! Vamos ao parque! Preciso de um lugar para inspirar meus cenarios de RPG "
                # jump park, ganha nenhum ponto 
                jump capitulo2
            "Vamos a Praia":
                p "Estava precisando pegar um sol , estou precisando de um pouco de vitamina D "
                # jump Praia , ganha nenhum ponto 
                jump capitulo2
            "Vamos a Cafeteria !":
                p " Um cafezinho seria bom agora , preciso ficar ligada , estou com um pouco de sono " 
                # jump Cafeteria , ganha nenhum ponto 
            "Vamos ao Fliperama !":
                p "Adoro fliperamas!!! , tem um jogo novo lá chamado Flinka é muito divertido você vai adorar"
                # jump Fliperama , ganha muito ponto aqui com ela 
            "Vamos a Biblioteca !!":
                p "Vamos !! Preciso pegar uns livros emprestados lá "
                # jump biblioteca, aqui ganha poucos pontos   
                
                jump capitulo2
        
    # j "Oi, tudo bem?"
    # p "Sim! Vamos começar a aventura!"

    # menu:
    #     "Vamos ao parque!":
    #         p "Ótimo! Vamos ao parque!"
    #         # jump park
    #         jump capitulo2
    #     "Vamos ao shopping!":
    #         p "Interessante, vamos ao shopping!"
    #         # jump shopping
            
        