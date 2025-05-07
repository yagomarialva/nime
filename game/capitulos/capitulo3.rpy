label capitulo3:
    # Cena 1 – Aviso Inesperado
    scene bg campus_morning with fade
    narrator "Na manhã de uma segunda-feira, [nome] chega ao campus e percebe uma agitação incomum. Cartazes estão sendo pregados às pressas, e há um burburinho geral entre os estudantes."

    show professor_wendell neutral at center
    professor_wendell "Atenção, alunos da moradia estudantil Alfa e Beta: por conta de infiltrações estruturais, os dormitórios estão interditados. Vocês serão realocados temporariamente em casas compartilhadas."

    hide professor_wendell neutral
    "[nome]" "Casa compartilhada… Rua Aurora, número 57. Espera… esse é o meu endereço!"

    scene bg rua_aurora with dissolve
    narrator "Ao chegar em casa, ele encontra todas as garotas do grupo na frente do portão, cada uma com sua mala."
    show samantha happy at left
    samantha "O quê?! Você também vai morar aqui?!"
    hide samantha happy

    show katia neutral at center
    katia "Isso só pode ser pegadinha."
    hide katia neutral
    show camille gentle at right
    camille "Talvez o universo esteja nos unindo por alguma razão… cósmica?"
    hide camille gentle
    show nicole neutral at left
    nicole "Isso é uma falha logística gritante. Inaceitável. Mas… irreversível."
    hide nicole neutral
    show larissa neutral at center
    larissa "Pelo menos tem quintal. Dá pra correr de manhã."
    hide larissa neutral
    show huey happy at right
    huey "AAAAAA EU SEMPRE QUIS MORAR EM UMA SÉRIE DE TV!"
    hide huey happy
    
    "[nome]" "Isso vai dar muito certo. Ou muito errado."

    # Cena 2 – Organização dos Quartos
    scene bg casa_interior with dissolve
    narrator "Todos entram na casa, que tem sete quartos individuais, uma cozinha, sala ampla e dois banheiros."

    menu:
        "Escolher o quarto ao lado de Samantha":
            $ points_samantha += 3
            jump quarto_samantha
        "Escolher o quarto ao lado de Nicole":
            $ points_nicole += 3
            jump quarto_nicole
        "Escolher o quarto ao lado de Camille":
            $ points_camille += 3
            jump quarto_camille
        "Escolher o quarto ao lado de Huey":
            $ points_huey += 3
            jump quarto_huey
        "Escolher o quarto ao lado de Larissa":
            $ points_larissa += 3
            jump quarto_larissa
        "Escolher o quarto ao lado de Katia":
            $ points_katia += 3
            jump quarto_katia
        "Escolher o quarto do fundo, longe de todos":
            jump quarto_fundo

    # Cena 3 – Conflitos na Convivência
label convivencia:
    scene bg sala_casa with dissolve
    narrator "No dia seguinte, todos se reúnem na sala para definir as regras da casa."

    show samantha neutral at left
    samantha "Cada um lava o que usa. Sem exceções."

    show nicole neutral at center
    nicole "E criamos um calendário de tarefas rotativo. Excel, compartilhado no Drive."

    show katia neutral at right
    katia "Eu não vou limpar banheiro que outra pessoa sujou."

    show huey happy at left
    huey "Eu posso organizar tudo com base nas suas cores favoritas!"

    show larissa neutral at center
    larissa "Eu só quero que ninguém toque nas minhas coisas de treino."

    show camille gentle at right
    camille "A gente pode colocar um cristal de equilíbrio no centro da casa. Ajuda, juro."

    menu:
        "Propor regras rígidas":
            $ points_nicole += 1
            $ points_katia += 1
            jump convivencia_rigida
        "Sugerir uma convivência flexível e amigável":
            $ points_camille += 1
            $ points_huey += 1
            jump convivencia_flexivel
        "Apoiar a ideia de lavar só o que usou":
            $ points_samantha += 1
            $ points_larissa += 1
            jump convivencia_lavar

    # Cena 4 – Noite de Tempestade
