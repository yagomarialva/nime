# === QUARTA ESCOLHA - QUESTIONÁRIO DE CONEXÕES FUTURAS ===
label capitulo1_quarta_escolha:
    scene bg campus_morning with fade
    
    # Inicializar variáveis do sistema de conexões futuras
    $ connection_interests = {"analytical": False, "creative": False, "social": False}
    $ connection_style = {"independent": False, "collaborative": False, "leadership": False}
    $ connection_environment = {"quiet": False, "dynamic": False, "creative": False}
    $ connection_approach = {"analytical": False, "intuitive": False, "adaptive": False}
    $ connection_impact = {"efficiency": False, "community": False, "innovation": False}
    $ chosen_connection = ""
    $ future_team = []
    $ connection_description = ""
    $ connection_benefits = ""
    
    narrator "O quarto dia na Faculdade Solária havia começado. Após as experiências incríveis dos dias anteriores, senti que era hora de refletir sobre o futuro."
    narrator "O Professor Wendell havia me convidado para uma conversa especial sobre desenvolvimento pessoal e conexões humanas."
    
    scene bg sala_reuniao with fade
    show professor_wendell neutral at center
    
    narrator "Encontrei o Professor Wendell em seu escritório, organizando alguns documentos. Ele parecia estar esperando por alguém."
    
    professor_wendell "Ah, você! Estava esperando sua visita. Após observar suas interações nos últimos dias, tenho algumas ideias sobre seu desenvolvimento pessoal."
    professor_wendell "Acredito que seria interessante fazer um questionário para entender melhor seus interesses e como você pode se conectar com diferentes pessoas no campus."
    professor_wendell "Isso nos ajudará a identificar quais áreas e pessoas podem ser mais significativas para seu crescimento nos próximos capítulos da sua jornada."
    
    narrator "O Professor Wendell se acomodou em sua cadeira e pegou um formulário. Sua expressão era séria, mas acolhedora."
    
    professor_wendell "Primeiro, me conte sobre seus interesses acadêmicos. O que mais te motiva nos estudos?"
    
    menu:
        "Análise de dados e metodologia":
            $ connection_interests["analytical"] = True
            $ connection_interests["creative"] = False
            $ connection_interests["social"] = False
            narrator "Mencionei minha paixão por análise de dados, metodologia e estruturas organizacionais."
            professor_wendell "Interessante... uma mente analítica. Isso pode criar conexões muito especiais com pessoas que valorizam a precisão e organização."
            
        "Arte e expressão criativa":
            $ connection_interests["analytical"] = False
            $ connection_interests["creative"] = True
            $ connection_interests["social"] = False
            narrator "Falei sobre meu interesse em arte, criatividade e expressão visual."
            professor_wendell "Fascinante... a criatividade é uma linguagem universal que conecta pessoas de formas únicas."
            
        "Interação social e comunicação":
            $ connection_interests["analytical"] = False
            $ connection_interests["creative"] = False
            $ connection_interests["social"] = True
            narrator "Comentei sobre minha paixão por interação social, comunicação e trabalho em equipe."
            professor_wendell "Excelente... as conexões humanas são o coração de qualquer jornada significativa."
    
    professor_wendell "Agora, me conte sobre seu estilo de interação preferido. Como você gosta de se conectar com as pessoas?"
    
    menu:
        "Conversas profundas e individuais":
            $ connection_style["independent"] = True
            $ connection_style["collaborative"] = False
            $ connection_style["leadership"] = False
            narrator "Mencionei que prefiro conversas profundas e individuais, com foco e concentração."
            professor_wendell "Entendo... conexões íntimas e pessoais. Muito valioso para o crescimento mútuo."
            
        "Interações em grupo e colaborativas":
            $ connection_style["independent"] = False
            $ connection_style["collaborative"] = True
            $ connection_style["leadership"] = False
            narrator "Falei sobre minha preferência por interações em grupo e colaboração."
            professor_wendell "Perfeito... as conexões em grupo são fundamentais para criar uma comunidade forte."
            
        "Liderança e coordenação de atividades":
            $ connection_style["independent"] = False
            $ connection_style["collaborative"] = False
            $ connection_style["leadership"] = True
            narrator "Comentei sobre minha paixão por liderança e coordenação de atividades."
            professor_wendell "Impressionante... líderes natos são raros e podem inspirar muitos ao seu redor."
    
    professor_wendell "Qual tipo de ambiente você considera mais propício para criar conexões significativas?"
    
    menu:
        "Ambiente silencioso e contemplativo":
            $ connection_environment["quiet"] = True
            $ connection_environment["dynamic"] = False
            $ connection_environment["creative"] = False
            narrator "Mencionei que prefiro ambientes silenciosos e contemplativos para conversas profundas."
            professor_wendell "Compreensível... a introspecção é essencial para conexões autênticas."
            
        "Ambiente dinâmico e energético":
            $ connection_environment["quiet"] = False
            $ connection_environment["dynamic"] = True
            $ connection_environment["creative"] = False
            narrator "Falei sobre minha preferência por ambientes dinâmicos e energéticos."
            professor_wendell "Excelente... a energia é contagiante e pode criar laços fortes."
            
        "Ambiente criativo e inspirador":
            $ connection_environment["quiet"] = False
            $ connection_environment["dynamic"] = False
            $ connection_environment["creative"] = True
            narrator "Comentei sobre minha paixão por ambientes criativos e inspiradores."
            professor_wendell "Maravilhoso... a inspiração é o motor das conexões mais profundas."
    
    professor_wendell "Como você lida com desafios e conflitos em relacionamentos?"

    menu:
        "Análise sistemática e comunicação clara":
            $ connection_approach["analytical"] = True
            $ connection_approach["intuitive"] = False
            $ connection_approach["adaptive"] = False
            narrator "Mencionei que prefiro analisar sistematicamente e comunicar claramente para resolver conflitos."
            professor_wendell "Muito bom... a abordagem metódica evita muitos mal-entendidos."
            
        "Intuição e empatia":
            $ connection_approach["analytical"] = False
            $ connection_approach["intuitive"] = True
            $ connection_approach["adaptive"] = False
            narrator "Falei sobre minha confiança na intuição e empatia para entender as pessoas."
            professor_wendell "Interessante... a intuição pode ser uma ferramenta poderosa para conexões profundas."
            
        "Adaptação rápida e flexibilidade":
            $ connection_approach["analytical"] = False
            $ connection_approach["intuitive"] = False
            $ connection_approach["adaptive"] = True
            narrator "Comentei sobre minha capacidade de adaptação rápida e flexibilidade em diferentes situações."
            professor_wendell "Excelente... a adaptabilidade é crucial para manter relacionamentos saudáveis."
    
    professor_wendell "Por fim, qual tipo de impacto você gostaria de ter nas vidas das pessoas ao seu redor?"
    
    menu:
        "Ajudar a organizar e estruturar vidas":
            $ connection_impact["efficiency"] = True
            $ connection_impact["community"] = False
            $ connection_impact["innovation"] = False
            narrator "Mencionei meu interesse em ajudar as pessoas a organizar e estruturar suas vidas."
            professor_wendell "Muito nobre... a organização beneficia todos e cria estabilidade."
            
        "Fortalecer laços e conexões":
            $ connection_impact["efficiency"] = False
            $ connection_impact["community"] = True
            $ connection_impact["innovation"] = False
            narrator "Falei sobre meu desejo de fortalecer laços e conexões entre as pessoas."
            professor_wendell "Admirável... as conexões são o coração de qualquer comunidade."
            
        "Promover criatividade e inspiração":
            $ connection_impact["efficiency"] = False
            $ connection_impact["community"] = False
            $ connection_impact["innovation"] = True
            narrator "Comentei sobre minha paixão por promover criatividade e inspiração nas pessoas."
            professor_wendell "Inspirador... a criatividade é o futuro do crescimento pessoal."
    
    # === ANÁLISE DAS RESPOSTAS E DETERMINAÇÃO DAS CONEXÕES FUTURAS ===
    narrator "O Professor Wendell analisou minhas respostas cuidadosamente, fazendo algumas anotações em seu formulário."
    
    professor_wendell "Baseado em suas respostas, identifiquei quais tipos de conexões serão mais significativas para você nos próximos capítulos. Vou apresentar três áreas onde você terá mais interações."
    
    # Calcular pontuações para determinar as conexões futuras
    $ analytical_score = 0
    $ creative_score = 0
    $ social_score = 0
    
    if connection_interests["analytical"]:
        $ analytical_score += 2
    if connection_interests["creative"]:
        $ creative_score += 2
    if connection_interests["social"]:
        $ social_score += 2
    
    if connection_style["independent"]:
        $ analytical_score += 1
    if connection_style["collaborative"]:
        $ social_score += 1
    if connection_style["leadership"]:
        $ social_score += 1
    
    if connection_environment["quiet"]:
        $ analytical_score += 1
    if connection_environment["dynamic"]:
        $ social_score += 1
    if connection_environment["creative"]:
        $ creative_score += 1
    
    if connection_approach["analytical"]:
        $ analytical_score += 1
    if connection_approach["intuitive"]:
        $ creative_score += 1
    if connection_approach["adaptive"]:
        $ social_score += 1
    
    if connection_impact["efficiency"]:
        $ analytical_score += 1
    if connection_impact["community"]:
        $ social_score += 1
    if connection_impact["innovation"]:
        $ creative_score += 1
    
    # Determinar as conexões futuras baseado nas pontuações
    if analytical_score >= creative_score and analytical_score >= social_score:
        $ chosen_connection = "academic_focus"
        $ future_team = ["nicole", "katia", "huey"]
        $ connection_description = "Foco Acadêmico e Intelectual"
        $ connection_benefits = "Você terá mais interações com Nicole em projetos de análise, Katia em discussões sobre narrativas e Huey em explorações artísticas"
    elif creative_score >= social_score:
        $ chosen_connection = "creative_focus"
        $ future_team = ["huey", "camille", "samantha"]
        $ connection_description = "Foco Criativo e Inspiracional"
        $ connection_benefits = "Você terá mais interações com Huey em projetos artísticos, Camille em práticas espirituais e Samantha em atividades criativas"
    else:
        $ chosen_connection = "social_focus"
        $ future_team = ["larissa", "samantha", "camille"]
        $ connection_description = "Foco Social e Comunitário"
        $ connection_benefits = "Você terá mais interações com Larissa em atividades esportivas, Samantha em jogos e entretenimento e Camille em eventos comunitários"
    
    professor_wendell "Perfeito! Baseado em seu perfil, identifiquei que você terá conexões mais profundas na área de [connection_description]."
    # professor_wendell "[connection_benefits]."
    # professor_wendell "Essas pessoas passarão por situações e locais onde você estará presente, criando oportunidades naturais de interação nos próximos capítulos."
    
    narrator "O Professor Wendell me entregou um documento com observações sobre meu perfil e as pessoas com quem eu teria mais afinidade natural."
    
    # Adicionar memória compartilhada sobre as conexões futuras
    $ add_shared_memory("future_connections", future_team, f"Conexões futuras identificadas na área de {connection_description} com foco em {connection_benefits}")
    
    # Adicionar pontos de afinidade com as pessoas das conexões futuras
    python:
        for character in future_team:
            add_affinity_points(character, 15, "Conexão futura identificada")
    
    professor_wendell "Agora, deixe-me explicar mais detalhadamente como essas conexões funcionarão na prática."
    
    if chosen_connection == "academic_focus":
        professor_wendell "Com seu foco acadêmico e intelectual, você terá mais interações em ambientes de estudo e pesquisa."
        professor_wendell "Uma pessoa aparecerá em projetos de análise de dados, onde vocês poderão colaborar em metodologias e estruturas organizacionais."
        professor_wendell "Outra estará presente em discussões sobre narrativas e cinema, oferecendo perspectivas únicas sobre storytelling."
        professor_wendell "Uma terceira participará de explorações artísticas e curadoria, onde vocês poderão discutir a interseção entre arte e academia."
        
    elif chosen_connection == "creative_focus":
        professor_wendell "Com seu foco criativo e inspiracional, você terá mais interações em ambientes artísticos e expressivos."
        professor_wendell "Uma pessoa estará presente em projetos artísticos e exposições, onde vocês poderão explorar diferentes formas de expressão visual."
        professor_wendell "Outra participará de práticas espirituais e meditativas, oferecendo momentos de introspecção e conexão interior."
        professor_wendell "Uma terceira estará envolvida em atividades criativas e jogos, onde vocês poderão desenvolver narrativas interativas juntos."
        
    else:  # social_focus
        professor_wendell "Com seu foco social e comunitário, você terá mais interações em ambientes dinâmicos e colaborativos."
        professor_wendell "Uma pessoa estará presente em atividades esportivas e competições, onde vocês poderão trabalhar em equipe e superar desafios."
        professor_wendell "Outra participará de jogos e atividades de entretenimento, oferecendo momentos de diversão e criatividade."
        professor_wendell "Uma terceira estará envolvida em eventos comunitários e práticas de mindfulness, onde vocês poderão fortalecer laços sociais."
    
    professor_wendell "Essas pessoas aparecerão naturalmente em sua jornada, criando oportunidades orgânicas de interação e crescimento mútuo."
    professor_wendell "Cada encontro será uma chance de aprofundar os relacionamentos e descobrir novos aspectos de si mesmo e dos outros."
    
    narrator "O Professor Wendell me entregou um documento detalhado com observações sobre meu perfil e as atividades específicas onde eu teria mais interações."
    
    # Adicionar pontos extras de afinidade por interesse demonstrado
    python:
        for character in future_team:
            add_affinity_points(character, 10, "Interesse em atividades específicas")
    
    jump capitulo1_final
