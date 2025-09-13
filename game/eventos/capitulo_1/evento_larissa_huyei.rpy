# --- Evento Larissa e Huey ---
label evento_larissa_huey:
    $ points_larissa += 1
    scene bg quadra_volei with dissolve
    show larissa_volei at left
    show huey voley at right

    narrator "Larissa me convidou para uma partida de vôlei na quadra da universidade. O ambiente estava movimentado, com outros estudantes treinando e o som das bolas ecoando."
    narrator "Huey apareceu com seu caderno de desenhos, mas parecia um pouco perdida no ambiente esportivo."

    larissa "Vamos aquecer antes do jogo. Preparado para suar a camisa? Hoje vamos treinar duro!"
    huey "O movimento dos corpos em ação... é como uma dança. Cada gesto conta uma história."
    
    larissa "Dança? Huey, isso é esporte! Precisamos de foco, técnica e determinação para vencer."
    huey "Mas a beleza está no processo, não apenas no resultado final. Cada movimento tem sua própria poesia."
    
    larissa "Beleza? Huey, no vôlei o que importa é ganhar! Pontos, sets, vitórias. É isso que conta."
    huey "E se eu te disser que a verdadeira vitória está em encontrar significado em cada momento?"
    
    narrator "Senti que havia uma tensão sutil entre as duas perspectivas. Larissa focada na competição, Huey na essência artística."

    # Primeira interação: Quadra de vôlei
    menu:
        "Apoiar a abordagem competitiva de Larissa":
            $ points_larissa += 1
            narrator "Concordei que o esporte é sobre vitória e superação."
            larissa "Exato! Sem competição, não há evolução. Precisamos sempre buscar ser melhores."
            huey "Mas e se a evolução vier de dentro? De entender o que realmente nos move?"
            larissa "Huey, números não mentem. Vitórias, recordes, títulos... isso é o que importa."

        "Apoiar a perspectiva artística de Huey":
            $ points_huey += 1
            narrator "Concordei que há beleza e significado no processo esportivo."
            huey "Obrigada por entender... cada movimento é uma expressão, cada jogo uma história."
            larissa "Mas Huey, sem competição, como vamos medir nosso progresso? Como saber se estamos melhorando?"
            huey "Talvez o progresso não seja só sobre números, mas sobre como nos sentimos ao jogar."

        "Tentar mediar as duas perspectivas":
            $ points_larissa += 1
            $ points_huey += 1
            narrator "Sugeri que talvez ambas as abordagens tivessem seu valor."
            larissa "Hmm... talvez você tenha razão. Mas ainda acho que precisamos de objetivos claros."
            huey "E eu acho que podemos encontrar beleza mesmo na competição mais acirrada."

        "Perguntar a Larissa sobre o que a motiva no esporte":
            $ points_larissa += 1
            larissa "A adrenalina da competição, a sensação de superar limites, de vencer! É indescritível."
            huey "Interessante... eu sinto algo parecido quando estou criando. Mas para mim é mais sobre conexão."
            larissa "Conexão? Huey, no vôlei você precisa estar focado em si mesmo, em sua performance."

        "Perguntar a Huey sobre o que ela vê de belo no esporte":
            $ points_huey += 1
            huey "A concentração nos olhos, a sincronia entre os jogadores, a emoção pura... é arte em movimento."
            larissa "Arte? Huey, isso é estratégia, técnica, força física! Não tem nada de artístico."
            huey "Mas Larissa, você não sente que há algo mágico quando tudo se alinha perfeitamente?"

    # Transição para o jardim
    scene bg jardim_universidade with dissolve
    show larissa neutral at left
    show huey neutral at right

    narrator "Depois do treino, Larissa sugeriu que fôssemos ao jardim da universidade para relaxar."
    narrator "O ambiente contrastava com a intensidade da quadra - mais calmo, mais contemplativo."

    larissa "Esse lugar é perfeito para recarregar as energias depois de um treino. Preciso me alongar e hidratar."
    huey "As cores aqui... são inspiradoras. Cada folha, cada flor tem sua própria personalidade."
    
    larissa "Personalidade? Huey, são só plantas. O importante é que o ar fresco ajuda na recuperação muscular."
    huey "Mas Larissa, não sente que há algo especial neste lugar? Como se cada elemento tivesse uma história para contar?"
    
    larissa "História? Huey, estou pensando no próximo treino, na próxima competição. Preciso manter o foco."
    huey "E se eu te disser que parar para observar pode te ajudar a jogar melhor? Às vezes a pausa é parte do processo."

    # Segunda interação: Jardim da universidade
    menu:
        "Apoiar a abordagem prática de Larissa":
            $ points_larissa += 1
            narrator "Concordei que o foco deve estar nos objetivos esportivos."
            larissa "Exato! Cada minuto conta. Preciso otimizar meu tempo para maximizar resultados."
            huey "Mas e se a 'otimização' incluir momentos de contemplação? Às vezes a resposta vem quando paramos de procurar."
            larissa "Huey, no esporte não há tempo para contemplação. É ação, reação, resultado."

        "Apoiar a perspectiva contemplativa de Huey":
            $ points_huey += 1
            narrator "Concordei que há valor em parar e observar."
            huey "Obrigada... às vezes as melhores ideias vêm quando estamos em paz com o momento."
            larissa "Mas Huey, como isso vai me ajudar a vencer? Preciso de estratégias, não de poesia."
            huey "Talvez a poesia seja a estratégia que você está procurando."

        "Tentar encontrar um meio termo":
            $ points_larissa += 1
            $ points_huey += 1
            narrator "Sugeri que talvez ambas as abordagens pudessem se complementar."
            larissa "Hmm... talvez você tenha razão. Mas ainda acho que precisamos de foco nos objetivos."
            huey "E eu acho que podemos encontrar clareza mesmo nos momentos mais calmos."

        "Perguntar a Larissa sobre seus objetivos competitivos":
            $ points_larissa += 1
            larissa "Quero ser a melhor. Competir em alto nível, quebrar recordes, ganhar títulos."
            huey "E o que acontece depois que você conquista tudo isso? O que fica?"
            larissa "Huey, você não entende. A competição nunca acaba. Sempre há um próximo nível para alcançar."

        "Perguntar a Huey sobre o que a inspira na natureza":
            $ points_huey += 1
            huey "A imperfeição perfeita de cada folha, a forma como a luz dança entre as árvores... é pura arte."
            larissa "Arte? Huey, isso não vai me ajudar a melhorar meu saque ou minha defesa."
            huey "Mas Larissa, você não sente que há uma conexão entre a harmonia da natureza e a fluidez do movimento?"

    # Transição para a cafeteria
    scene bg cafeteria with dissolve
    show larissa neutral at left
    show huey neutral at right

    narrator "Para encerrar o dia, decidimos ir até a cafeteria da universidade para tomar algo e continuar a conversa."
    narrator "O ambiente estava movimentado, com estudantes conversando e o barulho das máquinas de café."

    larissa "Depois de tanto exercício, um suco gelado cai muito bem! Preciso repor os eletrólitos."
    huey "E um café para me manter alerta... preciso finalizar alguns esboços que fiz hoje."
    
    larissa "Ainda está desenhando? Huey, você deveria estar pensando no próximo treino, não em desenhos."
    huey "Mas Larissa, estes desenhos são importantes para mim. Eles capturam momentos que nunca mais voltarão."
    
    larissa "Momentos? Huey, o que importa é o futuro, os próximos jogos, as próximas vitórias!"
    huey "E se eu te disser que entender o passado pode te ajudar a melhorar no futuro?"

    # Terceira interação: Cafeteria
    menu:
        "Apoiar a visão focada no futuro de Larissa":
            $ points_larissa += 1
            narrator "Concordei que o foco deve estar nos objetivos futuros."
            larissa "Exato! Preciso sempre estar pensando no próximo passo, na próxima melhoria."
            huey "Mas e se parar para refletir sobre o que já conquistou te der força para continuar?"
            larissa "Huey, reflexão não ganha jogos. Ação, determinação, foco... isso sim."

        "Apoiar a perspectiva reflexiva de Huey":
            $ points_huey += 1
            narrator "Concordei que há valor em refletir sobre o presente e o passado."
            huey "Obrigada... cada momento tem sua própria beleza e lição."
            larissa "Mas Huey, como isso vai me ajudar a vencer? Preciso de resultados, não de filosofia."
            huey "Talvez a filosofia seja o que está faltando para você encontrar uma nova forma de jogar."

        "Tentar unir as duas perspectivas":
            $ points_larissa += 1
            $ points_huey += 1
            narrator "Sugeri que talvez ambas as abordagens pudessem trabalhar juntas."
            larissa "Hmm... talvez você tenha razão. Mas ainda acho que precisamos de foco nos objetivos."
            huey "E eu acho que podemos encontrar clareza mesmo nos momentos mais reflexivos."

        "Perguntar a Larissa sobre o que a motiva a continuar competindo":
            $ points_larissa += 1
            larissa "A sensação de superar limites, de ser melhor que ontem, de vencer! É viciante."
            huey "E quando você não vence? O que te mantém motivada?"
            larissa "Huey, derrota é só combustível para treinar mais duro. Cada perda me torna mais forte."
            huey "Mas e se houver outras formas de se fortalecer além da competição?"

        "Perguntar a Huey sobre o que ela aprende com seus desenhos":
            $ points_huey += 1
            huey "Cada desenho me ensina algo sobre mim mesma, sobre como vejo o mundo."
            larissa "E como isso vai te ajudar na vida real? Na carreira, nos estudos?"
            huey "Larissa, talvez a 'vida real' seja exatamente isso: entender quem somos e o que nos move."
            larissa "Huey, você precisa de objetivos concretos, metas mensuráveis, resultados tangíveis."

    # === MOMENTO DE REFLEXÃO E CRESCIMENTO MÚTUO ===
    narrator "Por um momento, todas ficaram em silêncio, processando as diferentes perspectivas que haviam sido compartilhadas."
    narrator "O ambiente da cafeteria parecia ter se transformado em um espaço de reflexão profunda."
    
    # Larissa mostra crescimento
    larissa "Huey... eu nunca tinha pensado no esporte dessa forma. Sempre foquei apenas em vencer, em ser melhor."
    larissa "Mas talvez você tenha razão. Talvez haja algo mais profundo que eu estava perdendo."
    
    # Huey mostra crescimento
    huey "E eu nunca tinha considerado que a competição pudesse ser uma forma de arte também."
    huey "A paixão que você tem, a determinação... isso também é belo, também tem significado."
    
    # Momento de conexão
    narrator "As duas se olharam com uma nova compreensão, como se tivessem descoberto algo importante sobre si mesmas."
    
    larissa "Talvez... talvez possamos aprender uma com a outra. Eu posso te ensinar sobre determinação e foco."
    huey "E eu posso te mostrar como encontrar beleza e significado em cada momento."
    
    # Crescimento mútuo
    narrator "Era como se cada uma tivesse encontrado uma parte de si mesma que não sabia que estava perdida."
    narrator "Larissa descobrindo que há poesia na competição, Huey descobrindo que há arte na determinação."
    
    # Promessa de continuidade
    larissa "Que tal treinarmos juntas? Eu te ensino sobre esporte, você me ensina sobre... sobre ver as coisas de forma diferente."
    huey "Adorei a ideia! E posso desenhar você treinando, capturar a beleza da sua determinação."
    
    narrator "Ambas sorriram, e pela primeira vez, pareciam verdadeiramente conectadas."
    
    # Memória compartilhada especial
    $ add_shared_memory("sport_art_connection", ["larissa", "huey"], "O momento em que descobrimos que competição e arte podem coexistir harmoniosamente")

    hide larissa
    hide huey
    narrator "Após a conversa, nos despedimos com sorrisos e a promessa de repetir a experiência."
    narrator "Foi um dia que mudou a forma como vemos o esporte e a arte - não como opostos, mas como complementos."
    narrator "Era como se tivéssemos descoberto uma nova forma de ver o mundo, onde determinação e beleza dançavam juntas em perfeita harmonia."

    jump capitulo1_final
