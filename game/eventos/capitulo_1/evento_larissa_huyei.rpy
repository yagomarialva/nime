# === EVENTO LARISSA E HUEY - MASTER EDITION ===
# Tema: A Estética do Esforço (Competição vs Arte)

label evento_larissa_huey:
    $ points_larissa += 1
    
    # Cenário definido em scenarios.rpy
    scene bg quadra_volei with dissolve

    # AÇÃO IMEDIATA: Som e movimento
    narrator "O som de uma mão golpeando o couro ecoou pelo ginásio como um tiro seco."
    narrator "*PÁ!*"

    # Usando o sprite correto 'larissa voley' definido em personagens.rpy
    show larissa voley at left
    
    # Larissa em ação (Show, Don't Tell)
    larissa "49... 50! Mais uma série! O suor é só a fraqueza saindo do corpo!"
    
    narrator "A garota na quadra parecia uma máquina. Ela saltava e cortava com uma precisão assustadora, totalmente sozinha."
    
    # O MC observa alguém observando
    narrator "Mas ela não era a única ali. Na arquibancada, escondida atrás de um pilar..."

    # Usando sprite correto 'huey neutral'
    show huey neutral at right
    
    # Huey murmurando, focada no desenho
    huey "A curva do deltoide na extensão máxima... fascinante. A tensão dinâmica é perfeita."
    
    # O MC intervém
    mc "Ei, você não deveria pedir permissão antes de usar alguém como modelo vivo?"
    
    # Huey se assusta levemente (usando 'happy' pois não há 'surprised')
    show huey happy
    huey "Oh. Olá, [nome]. A permissão alteraria a pose. A autoconsciência mata a autenticidade do movimento."
    
    # Larissa percebe os dois e fica irritada ('larissa angry' existe)
    show larissa angry
    larissa "EI! VOCÊS DOIS! Estão atrapalhando meu foco! Se não vieram treinar, saiam da quadra!"
    
    mc "Calma, Larissa, a gente só estava..."
    
    larissa "Calma é para quem perde. Eu tenho um campeonato estadual em três semanas e minha recepção ainda está 0.5 segundos lenta."
    
    # Huey muda para tom mais sério/neutro
    show huey neutral
    huey "Na verdade... sua recepção está lenta porque você tensiona o ombro esquerdo antes de pular. Quebra a simetria."
    
    # O Choque: A artista dá uma dica técnica.
    # Como não tem 'surprised', usamos 'neutral' para mostrar que ela parou de gritar
    show larissa neutral
    
    larissa "O quê? Quem é você para falar da minha técnica? Alguma treinadora nova?"
    
    huey "Sou Huey. Apenas observo as linhas. E sua linha de força está... truncada."
    huey "Olhe aqui no esboço."
    
    # Larissa olha o desenho.
    narrator "Larissa marchou até a arquibancada, pronta para brigar, mas parou ao ver o caderno de Huey."
    
    # Usando 'blush' para mostrar que ela ficou desconcertada/impressionada
    show larissa blush
    larissa "Isso... sou eu? Por que estou parecendo uma... estátua grega?"
    
    huey "Porque o esforço é belo. Mas veja aqui... o ombro. Está rígido no desenho. O corpo não mente."
    
    # === MENU DE ESCOLHA ===
    menu:
        "Validar a observação da Huey (Apoiar Arte/Técnica)":
            $ points_huey += 1
            
            mc "Ela tem um ponto, Larissa. Às vezes quem está de fora vê vícios de postura que você não percebe."
            
            show larissa neutral
            larissa "Hmpf. Deixe-me ver isso direito..."
            larissa "Talvez... se eu relaxar o trapézio... Tsc. Não é que faz sentido?"

        "Elogiar a força da Larissa (Apoiar Esporte)":
            $ points_larissa += 1
            
            mc "Não liga pro desenho. Sua explosão muscular estava incrível, deu pra ouvir o estalo da bola daqui."
            
            show larissa happy
            larissa "Exato! Força bruta e repetição resolvem qualquer problema de postura."
            
            show huey sad
            huey "A força sem forma é apenas violência. Mas... a energia é inegável."

        "Sugerir uma colaboração (União)":
            $ points_larissa += 1
            $ points_huey += 1
            
            mc "Larissa, use o desenho como replay instantâneo. Huey, continue desenhando para acharmos os erros."
            
            show huey happy
            huey "Seria... um estudo de anatomia em tempo real. Aceito."
            
            show larissa happy
            larissa "Usar arte para ganhar medalha? ...Tsc. Se me ajudar a vencer, eu topo."

    # === TRANSIÇÃO PARA CAFETERIA ===
    scene bg cafeteria with fade
    
    narrator "Trinta minutos de saques, esboços e correções depois..."
    
    show larissa happy at left
    show huey happy at right
    
    larissa "Aquele último saque foi perfeito! Eu senti a fluidez que você falou!"
    
    huey "E o desenho ficou... dinâmico. Você tem uma energia cinética incrível, Larissa."
    
    mc "Viu? Arte e Esporte não são inimigos."
    
    show larissa blush
    larissa "É... acho que você não é só uma garota estranha com um caderno, afinal."
    
    huey "E você não é apenas músculos em movimento. Há uma dança na sua determinação."
    
    # Fechamento
    narrator "Larissa virou uma garrafa de água inteira, enquanto Huey sombreava o último desenho. Havia um respeito silencioso nascendo ali."

    # Memória compartilhada
    $ add_shared_memory("sport_art_connection", ["larissa", "huey"], "O dia em que corrigimos um saque de vôlei usando desenho artístico.")

    return