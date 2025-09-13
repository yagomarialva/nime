# === CAMINHADA NOTURNA COM NICOLE ===
# Momento especial de conexão individual

label caminhada_nicole:
    scene bg campus_night with fade
    show nicole neutral at center
    
    narrator "Nicole e eu saímos da festa juntos, caminhando pelas ruas iluminadas do campus."
    
    nicole "Obrigada por me acompanhar... é bom ter alguém para conversar depois de uma festa assim."
    nicole "Estes últimos dias foram... especiais. Nunca pensei que encontraria pessoas que realmente me entendessem."
    
    narrator "Caminhamos em silêncio por alguns momentos, apreciando a tranquilidade da noite."
    
    nicole "Você sabe... às vezes sinto que sou muito metódica, muito analítica. Mas você me mostrou que isso pode ser uma força."
    nicole "E hoje, vendo todas aquelas pessoas incríveis... sinto que finalmente encontrei meu lugar."
    
    menu:
        "Concordar com a força da metodologia de Nicole":
            $ points_nicole += 3
            narrator "Concordei que a metodologia de Nicole era uma grande força."
            nicole "Obrigada... é reconfortante saber que alguém valoriza minha forma de pensar."
            nicole "Você me faz sentir... compreendida. É raro encontrar alguém assim."
            
        "Comentar sobre sua personalidade única":
            $ points_nicole += 2
            narrator "Comentei sobre a personalidade única e especial de Nicole."
            nicole "Você realmente me vê, não é? Às vezes sinto que sou muito diferente das outras pessoas..."
            nicole "Mas com você... me sinto aceita como sou."
            
        "Refletir sobre a conexão especial":
            $ points_nicole += 1
            narrator "Refletimos sobre a conexão especial que parecia existir entre nós."
            nicole "Há algo especial em você... algo que me faz sentir segura para ser eu mesma."
            nicole "Obrigada por estar aqui... por me entender."
    
    narrator "Chegamos à república de Nicole. A casa estava iluminada, com outras estudantes conversando na varanda."
    
    nicole "Bem... aqui estamos. Obrigada por me acompanhar... foi um momento especial."
    nicole "Espero que possamos ter mais momentos assim... conversas profundas, conexões genuínas."
    
    narrator "Nicole me olhou nos olhos por um momento, e senti algo especial passando entre nós."
    
    nicole "Até amanhã... e obrigada por ser quem você é."
    
    narrator "Ela entrou na casa, mas antes de fechar a porta, olhou para trás com um sorriso tímido."
    
    scene bg campus_night with fade
    narrator "Caminhei de volta para casa, pensando em tudo que havia acontecido. A noite havia sido especial, e senti que algo importante havia começado..."
    
    jump capitulo1_final
