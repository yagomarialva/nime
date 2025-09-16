# === EVENTO HUEY E CAMILLE - PRIMEIRO ENCONTRO ===
# Artista vs. Espiritual

label evento_huey_camille:
    $ points_huey += 1
    scene bg art_room with dissolve
    narrator "Entrei na galeria de arte e espaços criativos da universidade, procurando um lugar para me inspirar. O ambiente estava silencioso e contemplativo, com obras de arte espalhadas pelas paredes."
    narrator "Foi então que percebi que não estava sozinho..."

    # Apresentação natural da Huey
    show huey gentle at left
    huey "Ah, oi, [nome]! Que coincidência te encontrar aqui."
    huey "Estava procurando um lugar para me inspirar para um projeto sobre conexões humanas."
    huey "É bom te ver aqui... sempre valorizo sua perspectiva sobre arte."

    narrator "Huey se acomodou em um canto da galeria, carregando um caderno de esboços e alguns materiais de arte. Havia algo contemplativo em sua presença, como se ela estivesse sempre absorvendo a beleza ao redor."

    # Apresentação natural da Camille
    show camille gentle at right
    camille "Olaá, [nome]! Muito bom te ver aqui."
    camille "Estou trabalhando em um projeto sobre conexões energéticas... é fascinante como podemos sentir a energia que permeia tudo."

    narrator "Camille organizou seus materiais com cuidado, carregando um caderno de anotações e alguns cristais pequenos."
    narrator "Havia algo sereno em sua presença, como se ela trouxesse calma para o ambiente, mas também notei um olhar curioso em direção a Huey."

    # Apresentação entre elas
    narrator "Ambas pareceram interessadas em conhecer a perspectiva uma da outra sobre os temas que estavam trabalhando."

    # Primeiro momento de tensão sutil - elas se conhecem através do jogador
    huey "Hmm... interessante. E qual sua abordagem para conexões? Você prefere arte ou mais espiritual?"
    huey "Este projeto que estou fazendo... é sobre como capturar emoções através da arte."

    camille "Que coincidência! Eu também estou trabalhando com conexões, mas focando em energia e espiritualidade."
    camille "Estou organizando um projeto sobre como sentir a energia que permeia tudo... é fascinante como podemos nos conectar com o universo."

    # Primeiro momento de tensão sutil - elas se conhecem
    huey "Conexões energéticas? Você também sente isso? É como se cada obra tivesse sua própria aura, sua própria emoção..."
    huey "É raro encontrar alguém que realmente entenda de sensibilidade."

    camille "Sim, adoro sentir como as energias fluem através de tudo. Cada elemento tem seu propósito, cada vibração contribui para o todo."
    camille "É fascinante como podemos nos conectar com algo maior que nós mesmos."

    # Apresentação entre elas
    huey "Interessante. Sou Huey, estudo artes visuais e expressão criativa."
    huey "É bom conhecer alguém que entende de sensibilidade."

    camille "Prazer, Camille. Estudo conexões energéticas e práticas de mindfulness."
    camille "É reconfortante encontrar alguém que valoriza a sensibilidade tanto quanto eu..."

    huey "Conexões energéticas? Interessante."
    huey "Sua abordagem parece... espiritual."

    camille "E sua paixão pela arte é... inspiradora."
    camille "É fascinante como conseguimos ver a mesma coisa de perspectivas diferentes."

    # Tensão sutil entre elas
    narrator "Senti que havia uma tensão sutil no ar. Ambas pareciam interessadas em se conhecer, mas também havia algo de... competitividade?"
    narrator "E eu estava no meio, observando como duas abordagens aparentemente complementares podiam criar uma dinâmica interessante."

    scene bg art_room with dissolve
    menu:
        "Discutir como a arte captura emoções":
            $ points_huey += 3
            narrator "Concordei com a perspectiva de Huey sobre arte e emoção."
            huey "Exato! A arte é sobre traduzir o que sentimos em algo tangível!"
            huey "Cada cor, cada pincelada... tudo é uma forma de expressar emoções que não conseguimos dizer com palavras!"
            huey "Você parece ter uma perspectiva interessante sobre isso..."
            camille "Huey, você disse exatamente o que eu sinto! É como se a arte fosse uma linguagem universal das emoções!"
            camille "É reconfortante saber que você valoriza tanto a expressão artística quanto a espiritual..."

        "Explorar a energia que permeia a arte":
            $ points_camille += 3
            narrator "Concordei com a perspectiva de Camille sobre energia e arte."
            camille "Exato! Cada obra carrega a energia de quem a criou!"
            camille "Quando você se conecta com uma obra, consegue sentir a essência que o artista colocou nela!"
            camille "É reconfortante encontrar alguém que valoriza a sensibilidade tanto quanto eu..."
            huey "Nossa, Camille, você descreveu perfeitamente! É exatamente isso que sinto quando olho para uma pintura!"
            huey "Sua abordagem é... espiritual."

        "Compartilhar sua própria perspectiva sobre arte e espiritualidade":
            $ points_huey += 1
            $ points_camille += 1
            narrator "Compartilhei minha própria visão sobre arte e espiritualidade, tentando encontrar um meio termo."
            huey "Interessante perspectiva. Você parece equilibrar bem os dois lados."
            huey "Você tem uma forma única de ver as coisas..."
            camille "Sinto que você tem uma energia muito equilibrada... como se conseguisse ver o valor em ambas as abordagens."
            camille "É reconfortante saber que você valoriza tanto a arte quanto a espiritualidade..."

        "Perguntar a Huey sobre seus projetos artísticos":
            $ points_huey += 2
            narrator "Perguntei sobre os projetos artísticos de Huey."
            huey "Bem... sempre me conecto com a energia criativa antes de começar a pintar."
            huey "É raro encontrar alguém que realmente entenda de sensibilidade..."
            camille "Fascinante! Eu também sinto energia, mas nunca pensei em expressá-la através da arte como você faz!"
            camille "É interessante como vocês dois parecem ter gostos similares..."

        "Perguntar a Camille sobre suas práticas espirituais":
            $ points_camille += 2
            narrator "Perguntei sobre as práticas espirituais de Camille."
            camille "Bem... uso meditação e mindfulness para me conectar com a energia universal."
            camille "É reconfortante encontrar alguém que valoriza a sensibilidade tanto quanto eu..."
            huey "Interessante. Sua abordagem é... metódica."
            huey "É raro encontrar alguém que sinta energia de forma tão... espiritual."

    # Cena adicional 2 – Workshop prático
    hide huey
    hide camille
    scene bg art_room with dissolve
    show huey gentle at left
    show camille gentle at right

    narrator "Decidimos colocar a teoria em prática. Huey propôs um workshop de pintura para explorar juntas a conexão entre arte e energia."

    huey "Vamos pintar! Vou te mostrar como sinto a energia fluir através das cores e formas!"
    huey "Camille, você vai ver como é diferente quando você se conecta com a essência criativa!"

    camille "Que ideia maravilhosa! E antes de começar, vamos meditar um pouco? Para alinhar nossa energia criativa?"
    camille "A arte flui melhor quando estamos conectadas com nossa essência mais profunda."

    huey "Meditar? Camille, que ideia linda! É exatamente isso que faço antes de pintar!"
    huey "Sinto que preciso me conectar com algo maior antes de colocar a tinta na tela..."

    camille "Huey, você entende perfeitamente! A arte começa com essa conexão interior, com a energia que você canaliza."
    camille "Quando você está alinhada com sua essência, a obra ganha vida própria!"

    narrator "O workshop começou, e foi fascinante ver como Huey e Camille complementavam perfeitamente suas abordagens sensíveis."

    huey "Nossa... quando me conecto assim, sinto que as cores escolhem a si mesmas!"
    huey "É como se a obra já existisse em algum lugar e eu apenas a estivesse revelando..."

    camille "Exato! Huey, você está canalizando a energia criativa perfeitamente!"
    camille "Sinto a energia fluindo através de você... é lindo de ver!"

    narrator "Huey e Camille trabalhavam em perfeita sintonia, cada uma contribuindo com sua sensibilidade única para a criação."

    menu:
        "Focar na conexão emocional com a arte":
            $ points_huey += 3
            narrator "Concordei com a abordagem emocional de Huey."
            huey "Exato! A arte é sobre conectar-se com as emoções mais profundas!"
            huey "Cada pincelada é um sentimento, cada cor é uma emoção traduzida em forma!"
            camille "Huey, você expressou perfeitamente! É exatamente isso que sinto quando me conecto com a energia criativa!"

        "Explorar a energia espiritual na criação":
            $ points_camille += 3
            narrator "Concordei com a abordagem espiritual de Camille."
            camille "Exato! A arte é sobre canalizar a energia universal!"
            camille "Quando você se conecta com essa energia, a obra ganha vida própria!"
            huey "Nossa, Camille, você descreveu exatamente o que sinto quando estou no meu estado criativo!"

        "Combinar sensibilidade artística e espiritual":
            $ points_huey += 2
            $ points_camille += 2
            narrator "Sugeri que combinassem ambas as abordagens sensíveis."
            huey "Que ideia linda! Podemos explorar como a sensibilidade artística e espiritual se complementam!"
            camille "Sim! É fascinante como chegamos ao mesmo lugar por caminhos diferentes!"
            huey "É como se fôssemos duas almas gêmeas da criatividade!"

    # Cena adicional 3 – Reflexão
    hide huey
    hide camille
    scene bg art_room with dissolve
    show huey gentle at left
    show camille gentle at right

    narrator "Após o workshop, decidimos refletir sobre a conexão especial que havíamos descoberto."

    huey "Nossa... nunca pensei que encontraria alguém que sentisse a arte da mesma forma que eu."
    huey "Camille, você realmente entende o que é canalizar emoções através da criação!"

    camille "Huey, eu que fico impressionada! Sua sensibilidade para capturar a essência das coisas..."
    camille "É como se você conseguisse traduzir em cores e formas o que eu sinto apenas como energia."

    huey "Camille, você descreveu perfeitamente! É exatamente isso que sinto quando pinto!"
    huey "É como se estivéssemos falando a mesma língua, apenas usando meios diferentes!"

    camille "Sim! E é incrível como chegamos ao mesmo lugar por caminhos diferentes."
    camille "Você através da arte, eu através da meditação... mas ambas sentimos a mesma conexão profunda."

    narrator "Era como se tivessem encontrado uma alma gêmea sensível. Ambas compartilhavam a mesma capacidade de perceber e expressar as energias sutis do mundo."

    # Momento de crescimento mútuo
    narrator "Por um momento, ambas ficaram em silêncio, processando a conexão especial que haviam descoberto."

    huey "Camille... obrigada por me mostrar que há mais na arte do que apenas técnica."
    huey "Você me ensinou que a energia espiritual pode ser tão poderosa quanto a expressão artística."

    camille "Huey... obrigada por me mostrar que a arte pode ser tão profunda!"
    camille "Você me ensinou que cada pincelada pode carregar a mesma energia que sinto na meditação!"

    # Crescimento mútuo
    narrator "Era como se tivessem descoberto que eram duas almas da mesma essência - ambas sensíveis e conectadas com as energias sutis do mundo."

    # Opções de aprofundamento
    menu:
        "Sugerir uma colaboração em arte espiritual":
            $ points_huey += 2
            $ points_camille += 2
            narrator "Sugeri que Huey e Camille colaborassem em um projeto de arte espiritual."
            huey "Que ideia maravilhosa! Podemos criar um workshop que combine meditação e pintura!"
            camille "Nossa, que lindo! Eu posso guiar as práticas de conexão energética, e você pode ensinar a expressar isso através da arte!"
            huey "Exato! Meditação para conectar, arte para expressar! Seria uma experiência completa!"

        "Perguntar sobre suas práticas criativas":
            $ points_huey += 1
            $ points_camille += 1
            narrator "Perguntei sobre as práticas criativas de cada uma."
            huey "Bem... sempre medito antes de pintar, para me conectar com a energia criativa."
            huey "E você, Camille? Como você canaliza essa energia que sente?"
            camille "Eu medito e sinto a energia fluir... mas nunca pensei em expressá-la através da arte como você faz!"

        "Refletir sobre a conexão especial":
            $ points_huey += 1
            $ points_camille += 1
            narrator "Sugeri que refletissem sobre a conexão especial que haviam descoberto."
            huey "Nunca pensei que encontraria alguém que sentisse a arte da mesma forma que eu..."
            camille "E eu nunca imaginei que encontraria alguém que canalizasse energia através da arte como você!"
            huey "É como se fôssemos duas almas gêmeas da sensibilidade..."

    # Memória compartilhada especial
    $ add_shared_memory("sensitive_souls_connection", ["huey", "camille"], "O momento em que descobrimos nossa conexão especial como almas sensíveis e criativas")

    hide huey
    hide camille
    scene bg art_room with dissolve

    narrator "O sol começava a se pôr sobre a galeria, mas a conversa continuava inspiradora."
    narrator "Era como se tivéssemos descoberto algo especial... uma conexão entre duas perspectivas que pareciam opostas, mas que na verdade se complementavam perfeitamente."

    narrator "Huey e Camille haviam encontrado um terreno comum, e eu mal podia esperar para ver o que essa colaboração poderia gerar..."
    narrator "Mas também havia algo de... tensão no ar, como se cada uma quisesse ser a única a compartilhar essa paixão comigo."

    narrator "Era como se tivéssemos descoberto uma nova forma de ver o mundo, onde arte e espiritualidade dançavam juntas em perfeita harmonia."
    narrator "Mas também havia algo de... estranho no ar, como se cada uma quisesse ser a única a me ensinar sobre sensibilidade."

    return
