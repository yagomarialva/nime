# === EVENTO QUADRA: LARISSA E HUEY ===
# Tema: Estetizando o sofrimento

label evento_larissa_huey:
    $ points_larissa += 1
    
    scene bg quadra_volei with dissolve

    narrator "O clarão das luzes halógenas da quadra zumbia incansavelmente. O som do golpe de couro contra a parede de concreto era visceral."
    narrator "*PÁ!*"

    show larissa voley at left
    
    narrator "Larissa cravava outra bola esportiva com força desproporcional. Seu maxilar estava tão tensionado que os tendões de seu pescoço pareciam a ponto de estourar. O suor não era de treino; era de purga."
    
    larissa "Mais. Rápido. O tempo de reação não pode existir. Eu não quero pensar antes de bater!"
    
    narrator "Na arquibancada isolada das sombras, um pedaço de carvão rangia seco contra papel poroso."

    show huey neutral at right
    
    narrator "Huey acompanhava os movimentos da atleta, mas seus olhos paravam nos instantes errados: na dor do impacto, na queda pesada."
    
    huey "A destruição da articulação do manguito rotador... Que linhas dolorosamente autoimolantes."
    
    mc "Acho que a ideia de um esporte não é a autoflagelação artística."
    
    narrator "Minha voz assustou o ginásio vazio, interrompendo o fluxo. A bola de Larissa bateu na quina do teto e escorregou impotente."
    
    show larissa angry
    larissa "QUEM MANDOU VOCÊS PARAREM O RITMO? Se o meu fluxo de adrenalina cair agora, eu sou um pedaço de peso morto!"
    
    narrator "A artista ergueu os olhos do caderno com vagareza, não intimidada pelos gritos de quem claramente estava lutando contra si mesma."
    
    show huey neutral
    huey "Você parece peso morto mesmo quando atinge uma força G de salto. Suas pernas querem voar, mas seu ombro está se punindo."
    
    show larissa
    larissa "O que você disse, sua esquisitice de arquibancada? Eu estou treinando pra um campeonato! Você desenha rascunho de passarinho!"
    
    huey "Eu desenho o desespero. E você exala um terror cinético patético de que se parar de correr, o vazio vai te pegar."
    
    narrator "Larissa hesitou, o peito subindo e descendo tão bruscamente que achei que suas costelas estalariam. Ela tentou esmagar a bola nos dedos, falhando."
    
    menu:
        "Atacar o voyeurismo da artista (Huey)":
            $ points_larissa += 1
            mc "Romanticizar quem está quebrando os próprios ossos não faz de você profunda, Huey. Só faz de você sádica."
            huey "O olhar que fixa a ruína é cruel por natureza, não por malícia."
            larissa "Não ouse pintar meu esforço como tragédia. Fique longe da minha linha."
            
        "Expor a anestesia no esforço (Larissa)":
            $ points_huey += 1
            mc "Bater até o braço sangrar não vai calar tudo. O traço do desenho dela viu a rachadura óbvia na sua armadura, Larissa."
            larissa "Cala a boca! Cala a boca! Os tombos no asfalto curam furos reais na alma! A tinta dela não derrama suor!"
            huey "Mas enxerga o sangramento interno muito mais nítido do que os seus óculos de esporte cego."
            
        "Pausar o sangramento de ambas":
            $ points_larissa += 1
            $ points_huey += 1
            mc "As duas falharam em achar cura hoje. Vão para as suas tocas curtir o esgotamento em paz."
            narrator "Nenhuma das duas rebateu. A guerra fria de perspectivas não tinha troféu."
            
    narrator "Larissa atirou a bola num canto distante e arrastou a mochila no chão da quadra com violência, sumindo pelos vestiários num baque metálico de portas."
    narrator "Huey encarou seu caderno machado de carvão negro em um borrão irreconhecível de traços distorcidos, suspirando e o fechando devagar."
    
    # Memória compartilhada renomeada para seguir tom
    $ add_shared_memory("sport_art_connection", ["larissa", "huey"], "O dia em que a destruição física expôs a fragilidade artística.")

    return