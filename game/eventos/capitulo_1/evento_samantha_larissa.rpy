# === EVENTO SAMANTHA E LARISSA ===
# Nerd Gamer vs. Esportiva Competitiva

label evento_samantha_larissa:
    $ points_samantha += 1
    scene bg quadra_volei with dissolve
    show samantha happy at left
    show larissa happy at right

    narrator "Samantha me convidou para uma sessão de RPG na quadra de vôlei. O ambiente estava movimentado, com outros estudantes treinando e o som das bolas ecoando."
    narrator "Larissa apareceu de surpresa, carregando uma bola de vôlei e com um sorriso contagiante."

    samantha "Nossa, que legal! Vamos fazer uma sessão épica de RPG aqui na quadra!"
    samantha "Imaginem só... uma aventura onde vocês são aventureiros em uma arena mágica!"

    larissa "RPG? Samantha, que interessante! Eu adoro desafios estratégicos!"
    larissa "E olha só, trouxe minha bola! Podemos treinar e liberar endorfina de verdade!"

    samantha "Larissa, você também gosta de estratégia? No RPG você precisa pensar em cada movimento, planejar ataques, trabalhar em equipe!"
    samantha "É sobre superar desafios, resolver problemas, vencer obstáculos! É tipo esporte, mas com mais criatividade!"

    larissa "Samantha, você descreveu exatamente o que amo no vôlei! Estratégia, trabalho em equipe, superar desafios!"
    larissa "Cada ponto é uma vitória conquistada através de planejamento e execução perfeita!"

    samantha "Nossa, Larissa! É exatamente isso que sinto no RPG! Cada batalha é uma vitória conquistada através de estratégia!"
    samantha "E você pode jogar com amigos, criar histórias incríveis, viver aventuras épicas!"

    larissa "Samantha, no vôlei também vivemos aventuras reais! Cada partida é uma história única!"
    larissa "E você pode jogar com amigos, criar memórias incríveis, superar desafios físicos e mentais!"

    narrator "Senti que havia uma conexão genuína entre elas. Ambas compartilhavam a mesma paixão por desafios, estratégia e superação, apenas com linguagens diferentes."

    scene bg quadra_volei with dissolve
    menu:
        "Discutir estratégias de RPG":
            $ points_samantha += 3
            narrator "Concordei com a paixão de Samantha por estratégia em RPG."
            samantha "Exato! No RPG você precisa pensar em cada movimento, planejar ataques, trabalhar em equipe!"
            samantha "É sobre superar desafios, resolver problemas, vencer obstáculos! É tipo esporte, mas com mais criatividade!"
            larissa "Samantha, você descreveu exatamente o que amo no vôlei! Estratégia, trabalho em equipe, superar desafios!"

        "Apoiar a perspectiva esportiva de Larissa":
            $ points_larissa += 3
            narrator "Concordei com a paixão de Larissa por estratégia no esporte."
            larissa "Exato! No vôlei você precisa pensar em cada jogada, planejar ataques, trabalhar em equipe!"
            larissa "É sobre força, coordenação, reação rápida! É sobre superar desafios físicos!"
            samantha "Entendo... mas como vamos viver aventuras épicas sem imaginação?"

        "Compartilhar experiências de superação":
            $ points_samantha += 2
            $ points_larissa += 2
            narrator "Sugeri que compartilhassem suas experiências de superação."
            samantha "Que ideia incrível! É fascinante como cada uma de nós supera desafios de forma diferente!"
            larissa "Sim! E é incrível como chegamos ao mesmo lugar por caminhos diferentes!"
            samantha "É como se fôssemos duas guerreiras da mesma alma, apenas usando armas diferentes!"

    # Cena adicional 2 – Atividade híbrida
    hide samantha
    hide larissa
    scene bg quadra_volei with dissolve
    show samantha happy at left
    show larissa happy at right

    narrator "Decidimos colocar a teoria em prática. Samantha propôs uma atividade que combinasse RPG com esporte."

    samantha "Vamos fazer uma aventura épica! Vocês são aventureiros em uma arena mágica!"
    samantha "Larissa, você pode ser uma guerreira que usa vôlei como arma! Cada saque é um ataque mágico!"

    larissa "Guerreira? Samantha, que ideia incrível! Eu adoro desafios estratégicos!"
    larissa "Vamos! A bola está esperando, a quadra está pronta... é hora de competir com estratégia!"

    samantha "Larissa, no RPG você pode ser qualquer coisa! Um guerreiro, um mago, um arqueiro..."
    samantha "É sobre criatividade, estratégia, trabalho em equipe! É tipo esporte, mas com mais imaginação!"

    larissa "Samantha, no vôlei também precisamos de estratégia, trabalho em equipe, e muito mais!"
    larissa "É sobre força física, coordenação, reação rápida! É sobre superar limites reais!"

    narrator "A atividade começou, e foi fascinante ver como Samantha e Larissa complementavam perfeitamente suas abordagens estratégicas."

    samantha "Nossa... posso ver como a estratégia funciona tanto no RPG quanto no vôlei!"
    samantha "Cada ponto pode ser uma vitória épica, cada jogada uma estratégia genial..."

    larissa "Exato! Samantha, você entende perfeitamente! O vôlei é sobre reação, instinto, mas também estratégia!"
    larissa "É sobre sentir e reagir, mas com planejamento!"

    narrator "Samantha e Larissa trabalhavam em perfeita sintonia, cada uma contribuindo com sua perspectiva estratégica única."

    menu:
        "Focar na estratégia criativa":
            $ points_samantha += 3
            narrator "Concordei com a abordagem estratégica criativa de Samantha."
            samantha "Exato! Se pudermos imaginar que cada ponto é uma vitória épica..."
            samantha "Imagine poder viver aventuras incríveis enquanto treina!"
            larissa "Samantha, você tem razão! A criatividade pode tornar o treino muito mais divertido!"

        "Explorar a estratégia competitiva":
            $ points_larissa += 3
            narrator "Concordei com a abordagem estratégica competitiva de Larissa."
            larissa "Exato! No vôlei, você precisa de estratégia e reação rápida!"
            larissa "É sobre confiança, sobre acreditar que você consegue fazer o ponto!"
            samantha "Nossa, Larissa! É exatamente isso que sinto no RPG! Cada batalha é uma vitória conquistada através de estratégia!"

        "Combinar estratégias criativas e competitivas":
            $ points_samantha += 2
            $ points_larissa += 2
            narrator "Sugeri que combinassem ambas as abordagens estratégicas."
            samantha "Que ideia incrível! Podemos usar a criatividade para tornar o esporte mais divertido!"
            larissa "Sim! E podemos usar a estratégia competitiva para tornar o RPG mais emocionante!"
            samantha "É como se fôssemos duas estrategistas da mesma alma, apenas usando táticas diferentes!"

    # Cena adicional 3 – Reflexão
    hide samantha
    hide larissa
    scene bg quadra_volei with dissolve
    show samantha happy at left
    show larissa happy at right

    narrator "Após a atividade, decidimos refletir sobre a conexão especial que havíamos descoberto."

    samantha "Nossa... nunca pensei que encontraria alguém que entendesse estratégia da mesma forma que eu."
    samantha "Larissa, você realmente entende o que é superar desafios através de planejamento e execução!"

    larissa "Samantha, eu que fico impressionada! Sua capacidade de pensar estrategicamente em situações criativas..."
    larissa "É como se você conseguisse traduzir em jogos o que eu sinto apenas como competição."

    samantha "Larissa, você descreveu perfeitamente! É exatamente isso que sinto quando jogo RPG!"
    samantha "É como se estivéssemos falando a mesma língua, apenas usando meios diferentes!"

    larissa "Sim! E é incrível como chegamos ao mesmo lugar por caminhos diferentes."
    larissa "Você através da criatividade, eu através da competição... mas ambas usamos estratégia para vencer!"

    narrator "Era como se tivessem encontrado uma alma gêmea estratégica. Ambas compartilhavam a mesma paixão por desafios, planejamento e superação."

    # Momento de crescimento mútuo
    narrator "Por um momento, ambas ficaram em silêncio, processando a conexão especial que haviam descoberto."

    samantha "Larissa... obrigada por me mostrar que há mais na competição do que apenas fantasia."
    samantha "Você me ensinou que a superação real pode ser tão emocionante quanto as aventuras imaginárias."

    larissa "Samantha... obrigada por me mostrar que a criatividade pode ser tão estratégica!"
    larissa "Você me ensinou que cada jogo pode carregar a mesma paixão que sinto no esporte!"

    # Crescimento mútuo
    narrator "Era como se tivessem descoberto que eram duas estrategistas da mesma essência - ambas apaixonadas por desafios e superação."

    # Opções de aprofundamento
    menu:
        "Sugerir uma colaboração estratégica":
            $ points_samantha += 2
            $ points_larissa += 2
            narrator "Sugeri que Samantha e Larissa colaborassem em um projeto estratégico."
            samantha "Que ideia incrível! Podemos criar uma atividade que combine estratégia criativa com competitiva!"
            larissa "Nossa, que legal! Eu posso ensinar sobre estratégia esportiva, e você sobre estratégia de jogos!"
            samantha "Exato! Estratégia criativa para imaginar, estratégia competitiva para executar! Seria uma combinação perfeita!"

        "Perguntar sobre suas estratégias favoritas":
            $ points_samantha += 1
            $ points_larissa += 1
            narrator "Perguntei sobre as estratégias favoritas de cada uma."
            samantha "Bem... sempre gosto de planejar ataques coordenados e trabalhar em equipe no RPG."
            samantha "E você, Larissa? Como você desenvolve suas estratégias no vôlei?"
            larissa "Eu analiso o adversário, planejo jogadas específicas... mas nunca pensei em aplicar isso em jogos como você faz!"

        "Refletir sobre a conexão estratégica":
            $ points_samantha += 1
            $ points_larissa += 1
            narrator "Sugeri que refletissem sobre a conexão estratégica que haviam descoberto."
            samantha "Nunca pensei que encontraria alguém que entendesse estratégia da mesma forma que eu..."
            larissa "E eu nunca imaginei que encontraria alguém que aplicasse estratégia em jogos como você!"
            samantha "É como se fôssemos duas estrategistas da mesma alma... N-não é como se eu estivesse sendo sentimental ou qualquer coisa assim!"

    # Memória compartilhada especial
    $ add_shared_memory("strategic_minds_connection", ["samantha", "larissa"], "O momento em que descobrimos nossa conexão especial como estrategistas apaixonadas por desafios")

    hide samantha
    hide larissa
    scene bg quadra_volei with dissolve

    narrator "O sol começava a se pôr sobre a quadra, mas a conversa continuava animada."
    narrator "Era como se tivéssemos descoberto algo especial... uma conexão entre duas perspectivas que pareciam opostas, mas que na verdade se complementavam perfeitamente."

    narrator "Samantha e Larissa haviam encontrado um terreno comum, e eu mal podia esperar para ver o que essa colaboração poderia gerar..."

    return
