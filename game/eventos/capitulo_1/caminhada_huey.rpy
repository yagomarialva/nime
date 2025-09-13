# === CAMINHADA NOTURNA COM HUEY ===
# Momento especial de conexão individual

label capitulo1_caminhada_huey:
    scene bg campus_night with fade
    show huey gentle at center
    
    narrator "Huey e eu saímos da festa juntos, caminhando pelas ruas iluminadas do campus."
    
    huey "Obrigada por me acompanhar... é bom ter alguém para conversar depois de uma festa assim."
    huey "Estes últimos dias foram... inspiradores. Nunca pensei que encontraria pessoas que realmente entendessem de arte."
    
    narrator "Caminhamos em silêncio por alguns momentos, apreciando a tranquilidade da noite."
    
    huey "Você sabe... às vezes sinto que sou muito sensível, muito contemplativa. Mas você me mostrou que isso pode ser uma força."
    huey "E hoje, vendo todas aquelas pessoas incríveis... sinto que finalmente encontrei pessoas que me compreendem."
    
    menu:
        "Concordar com a força da sensibilidade de Huey":
            $ points_huey += 3
            narrator "Concordei que a sensibilidade artística de Huey era uma grande força."
            huey "Obrigada... é reconfortante saber que alguém valoriza minha forma de perceber o mundo."
            huey "Você me faz sentir... compreendida. É raro encontrar alguém assim."
            
        "Comentar sobre sua visão artística única":
            $ points_huey += 2
            narrator "Comentei sobre a visão artística única de Huey."
            huey "Você realmente me vê, não é? Às vezes sinto que vejo as coisas de forma diferente..."
            huey "Mas com você... me sinto aceita como sou."
            
        "Refletir sobre a conexão especial":
            $ points_huey += 1
            narrator "Refletimos sobre a conexão especial que parecia existir entre nós."
            huey "Há algo especial em você... algo que me faz sentir segura para ser eu mesma."
            huey "Obrigada por estar aqui... por me entender."
    
    narrator "Chegamos à república de Huey. A casa estava iluminada, com outras estudantes conversando na varanda."
    
    huey "Bem... aqui estamos. Obrigada por me acompanhar... foi um momento especial."
    huey "Espero que possamos ter mais momentos assim... conversas profundas, conexões genuínas."
    
    narrator "Huey me olhou nos olhos por um momento, e senti algo especial passando entre nós."
    
    huey "Até amanhã... e obrigada por ser quem você é."
    
    narrator "Ela entrou na casa, mas antes de fechar a porta, olhou para trás com um sorriso tímido."
    
    scene bg campus_night with fade
    narrator "Caminhei de volta para casa, pensando em tudo que havia acontecido. A noite havia sido especial, e senti que algo importante havia começado..."
    
    jump capitulo1_final
