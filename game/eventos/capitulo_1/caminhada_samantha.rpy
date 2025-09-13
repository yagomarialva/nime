# === CAMINHADA NOTURNA COM SAMANTHA ===
# Momento especial de conexão individual

label caminhada_samantha:
    scene bg campus_night with fade
    show samantha happy at center
    
    narrator "Samantha e eu saímos da festa juntos, caminhando pelas ruas iluminadas do campus."
    
    samantha "Nossa, obrigada por me acompanhar! É bom ter alguém para conversar depois de uma festa assim!"
    samantha "Estes últimos dias foram... épicos! Nunca pensei que encontraria pessoas tão incríveis!"
    
    narrator "Caminhamos em silêncio por alguns momentos, apreciando a tranquilidade da noite."
    
    samantha "Você sabe... às vezes sinto que sou muito nerd, muito entusiasmada. Mas você me mostrou que isso pode ser uma força."
    samantha "E hoje, vendo todas aquelas pessoas incríveis... sinto que finalmente encontrei pessoas que me aceitam como sou!"
    
    menu:
        "Concordar com a força do entusiasmo de Samantha":
            $ points_samantha += 3
            narrator "Concordei que o entusiasmo contagiante de Samantha era uma grande força."
            samantha "Nossa, obrigada! É reconfortante saber que alguém valoriza minha forma de ser!"
            samantha "Você me faz sentir... compreendida. É raro encontrar alguém assim!"
            
        "Comentar sobre sua paixão pelos jogos":
            $ points_samantha += 2
            narrator "Comentei sobre a paixão única de Samantha pelos jogos e RPG."
            samantha "Você realmente me entende, não é? Às vezes sinto que sou muito diferente das outras pessoas..."
            samantha "Mas com você... me sinto aceita como sou!"
            
        "Refletir sobre a conexão especial":
            $ points_samantha += 1
            narrator "Refletimos sobre a conexão especial que parecia existir entre nós."
            samantha "Há algo especial em você... algo que me faz sentir segura para ser eu mesma!"
            samantha "Obrigada por estar aqui... por me entender!"
    
    narrator "Chegamos à república de Samantha. A casa estava iluminada, com outras estudantes conversando na varanda."
    
    samantha "Bem... aqui estamos. Obrigada por me acompanhar... foi um momento especial!"
    samantha "Espero que possamos ter mais momentos assim... conversas profundas, conexões genuínas!"
    
    narrator "Samantha me olhou nos olhos por um momento, e senti algo especial passando entre nós."
    
    samantha "Até amanhã... e obrigada por ser quem você é!"
    
    narrator "Ela entrou na casa, mas antes de fechar a porta, olhou para trás com um sorriso radiante."
    
    scene bg campus_night with fade
    narrator "Caminhei de volta para casa, pensando em tudo que havia acontecido. A noite havia sido especial, e senti que algo importante havia começado..."
    
    jump capitulo1_final
