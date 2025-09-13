# === CAMINHADA NOTURNA COM LARISSA ===
# Momento especial de conexão individual

label capitulo1_caminhada_larissa:
    scene bg campus_night with fade
    show larissa happy at center
    
    narrator "Larissa e eu saímos da festa juntos, caminhando pelas ruas iluminadas do campus."
    
    larissa "Nossa, obrigada por me acompanhar! É bom ter alguém para conversar depois de uma festa assim!"
    larissa "Estes últimos dias foram... incríveis! Nunca pensei que encontraria pessoas tão especiais!"
    
    narrator "Caminhamos em silêncio por alguns momentos, apreciando a tranquilidade da noite."
    
    larissa "Você sabe... às vezes sinto que sou muito energética, muito competitiva. Mas você me mostrou que isso pode ser uma força."
    larissa "E hoje, vendo todas aquelas pessoas incríveis... sinto que finalmente encontrei pessoas que me entendem!"
    
    menu:
        "Concordar com a força da energia de Larissa":
            $ points_larissa += 3
            narrator "Concordei que a energia contagiante de Larissa era uma grande força."
            larissa "Nossa, obrigada! É reconfortante saber que alguém valoriza minha forma de ser!"
            larissa "Você me faz sentir... compreendida. É raro encontrar alguém assim!"
            
        "Comentar sobre sua personalidade contagiante":
            $ points_larissa += 2
            narrator "Comentei sobre a personalidade contagiante e positiva de Larissa."
            larissa "Você realmente me vê, não é? Às vezes sinto que sou muito diferente das outras pessoas..."
            larissa "Mas com você... me sinto aceita como sou!"
            
        "Refletir sobre a conexão especial":
            $ points_larissa += 1
            narrator "Refletimos sobre a conexão especial que parecia existir entre nós."
            larissa "Há algo especial em você... algo que me faz sentir segura para ser eu mesma!"
            larissa "Obrigada por estar aqui... por me entender!"
    
    narrator "Chegamos à república de Larissa. A casa estava iluminada, com outras estudantes conversando na varanda."
    
    larissa "Bem... aqui estamos. Obrigada por me acompanhar... foi um momento especial!"
    larissa "Espero que possamos ter mais momentos assim... conversas profundas, conexões genuínas!"
    
    narrator "Larissa me olhou nos olhos por um momento, e senti algo especial passando entre nós."
    
    larissa "Até amanhã... e obrigada por ser quem você é!"
    
    narrator "Ela entrou na casa, mas antes de fechar a porta, olhou para trás com um sorriso radiante."
    
    scene bg campus_night with fade
    narrator "Caminhei de volta para casa, pensando em tudo que havia acontecido. A noite havia sido especial, e senti que algo importante havia começado..."
    
    jump capitulo1_final
