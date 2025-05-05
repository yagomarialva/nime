label evento_individual_nicole:
    scene bg cafeteria with fade
    show nicole neutral at center

    narrator "Nicole me convidou para tomar um café e conversar sobre ideias e projetos. Ela parecia tranquila, mas seu olhar focado mostrava que já estava pensando em algo."

    nicole "Obrigada por vir. Eu precisava de alguém para trocar ideias. Às vezes, pensar sozinho não é suficiente."

    narrator "Nicole era direta, como sempre, mas havia algo mais relaxado em sua postura hoje. Parecia uma boa oportunidade para conhecê-la melhor."

    menu:
        "Perguntar sobre o projeto em que ela está trabalhando":
            $ points_nicole += 1
            nicole "Estou desenvolvendo um plano para ajudar artistas a monetizar suas obras sem comprometer sua autenticidade."
            narrator "Nicole explicou sua visão com clareza, mostrando sua paixão por unir estratégia e criatividade."

        "Elogiar sua habilidade de organização e planejamento":
            $ points_nicole += 1
            nicole "Obrigada. Organização é essencial para transformar ideias em resultados concretos."
            narrator "Nicole parecia satisfeita com o elogio, mas manteve seu tom profissional."

        "Perguntar como ela lida com desafios emocionais no trabalho":
            $ points_nicole += 1
            nicole "Ainda estou aprendendo. Emoções podem ser complicadas, mas estou tentando usá-las como uma ferramenta, não como um obstáculo."
            narrator "Nicole parecia reflexiva, mostrando um lado mais vulnerável."

    # Cena 1: Discussão sobre ideias
    scene bg cafeteria with dissolve
    show nicole neutral at center
    narrator "Enquanto tomávamos café, a conversa se aprofundou. Nicole parecia interessada em ouvir minha opinião sobre alguns tópicos."

    menu:
        "Discutir como equilibrar autenticidade e estratégia":
            $ points_nicole += 1
            nicole "Esse é o maior desafio. Encontrar o equilíbrio entre ser verdadeiro e ser eficiente é uma arte."
            narrator "Nicole parecia impressionada com minha perspectiva e anotou algumas ideias."

        "Sugerir formas de engajar o público de maneira criativa":
            $ points_nicole += 1
            nicole "Engajamento é tudo. Se você não conecta com as pessoas, sua mensagem se perde."
            narrator "Nicole parecia animada com as sugestões e começou a pensar em como aplicá-las."

        "Perguntar como ela se inspira para criar estratégias":
            $ points_nicole += 1
            nicole "Eu observo o que funciona em outros setores e adapto para o meu contexto. Inspiração está em todo lugar, se você souber onde procurar."
            narrator "Nicole compartilhou algumas de suas fontes de inspiração, mostrando sua abordagem prática."

    # Cena 2: Reflexão pessoal
    scene bg cafeteria with dissolve
    show nicole neutral at center
    narrator "Depois de discutir ideias, a conversa tomou um tom mais pessoal. Nicole parecia disposta a compartilhar mais sobre si mesma."

    nicole "Sabe, às vezes me pergunto se estou no caminho certo. Ser tão focada em resultados pode me fazer parecer fria."

    menu:
        "Dizer que o equilíbrio entre razão e emoção é importante":
            $ points_nicole += 1
            nicole "Você tem razão. Talvez eu precise trabalhar mais nisso. Obrigada por me lembrar."
            narrator "Nicole parecia grata pela perspectiva, mostrando um raro momento de vulnerabilidade."

        "Elogiar sua determinação e foco":
            $ points_nicole += 1
            nicole "Obrigada. Determinação é o que me mantém em movimento, mas é bom ouvir que isso é valorizado."
            narrator "Nicole parecia satisfeita com o elogio, mas ainda reflexiva."

        "Sugerir que ela tire um tempo para relaxar e se reconectar":
            $ points_nicole += 1
            nicole "Talvez você esteja certo. Um pouco de descanso pode ajudar a clarear a mente."
            narrator "Nicole parecia considerar seriamente a sugestão, algo que parecia raro para ela."

    # Cena 3: Finalizando o encontro
    scene bg cafeteria with dissolve
    show nicole neutral at center
    narrator "Depois de algum tempo, Nicole olhou para o relógio e sorriu levemente."

    nicole "Foi bom conversar com você. Acho que precisava disso mais do que imaginava."

    menu:
        "Agradecer pela conversa e dizer que aprendeu muito":
            $ points_nicole += 1
            nicole "Fico feliz em ouvir isso. Espero que possamos trocar mais ideias no futuro."

        "Sugerir que vocês colaborem em um projeto juntos":
            $ points_nicole += 1
            nicole "Isso seria interessante. Tenho certeza de que podemos criar algo incrível juntos."

        "Elogiar sua visão estratégica e dizer que ela é inspiradora":
            $ points_nicole += 1
            nicole "Obrigada. Isso significa muito para mim. Vou continuar trabalhando para melhorar."

    hide nicole
    narrator "Passei uma tarde inspiradora com Nicole, aprendendo mais sobre sua visão estratégica e seu lado mais humano. Foi uma experiência que certamente ficará na memória."
    jump capitulo2_conclusao