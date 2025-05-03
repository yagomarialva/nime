# Inicializa a variável global para rastrear interações realizadas
default interacoes_realizadas = []
label capitulo4:
    scene bg casa_morning with fade
    narrator "A rotina começa a se instalar na república da Rua Aurora. As manhãs são barulhentas, os banheiros sempre ocupados, e o café nunca é suficiente para todos."

    show nicole neutral at left
    nicole "Quem usou meu adoçante orgânico sem avisar?!"

    show samantha neutral at center
    samantha "Sei lá, parecia uma poção de mana."

    show larissa happy at right
    larissa "Gente, hoje é dia de agachamento coletivo, hein!"

    show katia neutral at left
    katia "Se me chamar pra isso de novo, vou tacar meu DVD do Exorcista na sua cara."

    show huey happy at center
    huey "Posso pintar esse momento? É caos puro."

    show camille gentle at right
    camille "A energia dessa casa precisa de alinhamento… e talvez de chá de lavanda."

    hide nicole
    hide samantha
    hide larissa
    hide katia
    hide huey
    hide camille

    narrator "Apesar do caos, você começa a perceber que a convivência está criando laços inesperados entre todos. Pequenos momentos de interação tornam os dias mais interessantes."

    # Inicializa a lista de interações realizadas
    $ interacoes_realizadas = []

    jump capitulo4_interacoes_diarias

label capitulo4_interacoes_diarias:
    scene bg sala_casa with dissolve
    narrator "Durante a semana, você tem a chance de interagir com os colegas em momentos casuais. Cada interação revela algo novo sobre eles."

    # Verifica se todas as interações foram realizadas
    if len(interacoes_realizadas) == 6:
        jump capitulo4_decisao_fim_de_semana

    menu:
        "Ajudar Samantha a configurar um jogo" if "samantha" not in interacoes_realizadas:
            $ interacoes_realizadas.append("samantha")
            $ points_samantha += 3
            jump interacao_samantha
        "Acompanhar Nicole em uma ida ao mercado" if "nicole" not in interacoes_realizadas:
            $ interacoes_realizadas.append("nicole")
            $ points_nicole += 3
            jump interacao_nicole
        "Assistir Larissa treinar no quintal" if "larissa" not in interacoes_realizadas:
            $ interacoes_realizadas.append("larissa")
            $ points_larissa += 3
            jump interacao_larissa
        "Conversar com Huey sobre arte" if "huey" not in interacoes_realizadas:
            $ interacoes_realizadas.append("huey")
            $ points_huey += 3
            jump interacao_huey
        "Ajudar Katia a organizar sua coleção de filmes" if "katia" not in interacoes_realizadas:
            $ interacoes_realizadas.append("katia")
            $ points_katia += 3
            jump interacao_katia
        "Meditar com Camille no jardim" if "camille" not in interacoes_realizadas:
            $ interacoes_realizadas.append("camille")
            $ points_camille += 3
            jump interacao_camille


label capitulo4_decisao_fim_de_semana:
    scene bg sala_casa with dissolve
    narrator "Com o fim de semana chegando, a casa decide que cada um deve organizar uma atividade para todo o grupo. O jogador deve escolher qual participar."

    menu:
        "Caminhada mística com Camille":
            $ points_camille += 3
            jump caminhada_camille
        "Maratona de filmes de terror com Katia":
            $ points_katia += 3
            jump filmes_katia
        "Torneio de boardgames com Samantha":
            $ points_samantha += 3
            jump boardgames_samantha
        "Oficina de arte livre com Huey":
            $ points_huey += 3
            jump arte_huey
        "Aulão funcional com Larissa":
            $ points_larissa += 3
            jump funcional_larissa
        "Workshop de finanças criativas com Nicole":
            $ points_nicole += 3
            jump financas_nicole


