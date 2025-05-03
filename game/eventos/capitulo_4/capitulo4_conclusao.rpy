label capitulo4_conclusao:
    scene bg casa_noite with fade

    narrator "A noite caiu sobre a Rua Aurora, e a casa estava finalmente em silêncio. Depois de uma semana cheia de atividades e interações, parecia que os laços entre todos estavam se fortalecendo."

    narrator "Cada momento compartilhado trouxe algo único, algo que me fez refletir sobre as pessoas ao meu redor e sobre mim mesmo."

    # Reflexão sobre os personagens
    if points_samantha > 0:
        show samantha happy at left
        narrator "Samantha, com sua paixão por jogos e competitividade, me mostrou como é importante se divertir e encontrar alegria nas pequenas coisas. Sua energia era contagiante."
        hide samantha

    if points_nicole > 0:
        show nicole neutral at left
        narrator "Nicole, com sua organização impecável e visão estratégica, me ensinou a importância de planejar e agir com propósito. Apesar de sua postura séria, ela mostrou um lado mais humano."
        hide nicole

    if points_huey > 0:
        show huey happy at left
        narrator "Huey, com sua arte e entusiasmo, me fez perceber a beleza nos pequenos detalhes e a importância de manter a criatividade viva, mesmo em momentos difíceis."
        hide huey

    if points_larissa > 0:
        show larissa happy at left
        narrator "Larissa, com sua energia vibrante e paixão por esportes, me lembrou que cuidar do corpo também é cuidar da mente. Sua determinação era inspiradora."
        hide larissa

    if points_katia > 0:
        show katia neutral at left
        narrator "Katia, com sua personalidade tsundere e amor por filmes de terror, me mostrou que, por trás de uma fachada dura, há sempre algo profundo e significativo esperando para ser descoberto."
        hide katia

    if points_camille > 0:
        show camille gentle at left
        narrator "Camille, com sua serenidade e espiritualidade, me ensinou a importância de encontrar equilíbrio e paz interior, mesmo em meio ao caos da convivência."
        hide camille

    # Reflexão final
    narrator "Esses dias foram um teste de paciência, mas também uma oportunidade de criar laços. Cada interação, cada conversa, cada momento compartilhado foi uma peça importante no quebra-cabeça que é a vida em grupo."

    narrator "Enquanto eu olhava pela janela, vendo as luzes da cidade ao longe, senti que algo estava mudando. Não apenas em mim, mas em todos nós. A convivência estava nos transformando, de formas que talvez ainda não entendêssemos completamente."

    narrator "O semestre ainda estava no início, mas eu sabia que, com essas pessoas ao meu lado, cada dia seria uma nova aventura."

    jump capitulo5