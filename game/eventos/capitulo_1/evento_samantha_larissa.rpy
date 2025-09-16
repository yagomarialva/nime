# === EVENTO SAMANTHA E LARISSA - PRIMEIRO ENCONTRO ===
# Nerd Gamer vs. Esportiva Competitiva

label evento_samantha_larissa:
    $ points_samantha += 1
    scene bg quadra_volei with dissolve
    narrator "Entrei na quadra esportiva e áreas de lazer da universidade, procurando um lugar para me exercitar. O ambiente estava movimentado, com outros estudantes treinando e o som das bolas ecoando."
    narrator "Foi então que percebi que não estava sozinho..."

    # Apresentação natural da Samantha
    show samantha happy at left
    samantha "O-oi, [nome]... que sorte te encontrar aqui."
    samantha "Estava procurando um lugar para jogar RPG... a quadra tem uma energia incrível para aventuras épicas!"
    samantha "É bom te ver aqui... sempre valorizo sua perspectiva sobre jogos."

    narrator "Samantha se acomodou em um canto da quadra, carregando dados, fichas de personagem e alguns livros de RPG. Havia algo tímido em sua presença, mas também uma paixão genuína pelos jogos."

    # Apresentação natural da Larissa
    show larissa_volei at right
    larissa "Eaí, [nome]! Que bom te ver por aqui!"
    larissa "Estou trabalhando em um projeto sobre estratégia esportiva... é fascinante como podemos superar desafios através do esporte!"

    narrator "Larissa organizou seus materiais com energia contagiante - bola de vôlei, equipamentos de treino, até um cronômetro na mão."
    narrator "Havia algo competitivo em sua presença, como se ela estivesse sempre pronta para um desafio, mas também notei um olhar curioso em direção a Samantha."

    # Apresentação entre elas
    narrator "Ambas pareceram interessadas em conhecer a perspectiva uma da outra sobre os temas que estavam trabalhando."

    # Primeiro momento de tensão sutil - elas se conhecem através do jogador
    samantha "Hmm... interessante. E qual sua abordagem para estratégia? Você prefere jogos ou mais esporte?"
    samantha "Este projeto que estou fazendo... é sobre como usar estratégia em RPGs."

    larissa "Que coincidência! Eu também estou trabalhando com estratégia, mas focando em esportes e competição."
    larissa "Estou organizando um projeto sobre como superar desafios através do vôlei... é fascinante como podemos vencer com estratégia!"

    # Primeiro momento de tensão sutil - elas se conhecem
    samantha "Estratégia esportiva? Você também gosta de desafios? No RPG você precisa pensar em cada movimento, planejar ataques, trabalhar em equipe!"
    samantha "É sobre superar desafios, resolver problemas, vencer obstáculos! É tipo esporte, mas com mais criatividade!"

    larissa "Sim, adoro desafios! No vôlei você precisa pensar em cada jogada, planejar ataques, trabalhar em equipe!"
    larissa "É sobre força, coordenação, reação rápida! É sobre superar desafios físicos e mentais!"

    # Apresentação entre elas
    samantha "Hmm... interessante. Sou Samantha, estudo jogos e estratégia criativa."
    samantha "É bom conhecer alguém que entende de desafios..."

    larissa "Prazer, Larissa. Estudo educação física e estratégia esportiva."
    larissa "É reconfortante encontrar alguém que valoriza a superação tanto quanto eu..."

    samantha "Hmm... estratégia esportiva? Interessante."
    samantha "Sua abordagem parece... competitiva."

    larissa "E sua paixão por jogos é... inspiradora."
    larissa "É fascinante como conseguimos ver a mesma coisa de perspectivas diferentes."

    # Tensão sutil entre elas
    narrator "Senti que havia uma tensão sutil no ar. Ambas pareciam interessadas em se conhecer, mas também havia algo de... competitividade?"
    narrator "E eu estava no meio, observando como duas abordagens aparentemente complementares podiam criar uma dinâmica interessante."

    scene bg quadra_volei with dissolve
    menu:
        "Discutir estratégias de RPG":
            $ points_samantha += 3
            narrator "Concordei com a paixão de Samantha por estratégia em RPG."
            samantha "Exato! No RPG você precisa pensar em cada movimento, planejar ataques, trabalhar em equipe!"
            samantha "É sobre superar desafios, resolver problemas, vencer obstáculos! É tipo esporte, mas com mais criatividade!"
            samantha "Você parece ter uma perspectiva interessante sobre isso..."
            larissa "Samantha, você descreveu exatamente o que amo no vôlei! Estratégia, trabalho em equipe, superar desafios!"
            larissa "É reconfortante saber que você valoriza tanto a estratégia criativa quanto a competitiva..."

        "Apoiar a perspectiva esportiva de Larissa":
            $ points_larissa += 3
            narrator "Concordei com a paixão de Larissa por estratégia no esporte."
            larissa "Exato! No vôlei você precisa pensar em cada jogada, planejar ataques, trabalhar em equipe!"
            larissa "É sobre força, coordenação, reação rápida! É sobre superar desafios físicos!"
            larissa "É reconfortante encontrar alguém que valoriza a superação tanto quanto eu..."
            samantha "Entendo... mas como vamos viver aventuras épicas sem imaginação?"
            samantha "Sua abordagem é... competitiva."

        "Compartilhar sua própria perspectiva sobre estratégia":
            $ points_samantha += 1
            $ points_larissa += 1
            narrator "Compartilhei minha própria visão sobre estratégia, tentando encontrar um meio termo."
            samantha "Interessante perspectiva. Você parece equilibrar bem os dois lados."
            samantha "Você tem uma forma única de ver as coisas..."
            larissa "Sinto que você tem uma energia muito equilibrada... como se conseguisse ver o valor em ambas as abordagens."
            larissa "É reconfortante saber que você valoriza tanto a estratégia criativa quanto a competitiva..."

        "Perguntar a Samantha sobre seus jogos favoritos":
            $ points_samantha += 2
            narrator "Perguntei sobre os jogos favoritos de Samantha."
            samantha "Bem... sempre gosto de RPGs de estratégia e jogos cooperativos."
            samantha "É bom encontrar alguém que realmente entenda de desafios..."
            larissa "Fascinante! Eu também gosto de desafios, mas nunca pensei em aplicá-los em jogos como você faz!"
            larissa "É interessante como vocês dois parecem ter gostos similares..."

        "Perguntar a Larissa sobre seus esportes favoritos":
            $ points_larissa += 2
            narrator "Perguntei sobre os esportes favoritos de Larissa."
            larissa "Bem... adoro vôlei, basquete, qualquer esporte que exija estratégia e trabalho em equipe."
            larissa "É reconfortante encontrar alguém que valoriza a superação tanto quanto eu..."
            samantha "Interessante. Sua abordagem é... metódica."
            samantha "É raro encontrar alguém que veja esporte de forma tão... estratégica."

    # Cena adicional 2 – Atividade híbrida
    hide samantha
    hide larissa
    scene bg quadra_volei with dissolve
    show samantha happy at left
    show larissa_volei at right

    narrator "Decidimos colocar a teoria em prática. Samantha propôs uma atividade que combinasse RPG com esporte."

    samantha "Vamos fazer uma aventura épica! Vocês são aventureiros em uma arena mágica!"
    samantha "Larissa, você pode ser uma guerreira que usa vôlei como arma! Cada saque é um ataque mágico!"
    samantha "É bom ter você aqui... sempre valorizo sua perspectiva sobre estratégia..."

    larissa "Guerreira? Samantha, que ideia incrível! Eu adoro desafios estratégicos!"
    larissa "Vamos! A bola está esperando, a quadra está pronta... é hora de competir com estratégia!"
    larissa "É reconfortante saber que você valoriza tanto a estratégia criativa quanto a competitiva..."

    samantha "Larissa, no RPG você pode ser qualquer coisa! Um guerreiro, um mago, um arqueiro..."
    samantha "É sobre criatividade, estratégia, trabalho em equipe! É tipo esporte, mas com mais imaginação!"

    larissa "Samantha, no vôlei também precisamos de estratégia, trabalho em equipe, e muito mais!"
    larissa "É sobre força física, coordenação, reação rápida! É sobre superar limites reais!"

    narrator "A atividade começou, e foi fascinante ver como Samantha e Larissa complementavam perfeitamente suas abordagens estratégicas."
    narrator "Mas também notei uma tensão sutil entre elas, como se cada uma quisesse impressionar mais que a outra."

    samantha "Nossa... posso ver como a estratégia funciona tanto no RPG quanto no vôlei!"
    samantha "Cada ponto pode ser uma vitória épica, cada jogada uma estratégia genial..."
    samantha "É bom ter alguém que entende de desafios como você..."

    larissa "Exato! Samantha, você entende perfeitamente! O vôlei é sobre reação, instinto, mas também estratégia!"
    larissa "É sobre sentir e reagir, mas com planejamento!"
    larissa "É reconfortante encontrar alguém que valoriza a superação tanto quanto eu..."

    narrator "Samantha e Larissa trabalhavam em perfeita sintonia, cada uma contribuindo com sua perspectiva estratégica única."
    narrator "Mas havia algo de competitivo no ar, como se cada uma quisesse mostrar que entendia melhor de estratégia."

    menu:
        "Focar na estratégia criativa":
            $ points_samantha += 3
            narrator "Concordei com a abordagem estratégica criativa de Samantha."
            samantha "Exato! Se pudermos imaginar que cada ponto é uma vitória épica..."
            samantha "Imagine poder viver aventuras incríveis enquanto treina!"
            samantha "Você parece ter uma perspectiva interessante sobre isso..."
            larissa "Samantha, você tem razão! A criatividade pode tornar o treino muito mais divertido!"
            larissa "É reconfortante saber que você valoriza tanto a estratégia criativa quanto a competitiva..."

        "Explorar a estratégia competitiva":
            $ points_larissa += 3
            narrator "Concordei com a abordagem estratégica competitiva de Larissa."
            larissa "Exato! No vôlei, você precisa de estratégia e reação rápida!"
            larissa "É sobre confiança, sobre acreditar que você consegue fazer o ponto!"
            larissa "É reconfortante encontrar alguém que valoriza a superação tanto quanto eu..."
            samantha "Nossa, Larissa! É exatamente isso que sinto no RPG! Cada batalha é uma vitória conquistada através de estratégia!"
            samantha "Sua abordagem é... competitiva."

        "Combinar estratégias criativas e competitivas":
            $ points_samantha += 2
            $ points_larissa += 2
            narrator "Sugeri que combinassem ambas as abordagens estratégicas."
            samantha "Que ideia incrível! Podemos usar a criatividade para tornar o esporte mais divertido!"
            samantha "É bom ter alguém que entende de desafios como você..."
            larissa "Sim! E podemos usar a estratégia competitiva para tornar o RPG mais emocionante!"
            larissa "É reconfortante saber que você valoriza tanto a estratégia criativa quanto a competitiva..."
            samantha "É como se fôssemos duas estrategistas da mesma alma, apenas usando táticas diferentes!"

    # Cena adicional 3 – Reflexão
    hide samantha
    hide larissa
    scene bg quadra_volei with dissolve
    show samantha happy at left
    show larissa_volei at right

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
    narrator "Mas também havia algo de... ciúmes no ar, como se cada uma quisesse ser a única a compartilhar essa paixão comigo."

    # Momento de crescimento mútuo
    narrator "Por um momento, ambas ficaram em silêncio, processando a conexão especial que haviam descoberto."

    samantha "Larissa... obrigada por me mostrar que há mais na competição do que apenas fantasia."
    samantha "Você me ensinou que a superação real pode ser tão emocionante quanto as aventuras imaginárias."

    larissa "Samantha... obrigada por me mostrar que a criatividade pode ser tão estratégica!"
    larissa "Você me ensinou que cada jogo pode carregar a mesma paixão que sinto no esporte!"

    # Crescimento mútuo
    narrator "Era como se tivessem descoberto que eram duas estrategistas da mesma essência - ambas apaixonadas por desafios e superação."
    narrator "Mas também havia algo de... tensão no ar, como se cada uma quisesse ser a única a compartilhar essa paixão comigo."

    # Opções de aprofundamento
    menu:
        "Sugerir uma colaboração estratégica":
            $ points_samantha += 2
            $ points_larissa += 2
            narrator "Sugeri que Samantha e Larissa colaborassem em um projeto estratégico."
            samantha "Que ideia incrível! Podemos criar uma atividade que combine estratégia criativa com competitiva!"
            samantha "É bom ter alguém que entende de desafios como você..."
            larissa "Nossa, que legal! Eu posso ensinar sobre estratégia esportiva, e você sobre estratégia de jogos!"
            larissa "É reconfortante saber que você valoriza tanto a estratégia criativa quanto a competitiva..."
            samantha "Exato! Estratégia criativa para imaginar, estratégia competitiva para executar! Seria uma combinação perfeita!"

        "Perguntar sobre suas estratégias favoritas":
            $ points_samantha += 1
            $ points_larissa += 1
            narrator "Perguntei sobre as estratégias favoritas de cada uma."
            samantha "Bem... sempre gosto de planejar ataques coordenados e trabalhar em equipe no RPG."
            samantha "É bom encontrar alguém que realmente entenda de desafios..."
            larissa "Eu analiso o adversário, planejo jogadas específicas... mas nunca pensei em aplicar isso em jogos como você faz!"
            larissa "É reconfortante encontrar alguém que valoriza a superação tanto quanto eu..."

        "Refletir sobre a conexão estratégica":
            $ points_samantha += 1
            $ points_larissa += 1
            narrator "Sugeri que refletissem sobre a conexão estratégica que haviam descoberto."
            samantha "Nunca pensei que encontraria alguém que entendesse estratégia da mesma forma que eu..."
            samantha "É bom ter alguém que entende de desafios como você..."
            larissa "E eu nunca imaginei que encontraria alguém que aplicasse estratégia em jogos como você!"
            larissa "É reconfortante saber que você valoriza tanto a estratégia criativa quanto a competitiva..."
            samantha "É como se fôssemos duas estrategistas da mesma alma..."

    # Memória compartilhada especial
    $ add_shared_memory("strategic_minds_connection", ["samantha", "larissa"], "O momento em que descobrimos nossa conexão especial como estrategistas apaixonadas por desafios")

    hide samantha
    hide larissa
    scene bg quadra_volei with dissolve

    narrator "O sol começava a se pôr sobre a quadra, mas a conversa continuava animada."
    narrator "Era como se tivéssemos descoberto algo especial... uma conexão entre duas perspectivas que pareciam opostas, mas que na verdade se complementavam perfeitamente."

    narrator "Samantha e Larissa haviam encontrado um terreno comum, e eu mal podia esperar para ver o que essa colaboração poderia gerar..."
    narrator "Mas também havia algo de... tensão no ar, como se cada uma quisesse ser a única a compartilhar essa paixão comigo."

    narrator "Era como se tivéssemos descoberto uma nova forma de ver o mundo, onde estratégia criativa e competitiva dançavam juntas em perfeita harmonia."
    narrator "Mas também havia algo de... estranho no ar, como se cada uma quisesse ser a única a me ensinar sobre estratégia."

    return
