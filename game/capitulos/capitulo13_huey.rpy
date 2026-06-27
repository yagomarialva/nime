label capitulo13_huey:
    if status_huey == "ruina":
        scene bg quintal with fade
        narrator "A fumaça preta cobria o quintal da Rua Aurora."
        narrator "Huey fez uma fogueira no meio da noite e queimou todas as suas telas coloridas e mágicas, junto com as tintas."
        narrator "Eu tentei impedi-la, mas a frieza nos olhos dela era letal."
        narrator "Ela trancou seu ateliê, mudou de curso para Contabilidade Básica e cortou qualquer contato emocional comigo. A criadora de magia estava morta."
        scene black with fade
        centered "{b}FIM DE JOGO - CAMINHO RUÍM (Huey){/b}"
        return
        
    elif status_huey == "amizade":
        scene bg atelie_huey with fade
        narrator "O ateliê não estava mais sujo ou colorido."
        show huey neutral at center
        narrator "Huey estava pintando um retrato hiper-realista, geometricamente perfeito e absurdamente entediante de um cesto de maçãs."
        huey "A galeria nacional disse que vai comprar minha obra se eu mantiver esse padrão acadêmico."
        mc "E você sente o quê quando pinta isso?"
        huey "Nada. É um processo repetitivo de preenchimento de pixels."
        narrator "Ela continuou pintando mecanicamente. A magia das cores que existia na mente dela nunca mais voltaria."
        call end_of_chapter_validation("capitulo14")
        
    elif status_huey == "romance":
        scene bg muro_campus with fade
        narrator "As pessoas estavam parando nos corredores do campus, maravilhadas."
        show huey happy at center
        narrator "Huey, com as roupas respingadas de todas as cores possíveis, havia montado uma 'Galeria de Guerrilha'."
        narrator "Ela pendurou suas telas vibrantes, caóticas e cheias de magia nos muros da faculdade."
        huey "Dezenas de pessoas me perguntaram sobre o meu processo. Um grupo de teatro pediu pra eu pintar os cenários deles."
        show huey blush
        mc "E como o seu coração tá processando isso tudo?"
        huey "As emoções estão vazando do meu sistema de controle. É uma falha maravilhosa."
        narrator "Ela se inclinou na ponta dos pés. Antes de me beijar, ela encostou o dedo sujo de tinta vermelha na ponta do meu nariz."
        huey "Obrigada por colorir o meu mundo de novo."
        narrator "O beijo teve gosto de tinta e de arte pulsando nas veias."
        call end_of_chapter_validation("capitulo14")
