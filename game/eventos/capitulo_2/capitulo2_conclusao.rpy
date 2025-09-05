label capitulo2_final:
    scene bg campus_sunset with fade

    narrator "O sol começava a se pôr, tingindo o campus com tons dourados e alaranjados. Era o fim de mais um dia, e também o encerramento de um capítulo cheio de descobertas e conexões."

    # Momento emocional de reflexão
    call emotional_moment("chapter_reflection", None, "Reflexão sobre as conexões formadas no Capítulo 2") from _call_emotional_moment_cap2_4

    narrator "Ao longo dos últimos dias, tive a chance de conhecer melhor cada um dos meus colegas. Cada interação trouxe algo único, algo que me fez refletir sobre mim mesmo e sobre os outros."

    # Reflexão sobre os personagens com mais profundidade
    if points_samantha > 0:
        show samantha happy at left
        narrator "Samantha me mostrou o poder da criatividade e da paixão por tecnologia. Sua energia era contagiante, e suas ideias, inspiradoras."
        samantha "É incrível como a tecnologia pode ser uma ferramenta para conectar pessoas, não apenas dispositivos."
        narrator "Ela me ensinou que por trás de cada linha de código, há uma história humana esperando para ser contada."
        hide samantha

    if points_nicole > 0:
        show nicole neutral at left
        narrator "Nicole, com sua visão estratégica e determinação, me ensinou a importância de planejar e agir com propósito. Apesar de sua postura séria, ela mostrou um lado mais humano."
        nicole "Às vezes, a melhor estratégia é simplesmente ser autêntico. As pessoas conseguem sentir quando você está sendo verdadeiro."
        narrator "Ela me mostrou que por trás de cada plano, há um coração que busca conexão genuína."
        hide nicole

    if points_huey > 0:
        show huey neutral at left
        narrator "Huey, com sua conexão com a arte e a natureza, me fez perceber a beleza nos pequenos detalhes da vida. Sua calma era reconfortante."
        huey "A arte não precisa ser grandiosa para tocar o coração. Às vezes, um simples gesto pode mudar tudo."
        narrator "Ele me ensinou que a verdadeira beleza está na simplicidade e na autenticidade."
        hide huey

    if points_larissa > 0:
        show larissa happy at left
        narrator "Larissa, com sua energia vibrante e paixão por esportes, me lembrou da importância de se manter ativo e positivo, mesmo diante dos desafios."
        larissa "O movimento não é apenas físico - é também emocional. Quando nos movemos juntos, criamos algo maior que nós mesmos."
        narrator "Ela me mostrou que a energia positiva é contagiosa e pode transformar qualquer ambiente."
        hide larissa

    if points_katia > 0:
        show katia neutral at left
        narrator "Katia, com sua personalidade reservada e amor pela arte, me mostrou que há profundidade em cada gesto e que a expressão pode assumir muitas formas."
        katia "N-não é como se eu me importasse com o que você pensa ou qualquer coisa assim... mas você tem um gosto decente."
        narrator "Ela me ensinou que por trás de cada fachada, há uma pessoa complexa esperando para ser compreendida."
        hide katia

    if points_camille > 0:
        show camille neutral at left
        narrator "Camille, com sua serenidade e sabedoria, me ensinou a importância de encontrar equilíbrio e paz interior, mesmo em meio ao caos."
        camille "A paz não é a ausência de turbulência, mas a capacidade de encontrar calma dentro dela."
        narrator "Ela me mostrou que a verdadeira força vem da capacidade de permanecer centrado em meio às tempestades da vida."
        hide camille

    # Retrospectiva dos relacionamentos
    narrator "Cada momento compartilhado foi uma peça importante no quebra-cabeça que é a vida universitária. E, de alguma forma, senti que esses laços estavam apenas começando a se formar."

    # Mostrar resumo dos relacionamentos
    $ relationship_summary = get_relationship_summary()
    narrator "Vamos ver como estão os relacionamentos até agora:"
    
    python:
        for summary in relationship_summary:
            renpy.say(narrator, summary)

    # Verificar se pode progredir para o próximo capítulo
    $ can_progress, progress_message = check_chapter_progression_requirement(2)
    
    if can_progress:
        # Momento emocional de realização
        call emotional_moment("chapter_achievement", None, "Realização de ter criado conexões suficientes para continuar") from _call_emotional_moment_cap2_5
        
        narrator "[progress_message]"
        narrator "Enquanto o sol desaparecia no horizonte, senti uma mistura de gratidão e expectativa pelo que estava por vir. O semestre ainda tinha muito a oferecer, e eu estava pronto para enfrentar o que viesse."
        
        show samantha happy at left
        samantha "Parece que estamos todos mais conectados agora, né?"
        hide samantha
        
        show nicole neutral at right
        nicole "Sim, há algo especial acontecendo aqui. Algo que vai além de simples colegas de classe."
        hide nicole
        
        narrator "Era verdade. Algo mágico estava acontecendo entre nós - uma conexão que transcendeu as barreiras iniciais e criou algo genuinamente especial."
        
        jump capitulo3
    else:
        # Momento emocional de crescimento
        call emotional_moment("growth_opportunity", None, "Oportunidade de crescimento através da reflexão") from _call_emotional_moment_cap2_6
        
        narrator "[progress_message]"
        narrator "Enquanto o sol desaparecia no horizonte, senti que ainda havia muito a descobrir sobre essas pessoas incríveis que haviam entrado na minha vida."
        
        show katia neutral at left
        katia "N-não é como se eu estivesse preocupada ou qualquer coisa assim... mas talvez precisemos de mais tempo para nos conhecer melhor."
        hide katia
        
        show camille neutral at right
        camille "Cada conexão tem seu próprio ritmo. Não há pressa em descobrir o que o futuro nos reserva."
        hide camille
        
        narrator "Ela estava certa. Algumas conexões levam tempo para florescer, e talvez eu precisasse ser mais paciente e atento às oportunidades que ainda estavam por vir."
        
        menu:
            "Refletir sobre as conexões que ainda precisam ser exploradas":
                narrator "Decidi dedicar mais tempo a conhecer melhor cada pessoa. Cada interação era uma oportunidade de descobrir algo novo."
                jump capitulo2_final
                
            "Aceitar que algumas conexões levam tempo para se desenvolver":
                narrator "Entendi que a pressa não era necessária. As melhores conexões se desenvolvem naturalmente, no seu próprio tempo."
                jump capitulo2_final
                
            "Voltar ao menu principal":
                return
                
            "Tentar o Capítulo 2 novamente":
                jump capitulo2