label noite_tempestade:
    scene bg sala_escura with dissolve
    narrator "Chove forte. A luz acaba. Todos se reúnem na sala escura com lanternas."

    show camille gentle at left
    camille "Isso me lembra o retiro de artistas que fiz nas montanhas… só que sem as montanhas."

    show nicole neutral at center
    nicole "Apaguei meus backups hoje. Se meu notebook fritar, eu frito junto."

    show samantha neutral at right
    samantha "A casa parece assombrada. Não é que eu esteja com medo… mas posso sentar aí?"

    show katia neutral at left
    katia "Eu vou ficar na cozinha. Se algo aparecer, eu taco uma frigideira."

    show larissa neutral at center
    larissa "Vamos fazer uma série de exercícios para passar o tempo!"

    show huey happy at right
    huey "Hora da dança ritual de proteção contra espíritos!!!"

    menu:
        "Ficar ao lado de Samantha":
            $ points_samantha += 1
            jump noite_samantha
        "Ficar ao lado de Nicole":
            $ points_nicole += 1
            jump noite_nicole
        "Ficar ao lado de Huey":
            $ points_huey += 1
            jump noite_huey
        "Ajudar Katia na cozinha":
            $ points_katia += 1
            jump noite_katia
        "Ajudar Larissa a se alongar":
            $ points_larissa += 1
            jump noite_larissa
        "Participar da 'dança' com Camille":
            $ points_camille += 1
            jump noite_camille

label luz_volta:
    scene bg sala_casa with dissolve
    narrator "Depois de algumas horas no escuro, a luz finalmente voltou. Um suspiro coletivo de alívio ecoou pela casa."

    show samantha happy at left
    samantha "Finalmente! Achei que ia precisar usar meus óculos de visão noturna... se eu tivesse um, claro."
    hide samantha happy
    show nicole neutral at center
    nicole "Pelo menos agora posso voltar ao trabalho. Isso foi uma perda de tempo."
    hide nicole neutral
    show katia neutral at right
    katia "Hmpf. Eu sabia que não tinha nada de assombrado. Só um apagão comum."
    hide katia neutral
    show huey happy at left
    huey "Ahhh, mas foi divertido! Parecia um episódio de mistério!"
    hide huey happy
    show larissa neutral at center
    larissa "Agora sim! Vou preparar algo para comer. Ficar no escuro me deu fome."
    hide larissa neutral
    show camille gentle at right
    camille "A luz voltou, mas a energia que compartilhamos no escuro foi especial. Obrigada por isso."
    hide camille gentle
    # Interação personalizada com base na escolha
    if _return == "noite_samantha":
        $ points_samantha += 1    
        jump luz_samantha
    elif _return == "noite_nicole":
        $ points_nicole += 1
        jump luz_nicole
    elif _return == "noite_huey":
        $ points_huey += 1
        jump luz_huey
    elif _return == "noite_katia":
        $ points_katia += 1
        jump luz_katia
    elif _return == "noite_larissa":
        $ points_larissa += 1
        jump luz_larissa
    elif _return == "noite_camille":
        $ points_camille += 1
        jump luz_camille

label luz_samantha:
    show samantha neutral at center
    narrator "Samantha se aproximou, ainda animada com a ideia de transformar o apagão em uma aventura."
    
    samantha "Ei, foi divertido, né? Quem sabe na próxima a gente realmente jogue um RPG no escuro!"
    
    "[nome]" "Desde que você não me faça rolar dados para decidir se eu sobrevivo, tudo bem."
    
    show samantha happy at center
    samantha "Hahaha! Combinado. Mas eu vou te ensinar a criar um personagem incrível!"
    
    narrator "Samantha parecia mais animada do que nunca. Sua energia era contagiante."
    jump fim_de_semana

