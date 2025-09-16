# === CAMINHADA NOTURNA COM CAMILLE ===
# Momento especial de conexão individual

label capitulo1_caminhada_camille:
    scene bg campus_night with fade
    show camille gentle at center
    
    narrator "Camille e eu saímos da festa juntos, caminhando pelas ruas iluminadas do campus."
    
    camille "Obrigada por me acompanhar... é bom ter alguém para conversar depois de uma festa assim."
    camille "Estes últimos dias foram... transformadores. Nunca pensei que encontraria pessoas que realmente entendessem de espiritualidade."
    
    narrator "Caminhamos em silêncio por alguns momentos, apreciando a tranquilidade da noite."
    
    camille "Você sabe... às vezes sinto que sou muito espiritual, muito conectada com energias. Mas você me mostrou que isso pode ser uma força."
    camille "E hoje, vendo todas aquelas pessoas incríveis... sinto que finalmente encontrei pessoas que me compreendem."
    
    menu:
        "Concordar com a força da espiritualidade de Camille":
            $ points_camille += 3
            narrator "Concordei que a espiritualidade de Camille era uma grande força."
            camille "Obrigada... é reconfortante saber que alguém valoriza minha conexão com o universo."
            camille "Você me faz sentir... compreendida. É raro encontrar alguém assim."
            
        "Comentar sobre sua energia serena":
            $ points_camille += 2
            narrator "Comentei sobre a energia serena e espiritual de Camille."
            camille "Você realmente sente a energia, não é? Às vezes sinto que percebo as coisas de forma diferente..."
            camille "Mas com você... me sinto aceita como sou."
            
        "Refletir sobre a conexão especial":
            $ points_camille += 1
            narrator "Refletimos sobre a conexão especial que parecia existir entre nós."
            camille "Há algo especial em você... algo que me faz sentir segura para ser eu mesma."
            camille "Obrigada por estar aqui... por me entender."
    
    narrator "Chegamos à república de Camille. A casa estava iluminada, com outras estudantes conversando na varanda."
    
    camille "Bem... aqui estamos. Obrigada por me acompanhar... foi um momento especial."
    camille "Espero que possamos ter mais momentos assim... conversas profundas, conexões genuínas."
    
    narrator "Camille me olhou nos olhos por um momento, e senti algo especial passando entre nós."
    
    camille "Até amanhã... e obrigada por ser quem você é."
    
    narrator "Ela entrou na casa, mas antes de fechar a porta, olhou para trás com um sorriso sereno."
    
    scene bg campus_night with fade
    narrator "Caminhei de volta para casa, pensando em tudo que havia acontecido. A noite havia sido especial, e senti que algo importante havia começado..."
    
    jump capitulo1_quarta_escolha
