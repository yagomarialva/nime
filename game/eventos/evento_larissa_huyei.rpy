# --- Evento Larissa e hu wei ---
label evento_larissa:
    $ points_larissa += 1
    scene bg quadra_volei with dissolve
    show larissa_volei at left
    show huwei_volei neutral at right

    narrator "Larissa me convidou para uma partida de vôlei na quadra da universidade. hu wei apareceu para assistir e torcer."

    larissa "Vamos aquecer antes do jogo. Preparado para suar a camisa?"

    hu wei "A energia aqui é contagiante. Esportes realmente elevam o espírito."

    menu:
        "Treinar saques com Larissa":
            $ points_larissa += 1
            larissa "Ótimo saque! Com prática, você vai dominar essa técnica."

        "Conversar com hu wei sobre esportes e bem-estar":
            $ points_hu wei += 1
            hu wei "Atividades físicas equilibram corpo e mente. É essencial para a saúde."

        "Propor um jogo amistoso com todos":
            $ points_larissa += 1
            $ points_hu wei += 1
            larissa "Adoro a ideia! Vamos formar times mistos."
            hu wei "Será divertido e revigorante."

        "Perguntar a Larissa sobre sua rotina de treinos":
            $ points_larissa += 1
            larissa "Treino diariamente, focando em resistência e agilidade. Posso te passar algumas dicas."

        "Discutir com hu wei sobre a importância da respiração durante exercícios":
            $ points_hu wei += 1
            hu wei "A respiração correta melhora o desempenho e previne lesões. É fundamental."

    hide larissa
    hide hu wei
    narrator "Após o jogo, nos sentamos para recuperar o fôlego e conversar. Uma tarde energizante e cheia de aprendizado."
    jump capitulo2
