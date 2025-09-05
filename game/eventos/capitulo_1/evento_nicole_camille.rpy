label evento_nicole_camille:
    
    # === EVENTO MELHORADO COM DESENVOLVIMENTO ORGÂNICO ===
    $ feedback_nicole = add_affinity_points("nicole", 5, "Primeira conversa profunda")
    $ feedback_camille = add_affinity_points("camille", 5, "Primeira conexão espiritual")
    
    scene bg cafeteria with dissolve
    show nicole neutral at left
    show camille neutral at right

    narrator "Nicole me convidou para continuar a conversa no café da universidade. Camille também se juntou, atraída pelo tema de sustentabilidade."
    
    # Diálogos contextuais baseados no relacionamento
    $ nicole_dialogue = get_contextual_dialogue("nicole", "casual")
    $ camille_dialogue = get_contextual_dialogue("camille", "casual")

    nicole "[nicole_dialogue] Estou organizando um projeto para ajudar artistas a entender melhor como monetizar sua arte sem perder a essência."
    
    # Momento de vulnerabilidade inicial de Camille
    camille "Sabe... [camille_dialogue] A conexão entre arte e energia é mais profunda do que parece. Às vezes sinto que as pessoas não levam isso a sério..."
    
    # Primeira escolha significativa que afeta o desenvolvimento
    call meaningful_choice(
        "Como responder à vulnerabilidade de Camille?",
        "Mostrar interesse genuíno e perguntar mais sobre suas experiências",
        "Conectar com a visão prática de Nicole sobre monetização",
        "camille", "nicole", 8, 3
    ) from _call_meaningful_choice_1

    narrator "Enquanto tomávamos café, senti que esta conversa estava se tornando algo especial..."
    narrator "Não era apenas sobre projetos - era sobre pessoas reais compartilhando seus sonhos mais profundos."

    # Primeira rodada de escolhas
    menu:
        "Perguntar a Nicole sobre investimento em arte":
            $ points_nicole += 1

        "Falar com Camille sobre chakras e criatividade":
            $ points_camille += 1

        "Sugerir unir espiritualidade e planejamento no mesmo projeto":
            $ points_nicole += 1
            $ points_camille += 1

        "Contar uma ideia sua para um app de meditação com monetização criativa":
            $ points_camille += 1

        "Perguntar como manter autenticidade artística sem se perder no mercado":
            $ points_nicole += 1

        "Perguntar a ambas como lidam com críticas ao trabalho":
            $ points_nicole += 1
            $ points_camille += 1

    narrator "Com cada troca de ideia, sentíamos que havia algo especial naquela conversa."
    nicole "Sabia que muitos artistas desistem cedo por falta de apoio emocional e financeiro?"
    camille "A estrutura importa. Quando corpo e mente estão alinhados, a arte floresce."

    # Segunda rodada de escolhas
    menu:
        "Propor uma ideia para um evento colaborativo entre artistas":
            $ points_nicole += 1
            $ points_camille += 1

        "Perguntar sobre os desafios que enfrentaram em seus projetos":
            $ points_nicole += 1
            $ points_camille += 1

        "Compartilhar uma experiência pessoal sobre criatividade":
            $ points_nicole += 1
            $ points_camille += 1

        "Discutir como a tecnologia pode ajudar artistas a se conectarem":
            $ points_nicole += 1
            $ points_camille += 1

        "Perguntar sobre como equilibrar vida pessoal e profissional":
            $ points_nicole += 1
            $ points_camille += 1

    narrator "Depois de mais uma rodada de café, as ideias começaram a tomar formas mais concretas."
    camille "Eu sonho em criar um espaço holístico para artistas. Um retiro criativo, talvez."
    nicole "E eu penso em uma plataforma com cursos e consultorias que ajudem a profissionalizar sem robotizar."

    # Terceira rodada de escolhas
    menu:
        "Discutir espiritualidade no processo criativo":
            $ points_camille += 1

        "Explorar como o branding pode ser aliado à autenticidade":
            $ points_nicole += 1

        "Sugerir uma série de vídeos com entrevistas a artistas locais":
            $ points_nicole += 1
            $ points_camille += 1

        "Contar sobre um sonho recorrente que te inspira a criar":
            $ points_camille += 1

        "Falar sobre o papel da arte em tempos de crise":
            $ points_nicole += 1
            $ points_camille += 1

    narrator "Por um momento, todos ficaram em silêncio, contemplando o que poderia surgir se unissem forças."

    camille "Já pensou se tudo isso fosse mais do que ideias soltas? E se fosse o início de algo real?"
    nicole "Talvez devêssemos pilotar uma iniciativa em conjunto... uma incubadora de criatividade consciente."
    
    # Transição para o espaço criativo
    scene bg art_room with dissolve
    show nicole neutral at left
    show camille neutral at right

    narrator "A sala estava aconchegante, com luzes suaves e uma atmosfera que convidava à introspecção criativa."

    camille "A energia aqui está ótima hoje. Perfeita pra fluidez criativa."
    nicole "Trouxe alguns materiais pra gente experimentar. A ideia é deixar a intuição guiar."

    menu:
        "Explorar os materiais com Nicole":
            $ points_nicole += 1
            nicole "Esses objetos contam histórias. A criação começa quando a gente escuta."

        "Participar de uma meditação guiada com Camille":
            $ points_camille += 1
            camille "Feche os olhos. Respire... Sinta a inspiração surgir de dentro para fora."

        "Observar as duas trabalhando antes de agir":
            $ points_nicole += 1
            $ points_camille += 1
            narrator "Assisti enquanto Camille traçava padrões em aquarela e Nicole fazia anotações. Era como ver duas linguagens diferentes conversando sem palavras."

    narrator "A sessão avançava, e as criações começaram a tomar forma. Camille propôs uma dinâmica em grupo."

    camille "Vamos fazer uma peça conjunta. Cada um contribui com algo espontâneo, sem julgar, só sentindo."

    menu:
        "Contribuir com um poema livre":
            $ points_camille += 1
            narrator "Escrevi alguns versos rápidos sobre silêncio e transformação. Camille sorriu ao ler."

        "Desenhar um símbolo com tintas vibrantes":
            $ points_nicole += 1
            narrator "Usei cores fortes para pintar um símbolo que parecia pulsar energia. Nicole elogiou a ousadia."

        "Fazer uma colagem com texturas e papel rasgado":
            $ points_nicole += 1
            $ points_camille += 1
            narrator "A mistura de texturas provocou reações diversas. As duas pareciam intrigadas com minha composição."

    narrator "Ao final, Camille sugeriu compartilharmos o que sentimos."

    menu:
        "Falar sobre desbloqueio criativo":
            $ points_camille += 1
            camille "Isso é lindo. Criar é também curar."

        "Refletir sobre propósito artístico":
            $ points_nicole += 1
            nicole "Saber o 'porquê' dá direção ao nosso fazer. Esse espaço foi poderoso."

        "Agradecer pela experiência e escutar":
            $ points_nicole += 1
            $ points_camille += 1
            narrator "Ouvi as reflexões de ambas com atenção. A gratidão pairava no ar."

    # === MOMENTO NAKIGE - CONEXÃO EMOCIONAL PROFUNDA ===
    scene bg art_room with fade
    show nicole happy at left
    show camille gentle at right
    
    # Camille revela algo pessoal (desenvolvimento de personagem)
    camille "Vocês sabem... eu nunca tinha conseguido explicar essas sensações para alguém antes."
    camille "Desde pequena, sinto as energias ao meu redor, mas sempre achei que era 'estranha' demais..."
    
    # Nicole mostra crescimento emocional
    nicole "Camille... eu sempre fui tão focada em números e resultados que esqueci da magia por trás da arte."
    nicole "Hoje você me lembrou de algo que eu tinha perdido."
    
    # Momento de conexão mútua
    call emotional_moment("vulnerability", "camille", "Camille se abre sobre suas inseguranças espirituais") from _call_emotional_moment_evento_nc_2
    
    narrator "O silêncio que se seguiu não era vazio - era repleto de compreensão mútua."
    narrator "Senti que algo fundamental havia mudado entre nós três naquele momento."
    
    # Crescimento mútuo dos personagens
    $ growth_camille = trigger_character_growth("camille", "confidence")
    $ growth_nicole = trigger_character_growth("nicole", "empathy")
    
    narrator "[growth_camille]"
    narrator "[growth_nicole]"
    
    # Promessa de continuidade (foreshadowing)
    camille "Obrigada por... por me ouvirem de verdade."
    nicole "Acho que este é só o começo de algo muito especial."
    
    show screen emotional_moment_notification("💫 Uma amizade verdadeira começou a florescer...")
    pause 3.0
    hide screen emotional_moment_notification
    
    # Memória compartilhada especial
    $ add_shared_memory("artistic_awakening", ["nicole", "camille"], "O momento em que descobrimos a magia da criatividade compartilhada")

    hide nicole
    hide camille
    narrator "Saí da sala com o coração aquecido e a mente cheia de possibilidades."
    narrator "Esta não foi apenas uma tarde de atividades - foi o nascimento de algo que mudaria todos nós."

    jump capitulo1_final
