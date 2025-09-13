# === CAMINHADA NOTURNA COM KATIA ===
# Momento especial de conexão individual

label caminhada_katia:
    scene bg campus_night with fade
    show katia neutral at center
    
    narrator "Katia e eu saímos da festa juntos, caminhando pelas ruas iluminadas do campus."
    
    katia "Hmm... obrigada por me acompanhar. É bom ter alguém para conversar depois de uma festa assim."
    katia "Estes últimos dias foram... diferentes. Nunca pensei que encontraria pessoas que realmente entendessem de cinema."
    
    narrator "Caminhamos em silêncio por alguns momentos, apreciando a tranquilidade da noite."
    
    katia "Você sabe... às vezes sinto que sou muito crítica, muito tsundere. Mas você me mostrou que isso pode ser uma força."
    katia "E hoje, vendo todas aquelas pessoas incríveis... sinto que finalmente encontrei pessoas que me aceitam como sou."
    
    menu:
        "Concordar com a força da personalidade de Katia":
            $ points_katia += 3
            narrator "Concordei que a personalidade única de Katia era uma grande força."
            katia "Hmpf... é reconfortante saber que alguém valoriza minha forma de ser."
            katia "N-não é como se eu estivesse impressionada ou qualquer coisa assim... mas é raro encontrar alguém assim."
            
        "Comentar sobre sua paixão pelo cinema":
            $ points_katia += 2
            narrator "Comentei sobre a paixão única de Katia pelo cinema."
            katia "Você realmente me entende, não é? Às vezes sinto que sou muito diferente das outras pessoas..."
            katia "Mas com você... me sinto aceita como sou."
            
        "Refletir sobre a conexão especial":
            $ points_katia += 1
            narrator "Refletimos sobre a conexão especial que parecia existir entre nós."
            katia "Há algo especial em você... algo que me faz sentir segura para ser eu mesma."
            katia "Obrigada por estar aqui... por me entender."
    
    narrator "Chegamos à república de Katia. A casa estava iluminada, com outras estudantes conversando na varanda."
    
    katia "Bem... aqui estamos. Obrigada por me acompanhar... foi um momento especial."
    katia "Espero que possamos ter mais momentos assim... conversas profundas, conexões genuínas."
    
    narrator "Katia me olhou nos olhos por um momento, e senti algo especial passando entre nós."
    
    katia "Até amanhã... e obrigada por ser quem você é."
    
    narrator "Ela entrou na casa, mas antes de fechar a porta, olhou para trás com um sorriso tímido."
    
    scene bg campus_night with fade
    narrator "Caminhei de volta para casa, pensando em tudo que havia acontecido. A noite havia sido especial, e senti que algo importante havia começado..."
    
    jump capitulo1_final
