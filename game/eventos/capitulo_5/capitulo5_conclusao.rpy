label capitulo5_final:
    scene bg quarto_protagonista_manha with dissolve
    narrator "O sol da manhã entra pela janela, marcando o início de um novo dia. Você reflete sobre tudo o que aconteceu nos últimos dias e como isso afetou suas relações com os outros moradores da república."

    # Momento emocional de reflexão sobre o eclipse
    call emotional_moment("eclipse_reflection", None, "Reflexão sobre o eclipse e os momentos especiais compartilhados") from _call_emotional_moment_cap5_final_1

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
        show camille gentle at left
        camille "O eclipse foi um momento de transformação para todos nós. Sinto que algo mudou dentro de mim."
        narrator "A maneira como ela segurou sua mão durante o eclipse e como ela apareceu à noite para compartilhar suas reflexões... tudo isso deixou uma marca em você."
        hide camille
    elif personagem_principal == "samantha":
        narrator "Os momentos com Samantha foram cheios de risadas e descontração. Ela sempre encontrou uma maneira de transformar situações comuns em algo divertido e único."
        show samantha happy at left
        samantha "A gincana foi incrível! É como se o universo tivesse preparado uma aventura perfeita para nós!"
        narrator "Você se lembra de como ela te envolveu na gincana e como ela apareceu à noite, nervosa, mas sincera. Samantha tem um jeito especial de fazer você se sentir à vontade."
        hide samantha
    elif personagem_principal == "nicole":
        narrator "Nicole, com sua postura séria e organizada, mostrou um lado mais vulnerável nos últimos dias. Você percebeu que, por trás de sua rigidez, há alguém que valoriza profundamente as conexões."
        show nicole neutral at left
        nicole "O eclipse me fez perceber que nem tudo precisa ser perfeitamente organizado. Às vezes, a beleza está na espontaneidade."
        narrator "A maneira como ela confiou em você durante o eclipse e como ela apareceu à noite para compartilhar suas preocupações... tudo isso aproximou vocês dois."
        hide nicole
    elif personagem_principal == "katia":
        narrator "Katia, com sua atitude defensiva e comentários sarcásticos, revelou um lado mais genuíno nos últimos dias. Apesar de sua resistência, ela mostrou que se importa de maneiras sutis."
        show katia neutral at left
        katia "N-não é como se eu tivesse gostado do eclipse ou qualquer coisa assim! É só que... foi menos chato com você por perto."
        narrator "Você se lembra de como ela aceitou sua companhia durante o eclipse e como ela trouxe um DVD para você à noite, mesmo tentando esconder suas intenções. Esses momentos mostraram que há mais em Katia do que ela deixa transparecer."
        hide katia
    elif personagem_principal == "huey":
        narrator "Huey, com sua sensibilidade artística e jeito calmo, trouxe uma nova perspectiva para sua vida. Ela sempre encontrou beleza nas pequenas coisas e compartilhou isso com você."
        show huey happy at left
        huey "Pintar durante o eclipse foi mágico! Cada pessoa aqui é uma obra de arte, e o eclipse foi o cenário perfeito!"
        narrator "Você se lembra de como vocês pintaram juntos durante o eclipse e como ela trouxe uma pintura para você à noite, cheia de significado. Huey tem um jeito único de se conectar com as pessoas."
        hide huey
    elif personagem_principal == "larissa":
        narrator "Larissa, com sua energia contagiante e espírito motivador, fez você se sentir mais vivo nos últimos dias. Ela sempre encontrou uma maneira de te animar e te inspirar."
        show larissa happy at left
        larissa "Correr durante o eclipse foi incrível! É como se a energia cósmica tivesse nos impulsionado!"
        narrator "Você se lembra de como vocês correram juntos durante o eclipse e como ela apareceu à noite, com um sorriso caloroso e palavras encorajadoras. Larissa tem um jeito especial de fazer você se sentir importante."
        hide larissa

    # Retrospectiva dos relacionamentos
    narrator "Você percebe que, aos poucos, está construindo laços mais profundos com os moradores da república. Cada momento compartilhado, cada conversa, cada gesto... tudo isso está moldando as relações que você tem com eles."

    # Mostrar resumo dos relacionamentos
    $ relationship_summary = get_relationship_summary()
    narrator "Vamos ver como estão os relacionamentos até agora:"
    
    python:
        for summary in relationship_summary:
            renpy.say(narrator, summary)

    # Verificar se pode progredir para o próximo capítulo
    $ can_progress, progress_message = check_chapter_progression_requirement(5)
    
    if can_progress:
        # Momento emocional de realização
        call emotional_moment("chapter_achievement", None, "Realização de ter criado conexões suficientes para continuar") from _call_emotional_moment_cap5_final_2
        
        narrator "[progress_message]"
        narrator "O eclipse havia sido um momento de transformação. Algo havia mudado em todos nós, criando conexões mais profundas e significativas."
        
        show samantha happy at left
        samantha "Parece que o eclipse realmente trouxe mudanças, né?"
        hide samantha
        
        show nicole neutral at right
        nicole "Sim, há algo diferente no ar. Como se tivéssemos passado por uma transformação coletiva."
        hide nicole
        
        narrator "Era verdade. O eclipse havia sido mais que um fenômeno astronômico - havia sido um portal de transformação que nos uniu de formas que nunca imaginamos."
        
        jump capitulo6
    else:
        # Momento emocional de crescimento
        call emotional_moment("growth_opportunity", None, "Oportunidade de crescimento através da reflexão") from _call_emotional_moment_cap5_final_3
        
        narrator "[progress_message]"
        narrator "O eclipse havia sido especial, mas senti que ainda havia muito a descobrir sobre essas pessoas incríveis que haviam se tornado parte da minha vida."
        
        show katia neutral at left
        katia "N-não é como se eu estivesse preocupada ou qualquer coisa assim... mas talvez precisemos de mais tempo para nos conhecer melhor."
        hide katia
        
        show camille gentle at right
        camille "Cada conexão tem seu próprio ritmo. O eclipse foi apenas o início de nossa jornada."
        hide camille
        
        narrator "Ela estava certa. O eclipse havia sido apenas o início. Havia muito mais para descobrir e viver juntos."
        
        menu:
            "Refletir sobre as conexões que ainda precisam ser exploradas":
                narrator "Decidi dedicar mais tempo a conhecer melhor cada pessoa. Cada interação era uma oportunidade de descobrir algo novo."
                jump capitulo5_final
                
            "Aceitar que algumas conexões levam tempo para se desenvolver":
                narrator "Entendi que a pressa não era necessária. As melhores conexões se desenvolvem naturalmente, no seu próprio tempo."
                jump capitulo5_final
                
            "Voltar ao menu principal":
                return
                
            "Tentar o Capítulo 5 novamente":
                jump capitulo5
