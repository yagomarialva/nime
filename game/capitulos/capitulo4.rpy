# Inicializa a variável global para rastrear interações realizadas
default interacoes_realizadas = []
label capitulo4:
    if "capitulo4" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo4")
    
    scene bg casa_morning with fade
    narrator "A rotina começa a se instalar na república da Rua Aurora. As manhãs são barulhentas, os banheiros sempre ocupados, e o café nunca é suficiente para todos."
    
    # Momento emocional de rotina estabelecida
    call emotional_moment("routine_established", None, "A rotina da convivência se estabelece e os laços se aprofundam") from _call_emotional_moment_cap4_1
    
    narrator "Mas havia algo especial nesse caos matinal. Era o som de uma família se formando, de pessoas que estavam aprendendo a viver juntas."

    show nicole neutral at left
    nicole "Quem usou meu adoçante orgânico sem avisar?!"
    nicole "Bem... pelo menos alguém está se alimentando de forma saudável."
    $ add_affinity_points("nicole", 2, "Aceitação da convivência")
    hide nicole

    show samantha neutral at center
    samantha "Sei lá, parecia uma poção de mana."
    samantha "Mas é legal ter gente que entende minhas referências de jogos!"
    $ add_affinity_points("samantha", 2, "Conexão através de referências")
    hide samantha

    show larissa happy at right
    larissa "Gente, hoje é dia de agachamento coletivo, hein!"
    larissa "Quem quiser se juntar, é só aparecer! Vai ser divertido!"
    $ add_affinity_points("larissa", 2, "Energia contagiante")
    hide larissa

    show katia neutral at left
    katia "Se me chamar pra isso de novo, vou tacar meu DVD do Exorcista na sua cara."
    katia "N-não é como se eu não gostasse de vocês ou qualquer coisa assim! É só que... prefiro filmes."
    $ add_affinity_points("katia", 2, "Reação tsundere à convivência")
    hide katia

    show huey happy at center
    huey "Posso pintar esse momento? É caos puro."
    huey "Mas é um caos lindo! Cada pessoa aqui é uma obra de arte!"
    $ add_affinity_points("huey", 2, "Apreciação artística da convivência")
    hide huey

    show camille gentle at right
    camille "A energia dessa casa precisa de alinhamento… e talvez de chá de lavanda."
    camille "Mas há algo especial aqui. Uma energia de família que está se formando."
    $ add_affinity_points("camille", 2, "Conexão espiritual com a casa")
    hide camille

    narrator "Apesar do caos, você começa a perceber que a convivência está criando laços inesperados entre todos. Pequenos momentos de interação tornam os dias mais interessantes."

    # Inicializa a lista de interações realizadas
    $ interacoes_realizadas = []

    jump capitulo4_interacoes_diarias