label luz_nicole:
    show nicole neutral at center
    narrator "Nicole suspirou aliviada, mas ainda parecia um pouco tensa."
    
    nicole "Finalmente. Agora posso voltar ao trabalho. Mas... obrigada por ficar por perto."
    
    "[nome]" "Sem problemas. Às vezes, até você precisa de uma pausa, sabia?"
    
    show nicole blush at center
    nicole "Hmpf. Talvez você esteja certo. Mas não se acostume com isso."
    
    narrator "Nicole deu um pequeno sorriso antes de voltar ao seu notebook. Foi um momento raro, mas especial."
    jump fim_de_semana

label luz_huey:
    show huey happy at center
    narrator "Huey parecia radiante, como se o apagão tivesse sido a melhor parte do dia."
    
    huey "Isso foi tão divertido! Eu até desenhei algumas ideias para uma história de mistério."
    
    "[nome]" "Você realmente consegue transformar qualquer coisa em arte, né?"
    
    show huey blush at center
    huey "Hahaha, talvez. Mas você foi uma ótima companhia. Obrigada por isso!"
    
    narrator "Huey mostrou alguns de seus desenhos, e você não pôde deixar de admirar sua criatividade."
    jump fim_de_semana

label luz_katia:
    show katia neutral at center
    narrator "Katia cruzou os braços, tentando parecer indiferente."
    
    katia "Hmpf. Não é como se eu precisasse de você lá na cozinha, mas... foi menos chato com você por perto."
    
    "[nome]" "Ah, então você admite que gostou da minha companhia?"
    
    show katia blush at center
    katia "N-Não se ache tanto! Só estou dizendo que você não foi completamente inútil."
    
    narrator "Apesar de suas palavras duras, Katia parecia satisfeita. Você até conseguiu arrancar um pequeno sorriso dela."
    jump fim_de_semana

label luz_larissa:
    show larissa neutral at center
    narrator "Larissa parecia aliviada, mas ainda cheia de energia."
    
    larissa "Agora que a luz voltou, podemos fazer um treino de verdade! Que tal?"
    
    "[nome]" "Depois de tudo isso? Acho que vou passar."
    
    show larissa happy at center
    larissa "Hahaha! Tudo bem, você merece um descanso. Mas amanhã não tem desculpa!"
    
    narrator "Larissa deu um tapinha amigável no seu ombro antes de sair. Sua energia era contagiante."
    jump fim_de_semana

label luz_camille:
    show camille gentle at center
    narrator "Camille sorriu suavemente, como se o apagão tivesse sido uma experiência especial para ela."
    
    camille "A luz voltou, mas eu gostei do que compartilhamos no escuro. Foi... único."
    
    "[nome]" "Você realmente consegue encontrar beleza em qualquer situação, não é?"
    
    show camille happy at center
    camille "Talvez. Mas acho que foi você que tornou o momento especial."
    
    narrator "Camille parecia genuinamente grata. Sua serenidade era reconfortante."
    jump fim_de_semana
    # Cena 5 – Primeiro Fim de Semana Juntos
label fim_de_semana:
    scene bg sala_casa with dissolve
    narrator "A casa decide fazer uma noite de pizzas e filmes."

    show huey happy at left
    huey "Cada um escolhe um filme. No final, votação pra saber o campeão."

    show samantha neutral at center
    samantha "Eu trouxe uns animes. Ouvi dizer que alguns aqui curtem…"

    show nicole neutral at right
    nicole "Dividi os títulos por gênero e duração. Está tudo nesse QR Code."

    show katia neutral at left
    katia "Só escolham algo que não tenha romance meloso."

    show camille gentle at center
    camille "Eu trouxe um documentário sobre energia vital e conexões humanas."

    show larissa neutral at right
    larissa "Se tiver cena de ação e explosão emocional, já ganhou meu voto!"

    menu:
        "Sentar-se ao lado de Samantha":
            $ points_samantha += 1
            jump filme_samantha
        "Sentar-se ao lado de Katia":
            $ points_katia += 1
            jump filme_katia
        "Sentar-se ao lado de Nicole":
            $ points_nicole += 1
            jump filme_nicole
        "Sentar-se ao lado de Camille":
            $ points_camille += 1
            jump filme_camille
        "Sentar-se ao lado de Larissa":
            $ points_larissa += 1
            jump filme_larissa

    return