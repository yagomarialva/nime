label capitulo2:
    if "capitulo2" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo2")
    scene bg campus_day with fade
    narrator "O segundo capítulo do semestre começou com uma energia renovada no campus. O grupo de amigos começava a se conhecer melhor, e novas possibilidades surgiam a cada dia."

    # Primeiro dia de interações
    menu:
        "Passar um tempo com Samantha no laboratório de tecnologia":
            jump evento_samantha_larissa_lab

        "Ajudar Nicole e Camille com ideias para o projeto de sustentabilidade":
            jump evento_nicole_camille_lab

        "Acompanhar Huey e Katia numa feira de arte independente":
            jump evento_huey_katia_feira

    # Segundo dia de interações
    label segundo_dia_interacoes:
    scene bg campus_day with fade
    narrator "No dia seguinte, novas oportunidades surgiram para explorar ideias e laços com mais colegas."

    menu:
        "Participar de uma atividade esportiva criativa com Larissa e Huey":
            jump evento_larissa_huey_esporte

        "Ir a um passeio cultural com Katia e Nicole":
            jump evento_katia_nicole_cultura

    # Terceiro dia: evento individual
    label terceiro_dia_escolha:
    scene bg campus_day with fade
    narrator "No terceiro dia, uma escolha mais íntima surgiu: um tempo a sós com alguém para se conectar em outro nível."

    menu:
        "Passar um tempo sozinho com Samantha":
            jump evento_individual_samantha

        "Ter uma conversa profunda com Nicole":
            jump evento_individual_nicole

        "Passar uma tarde relaxante com Huey":
            jump evento_individual_huey

        "Explorar o parque com Larissa":
            jump evento_individual_larissa

        "Tomar um café reflexivo com Katia":
            jump evento_individual_katia

        "Participar de uma meditação com Camille":
            jump evento_individual_camille

    jump capitulo2_conclusao
