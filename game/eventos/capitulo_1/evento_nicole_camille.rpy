label evento_nicole_camille:
    
    # === EVENTO MELHORADO COM CONFLITO ORGÂNICO ===
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
    
    # Primeira tensão: Nicole foca em resultados, Camille em energia
    camille "Sabe... [camille_dialogue] A conexão entre arte e energia é mais profunda do que parece. Às vezes sinto que as pessoas não levam isso a sério..."
    
    # Nicole responde com ceticismo prático
    nicole "Energia? Camille, precisamos de dados concretos, métricas, resultados mensuráveis. Como vamos medir o sucesso se não tivermos indicadores claros?"
    
    # Camille fica defensiva
    camille "Nicole, nem tudo na vida pode ser medido com números! Existe uma intuição, uma energia que guia as pessoas..."
    
    # Primeira escolha significativa que afeta o desenvolvimento
    call meaningful_choice(
        "Como mediar essa discussão?",
        "Defender a abordagem de Nicole sobre dados e métricas",
        "Apoiar a visão espiritual de Camille sobre energia",
        "nicole", "camille", 8, 3
    ) from _call_meaningful_choice_1

    narrator "Enquanto tomávamos café, senti que esta conversa estava se tornando algo especial..."
    narrator "Não era apenas sobre projetos - era sobre duas visões de mundo muito diferentes tentando se entender."

    # Primeira rodada de escolhas
    menu:
        "Perguntar a Nicole sobre como medir o impacto emocional":
            $ points_nicole += 1
            nicole "Boa pergunta! Podemos usar pesquisas de satisfação, feedback qualitativo, indicadores de engajamento..."

        "Falar com Camille sobre como a energia se manifesta na prática":
            $ points_camille += 1
            camille "Você sente quando algo está 'certo', sabe? É como uma vibração que te guia..."

        "Sugerir unir dados objetivos com percepções subjetivas":
            $ points_nicole += 1
            $ points_camille += 1
            narrator "Ambas parecem interessadas na ideia de combinar abordagens."

        "Contar uma experiência onde a intuição te guiou":
            $ points_camille += 1
            camille "Exato! Às vezes você sabe que algo vai dar certo antes mesmo de ter os dados..."

        "Perguntar como Nicole lida com situações onde os dados não explicam tudo":
            $ points_nicole += 1
            nicole "Hmm... confesso que isso me incomoda. Prefiro ter controle total sobre as variáveis."

        "Perguntar a ambas como lidam com incertezas":
            $ points_nicole += 1
            $ points_camille += 1
            narrator "Ambas compartilham suas estratégias para lidar com o desconhecido."

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
    camille "Eu sonho em criar um espaço holístico para pessoas. Um lugar onde a energia flui naturalmente."
    nicole "E eu penso em uma plataforma com cursos e consultorias que ajudem a profissionalizar sem perder a essência humana."

    # Terceira rodada de escolhas
    menu:
        "Discutir como medir o sucesso de projetos holísticos":
            $ points_camille += 1
            camille "O sucesso não é só números... é sobre transformação, sobre pessoas se sentindo completas."

        "Explorar como dados podem validar experiências subjetivas":
            $ points_nicole += 1
            nicole "Podemos criar métricas para medir bem-estar, satisfação, crescimento pessoal..."

        "Sugerir uma série de vídeos com entrevistas sobre diferentes abordagens":
            $ points_nicole += 1
            $ points_camille += 1
            narrator "Ambas gostaram da ideia de mostrar diferentes perspectivas."

        "Contar sobre uma experiência onde a intuição te guiou":
            $ points_camille += 1
            camille "Exato! Às vezes você sabe que algo vai dar certo antes mesmo de ter os dados..."

        "Falar sobre o papel da intuição em decisões importantes":
            $ points_nicole += 1
            $ points_camille += 1
            narrator "Ambas compartilham suas experiências com intuição e dados."

    narrator "Por um momento, todos ficaram em silêncio, contemplando o que poderia surgir se unissem forças."

    camille "Já pensou se tudo isso fosse mais do que ideias soltas? E se fosse o início de algo real?"
    nicole "Talvez devêssemos pilotar uma iniciativa em conjunto... uma incubadora de projetos conscientes."
    
    # Transição para um espaço neutro - biblioteca
    scene bg library with dissolve
    show nicole neutral at left
    show camille neutral at right

    narrator "A biblioteca estava silenciosa, com luzes suaves e uma atmosfera que convidava à reflexão profunda."

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

    narrator "A sessão avançava, e as ideias começaram a tomar forma. Camille propôs uma dinâmica em grupo."

    camille "Vamos fazer uma atividade conjunta. Cada um contribui com algo espontâneo, sem julgar, só sentindo."

    menu:
        "Contribuir com uma ideia sobre energia e dados":
            $ points_camille += 1
            narrator "Escrevi algumas ideias sobre como medir energia através de dados. Camille sorriu ao ler."

        "Desenhar um diagrama sobre intuição vs. lógica":
            $ points_nicole += 1
            narrator "Usei cores fortes para criar um diagrama que mostrava a interseção entre intuição e dados. Nicole elogiou a clareza."

        "Fazer uma colagem com diferentes abordagens":
            $ points_nicole += 1
            $ points_camille += 1
            narrator "A mistura de abordagens provocou reações diversas. As duas pareciam intrigadas com minha composição."

    narrator "Ao final, Camille sugeriu compartilharmos o que sentimos."

    menu:
        "Falar sobre como unir intuição e dados":
            $ points_camille += 1
            camille "Isso é lindo. Unir diferentes perspectivas é também curar."

        "Refletir sobre propósito de projetos conscientes":
            $ points_nicole += 1
            nicole "Saber o 'porquê' dá direção ao nosso fazer. Esse espaço foi poderoso."

        "Agradecer pela experiência e escutar":
            $ points_nicole += 1
            $ points_camille += 1
            narrator "Ouvi as reflexões de ambas com atenção. A gratidão pairava no ar."

    # === MOMENTO NAKIGE - CONEXÃO EMOCIONAL PROFUNDA ===
    scene bg library with fade
    show nicole happy at left
    show camille gentle at right
    
    # Camille revela algo pessoal (desenvolvimento de personagem)
    camille "Vocês sabem... eu nunca tinha conseguido explicar essas sensações para alguém antes."
    camille "Desde pequena, sinto as energias ao meu redor, mas sempre achei que era 'estranha' demais..."
    
    # Nicole mostra crescimento emocional
    nicole "Camille... eu sempre fui tão focada em números e resultados que esqueci da magia por trás das conexões humanas."
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
    scene bg campus_sunset with fade
    camille "Obrigada por... por me ouvirem de verdade."
    nicole "Acho que este é só o começo de algo muito especial."
    
    show screen emotional_moment_notification("💫 Uma amizade verdadeira começou a florescer...")
    pause 3.0
    hide screen emotional_moment_notification
    
    # Memória compartilhada especial
    $ add_shared_memory("conscious_awakening", ["nicole", "camille"], "O momento em que descobrimos a magia da conexão entre dados e energia")

    hide nicole
    hide camille
    narrator "Saí da biblioteca com o coração aquecido e a mente cheia de possibilidades."
    narrator "Esta não foi apenas uma tarde de conversas - foi o nascimento de algo que mudaria todos nós."

    jump capitulo1_final
