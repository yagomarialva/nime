label evento_individual_samantha:
    scene bg tech_lab with fade
    show samantha happy at center

    narrator "Samantha me convidou para passar um tempo no laboratório de tecnologia. Ela parecia animada, como sempre, com várias ideias fervilhando em sua mente."

    samantha "Ei! Que bom que você veio! Eu estava pensando em testar algumas ideias para um sistema de RPG digital. Quer me ajudar?"

    narrator "Samantha estava cercada por telas, anotações e protótipos. Sua energia era contagiante, e eu sabia que seria uma tarde interessante."

    menu:
        "Perguntar sobre o sistema de RPG que ela está criando":
            $ points_samantha += 1
            samantha "Ah, é um sistema que mistura narrativa interativa com mecânicas de combate dinâmicas. Quero que os jogadores sintam que estão realmente dentro da história!"
            narrator "Samantha explicou com entusiasmo, detalhando suas ideias inovadoras."

        "Oferecer ajuda para revisar o código do sistema":
            $ points_samantha += 1
            samantha "Sério? Isso seria incrível! Eu estava quebrando a cabeça com alguns bugs."
            narrator "Passei algum tempo ajudando Samantha a depurar o código, e ela parecia grata pela ajuda."

        "Sugerir ideias para integrar elementos de narrativa ao sistema":
            $ points_samantha += 1
            samantha "Ótima ideia! Isso pode tornar a experiência ainda mais imersiva."
            narrator "Samantha anotou minhas sugestões, claramente animada com as possibilidades."

    # Cena 1: Testando o sistema
    scene bg tech_lab with dissolve
    narrator "Depois de ajustar algumas coisas, Samantha decidiu testar o sistema comigo."

    samantha "Ok, você será o jogador de teste. Vamos ver como isso funciona na prática!"

    menu:
        "Escolher um personagem e explorar a narrativa":
            $ points_samantha += 1
            samantha "Você escolheu bem! Esse personagem tem habilidades interessantes para a história."
            narrator "Samantha parecia satisfeita com minha escolha e acompanhou atentamente o teste."

        "Focar nas mecânicas de combate e dar feedback":
            $ points_samantha += 1
            samantha "Boa observação! Vou ajustar isso para deixar o combate mais fluido."
            narrator "Samantha anotou minhas sugestões, claramente interessada em melhorar o sistema."

        "Sugerir melhorias para a interface do sistema":
            $ points_samantha += 1
            samantha "Você tem um bom olho para detalhes! Vou trabalhar nisso."
            narrator "Samantha parecia impressionada com minhas sugestões e começou a fazer ajustes imediatamente."

    # Cena 2: Conversa sobre RPGs
    scene bg tech_lab with dissolve
    narrator "Depois de testar o sistema, começamos a conversar sobre RPGs em geral."

    samantha "Eu adoro como RPGs permitem que você crie histórias únicas. É como ser o autor e o protagonista ao mesmo tempo."

    menu:
        "Perguntar sobre o RPG favorito dela":
            $ points_samantha += 1
            samantha "Difícil escolher, mas acho que seria D&D. É um clássico, e as possibilidades são infinitas!"
            narrator "Samantha falou com paixão sobre suas experiências jogando RPGs."

        "Compartilhar sua experiência com RPGs":
            $ points_samantha += 1
            samantha "Sério? Isso é incrível! Precisamos jogar juntos algum dia."
            narrator "Samantha parecia animada com a ideia de compartilhar uma campanha comigo."

        "Discutir como RPGs podem ser usados para contar histórias profundas":
            $ points_samantha += 1
            samantha "Exatamente! É por isso que eu amo RPGs. Eles permitem explorar temas complexos de uma forma única."
            narrator "Samantha parecia impressionada com minha visão sobre RPGs."

    # Cena 3: Finalizando o dia
    scene bg tech_lab with dissolve
    narrator "Depois de algumas horas, Samantha parecia satisfeita com o progresso que fizemos."

    samantha "Hoje foi incrível! Obrigada por me ajudar. Acho que o sistema está muito melhor agora."

    menu:
        "Agradecer a Samantha pela oportunidade de ajudar":
            $ points_samantha += 1
            samantha "Ah, não precisa agradecer! Foi ótimo ter você aqui."

        "Sugerir que vocês joguem uma campanha juntos no futuro":
            $ points_samantha += 1
            samantha "Com certeza! Já estou pensando em uma história épica para a gente jogar."

        "Elogiar a criatividade dela e o sistema que está criando":
            $ points_samantha += 1
            samantha "Obrigada! Isso significa muito para mim. Vou continuar trabalhando duro."

    hide samantha
    narrator "Passei uma tarde incrível com Samantha, aprendendo mais sobre sua paixão por RPGs e tecnologia. Mal posso esperar para ver o que ela criará no futuro."
    return