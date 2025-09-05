# Eventos do Eclipse

label eclipse_camille:
    $ points_camille += 6
    scene bg jardim with dissolve
    show camille gentle at center
    narrator "Você encontra Camille no jardim, sentada em posição de meditação enquanto observa o eclipse."
    camille "Ah, [nome]. Que bom que veio. Esse momento é tão poderoso, não acha?"
    "[nome]" "Sim, é incrível. Parece que o tempo parou."
    camille "É nesses momentos que percebemos como somos pequenos, mas ao mesmo tempo conectados ao universo."
    narrator "Vocês conversaram sobre conexões cósmicas e destinos cruzados. Camille parecia mais aberta e vulnerável do que nunca."
    if points_camille >= 7:
        camille "Eu sinto que... você entende isso de uma forma especial. Obrigada por estar aqui comigo."
        narrator "Camille segurou sua mão por um breve momento, antes de voltar a observar o eclipse."
    jump capitulo5_decisao_fim_de_semana

label eclipse_samantha:
    $ points_samantha += 6
    scene bg campus with dissolve
    show samantha happy at center
    narrator "Você decide participar da gincana temática com Samantha. O campus está cheio de estudantes animados."
    samantha "Olha só! Essa pista fala sobre um artefato perdido no tempo. Vamos resolver isso juntos!"
    "[nome]" "Parece divertido. Vamos lá!"
    narrator "Vocês correram pelo campus, resolvendo enigmas e rindo das situações inesperadas."
    if points_samantha >= 7:
        samantha "Você é muito bom nisso. Acho que formamos uma ótima dupla."
        narrator "No final, Samantha encontrou uma pista que parecia ter um significado especial. Ela sorriu e guardou para si."
    jump capitulo5_decisao_fim_de_semana

label eclipse_nicole:
    $ points_nicole += 6
    scene bg campus with dissolve
    show nicole neutral at center
    narrator "Você decide ajudar Nicole a organizar a segurança da atividade. Ela está distribuindo óculos de proteção e orientando os estudantes."
    nicole "Obrigada por ajudar. É importante que todos aproveitem o eclipse com segurança."
    "[nome]" "Você realmente pensa em tudo, não é?"
    show nicole happy at center
    nicole "Alguém precisa pensar. Mas é bom ter você aqui."
    narrator "Vocês trabalharam juntos em silêncio, mas a proximidade criou um momento de cumplicidade."
    if points_nicole >= 7:
        nicole "Eu... gosto de trabalhar com você. É fácil confiar em você."
        narrator "Nicole sorriu de forma discreta, mas significativa."
    jump capitulo5_decisao_fim_de_semana

label eclipse_larissa:
    $ points_larissa += 6
    scene bg parque with dissolve
    show larissa happy at center
    narrator "Você decide acompanhar Larissa em uma corrida leve durante o eclipse. O parque está tranquilo, com poucas pessoas."
    larissa "Correr durante o eclipse é incrível! Parece que estou correndo em outro mundo."
    "[nome]" "Você realmente tem energia infinita, hein?"
    show larissa laugh at center
    larissa "Hahaha! Talvez. Mas é bom ter companhia."
    narrator "Vocês correram juntos, e Larissa tentou te motivar com frases animadoras."
    if points_larissa >= 7:
        larissa "Você está melhorando! Quem sabe um dia não me acompanha em uma maratona?"
        narrator "Larissa deu um leve empurrão no seu ombro, rindo. Foi um momento cheio de energia e flerte."
    jump capitulo5_decisao_fim_de_semana

label eclipse_huey:
    $ points_huey += 6
    scene bg sala_arte with dissolve
    show huey happy at center
    narrator "Você decide fazer uma pintura colaborativa com Huey. Ela já está com pincéis e tintas preparados."
    huey "O eclipse é tão inspirador. Quero capturar isso na tela. Vamos pintar juntos?"
    "[nome]" "Eu não sou muito bom nisso, mas vou tentar."
    narrator "Vocês passaram o tempo pintando e trocando ideias sobre arte. Huey parecia mais confiante com você ao lado."
    if points_huey >= 7:
        huey "Eu acho que... essa pintura é sobre nós. Obrigada por estar aqui."
        narrator "Huey sorriu timidamente, mas seus olhos brilhavam com emoção."
    jump capitulo5_decisao_fim_de_semana

label eclipse_katia:
    $ points_katia += 6
    scene bg varanda with dissolve
    show katia neutral at center
    narrator "Você decide assistir ao eclipse com Katia em silêncio. Ela está na varanda, olhando para o céu."
    katia "Se veio aqui para falar sobre o eclipse, pode ir embora."
    "[nome]" "Na verdade, achei que você gostaria de companhia."
    show katia blush at center
    katia "Hmpf. Só não atrapalhe."
    narrator "Vocês ficaram em silêncio, observando o eclipse. Apesar de sua atitude defensiva, Katia parecia confortável com sua presença."
    if points_katia >= 7:
        katia "Isso não significa nada, tá? Só... obrigada por estar aqui."
        narrator "Katia segurou sua mão por um breve momento, antes de voltar a olhar para o céu."
    jump capitulo5_decisao_fim_de_semana
