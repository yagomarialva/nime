# === EVENTO KATIA E NICOLE ===
# Cinefila Tsundere vs. Metodista Analítica

label evento_katia_nicole:
    $ points_katia += 1
    scene bg biblioteca with dissolve
    show katia neutral at left
    show nicole neutral at right

    narrator "Katia me convidou para uma discussão na biblioteca da universidade. O ambiente estava silencioso, com estudantes estudando e o aroma de livros no ar."
    narrator "Nicole apareceu de surpresa, carregando uma pasta cheia de documentos e com um ar metódico."

    katia "Hmm... interessante que você tenha vindo. Estava pensando em algo importante sobre narrativas..."
    katia "Preciso de sua opinião sobre como analisar a estrutura de um filme de forma mais profunda."

    nicole "Que coincidência! Eu também estava pensando em análise narrativa."
    nicole "Estou organizando um projeto sobre como estruturar histórias que realmente engajem o público."

    katia "Análise narrativa? Nicole, você também se interessa por cinema?"
    katia "N-não é como se eu estivesse impressionada ou qualquer coisa assim... mas é raro encontrar alguém que realmente entende de narrativa."

    nicole "Sim, adoro analisar como as histórias funcionam. Cada elemento tem seu propósito, cada cena contribui para o todo."
    nicole "É fascinante como podemos quebrar uma narrativa em componentes e entender por que ela funciona."

    katia "Exato! E você já percebeu como alguns diretores usam a montagem para criar tensão?"
    katia "É tipo... cada corte tem uma razão de ser, cada plano conta uma parte da história."

    nicole "Katia, você entende exatamente o que eu quero dizer! A narrativa é como um sistema complexo onde cada parte se conecta."
    nicole "E quando você analisa os padrões, consegue identificar por que certas histórias nos tocam mais profundamente."

    narrator "Senti que havia uma conexão genuína entre elas. Ambas compartilhavam a mesma paixão por entender como as narrativas funcionam, apenas com abordagens ligeiramente diferentes."

    scene bg biblioteca with dissolve
    menu:
        "Discutir técnicas de montagem cinematográfica":
            $ points_katia += 3
            narrator "Concordei com a paixão de Katia pela análise cinematográfica."
            katia "Exato! A montagem é onde a magia acontece! Cada corte pode mudar completamente o significado de uma cena."
            katia "Você já viu como o Hitchcock usa a montagem para criar suspense? É genial!"
            nicole "Fascinante! E você já analisou como diferentes ritmos de montagem afetam a percepção emocional do espectador?"

        "Explorar padrões narrativos universais":
            $ points_nicole += 3
            narrator "Concordei com a abordagem analítica de Nicole."
            nicole "Exato! Existem padrões que se repetem em todas as culturas e épocas."
            nicole "A jornada do herói, os arquétipos, as estruturas de três atos... é fascinante como funcionam!"
            katia "Hmm... você tem razão. Mesmo os filmes mais experimentais seguem alguns padrões básicos."

        "Comparar diferentes gêneros cinematográficos":
            $ points_katia += 2
            $ points_nicole += 2
            narrator "Sugeri que explorassem diferentes gêneros juntas."
            katia "Que ideia interessante! Cada gênero tem suas próprias convenções e subversões."
            nicole "Exato! E é fascinante como alguns diretores misturam gêneros para criar algo único!"
            katia "N-não é como se eu estivesse empolgada ou qualquer coisa assim... mas seria legal analisar juntas!"

    # Cena adicional 2 – Workshop prático
    hide katia
    hide nicole
    scene bg biblioteca with dissolve
    show katia neutral at left
    show nicole neutral at right

    narrator "Decidimos colocar a teoria em prática. Katia propôs analisarmos juntas um filme para aplicar nossas perspectivas."

    katia "Vamos analisar um filme! Tenho algumas obras em mente que são perfeitas para discutir narrativa."
    katia "Nicole, você vai ver como a análise cinematográfica pode ser tão metódica quanto qualquer outra disciplina!"

    nicole "Que ideia excelente! Posso aplicar minha metodologia de análise de dados na estrutura narrativa."
    nicole "Vamos quebrar o filme em componentes e analisar como cada elemento contribui para o todo."

    katia "Exato! E podemos discutir as escolhas do diretor, a fotografia, a trilha sonora..."
    katia "Cada elemento tem uma função específica na narrativa!"

    narrator "O workshop começou, e foi fascinante ver como Katia e Nicole complementavam perfeitamente suas abordagens analíticas."

    nicole "Interessante... posso ver padrões claros na estrutura narrativa."
    nicole "Cada ato tem sua função, cada personagem tem seu arco definido... é como um sistema!"

    katia "Exato! E você percebeu como o diretor usa a fotografia para reforçar os temas?"
    katia "Cada plano é uma escolha consciente... nada é por acaso!"

    narrator "Katia e Nicole trabalhavam em perfeita sintonia, cada uma contribuindo com sua perspectiva única para a análise."

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
    scene bg biblioteca with dissolve
    show katia neutral at left
    show nicole neutral at right

    narrator "Após a análise, decidimos refletir sobre o que havíamos descoberto."

    katia "Nossa... nunca pensei que encontraria alguém que entendesse tanto de narrativa quanto eu."
    katia "Nicole, você realmente conhece cinema! Sua análise foi incrível!"

    nicole "Katia, eu que fico impressionada! Sua capacidade de perceber detalhes técnicos que eu nem notava..."
    nicole "É fascinante como complementamos perfeitamente nossas perspectivas analíticas."

    katia "N-não é como se eu estivesse impressionada ou qualquer coisa assim... mas você tem razão."
    katia "É raro encontrar alguém que realmente entende de cinema como você."

    nicole "E é ainda mais raro encontrar alguém que consegue analisar com tanta profundidade técnica."
    nicole "Katia, você tem um olhar único para detalhes que fazem toda a diferença na narrativa."

    narrator "Era como se tivessem encontrado uma alma gêmea intelectual. Ambas compartilhavam a mesma paixão pela análise narrativa, apenas com focos ligeiramente diferentes."

    # Momento de crescimento mútuo
    narrator "Por um momento, ambas ficaram em silêncio, processando a conexão especial que haviam descoberto."

    katia "Nicole... obrigada por me mostrar que há mais na análise do que apenas intuição."
    katia "Você me ensinou que a metodologia pode ser tão fascinante quanto a criatividade."

    nicole "Katia... obrigada por me mostrar que a análise técnica pode ser tão profunda!"
    nicole "Você me ensinou que cada detalhe cinematográfico tem seu propósito na narrativa!"

    # Crescimento mútuo
    narrator "Era como se tivessem descoberto que eram duas faces da mesma moeda - ambas apaixonadas por entender como as narrativas funcionam."

    # Opções de aprofundamento
    menu:
        "Sugerir uma colaboração em análise cinematográfica":
            $ points_katia += 2
            $ points_nicole += 2
            narrator "Sugeri que Katia e Nicole colaborassem em um projeto de análise cinematográfica."
            katia "Que ideia brilhante! Podemos criar um canal de análise cinematográfica juntas!"
            nicole "Nossa, que legal! Eu posso estruturar a metodologia de análise, e você pode focar nos aspectos técnicos!"
            katia "N-não é como se eu estivesse empolgada ou qualquer coisa assim... mas seria incrível trabalhar juntas!"

        "Perguntar sobre filmes favoritos":
            $ points_katia += 1
            $ points_nicole += 1
            narrator "Perguntei sobre os filmes favoritos de cada uma."
            katia "Hmm... tenho vários, mas adoro os filmes do Kubrick. A precisão técnica dele é incrível!"
            nicole "Fascinante! Eu adoro os filmes do Nolan. A forma como ele estrutura narrativas complexas é genial!"
            katia "Nossa, você tem bom gosto! O Nolan realmente domina a estrutura narrativa!"

        "Refletir sobre a conexão especial":
            $ points_katia += 1
            $ points_nicole += 1
            narrator "Sugeri que refletissem sobre a conexão especial que haviam descoberto."
            katia "Nunca pensei que encontraria alguém que entendesse tanto de narrativa quanto eu..."
            nicole "E eu nunca imaginei que encontraria alguém com tanta profundidade analítica!"
            katia "É como se fôssemos feitas para trabalhar juntas... N-não é como se eu estivesse sendo sentimental ou qualquer coisa assim!"

    # Memória compartilhada especial
    $ add_shared_memory("cinematic_analysis_connection", ["katia", "nicole"], "O momento em que descobrimos nossa paixão compartilhada pela análise cinematográfica e narrativa")

    hide katia
    hide nicole
    scene bg biblioteca with dissolve

    narrator "O sol começava a se pôr sobre a biblioteca, mas a conversa continuava inspiradora."
    narrator "Era como se tivéssemos descoberto algo especial... uma conexão entre duas perspectivas que pareciam opostas, mas que na verdade se complementavam perfeitamente."

    narrator "Katia e Nicole haviam encontrado um terreno comum, e eu mal podia esperar para ver o que essa colaboração poderia gerar..."

    return
