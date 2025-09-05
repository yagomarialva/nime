label capitulo3_final:
    scene bg casa_noite with fade

    narrator "A noite caiu sobre a Rua Aurora, e a casa estava finalmente em silêncio. Depois de dias intensos de convivência, parecia que todos estavam começando a se adaptar à nova rotina."

    # Momento emocional de reflexão sobre a convivência
    call emotional_moment("coexistence_reflection", None, "Reflexão sobre a nova vida em conjunto") from _call_emotional_moment_cap3_8

    narrator "Cada momento compartilhado trouxe algo único, algo que me fez refletir sobre as pessoas ao meu redor e sobre mim mesmo."

    # Reflexão sobre os personagens com mais profundidade
    if points_samantha > 0:
        show samantha happy at left
        narrator "Samantha, com sua paixão por jogos e criatividade, me mostrou como é importante manter a mente aberta e explorar novas ideias. Sua energia nerd era contagiante."
        samantha "Viver juntos tem sido... incrível. É como ter uma equipe de desenvolvimento 24/7!"
        narrator "Ela me ensinou que a criatividade floresce melhor quando compartilhada com pessoas que entendem sua paixão."
        hide samantha

    if points_nicole > 0:
        show nicole neutral at left
        narrator "Nicole, com sua organização impecável e visão estratégica, me ensinou a importância de manter o foco e planejar o futuro. Apesar de sua seriedade, ela mostrou um lado mais humano."
        nicole "A convivência me ensinou que nem tudo pode ser planejado. Às vezes, o melhor é deixar a vida acontecer."
        narrator "Ela me mostrou que por trás de cada plano perfeito, há uma pessoa que também precisa de flexibilidade e compreensão."
        hide nicole

    if points_huey > 0:
        show huey happy at left
        narrator "Huey, com sua arte e entusiasmo, me fez perceber a beleza nos pequenos detalhes e a importância de manter a criatividade viva, mesmo em momentos difíceis."
        huey "Cada dia aqui é uma nova inspiração! Vocês são minha musa coletiva!"
        narrator "Ele me ensinou que a arte não é apenas sobre criar, mas sobre compartilhar a beleza que vemos no mundo."
        hide huey

    if points_larissa > 0:
        show larissa happy at left
        narrator "Larissa, com sua energia vibrante e paixão por esportes, me lembrou que cuidar do corpo também é cuidar da mente. Sua determinação era inspiradora."
        larissa "Ter companhia para treinar mudou tudo! Agora tenho motivação extra para me superar!"
        narrator "Ela me mostrou que a energia positiva é contagiosa e pode transformar qualquer ambiente em um lugar de crescimento."
        hide larissa

    if points_katia > 0:
        show katia neutral at left
        narrator "Katia, com sua personalidade tsundere e amor pela arte, me mostrou que, por trás de uma fachada dura, há sempre algo profundo e significativo esperando para ser descoberto."
        katia "N-não é como se eu tivesse gostado de morar com vocês ou qualquer coisa assim! É só que... é menos solitário."
        narrator "Ela me ensinou que por trás de cada fachada, há uma pessoa que busca conexão, mesmo que não saiba como expressar isso."
        hide katia

    if points_camille > 0:
        show camille gentle at left
        narrator "Camille, com sua serenidade e espiritualidade, me ensinou a importância de encontrar equilíbrio e paz interior, mesmo em meio ao caos da convivência."
        camille "A energia desta casa se transformou. Há uma harmonia especial que só pode vir de pessoas que se importam umas com as outras."
        narrator "Ela me mostrou que a verdadeira paz não vem da ausência de conflito, mas da capacidade de encontrar equilíbrio em meio à diversidade."
        hide camille

    # Retrospectiva dos relacionamentos
    narrator "Esses dias foram um teste de paciência, mas também uma oportunidade de criar laços. Cada interação, cada conversa, cada momento compartilhado foi uma peça importante no quebra-cabeça que é a vida em grupo."

    # Mostrar resumo dos relacionamentos
    $ relationship_summary = get_relationship_summary()
    narrator "Vamos ver como estão os relacionamentos até agora:"
    
    python:
        for summary in relationship_summary:
            renpy.say(narrator, summary)

    # Verificar se pode progredir para o próximo capítulo
    $ can_progress, progress_message = check_chapter_progression_requirement(3)
    
    if can_progress:
        # Momento emocional de realização
        call emotional_moment("chapter_achievement", None, "Realização de ter criado conexões suficientes para continuar") from _call_emotional_moment_cap3_9
        
        narrator "[progress_message]"
        narrator "Enquanto eu olhava pela janela, vendo as luzes da cidade ao longe, senti que algo estava mudando. Não apenas em mim, mas em todos nós. A convivência estava nos transformando, de formas que talvez ainda não entendêssemos completamente."
        
        show samantha happy at left
        samantha "Parece que estamos nos tornando uma verdadeira família, né?"
        hide samantha
        
        show nicole neutral at right
        nicole "Sim, há algo especial acontecendo aqui. Algo que vai além de simples colegas de quarto."
        hide nicole
        
        narrator "Era verdade. Algo mágico estava acontecendo entre nós - uma conexão que transcendeu as barreiras iniciais e criou algo genuinamente especial. Uma família escolhida."
        
        jump capitulo4
    else:
        # Momento emocional de crescimento
        call emotional_moment("growth_opportunity", None, "Oportunidade de crescimento através da reflexão") from _call_emotional_moment_cap3_10
        
        narrator "[progress_message]"
        narrator "Enquanto eu olhava pela janela, vendo as luzes da cidade ao longe, senti que ainda havia muito a descobrir sobre essas pessoas incríveis que haviam se tornado parte da minha vida."
        
        show katia neutral at left
        katia "N-não é como se eu estivesse preocupada ou qualquer coisa assim... mas talvez precisemos de mais tempo para nos conhecer melhor."
        hide katia
        
        show camille gentle at right
        camille "Cada conexão tem seu próprio ritmo. Não há pressa em descobrir o que o futuro nos reserva."
        hide camille
        
        narrator "Ela estava certa. Algumas conexões levam tempo para florescer, e talvez eu precisasse ser mais paciente e atento às oportunidades que ainda estavam por vir."
        
        menu:
            "Refletir sobre as conexões que ainda precisam ser exploradas":
                narrator "Decidi dedicar mais tempo a conhecer melhor cada pessoa. Cada interação era uma oportunidade de descobrir algo novo."
                jump capitulo3_final
                
            "Aceitar que algumas conexões levam tempo para se desenvolver":
                narrator "Entendi que a pressa não era necessária. As melhores conexões se desenvolvem naturalmente, no seu próprio tempo."
                jump capitulo3_final
                
            "Voltar ao menu principal":
                return
                
            "Tentar o Capítulo 3 novamente":
                jump capitulo3