label capitulo2:
    if "capitulo2" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo2")
    
    scene bg campus_day with fade
    narrator "O segundo capítulo do semestre começou com uma energia renovada no campus. O grupo de amigos começava a se conhecer melhor, e novas possibilidades surgiam a cada dia."
    
    # Momento emocional de conexão mais profunda
    call emotional_moment("deepening_bonds", None, "Os laços começam a se aprofundar no segundo capítulo") from _call_emotional_moment_cap2_1
    
    narrator "Após as primeiras interações do Capítulo 1, senti que algo havia mudado. As conversas não eram mais apenas sobre apresentações - havia uma curiosidade genuína sobre quem cada um realmente era."
    
    # Apresentação melhorada do contexto
    show samantha happy at left
    samantha "Olha só, parece que estamos todos mais à vontade agora, né?"
    samantha "É incrível como algumas conversas podem mudar completamente a dinâmica de um grupo."
    hide samantha
    
    show nicole neutral at right
    nicole "Concordo. Há uma diferença entre conhecer alguém superficialmente e realmente... conectá-los."
    nicole "Estou curiosa para ver como essas conexões vão evoluir."
    hide nicole

    # Primeiro dia de interações
    narrator "O primeiro dia ofereceu oportunidades para explorar diferentes aspectos da vida universitária. Cada escolha prometia descobertas únicas."
    
    menu:
        "Passar um tempo com Samantha no laboratório de tecnologia (Explorar inovação e criatividade)":
            $ add_shared_memory("lab_technology_exploration", ["samantha", "larissa"], "Primeira exploração tecnológica em grupo")
            $ add_affinity_points("samantha", 8, "Interesse em tecnologia")
            $ add_affinity_points("larissa", 8, "Interesse em inovação")
            jump evento_samantha_larissa_lab

        "Ajudar Nicole e Camille com ideias para o projeto de sustentabilidade (Conectar estratégia e consciência)":
            $ add_shared_memory("sustainability_project", ["nicole", "camille"], "Primeiro projeto colaborativo de sustentabilidade")
            $ add_affinity_points("nicole", 8, "Interesse em projetos estratégicos")
            $ add_affinity_points("camille", 8, "Interesse em sustentabilidade")
            jump evento_nicole_camille_lab

        "Acompanhar Huey e Katia numa feira de arte independente (Mergulhar na expressão artística)":
            $ add_shared_memory("art_fair_exploration", ["huey", "katia"], "Primeira exploração de arte independente")
            $ add_affinity_points("huey", 8, "Interesse em arte")
            $ add_affinity_points("katia", 8, "Interesse em arte independente")
            jump evento_huey_katia_feira

    # Segundo dia de interações
    label segundo_dia_interacoes:
    scene bg campus_day with fade
    narrator "No dia seguinte, novas oportunidades surgiram para explorar ideias e laços com mais colegas."
    
    # Momento de reflexão sobre as conexões
    call emotional_moment("growing_connections", None, "As conexões começam a se fortalecer") from _call_emotional_moment_cap2_2
    
    narrator "Cada interação do dia anterior havia plantado sementes de curiosidade. Agora, era hora de vê-las florescer em novas formas de conexão."

    menu:
        "Participar de uma atividade esportiva criativa com Larissa e Huey (Unir movimento e expressão artística)":
            $ add_shared_memory("creative_sports_activity", ["larissa", "huey"], "Primeira atividade que combina esporte e arte")
            $ add_affinity_points("larissa", 8, "Interesse em atividades criativas")
            $ add_affinity_points("huey", 8, "Interesse em expressão corporal")
            jump evento_larissa_huey_esporte

        "Ir a um passeio cultural com Katia e Nicole (Explorar arte e estratégia)":
            $ add_shared_memory("cultural_exploration", ["katia", "nicole"], "Primeira exploração cultural em grupo")
            $ add_affinity_points("katia", 8, "Interesse em cultura")
            $ add_affinity_points("nicole", 8, "Interesse em análise cultural")
            jump evento_katia_nicole_cultura

    # Terceiro dia: evento individual
    label terceiro_dia_escolha:
    scene bg campus_day with fade
    narrator "No terceiro dia, uma escolha mais íntima surgiu: um tempo a sós com alguém para se conectar em outro nível."
    
    # Momento emocional de intimidade
    call emotional_moment("intimate_connection", None, "Momento de conexão mais íntima e pessoal") from _call_emotional_moment_cap2_3
    
    narrator "Após dois dias de interações em grupo, senti que era hora de aprofundar uma conexão específica. Cada pessoa oferecia algo único, e eu queria descobrir mais sobre quem realmente eram."

    menu:
        "Passar um tempo sozinho com Samantha (Explorar criatividade e tecnologia)":
            $ add_shared_memory("intimate_tech_exploration", ["samantha"], "Primeiro momento íntimo explorando tecnologia")
            $ add_affinity_points("samantha", 12, "Conexão íntima e pessoal")
            jump evento_individual_samantha

        "Ter uma conversa profunda com Nicole (Estratégia e crescimento pessoal)":
            $ add_shared_memory("deep_strategic_conversation", ["nicole"], "Primeira conversa profunda sobre estratégia e vida")
            $ add_affinity_points("nicole", 12, "Conexão íntima e pessoal")
            jump evento_individual_nicole

        "Passar uma tarde relaxante com Huey (Arte e natureza)":
            $ add_shared_memory("peaceful_artistic_moment", ["huey"], "Primeiro momento de paz e arte compartilhado")
            $ add_affinity_points("huey", 12, "Conexão íntima e pessoal")
            jump evento_individual_huey

        "Explorar o parque com Larissa (Energia e movimento)":
            $ add_shared_memory("energetic_park_exploration", ["larissa"], "Primeira exploração energética do parque")
            $ add_affinity_points("larissa", 12, "Conexão íntima e pessoal")
            jump evento_individual_larissa

        "Tomar um café reflexivo com Katia (Arte e cinema)":
            $ add_shared_memory("reflective_cinema_conversation", ["katia"], "Primeira conversa reflexiva sobre cinema e arte")
            $ add_affinity_points("katia", 12, "Conexão íntima e pessoal")
            jump evento_individual_katia

        "Participar de uma meditação com Camille (Paz e espiritualidade)":
            $ add_shared_memory("spiritual_meditation_moment", ["camille"], "Primeiro momento espiritual compartilhado")
            $ add_affinity_points("camille", 12, "Conexão íntima e pessoal")
            jump evento_individual_camille

    jump capitulo2_final
