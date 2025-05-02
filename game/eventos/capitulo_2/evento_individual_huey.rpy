label evento_individual_huey:
    scene bg park with fade
    show huey neutral at center

    narrator "Huey me convidou para passar uma tarde no parque. Ele parecia tranquilo, como sempre, com um sorriso sereno no rosto."

    huey "Obrigado por vir. Às vezes, é bom desacelerar e apenas apreciar o que está ao nosso redor."

    narrator "Huey parecia em paz, observando as árvores e ouvindo o som dos pássaros. Era uma oportunidade perfeita para conhecê-lo melhor."

    menu:
        "Perguntar o que ele mais gosta em momentos como este":
            $ points_huey += 1
            huey "A simplicidade. É incrível como pequenos momentos podem trazer tanta clareza."
            narrator "Huey falou com calma, como se estivesse compartilhando um segredo precioso."

        "Comentar sobre a conexão dele com a natureza":
            $ points_huey += 1
            huey "A natureza tem uma energia única. É como se ela nos lembrasse de quem realmente somos."
            narrator "Huey parecia feliz por compartilhar sua visão comigo."

        "Sugerir que vocês explorem o parque juntos":
            $ points_huey += 1
            huey "Ótima ideia. Vamos ver o que podemos descobrir por aqui."
            narrator "Huey parecia animado com a ideia de explorar o parque."

    # Cena 1: Caminhando pelo parque
    scene bg park_path with dissolve
    narrator "Começamos a caminhar pelo parque, conversando sobre arte, vida e tudo mais."

    huey "A arte e a natureza têm muito em comum. Ambas nos conectam a algo maior do que nós mesmos."

    menu:
        "Perguntar como ele encontra inspiração na natureza":
            $ points_huey += 1
            huey "Eu apenas observo. A natureza tem uma maneira de nos mostrar padrões e histórias que muitas vezes ignoramos."
            narrator "Huey parecia inspirado enquanto falava sobre sua conexão com o mundo ao seu redor."

        "Discutir como a arte pode capturar a essência da natureza":
            $ points_huey += 1
            huey "Exatamente. A arte é uma forma de traduzir o que sentimos quando estamos em contato com a natureza."
            narrator "Huey parecia impressionado com minha perspectiva."

        "Sugerir que ele crie algo inspirado no parque":
            $ points_huey += 1
            huey "Isso seria incrível. Talvez eu possa desenhar algo mais tarde."
            narrator "Huey parecia animado com a ideia de transformar sua experiência em arte."

    # Cena 2: Descanso à sombra de uma árvore
    scene bg park_tree with dissolve
    narrator "Depois de caminhar por um tempo, encontramos uma árvore grande e decidimos descansar à sua sombra."

    huey "Às vezes, tudo o que precisamos é de um momento de silêncio para reorganizar nossos pensamentos."

    menu:
        "Perguntar o que ele faz para relaxar":
            $ points_huey += 1
            huey "Eu gosto de desenhar ou apenas ouvir música. Algo que me permita desconectar por um tempo."
            narrator "Huey parecia relaxado enquanto compartilhava suas formas de encontrar paz."

        "Comentar sobre como o silêncio pode ser poderoso":
            $ points_huey += 1
            huey "Sim, o silêncio nos dá espaço para ouvir a nós mesmos. É algo que muitos subestimam."
            narrator "Huey parecia concordar profundamente com minha observação."

        "Sugerir que vocês aproveitem o momento para meditar":
            $ points_huey += 1
            huey "Boa ideia. Vamos apenas fechar os olhos e ouvir o mundo ao nosso redor."
            narrator "Passamos alguns minutos em silêncio, apenas apreciando o momento."

    # Cena 3: Finalizando o encontro
    scene bg park_exit with dissolve
    narrator "Depois de algum tempo, Huey olhou para o céu e sorriu."

    huey "Obrigado por passar esse tempo comigo. Foi bom desacelerar e apenas... estar presente."

    menu:
        "Agradecer a Huey por compartilhar sua perspectiva":
            $ points_huey += 1
            huey "Fico feliz que você tenha gostado. Espero que possamos fazer isso de novo algum dia."

        "Elogiar sua conexão com a natureza e a arte":
            $ points_huey += 1
            huey "Obrigado. É algo que tento cultivar todos os dias."

        "Sugerir que ele use essa experiência como inspiração para sua arte":
            $ points_huey += 1
            huey "Com certeza. Acho que já tenho algumas ideias para um novo projeto."

    hide huey
    narrator "Passei uma tarde tranquila e inspiradora com Huey, aprendendo mais sobre sua visão única do mundo. Foi um momento que certamente ficará na memória."
    jump capitulo2_conclusao