label capitulo5_conclusao:
    scene bg quarto_protagonista_manha with dissolve
    narrator "O sol da manhã entra pela janela, marcando o início de um novo dia. Você reflete sobre tudo o que aconteceu nos últimos dias e como isso afetou suas relações com os outros moradores da república."

    # Determina a personagem com maior afinidade
    $ afinidades = {
        "camille": points_camille,
        "samantha": points_samantha,
        "nicole": points_nicole,
        "katia": points_katia,
        "huey": points_huey,
        "larissa": points_larissa
    }
    $ personagem_principal = max(afinidades, key=afinidades.get)

    # Retrospectiva personalizada com base na personagem com maior afinidade
    if personagem_principal == "camille":
        narrator "Você se lembra dos momentos tranquilos com Camille. Sua presença sempre trouxe uma sensação de calma e conexão. Ela parecia entender você de uma forma que ninguém mais conseguia."
        narrator "A maneira como ela segurou sua mão durante o eclipse e como ela apareceu à noite para compartilhar suas reflexões... tudo isso deixou uma marca em você."
    elif personagem_principal == "samantha":
        narrator "Os momentos com Samantha foram cheios de risadas e descontração. Ela sempre encontrou uma maneira de transformar situações comuns em algo divertido e único."
        narrator "Você se lembra de como ela te envolveu na gincana e como ela apareceu à noite, nervosa, mas sincera. Samantha tem um jeito especial de fazer você se sentir à vontade."
    elif personagem_principal == "nicole":
        narrator "Nicole, com sua postura séria e organizada, mostrou um lado mais vulnerável nos últimos dias. Você percebeu que, por trás de sua rigidez, há alguém que valoriza profundamente as conexões."
        narrator "A maneira como ela confiou em você durante o eclipse e como ela apareceu à noite para compartilhar suas preocupações... tudo isso aproximou vocês dois."
    elif personagem_principal == "katia":
        narrator "Katia, com sua atitude defensiva e comentários sarcásticos, revelou um lado mais genuíno nos últimos dias. Apesar de sua resistência, ela mostrou que se importa de maneiras sutis."
        narrator "Você se lembra de como ela aceitou sua companhia durante o eclipse e como ela trouxe um DVD para você à noite, mesmo tentando esconder suas intenções. Esses momentos mostraram que há mais em Katia do que ela deixa transparecer."
    elif personagem_principal == "huey":
        narrator "Huey, com sua sensibilidade artística e jeito calmo, trouxe uma nova perspectiva para sua vida. Ela sempre encontrou beleza nas pequenas coisas e compartilhou isso com você."
        narrator "Você se lembra de como vocês pintaram juntos durante o eclipse e como ela trouxe uma pintura para você à noite, cheia de significado. Huey tem um jeito único de se conectar com as pessoas."
    elif personagem_principal == "larissa":
        narrator "Larissa, com sua energia contagiante e espírito motivador, fez você se sentir mais vivo nos últimos dias. Ela sempre encontrou uma maneira de te animar e te inspirar."
        narrator "Você se lembra de como vocês correram juntos durante o eclipse e como ela apareceu à noite, com um sorriso caloroso e palavras encorajadoras. Larissa tem um jeito especial de fazer você se sentir importante."

    narrator "Você percebe que, aos poucos, está construindo laços mais profundos com os moradores da república. Cada momento compartilhado, cada conversa, cada gesto... tudo isso está moldando as relações que você tem com eles."

    jump capitulo6
