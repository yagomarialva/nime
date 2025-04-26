label capitulo2_conclusao:
    scene bg campus_sunset with fade

    narrator "O sol começava a se pôr, tingindo o campus com tons dourados e alaranjados. Era o fim de mais um dia, e também o encerramento de um capítulo cheio de descobertas e conexões."

    narrator "Ao longo dos últimos dias, tive a chance de conhecer melhor cada um dos meus colegas. Cada interação trouxe algo único, algo que me fez refletir sobre mim mesmo e sobre os outros."

    # Reflexão sobre os personagens
    if points_samantha > 0:
        show samantha happy at left
        narrator "Samantha me mostrou o poder da criatividade e da paixão por tecnologia. Sua energia era contagiante, e suas ideias, inspiradoras."
        hide samantha

    if points_nicole > 0:
        show nicole neutral at left
        narrator "Nicole, com sua visão estratégica e determinação, me ensinou a importância de planejar e agir com propósito. Apesar de sua postura séria, ela mostrou um lado mais humano."
        hide nicole

    if points_huey > 0:
        show huey neutral at left
        narrator "Huey, com sua conexão com a arte e a natureza, me fez perceber a beleza nos pequenos detalhes da vida. Sua calma era reconfortante."
        hide huey

    if points_larissa > 0:
        show larissa happy at left
        narrator "Larissa, com sua energia vibrante e paixão por esportes, me lembrou da importância de se manter ativo e positivo, mesmo diante dos desafios."
        hide larissa

    if points_katia > 0:
        show katia neutral at left
        narrator "Katia, com sua personalidade reservada e amor pela arte, me mostrou que há profundidade em cada gesto e que a expressão pode assumir muitas formas."
        hide katia

    if points_camille > 0:
        show camille neutral at left
        narrator "Camille, com sua serenidade e sabedoria, me ensinou a importância de encontrar equilíbrio e paz interior, mesmo em meio ao caos."
        hide camille

    # Reflexão final
    narrator "Cada momento compartilhado foi uma peça importante no quebra-cabeça que é a vida universitária. E, de alguma forma, senti que esses laços estavam apenas começando a se formar."

    narrator "Enquanto o sol desaparecia no horizonte, senti uma mistura de gratidão e expectativa pelo que estava por vir. O semestre ainda tinha muito a oferecer, e eu estava pronto para enfrentar o que viesse."

    return