# === EVENTO KATIA E NICOLE - PRIMEIRO ENCONTRO ===
# Cinefila Tsundere vs. Metodista Analítica

label evento_katia_nicole:
    $ points_katia += 1
    scene bg library with dissolve
    narrator "Entrei no laboratório de comunicação e análise de dados da universidade, procurando um lugar para estudar. O ambiente estava silencioso, com computadores e equipamentos de análise."
    narrator "Foi então que percebi que não estava sozinho..."

    # Apresentação natural da Katia
    show katia neutral at left
    katia "Ah, você! Que coincidência te encontrar aqui."
    katia "Estava procurando um lugar silencioso para trabalhar em um projeto sobre análise narrativa."
    katia "N-não é como se eu estivesse procurando companhia ou qualquer coisa assim... mas é bom te ver aqui."

    narrator "Katia se acomodou em uma mesa próxima, carregando um laptop e alguns livros sobre teoria cinematográfica. Havia algo intenso em sua presença, como se ela estivesse sempre analisando tudo ao redor."

    # Apresentação natural da Nicole
    show nicole neutral at right
    nicole "Ah, você também está aqui! Que sincronia perfeita."
    nicole "Estou trabalhando em um projeto sobre metodologias de análise narrativa... é fascinante como podemos quantificar elementos criativos."

    narrator "Nicole organizou seus materiais com precisão metódica - cadernos, canetas coloridas, até um laptop com gráficos complexos na tela."
    narrator "Havia algo genuíno em sua paixão pelos dados e pela estrutura, mas também notei um olhar curioso em direção a Katia."

    # Apresentação entre elas
    narrator "Ambas pareceram interessadas em conhecer a perspectiva uma da outra sobre os temas que estavam trabalhando."

    # Primeiro momento de tensão sutil - elas se conhecem através do jogador
    katia "Hmm... interessante. E qual sua abordagem para análise narrativa? Você prefere análise técnica ou mais estrutural?"
    katia "Este projeto que estou fazendo... é sobre como diretores usam a montagem para criar tensão."

    nicole "Que coincidência! Eu também estou trabalhando com análise narrativa, mas focando em padrões estruturais."
    nicole "Estou organizando um projeto sobre como estruturar histórias que realmente engajem o público."

    # Primeiro momento de tensão sutil - elas se conhecem
    katia "Análise narrativa? Você também se interessa por cinema?"
    katia "N-não é como se eu estivesse impressionada ou qualquer coisa assim... mas é raro encontrar alguém que realmente entenda de narrativa."

    nicole "Sim, adoro analisar como as histórias funcionam. Cada elemento tem seu propósito, cada cena contribui para o todo."
    nicole "É fascinante como podemos quebrar uma narrativa em componentes e entender por que ela funciona."

    # Apresentação entre elas
    katia "Hmm... interessante. Sou Katia, estudo cinema e análise de narrativas."
    katia "N-não é como se eu estivesse procurando amizade ou qualquer coisa assim... mas é bom conhecer alguém que entende de narrativa."

    nicole "Prazer, Nicole. Estudo comunicação estratégica e análise de dados comportamentais."
    nicole "É reconfortante encontrar alguém que valoriza a precisão tanto quanto eu..."

    katia "Hmm... comunicação estratégica? Interessante."
    katia "N-não que eu me importe, mas sua abordagem parece... metódica."

    nicole "E sua paixão pelo cinema é... inspiradora."
    nicole "É fascinante como conseguimos ver a mesma coisa de perspectivas diferentes."

    # Ciúmes sutis começam a aparecer
    katia "Exato! E você já percebeu como alguns diretores usam a montagem para criar tensão?"
    katia "É tipo... cada corte tem uma razão de ser, cada plano conta uma parte da história."
    katia "N-não que eu me importe, mas você parece ter uma perspectiva interessante sobre isso..."

    nicole "Katia, você entende exatamente o que eu quero dizer! A narrativa é como um sistema complexo onde cada parte se conecta."
    nicole "E quando você analisa os padrões, consegue identificar por que certas histórias nos tocam mais profundamente."
    nicole "É... reconfortante encontrar alguém que compartilha essa paixão."

    # Tensão sutil entre elas
    narrator "Senti que havia uma tensão sutil no ar. Ambas pareciam interessadas em se conhecer, mas também havia algo de... competitividade?"
    narrator "E eu estava no meio, observando como duas abordagens aparentemente complementares podiam criar uma dinâmica interessante."

    scene bg library with dissolve
    menu:
        "Discutir técnicas de montagem cinematográfica":
            $ points_katia += 3
            narrator "Concordei com a paixão de Katia pela análise cinematográfica."
            katia "Exato! A montagem é onde a magia acontece! Cada corte pode mudar completamente o significado de uma cena."
            katia "Você já viu como o Hitchcock usa a montagem para criar suspense? É genial!"
            katia "N-não que eu me importe, mas você parece ter um bom gosto para cinema..."
            nicole "Fascinante! E você já analisou como diferentes ritmos de montagem afetam a percepção emocional do espectador?"
            nicole "É... interessante como você consegue explicar essas coisas de forma tão clara."

        "Explorar padrões narrativos universais":
            $ points_nicole += 3
            narrator "Concordei com a abordagem analítica de Nicole."
            nicole "Exato! Existem padrões que se repetem em todas as culturas e épocas."
            nicole "A jornada do herói, os arquétipos, as estruturas de três atos... é fascinante como funcionam!"
            nicole "É reconfortante encontrar alguém que valoriza a metodologia tanto quanto eu..."
            katia "Hmm... você tem razão. Mesmo os filmes mais experimentais seguem alguns padrões básicos."
            katia "N-não que eu me importe, mas sua abordagem é... interessante."

        "Compartilhar sua própria perspectiva sobre narrativa":
            $ points_katia += 1
            $ points_nicole += 1
            narrator "Compartilhei minha própria visão sobre narrativa, tentando encontrar um meio termo."
            katia "Hmm... interessante perspectiva. Você parece equilibrar bem os dois lados."
            katia "N-não que eu me importe, mas você tem uma forma única de ver as coisas..."
            nicole "Sinto que você tem uma energia muito equilibrada... como se conseguisse ver o valor em ambas as abordagens."
            nicole "É... reconfortante saber que você valoriza tanto a análise técnica quanto a estrutural."

        "Perguntar a Katia sobre seus filmes favoritos":
            $ points_katia += 2
            narrator "Perguntei sobre os filmes favoritos de Katia."
            katia "Hmm... tenho vários, mas adoro os filmes do Kubrick. A precisão técnica dele é incrível!"
            katia "N-não que eu me importe, mas é raro encontrar alguém que realmente entenda de cinema..."
            nicole "Fascinante! Eu adoro os filmes do Nolan. A forma como ele estrutura narrativas complexas é genial!"
            nicole "É... interessante como vocês dois parecem ter gostos similares..."

        "Perguntar a Nicole sobre sua metodologia":
            $ points_nicole += 2
            narrator "Perguntei sobre a metodologia de análise de Nicole."
            nicole "Bem... uso uma abordagem sistemática para quebrar narrativas em componentes mensuráveis."
            nicole "É reconfortante encontrar alguém que valoriza a precisão tanto quanto eu..."
            katia "Hmm... interessante. N-não que eu me importe, mas sua abordagem é... metódica."
            katia "É raro encontrar alguém que analise cinema de forma tão... científica."

    # Cena adicional 2 – Workshop prático
    hide katia
    hide nicole
    scene bg library with dissolve
    show katia neutral at left
    show nicole neutral at right

    narrator "Decidimos colocar a teoria em prática. Katia propôs analisarmos juntas um filme para aplicar nossas perspectivas."

    katia "Vamos analisar um filme! Tenho algumas obras em mente que são perfeitas para discutir narrativa."
    katia "Nicole, você vai ver como a análise cinematográfica pode ser tão metódica quanto qualquer outra disciplina!"
    katia "N-não que eu me importe, mas seria interessante ver como você aborda isso..."

    nicole "Que ideia excelente! Posso aplicar minha metodologia de análise de dados na estrutura narrativa."
    nicole "Vamos quebrar o filme em componentes e analisar como cada elemento contribui para o todo."
    nicole "É... reconfortante trabalhar com alguém que valoriza a precisão tanto quanto eu..."

    katia "Exato! E podemos discutir as escolhas do diretor, a fotografia, a trilha sonora..."
    katia "Cada elemento tem uma função específica na narrativa!"
    katia "N-não que eu me importe, mas você parece ter uma perspectiva interessante sobre isso..."

    narrator "O workshop começou, e foi fascinante ver como Katia e Nicole complementavam perfeitamente suas abordagens analíticas."
    narrator "Mas também notei uma tensão sutil entre elas, como se cada uma quisesse impressionar mais que a outra."

    nicole "Interessante... posso ver padrões claros na estrutura narrativa."
    nicole "Cada ato tem sua função, cada personagem tem seu arco definido... é como um sistema!"
    nicole "É... reconfortante encontrar alguém que entende a importância da estrutura..."

    katia "Exato! E você percebeu como o diretor usa a fotografia para reforçar os temas?"
    katia "Cada plano é uma escolha consciente... nada é por acaso!"
    katia "N-não que eu me importe, mas sua análise é... metódica."

    narrator "Katia e Nicole trabalhavam em perfeita sintonia, cada uma contribuindo com sua perspectiva única para a análise."
    narrator "Mas havia algo de competitivo no ar, como se cada uma quisesse mostrar que entendia melhor o assunto."

    menu:
        "Focar na análise técnica cinematográfica":
            $ points_katia += 3
            narrator "Concordei com a abordagem técnica de Katia."
            katia "Exato! A técnica cinematográfica é fundamental para contar uma história!"
            katia "Cada enquadramento, cada movimento de câmera... tudo tem um propósito narrativo!"
            nicole "Fascinante! E quando você analisa os padrões técnicos, consegue identificar o estilo único de cada diretor!"

        "Explorar a estrutura narrativa sistemática":
            $ points_nicole += 3
            narrator "Concordei com a abordagem sistemática de Nicole."
            nicole "Exato! A estrutura narrativa segue padrões que podem ser analisados e compreendidos!"
            nicole "É fascinante como cada elemento se conecta para criar uma experiência coesa!"
            katia "Hmm... você tem razão. Mesmo os filmes mais experimentais seguem uma lógica interna."

        "Combinar análise técnica e estrutural":
            $ points_katia += 2
            $ points_nicole += 2
            narrator "Sugeri que combinassem ambas as abordagens."
            katia "Que ideia brilhante! Podemos analisar como a técnica serve à estrutura narrativa!"
            nicole "Exato! E como a estrutura guia as escolhas técnicas do diretor!"
            katia "N-não é como se eu estivesse empolgada ou qualquer coisa assim... mas seria incrível trabalhar juntas!"

    # Cena adicional 3 – Reflexão
    hide katia
    hide nicole
    scene bg library with dissolve
    show katia neutral at left
    show nicole neutral at right

    narrator "Após a análise, decidimos refletir sobre o que havíamos descoberto."

    katia "Nossa... nunca pensei que encontraria alguém que entendesse tanto de narrativa quanto eu."
    katia "Nicole, você realmente conhece cinema! Sua análise foi incrível!"
    katia "N-não que eu me importe, mas é raro encontrar alguém com tanta profundidade..."

    nicole "Katia, eu que fico impressionada! Sua capacidade de perceber detalhes técnicos que eu nem notava..."
    nicole "É fascinante como complementamos perfeitamente nossas perspectivas analíticas."
    nicole "É... reconfortante encontrar alguém que valoriza a precisão tanto quanto eu..."

    katia "N-não é como se eu estivesse impressionada ou qualquer coisa assim... mas você tem razão."
    katia "É raro encontrar alguém que realmente entende de cinema como você."
    katia "N-não que eu me importe, mas você parece ter um gosto... interessante."

    nicole "E é ainda mais raro encontrar alguém que consegue analisar com tanta profundidade técnica."
    nicole "Katia, você tem um olhar único para detalhes que fazem toda a diferença na narrativa."
    nicole "É... reconfortante saber que você valoriza tanto a análise técnica quanto a estrutural."

    narrator "Era como se tivessem encontrado uma alma gêmea intelectual. Ambas compartilhavam a mesma paixão pela análise narrativa, apenas com focos ligeiramente diferentes."
    narrator "Mas também havia algo de... competitividade no ar, como se cada uma quisesse mostrar que entendia melhor o assunto."

    # Momento de crescimento mútuo
    narrator "Por um momento, ambas ficaram em silêncio, processando a conexão especial que haviam descoberto."

    katia "Nicole... obrigada por me mostrar que há mais na análise do que apenas intuição."
    katia "Você me ensinou que a metodologia pode ser tão fascinante quanto a criatividade."
    katia "N-não que eu me importe, mas sua abordagem é... interessante."

    nicole "Katia... obrigada por me mostrar que a análise técnica pode ser tão profunda!"
    nicole "Você me ensinou que cada detalhe cinematográfico tem seu propósito na narrativa!"
    nicole "É... reconfortante encontrar alguém que compartilha essa paixão..."

    # Crescimento mútuo
    narrator "Era como se tivessem descoberto que eram duas faces da mesma moeda - ambas apaixonadas por entender como as narrativas funcionam."
    narrator "Mas também havia algo de... ciúmes no ar, como se cada uma quisesse ser a única a compartilhar essa paixão comigo."

    # Opções de aprofundamento
    menu:
        "Sugerir uma colaboração em análise cinematográfica":
            $ points_katia += 2
            $ points_nicole += 2
            narrator "Sugeri que Katia e Nicole colaborassem em um projeto de análise cinematográfica."
            katia "Que ideia brilhante! Podemos criar um canal de análise cinematográfica juntas!"
            katia "N-não que eu me importe, mas seria interessante trabalhar com alguém que entende de narrativa..."
            nicole "Nossa, que legal! Eu posso estruturar a metodologia de análise, e você pode focar nos aspectos técnicos!"
            nicole "É... reconfortante saber que você valoriza tanto a análise técnica quanto a estrutural..."
            katia "N-não é como se eu estivesse empolgada ou qualquer coisa assim... mas seria incrível trabalhar juntas!"

        "Perguntar sobre filmes favoritos":
            $ points_katia += 1
            $ points_nicole += 1
            narrator "Perguntei sobre os filmes favoritos de cada uma."
            katia "Hmm... tenho vários, mas adoro os filmes do Kubrick. A precisão técnica dele é incrível!"
            katia "N-não que eu me importe, mas é raro encontrar alguém que realmente entenda de cinema..."
            nicole "Fascinante! Eu adoro os filmes do Nolan. A forma como ele estrutura narrativas complexas é genial!"
            nicole "É... interessante como vocês dois parecem ter gostos similares..."
            katia "Nossa, você tem bom gosto! O Nolan realmente domina a estrutura narrativa!"

        "Refletir sobre a conexão especial":
            $ points_katia += 1
            $ points_nicole += 1
            narrator "Sugeri que refletissem sobre a conexão especial que haviam descoberto."
            katia "Nunca pensei que encontraria alguém que entendesse tanto de narrativa quanto eu..."
            katia "N-não que eu me importe, mas é raro encontrar alguém com tanta profundidade..."
            nicole "E eu nunca imaginei que encontraria alguém com tanta profundidade analítica!"
            nicole "É... reconfortante saber que você valoriza tanto a análise técnica quanto a estrutural..."
            katia "É como se fôssemos feitas para trabalhar juntas... N-não é como se eu estivesse sendo sentimental ou qualquer coisa assim!"

        "Compartilhar sua própria perspectiva sobre narrativa":
            $ points_katia += 1
            $ points_nicole += 1
            narrator "Compartilhei minha própria visão sobre narrativa, tentando encontrar um meio termo."
            katia "Hmm... interessante perspectiva. Você parece equilibrar bem os dois lados."
            katia "N-não que eu me importe, mas você tem uma forma única de ver as coisas..."
            nicole "Sinto que você tem uma energia muito equilibrada... como se conseguisse ver o valor em ambas as abordagens."
            nicole "É... reconfortante saber que você valoriza tanto a análise técnica quanto a estrutural..."

    # Memória compartilhada especial
    $ add_shared_memory("cinematic_analysis_connection", ["katia", "nicole"], "O momento em que descobrimos nossa paixão compartilhada pela análise cinematográfica e narrativa")

    hide katia
    hide nicole
    scene bg library with dissolve

    narrator "O sol começava a se pôr sobre a biblioteca, mas a conversa continuava inspiradora."
    narrator "Era como se tivéssemos descoberto algo especial... uma conexão entre duas perspectivas que pareciam opostas, mas que na verdade se complementavam perfeitamente."

    narrator "Katia e Nicole haviam encontrado um terreno comum, e eu mal podia esperar para ver o que essa colaboração poderia gerar..."
    narrator "Mas também havia algo de... tensão no ar, como se cada uma quisesse ser a única a compartilhar essa paixão comigo."

    narrator "Era como se tivéssemos descoberto uma nova forma de ver o mundo, onde análise técnica e estrutural dançavam juntas em perfeita harmonia."
    narrator "Mas também havia algo de... estranho no ar, como se cada uma quisesse ser a única a me ensinar sobre narrativa."

    return