label capitulo4_interacoes_diarias:
    scene bg sala_casa with dissolve
    narrator "Durante a semana, você tem a chance de interagir com os colegas em momentos casuais. Cada interação revela algo novo sobre eles."
    
    # Momento emocional de conexões diárias
    call emotional_moment("daily_connections", None, "Conexões diárias que fortalecem os laços") from _call_emotional_moment_cap4_2
    
    narrator "Cada dia trazia novas oportunidades de conhecer melhor essas pessoas incríveis que haviam se tornado parte da minha vida."

    # Verifica se todas as interações foram realizadas
    if len(interacoes_realizadas) == 6:
        jump capitulo4_decisao_fim_de_semana

    menu:
        "Ajudar Samantha a configurar um jogo (Explorar tecnologia e criatividade)" if "samantha" not in interacoes_realizadas:
            $ interacoes_realizadas.append("samantha")
            $ add_shared_memory("daily_gaming_setup", ["samantha"], "Configuração de jogo em um momento casual")
            $ add_affinity_points("samantha", 6, "Ajuda com tecnologia")
            jump interacao_samantha
            
        "Acompanhar Nicole em uma ida ao mercado (Organização e estratégia)" if "nicole" not in interacoes_realizadas:
            $ interacoes_realizadas.append("nicole")
            $ add_shared_memory("daily_market_trip", ["nicole"], "Ida ao mercado em companhia")
            $ add_affinity_points("nicole", 6, "Companhia no mercado")
            jump interacao_nicole
            
        "Assistir Larissa treinar no quintal (Energia e movimento)" if "larissa" not in interacoes_realizadas:
            $ interacoes_realizadas.append("larissa")
            $ add_shared_memory("daily_training_support", ["larissa"], "Apoio durante o treino")
            $ add_affinity_points("larissa", 6, "Apoio no treino")
            jump interacao_larissa
            
        "Conversar com Huey sobre arte (Criatividade e expressão)" if "huey" not in interacoes_realizadas:
            $ interacoes_realizadas.append("huey")
            $ add_shared_memory("daily_art_conversation", ["huey"], "Conversa sobre arte em momento casual")
            $ add_affinity_points("huey", 6, "Conversa sobre arte")
            jump interacao_huey
            
        "Ajudar Katia a organizar sua coleção de filmes (Arte e organização)" if "katia" not in interacoes_realizadas:
            $ interacoes_realizadas.append("katia")
            $ add_shared_memory("daily_movie_organization", ["katia"], "Organização da coleção de filmes")
            $ add_affinity_points("katia", 6, "Ajuda com organização")
            jump interacao_katia
            
        "Meditar com Camille no jardim (Paz e espiritualidade)" if "camille" not in interacoes_realizadas:
            $ interacoes_realizadas.append("camille")
            $ add_shared_memory("daily_meditation", ["camille"], "Meditação compartilhada no jardim")
            $ add_affinity_points("camille", 6, "Meditação compartilhada")
            jump interacao_camille


label capitulo4_decisao_fim_de_semana:
    scene bg sala_casa with dissolve
    narrator "Com o fim de semana chegando, a casa decide que cada um deve organizar uma atividade para todo o grupo. O jogador deve escolher qual participar."
    
    # Momento emocional de atividades em grupo
    call emotional_moment("group_activities", None, "Atividades em grupo que fortalecem os laços familiares") from _call_emotional_moment_cap4_3
    
    narrator "Cada pessoa havia preparado algo especial para compartilhar com todos. Era uma oportunidade única de ver como cada uma expressava sua paixão e personalidade."

    menu:
        "Caminhada mística com Camille (Espiritualidade e conexão com a natureza)":
            $ add_shared_memory("weekend_mystical_walk", ["camille"], "Caminhada mística de fim de semana")
            $ add_affinity_points("camille", 8, "Atividade espiritual em grupo")
            jump caminhada_camille
            
        "Maratona de filmes de terror com Katia (Arte e entretenimento)":
            $ add_shared_memory("weekend_horror_marathon", ["katia"], "Maratona de filmes de terror")
            $ add_affinity_points("katia", 8, "Atividade cinematográfica em grupo")
            jump filmes_katia
            
        "Torneio de boardgames com Samantha (Competição e diversão)":
            $ add_shared_memory("weekend_boardgame_tournament", ["samantha"], "Torneio de boardgames")
            $ add_affinity_points("samantha", 8, "Atividade competitiva em grupo")
            jump boardgames_samantha
            
        "Oficina de arte livre com Huey (Criatividade e expressão)":
            $ add_shared_memory("weekend_art_workshop", ["huey"], "Oficina de arte livre")
            $ add_affinity_points("huey", 8, "Atividade artística em grupo")
            jump arte_huey
            
        "Aulão funcional com Larissa (Energia e movimento)":
            $ add_shared_memory("weekend_functional_training", ["larissa"], "Aulão funcional")
            $ add_affinity_points("larissa", 8, "Atividade física em grupo")
            jump funcional_larissa
            
        "Workshop de finanças criativas com Nicole (Estratégia e planejamento)":
            $ add_shared_memory("weekend_finance_workshop", ["nicole"], "Workshop de finanças criativas")
            $ add_affinity_points("nicole", 8, "Atividade estratégica em grupo")
            jump financas_nicole

    jump capitulo4_final


