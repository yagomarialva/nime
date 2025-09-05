# Portuguese Translation - Introduction Dialogues
# Tradução em português - Diálogos da Introdução

# Introduction - Portuguese Translation
translate portuguese prologo:
    scene bg city with fade

    sombra "Este jogo é recomendado para maiores de 18 anos."
    sombra "Você confirma que tem 18 anos ou mais?"

    menu:
        "Sim, tenho 18 anos ou mais.":
            jump nome_jogador

        "Não, sou menor de idade.":
            sombra "Infelizmente, você não poderá jogar este jogo. Obrigado pela compreensão!"
            return

translate portuguese nome_jogador:
    scene bg city with fade

    $ nome = renpy.input("Digite seu nome:", length=20)
    $ nome = nome.strip()
    if nome == "":
        $ nome = "Jogador"

    sombra "Olá, [nome]. Seja bem-vindo(a)!"

    jump aviso_jogo

translate portuguese aviso_jogo:
    scene bg city with fade
    with dissolve

    sombra "Todos os personagens deste jogo possuem 18 anos ou mais."
    sombra "Apesar de abordar relacionamentos e temas maduros, este NÃO é um jogo pornográfico."
    sombra "Nosso foco está na construção de narrativa, romance e escolhas com consequências."
    sombra "Esperamos que aproveite sua jornada com responsabilidade e respeito."

    jump tutorial_mecanicas

translate portuguese tutorial_mecanicas:
    scene bg city with dissolve
    
    sombra "Antes de começar sua jornada, [nome], deixe-me explicar como este mundo funciona..."
    sombra "NIME não é apenas uma história - é uma experiência onde suas escolhas moldam relacionamentos reais."
    
    menu:
        "Quero aprender sobre as mecânicas do jogo":
            jump explicar_mecanicas
        "Prefiro descobrir jogando":
            sombra "Entendo! Às vezes a descoberta é parte da diversão."
            sombra "Mas lembre-se: no canto superior esquerdo você sempre pode ver como seus relacionamentos estão evoluindo."
            jump iniciar_aventura

translate portuguese explicar_mecanicas:
    scene bg city with dissolve
    
    # === EXPLICAÇÃO DO SISTEMA DE RELACIONAMENTOS ===
    sombra "🏠 Bem-vindo ao sistema de relacionamentos de NIME!"
    sombra "Você conhecerá 6 personagens únicas, cada uma com sua personalidade, sonhos e vulnerabilidades."
    
    sombra "💕 No canto superior esquerdo, você verá os NÍVEIS DE RELACIONAMENTO:"
    sombra "🤝 Desconhecido → 🙂 Amigo → 😊 Amigo Próximo → 💕 Romântico"
    
    sombra "Cada interação positiva fortalece seus laços. Cada momento especial cria memórias duradouras."
    
    # === EXPLICAÇÃO DAS ESCOLHAS ===
    sombra "🎯 Suas ESCOLHAS têm consequências reais:"
    sombra "• Algumas aumentam afinidade com personagens específicos"
    sombra "• Outras afetam múltiplos relacionamentos"
    sombra "• Momentos especiais desbloqueiam quando você demonstra empatia genuína"
    
    sombra "🌱 Seu NÍVEL DE EMPATIA também importa - quanto mais você se importa com os outros, mais oportunidades especiais surgem."
    
    # === EXPLICAÇÃO DOS MOMENTOS ESPECIAIS ===
    sombra "✨ MOMENTOS ESPECIAIS acontecem quando conexões verdadeiras se formam:"
    sombra "• Conversas profundas que revelam vulnerabilidades"
    sombra "• Experiências compartilhadas que se tornam memórias preciosas"
    sombra "• Realizações sobre amor, amizade e crescimento pessoal"
    
    sombra "📚 Suas MEMÓRIAS COMPARTILHADAS ficam registradas - cada uma representa um momento único que você criou."
    
    # === EXPLICAÇÃO DO CRESCIMENTO ===
    sombra "🌟 Mas aqui está o mais importante:"
    sombra "Este não é um jogo sobre 'conquistar' alguém. É sobre crescimento mútuo."
    sombra "Cada personagem tem sua própria jornada de autodescoberta."
    sombra "Suas ações não apenas afetam como elas se sentem sobre você - mas como elas crescem como pessoas."
    
    # === EXPLICAÇÃO DOS FINAIS ===
    sombra "🎭 Existem múltiplos caminhos para sua história:"
    sombra "• Amizades profundas que duram a vida toda"
    sombra "• Relacionamentos românticos baseados em conexão genuína"
    sombra "• Crescimento pessoal que te transforma como pessoa"
    sombra "• Memórias que ficarão com você para sempre"
    
    sombra "A escolha é sua, [nome]. Que tipo de história você criará?"
    
    jump iniciar_aventura

translate portuguese iniciar_aventura:
    scene bg city with dissolve
    
    sombra "Sua aventura começa agora, [nome]."
    sombra "Lembre-se: cada escolha importa, cada momento conta."
    sombra "Bem-vindo ao NIME - onde amizades nascem e sonhos se realizam."
    
    # Iniciar o jogo real
    jump capitulo1