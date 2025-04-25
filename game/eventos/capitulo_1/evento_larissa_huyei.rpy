# --- Evento Larissa e Huey ---
label evento_larissa_huey:
    $ points_larissa += 1
    scene bg quadra_volei with dissolve
    show larissa_volei at left
    show huey neutral at right

    narrator "Larissa me convidou para uma partida de vôlei na quadra da universidade. Huey apareceu para assistir e torcer."

    larissa "Vamos aquecer antes do jogo. Preparado para suar a camisa?"
    huey "A energia aqui é contagiante. Esportes realmente elevam o espírito."

    # Primeira interação: Quadra de vôlei
    menu:
        "Treinar saques com Larissa":
            $ points_larissa += 1
            larissa "Ótimo saque! Com prática, você vai dominar essa técnica."
            narrator "Larissa me corrigiu algumas vezes, mas sempre com um sorriso encorajador."

        "Conversar com Huey sobre esportes e bem-estar":
            $ points_huey += 1
            huey "Atividades físicas equilibram corpo e mente. É essencial para a saúde."
            narrator "Huey falou sobre como o esporte pode ser uma forma de meditação ativa."

        "Propor um jogo amistoso com todos":
            $ points_larissa += 1
            $ points_huey += 1
            larissa "Adoro a ideia! Vamos formar times mistos."
            huey "Será divertido e revigorante."
            narrator "Jogamos uma partida descontraída. Larissa liderava com entusiasmo, enquanto Huey nos motivava com palavras de apoio."

        "Perguntar a Larissa sobre sua rotina de treinos":
            $ points_larissa += 1
            larissa "Treino diariamente, focando em resistência e agilidade. Posso te passar algumas dicas."
            narrator "Ela compartilhou algumas técnicas que usa para melhorar sua performance."

        "Discutir com Huey sobre a importância da respiração durante exercícios":
            $ points_huey += 1
            huey "A respiração correta melhora o desempenho e previne lesões. É fundamental."
            narrator "Huey demonstrou algumas técnicas de respiração que ele usa para manter o foco."

    # Transição para o jardim
    scene bg jardim_universidade with dissolve
    show larissa casual at left
    show huey neutral at right

    narrator "Depois do jogo, Larissa sugeriu que fôssemos ao jardim da universidade para relaxar e conversar."

    larissa "Esse lugar é perfeito para recarregar as energias depois de um treino."
    huey "A natureza sempre ajuda a equilibrar corpo e mente."

    # Segunda interação: Jardim da universidade
    menu:
        "Perguntar a Larissa como ela começou no vôlei":
            $ points_larissa += 1
            larissa "Comecei ainda criança. Sempre adorei esportes, mas o vôlei foi onde encontrei minha paixão."
            narrator "Ela contou histórias de campeonatos e como o esporte a ajudou a crescer como pessoa."

        "Conversar com Huey sobre a conexão entre natureza e bem-estar":
            $ points_huey += 1
            huey "A natureza nos ensina a respirar, a observar e a estar presentes. É um professor silencioso."
            narrator "Huey parecia em paz enquanto falava sobre a importância de se conectar com o ambiente ao nosso redor."

        "Propor uma caminhada pelo jardim":
            $ points_larissa += 1
            $ points_huey += 1
            larissa "Ótima ideia! Caminhar ajuda a relaxar os músculos depois de um treino."
            huey "E também é uma ótima forma de meditar em movimento."
            narrator "Caminhamos juntos, conversando sobre nossas rotinas e observando a beleza do jardim."

        "Perguntar a Huey sobre sua filosofia de vida":
            $ points_huey += 1
            huey "Minha filosofia é simples: equilíbrio. Tudo na vida é uma dança entre esforço e descanso."
            narrator "Huey compartilhou algumas reflexões que ele aprendeu ao longo dos anos."

        "Discutir com Larissa sobre como ela lida com derrotas":
            $ points_larissa += 1
            larissa "Derrotas fazem parte do jogo. O importante é aprender com elas e voltar mais forte."
            narrator "Ela falou sobre como usa as derrotas como motivação para melhorar."

    # Transição para a cafeteria
    scene bg cafe_universidade with dissolve
    show larissa casual at left
    show huey neutral at right

    narrator "Para encerrar o dia, decidimos ir até a cafeteria da universidade para tomar algo e continuar a conversa."

    larissa "Depois de tanto exercício, um suco gelado cai muito bem!"
    huey "E um chá para acalmar a mente. Perfeito para fechar o dia."

    # Terceira interação: Cafeteria
    menu:
        "Perguntar a Larissa sobre seus objetivos no esporte":
            $ points_larissa += 1
            larissa "Quero competir em alto nível e, quem sabe, inspirar outras pessoas a seguirem seus sonhos."
            narrator "Ela falou com paixão sobre como o esporte moldou sua vida."

        "Conversar com Huey sobre como ele começou a meditar":
            $ points_huey += 1
            huey "Comecei por curiosidade, mas logo percebi o impacto positivo que tinha na minha vida."
            narrator "Huey explicou como a meditação o ajudou a lidar com o estresse e a encontrar clareza."

        "Propor um brinde ao dia produtivo":
            $ points_larissa += 1
            $ points_huey += 1
            larissa "Um brinde ao esforço e à diversão!"
            huey "E à conexão que compartilhamos hoje."
            narrator "Levantamos nossos copos e brindamos ao dia cheio de aprendizado e boas energias."

        "Perguntar a ambos como equilibram estudos e hobbies":
            $ points_larissa += 1
            $ points_huey += 1
            larissa "É tudo uma questão de organização e disciplina. Sempre reservo tempo para o que amo."
            huey "E também é importante saber quando desacelerar. O equilíbrio é a chave."
            narrator "Ambos compartilharam dicas valiosas sobre como manter uma rotina saudável."

        "Agradecer pela companhia e pelas lições do dia":
            $ points_larissa += 1
            $ points_huey += 1
            narrator "Agradeci por terem compartilhado tanto comigo. Foi um dia que certamente ficaria na memória."

    hide larissa
    hide huey
    narrator "Após a conversa, nos despedimos com sorrisos e a promessa de repetir a experiência. Foi um dia energizante e cheio de aprendizado."

    jump capitulo2
