define sombra = Character("Narrador", color="#A9A9A9")  # Personagem misterioso e sombreado

label prologo:

    scene bg city with fade  # Substitua por sua imagem real

    sombra "Este jogo é recomendado para maiores de 18 anos."
    sombra "Você confirma que tem 18 anos ou mais?"

    menu:
        "Sim, tenho 18 anos ou mais.":
            jump nome_jogador

        "Não, sou menor de idade.":
            sombra "Infelizmente, você não poderá jogar este jogo. Obrigado pela compreensão!"
            return

label nome_jogador:
    scene bg city with fade

    $ nome = renpy.input("Digite seu nome:", length=20)
    $ nome = nome.strip()
    if nome == "":
        $ nome = "Jogador"

    sombra "Olá, [nome]. Seja bem-vindo(a)!"

    jump aviso_jogo

label aviso_jogo:
    scene bg city with fade
    with dissolve

    sombra "Todos os personagens deste jogo possuem 18 anos ou mais."
    sombra "Apesar de abordar relacionamentos e temas maduros, este NÃO é um jogo pornográfico."
    sombra "Nosso foco está na construção de narrativa, romance e escolhas com consequências."
    sombra "Esperamos que aproveite sua jornada com responsabilidade e respeito."

    jump tutorial_mecanicas

label tutorial_mecanicas:
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

label explicar_mecanicas:
    scene bg city with dissolve
    
    # === EXPLICAÇÃO DO SISTEMA DE RELACIONAMENTOS ===
    sombra "🏠 Bem-vindo ao sistema de relacionamentos de NIME!"
    sombra "Você conhecerá 6 personagens únicas, cada uma com sua personalidade, sonhos e vulnerabilidades."
    
    sombra "💕 No canto superior esquerdo, você verá os NÍVEIS DE RELACIONAMENTO:"
    sombra "🤝 Desconhecido → 🙂 Amigo → 😊 Amigo Próximo → 💖 Romântico"
    
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
    sombra "• Um romance profundo e significativo"
    sombra "• Uma irmandade eterna baseada em amor familiar"
    sombra "• Ou algo único que surge das escolhas que você fizer"
    
    sombra "🏡 Lembre-se: às vezes, a família que escolhemos é mais forte que qualquer romance."
    
    # === DICAS PRÁTICAS ===
    sombra "💡 Algumas dicas para sua jornada:"
    sombra "• Seja autêntico - as personagens valorizam honestidade"
    sombra "• Ouça com atenção - pequenos detalhes podem ser importantes"
    sombra "• Não force relacionamentos - deixe-os fluir naturalmente"
    sombra "• Cuide de todos - até mesmo quem não é 'sua rota' merece carinho"
    
    sombra "🎨 E principalmente: este é um jogo sobre arte, criatividade e conexão humana."
    sombra "Permita-se ser tocado pelas histórias que você vai viver."
    
    menu:
        "Entendi! Estou pronto para começar":
            jump iniciar_aventura
        "Posso ver um exemplo das mecânicas?":
            jump exemplo_mecanicas

label exemplo_mecanicas:
    scene bg city with dissolve
    
    sombra "Claro! Deixe-me mostrar como funciona na prática."
    sombra "Imagine que você está conversando com alguém que parece triste..."
    
    menu:
        "Perguntar se está tudo bem e oferecer apoio":
            $ feedback_exemplo = add_affinity_points("exemplo", 8, "Demonstração de empatia")
            sombra "✨ Excelente! Essa escolha demonstra empatia genuína."
            sombra "Você veria: '[feedback_exemplo]'"
            sombra "E talvez desbloqueasse um momento especial de vulnerabilidade."
            
        "Fazer uma piada para alegrar o ambiente":
            $ feedback_exemplo = add_affinity_points("exemplo", 3, "Tentativa de ajudar")
            sombra "🙂 Uma escolha carinhosa, mas talvez não o que ela precisava no momento."
            sombra "Você veria: '[feedback_exemplo]'"
            sombra "Ainda assim, sua intenção de ajudar seria valorizada."
    
    sombra "Viu como suas intenções se traduzem em consequências reais?"
    sombra "Agora imagine isso acontecendo ao longo de meses de convivência..."
    sombra "Cada escolha constrói a fundação dos relacionamentos que você terá."
    
    jump iniciar_aventura

label iniciar_aventura:
    scene bg city with dissolve
    
    sombra "🌟 Sua jornada na Faculdade Solária está prestes a começar, [nome]."
    sombra "Você conhecerá:"
    sombra "💼 Nicole - A estrategista que sonha em ajudar artistas"
    sombra "🎬 Katia - A cineasta que vê arte nas sombras"  
    sombra "🏐 Larissa - A atleta que encontra paz no movimento"
    sombra "🎨 Huey - A artista que vê magia em tudo"
    sombra "🎮 Samantha - A gamer que vive em mundos de fantasia"
    sombra "🧘 Camille - A espiritualista que sente as energias do universo"
    
    sombra "Cada uma tem seus sonhos, medos, e uma história única para contar."
    sombra "Mas o mais importante: cada uma pode mudar, crescer e florescer..."
    sombra "...dependendo de como você escolher se conectar com elas."
    
    sombra "💫 Que tipo de história vocês criarão juntos?"
    sombra "Isso, meu caro [nome], depende inteiramente de você."
    
    sombra "🏠 Bem-vindo à Rua Aurora, 57."
    sombra "Sua nova casa. Sua nova família. Sua nova vida."
    
    # Transição épica para o primeiro capítulo
    scene black with fade
    centered "{color=#FFD700}🌟 Sua jornada de conexões humanas começa agora... 🌟{/color}"
    pause 2.0

    jump capitulo1
