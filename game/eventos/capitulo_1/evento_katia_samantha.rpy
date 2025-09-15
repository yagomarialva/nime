# --- Evento Katia e Samantha - PRIMEIRO ENCONTRO ---
label evento_katia_samantha:
    $ points_katia += 1
    scene bg cinema with dissolve
    narrator "Entrei no cinema da universidade, procurando uma sessão interessante para assistir. O ambiente estava silencioso, com poucas pessoas na sessão da tarde."
    narrator "Escolhi um filme cult que estava sendo exibido - algo sobre identidade e realidade. Foi então que percebi que não estava sozinho..."

    # Apresentação natural da Katia
    show katia neutral at left
    katia "Hmm... você também veio assistir este filme? Interessante."
    katia "Sou Katia, estudo cinema e análise de narrativas. Este diretor tem uma abordagem única sobre subjetividade."
    katia "N-não é como se eu estivesse procurando companhia ou qualquer coisa assim... mas é raro encontrar alguém que aprecie cinema de verdade."

    narrator "Katia se acomodou na poltrona ao lado, carregando um caderno de anotações e uma caneta. Havia algo intenso em sua presença, como se ela estivesse sempre analisando tudo ao redor."

    # Apresentação natural da Samantha
    show samantha happy at right
    samantha "Nossa, que legal! Vocês também vieram assistir este filme?"
    samantha "Sou Samantha, estudo jogos e narrativas interativas! Este filme tem um enredo tão interessante... cheio de camadas filosóficas!"
    samantha "É tipo um RPG com múltiplas escolhas! Imaginem só... uma aventura onde vocês são aventureiros em uma realidade alternativa!"

    narrator "Samantha chegou com passos animados, carregando uma mochila cheia de livros e um caderno de anotações. Havia algo contagiante em seu entusiasmo."

    # Apresentação do jogador
    narrator "Me apresentei brevemente, explicando que era novo na universidade e estava explorando diferentes formas de arte e entretenimento."
    narrator "Ambas pareceram interessadas em conhecer minha perspectiva sobre o filme que estávamos prestes a assistir."

    katia "Hmm... interessante. E qual sua abordagem para análise cinematográfica? Você prefere análise técnica ou mais emocional?"
    katia "Este diretor tem uma abordagem única sobre subjetividade... não é para qualquer um."

    samantha "Nossa, que legal! Eu adoro quando as pessoas se interessam por narrativas complexas!"
    samantha "Este filme tem um enredo tão interessante... cheio de camadas filosóficas! É tipo um RPG com múltiplas escolhas!"

    katia "Tsc... é só um filme, não precisa fazer uma tese. E para de falar tão alto, estamos num cinema!"

    samantha "Ah, desculpa! É que eu fico muito empolgada com filmes cult. E claro que precisa de análise profunda!"
    samantha "O diretor usa simbolismo freudiano o tempo inteiro, e a fotografia tem influências do expressionismo alemão!"
    samantha "É tipo quando você joga um jogo indie e percebe todas as referências escondidas!"

    katia "Nossa, que pretensioso. Você nem deve ter assistido metade dos filmes que está citando."
    katia "E para de mexer na mochila, está fazendo barulho!"

    samantha "Ah, desculpa! É que eu trouxe meu caderno para anotar as referências... e alguns livros de teoria cinematográfica."
    samantha "E também trouxe meu tablet para jogar algo depois! Você não se importa, né? Posso compartilhar minhas anotações depois!"

    katia "Hmpf... como se eu precisasse das suas anotações. Eu já sei tudo sobre esse diretor."
    katia "Mas... se você quiser, posso te explicar algumas coisas que talvez você não tenha entendido."

    narrator "O clima entre elas era... tenso, mas havia algo de genuíno na interação. Katia tentando manter sua fachada tsundere, Samantha sendo sua versão nerd desajeitada."
    narrator "E eu estava no meio, observando como duas abordagens aparentemente opostas podiam coexistir."
    scene bg cinema_katia_samantha with dissolve
    menu:
        "Discutir simbolismos do filme com Katia":
            $ points_katia += 3
            show katia blush at left
            narrator "Concordei com a análise de Katia sobre os simbolismos do filme."
            katia "Você percebeu a metáfora sobre a perda da identidade? Pff... não achei que você fosse notar algo assim."
            katia "Quer dizer, não que eu esteja impressionada nem nada! Hmpf."
            katia "É só que... é raro encontrar alguém que realmente entende de cinema. N-não que eu me importe com sua opinião!"
            samantha "Nossa, que análise profunda! Eu tinha pensado nisso também, mas não consegui articular tão bem..."
            katia "Tsc... claro que você pensou. Qualquer pessoa com conhecimento básico de cinema pensaria."

        "Conversar com Samantha sobre trilhas sonoras de filmes":
            $ points_samantha += 3
            narrator "Concordei com a paixão de Samantha pela música cinematográfica."
            samantha "A música realmente amplifica as emoções. Tenho uma playlist inteira só de trilhas sonoras marcantes!"
            samantha "E também tenho várias trilhas de jogos! A do Final Fantasy VII é incrível! Quer que eu te envie depois?"
            katia "Hmpf... como se eu não conhecesse trilhas sonoras. Eu tenho a coleção completa do Ennio Morricone."
            samantha "Nossa, sério? Ele é um dos meus compositores favoritos! E você já ouviu as trilhas do Nobuo Uematsu? São épicas!"

        "Compartilhar sua própria perspectiva sobre cinema e jogos":
            $ points_katia += 1
            $ points_samantha += 1
            narrator "Compartilhei minha própria visão sobre cinema e jogos, tentando encontrar um meio termo."
            katia "Interessante perspectiva... você parece equilibrar bem os dois lados."
            samantha "Nossa, que legal! Eu adoro quando as pessoas conseguem ver o valor em ambas as formas de arte!"
            katia "Hmpf... talvez você tenha razão. Mas ainda acho que cinema é superior a jogos."

        "Perguntar a Katia sobre diretores independentes":
            $ points_katia += 3
            show katia neutral at left
            narrator "Concordei com o conhecimento de Katia sobre cinema independente."
            katia "Há muitos talentos emergentes que merecem reconhecimento. Não que você conheça, mas posso te indicar alguns... se quiser."
            katia "Mas só porque eu odeio quando bons diretores passam despercebidos! Não é por sua causa ou algo assim."
            katia "É só que... você parece ter um gosto decente. N-não que eu me importe com sua opinião ou qualquer coisa!"
            samantha "Nossa, que legal! Eu adoraria conhecer mais diretores independentes. Você pode me indicar alguns?"

        "Perguntar a Samantha sobre jogos com narrativas cinematográficas":
            $ points_samantha += 3
            narrator "Perguntei sobre jogos que têm narrativas complexas como filmes."
            samantha "Nossa, que pergunta incrível! Tem vários jogos que são verdadeiras obras de arte!"
            samantha "Tipo Persona 5, que tem uma história incrível, ou até jogos indie como Celeste que falam sobre saúde mental!"
            katia "Tsc... jogos? Sério que você está comparando cinema de arte com videogames?"
            samantha "Ah, mas Katia, os jogos podem ser arte também! Eles têm narrativa, direção, trilha sonora... é tipo cinema interativo!"

        "Tentar mediar a discussão entre as duas":
            $ points_katia += 1
            $ points_samantha += 1
            narrator "Tentei encontrar um meio termo entre as duas perspectivas."
            katia "Hmpf... talvez você tenha razão. Mas ainda acho que cinema é superior a jogos."
            samantha "E eu acho que podemos aprender muito com ambos! Que tal assistirmos filmes que inspiraram jogos?"
            katia "Tsc... se for para educar você sobre cinema de verdade, talvez eu aceite."

    # Cena adicional 1 – Debate no lobby
    
    narrator "Após o filme, fomos para o lobby do cinema, onde começamos a discutir nossas impressões."
    narrator "O ambiente estava mais movimentado agora, com outras pessoas saindo das sessões."
    scene bg cinema_lobby_empty with dissolve
    show katia neutral at left
    show samantha neutral at right

    katia "Bem... o filme foi... aceitável. A direção estava decente, pelo menos."
    samantha "Nossa, que filme incrível! A fotografia estava perfeita, e a trilha sonora me arrepiou!"
    samantha "Você viu como o diretor usou a iluminação para criar aquela atmosfera onírica? É tipo um jogo de terror!"

    katia "Tsc... claro que vi. É técnica básica de cinema. E para de falar tão alto, estamos em público."
    samantha "Ah, desculpa! É que eu fico muito empolgada quando vejo filmes bons. E aquele final... que interpretação você teve?"
    samantha "É tipo quando você termina um RPG e tem que escolher entre múltiplos finais!"

    katia "Hmpf... como se eu fosse compartilhar minha interpretação com você. Mas... se você insistir..."
    katia "O final obviamente representa a fragmentação da identidade moderna. Não que você vá entender."

    samantha "Nossa, que análise profunda! Eu tinha pensado em algo parecido, mas não consegui articular tão bem..."
    samantha "Você é realmente muito inteligente, Katia! É tipo ser uma mestre de RPG que conhece todas as regras!"

    katia "Tsc... claro que sou. E para de me elogiar, é constrangedor."

    menu:
        "Apoiar a análise de Katia":
            $ points_katia += 3
            narrator "Concordei com a interpretação de Katia sobre o filme."
            katia "Pelo menos alguém aqui tem bom senso. A direção foi impecável. Cada cena parecia uma pintura cuidadosamente composta..."
            katia "Mas... acho que só eu reparei nisso. Não que eu me importe."
            samantha "Nossa, que observação! Eu também reparei, mas não consegui expressar tão bem..."

        "Apoiar o entusiasmo de Samantha":
            $ points_samantha += 3
            narrator "Concordei com o entusiasmo de Samantha pelo filme."
            samantha "A trilha foi incrível! Eu fiquei arrepiada em várias cenas."
            samantha "Tenho até a versão em vinil desse compositor. Posso te mostrar depois!"
            katia "Hmpf... como se eu não conhecesse trilhas sonoras. Mas... se você quiser, posso te ensinar sobre compositores de verdade."

        "Tentar unir as duas perspectivas":
            $ points_katia += 1
            $ points_samantha += 1
            narrator "Sugeri que ambas as perspectivas tinham valor."
            katia "Hmpf... talvez você tenha razão. Mas ainda acho que minha análise é superior."
            samantha "E eu acho que podemos aprender muito uma com a outra! Que tal assistirmos mais filmes juntas?"

        "Perguntar a Katia sobre sua paixão pelo cinema":
            $ points_katia += 3
            narrator "Perguntei sobre o que motiva Katia no cinema."
            katia "Cinema é... é arte pura. Cada frame, cada corte, cada som... tudo tem propósito."
            katia "Não é como esses filmes comerciais que você provavelmente assiste. É... é algo maior."
            samantha "Nossa, que lindo! Eu também sinto isso, mas nunca consegui expressar tão bem..."

        "Perguntar a Samantha sobre sua conexão com jogos e cinema":
            $ points_samantha += 3
            narrator "Perguntei sobre como Samantha conecta jogos e cinema."
            samantha "É que ambos contam histórias, sabe? E ambos podem ser arte!"
            samantha "Os jogos têm a vantagem da interatividade, mas o cinema tem a vantagem da imersão total."
            katia "Tsc... jogos são jogos, cinema é cinema. Não confunda as coisas."

    # Cena adicional 2 – Café
    scene bg cinema_cafeteria with dissolve
    narrator "Decidimos tomar um café no cinema enquanto continuávamos a conversa."
    narrator "O ambiente estava mais íntimo agora, com poucas pessoas e uma atmosfera mais relaxada."
    show katia neutral at left
    show samantha neutral at right

    katia "Bem... o café aqui é... aceitável. Pelo menos não é daqueles instantâneos horríveis."
    samantha "Nossa, que legal! Eu adoro cafés de cinema, sempre têm um charme especial!"
    samantha "E olha só, eles têm até aqueles doces que aparecem em filmes clássicos! É tipo um item de RPG!"

    katia "Tsc... você fica empolgada com qualquer coisa, não é? E para de mexer na mesa, está fazendo barulho."
    samantha "Ah, desculpa! É que eu fico muito animada quando estou em lugares legais. E você, Katia, tem algum filme favorito?"

    katia "Hmpf... como se eu fosse compartilhar meus filmes favoritos com você. Mas... se você insistir..."
    katia "Eu adoro filmes que desafiam a mente... tipo os do David Lynch. Não que você vá entender."

    samantha "Nossa, que legal! Eu também gosto muito do David Lynch! Eraserhead é um dos meus favoritos!"
    samantha "Você já assistiu Twin Peaks? A série é incrível! É tipo um anime com mistério e elementos sobrenaturais!"

    katia "Tsc... claro que assisti. E para de falar tão alto, estamos em público."
    katia "Mas... se você quiser, posso te indicar alguns filmes que talvez você não conheça."

    menu:
        "Apoiar o conhecimento de Katia sobre cinema":
            $ points_katia += 3
            narrator "Concordei com o conhecimento de Katia sobre cinema."
            katia "Pelo menos alguém aqui reconhece qualidade. Cinema é arte, não entretenimento barato."
            katia "Mas... se você quiser, posso te ensinar sobre diretores de verdade. Não que eu me importe."
            samantha "Nossa, que legal! Eu adoraria aprender com você! Você é realmente muito inteligente!"

        "Apoiar o entusiasmo de Samantha":
            $ points_samantha += 3
            narrator "Concordei com o entusiasmo de Samantha."
            samantha "Obrigada! É que eu fico muito empolgada quando falo sobre coisas que gosto!"
            samantha "E você, Katia, tem algum jogo favorito? Ou você só assiste filmes? Que tal um RPG de mesa?"
            katia "Tsc... jogos? Sério que você está perguntando isso? Cinema é superior."

        "Tentar encontrar um meio termo":
            $ points_katia += 1
            $ points_samantha += 1
            narrator "Sugeri que ambas as paixões tinham valor."
            katia "Hmpf... talvez você tenha razão. Mas ainda acho que cinema é superior."
            samantha "E eu acho que podemos aprender muito uma com a outra! Que tal assistirmos filmes que inspiraram jogos?"
            samantha "Tipo Akira inspirou Cyberpunk, ou Ghost in the Shell inspirou vários jogos de ficção científica!"

        "Perguntar a Katia sobre o que a motiva no cinema":
            $ points_katia += 3
            narrator "Perguntei sobre a paixão de Katia pelo cinema."
            katia "Cinema é... é arte pura. Cada frame, cada corte, cada som... tudo tem propósito."
            katia "Não é como esses filmes comerciais que você provavelmente assiste. É... é algo maior."
            samantha "Nossa, que lindo! Eu também sinto isso, mas nunca consegui expressar tão bem..."
            samantha "É tipo quando você joga um jogo indie e percebe que cada pixel foi colocado com carinho!"

        "Perguntar a Samantha sobre sua paixão por jogos":
            $ points_samantha += 3
            narrator "Perguntei sobre a paixão de Samantha por jogos."
            samantha "É que os jogos me fazem sentir parte da história, sabe? É como ser o protagonista!"
            samantha "E muitos jogos têm narrativas incríveis, que rivalizam com os melhores filmes! Tipo Final Fantasy ou Persona!"
            samantha "E RPGs de mesa são ainda melhores! Você cria sua própria história junto com os amigos!"
            katia "Tsc... jogos são jogos, cinema é cinema. Não confunda as coisas."

    # Cena adicional 3 – Exposição
    hide katia
    hide samantha
    scene bg cinema_exhibition with dissolve
    narrator "Exploramos uma pequena exposição de pôsteres de filmes clássicos no cinema."
    scene bg cinema_lobby_empty with dissolve
    show katia neutral at left
    show samantha neutral at right

    menu:
        "Perguntar a Katia sobre o design dos pôsteres":
            $ points_katia += 3
            katia "Eles têm personalidade, sabe? Minimalistas, mas intensos. Como deveria ser."
            katia "Hoje em dia tudo parece feito no piloto automático..."

        "Perguntar a Samantha sobre a evolução do marketing de filmes":
            $ points_samantha += 3
            samantha "Hoje o marketing é quase uma ciência! Adoro estudar isso. É tipo manipulação social, mas artística!"
            samantha "Já viu os trailers dos anos 70? São uma viagem."

        "Comentar sobre como os pôsteres influenciam a percepção do público":
            $ points_katia += 1
            $ points_samantha += 1
            katia "Sim, um pôster bem feito já te prepara pro tipo de experiência que vem."
            samantha "É como um teaser visual. Eu tenho até uma coleção digital deles!"

    # Cena adicional 4 – Fliperama
    scene bg cinema_arcade with dissolve
    narrator "Passamos por uma área de fliperamas no cinema, e Samantha ficou animada."
    show katia neutral at left
    show samantha neutral at right

    menu:
        "Desafiar Samantha para um jogo de terror no fliperama":
            $ points_samantha += 3
            samantha "Você vai se arrepender! Eu platinei todos os Resident Evil."
            samantha "Prepare-se pra levar susto e perder feio."

        "Perguntar a Katia se ela gosta de jogos antigos":
            $ points_katia += 3
            katia "Não sou de jogar, mas esses jogos têm... charme. Meio nostálgico."
            katia "Além disso, ver você se empolgando tanto é... engraçado."

        "Sugerir um torneio entre os três":
            $ points_katia += 1
            $ points_samantha += 1
            katia "Sério? Aposto que vou te vencer só com sorte."
            samantha "Mal posso esperar. Já me sinto no modo competitivo!"

    # Cena adicional 5 – Saída
    scene bg cinema with dissolve
    narrator "Ao final da noite, saímos do cinema e nos despedimos."
    narrator "O ar noturno contrastava com o ambiente climatizado do cinema, criando uma sensação de despertar."
    show katia neutral at left
    show samantha neutral at right

    # Momento de reflexão e crescimento - Primeiro encontro
    narrator "Por um momento, todas ficaram em silêncio, processando a noite que haviam compartilhado."
    
    katia "Bem... foi... menos chato do que eu esperava. Você não é tão irritante quanto parecia."
    katia "É raro encontrar alguém que realmente entenda de cinema... e você parece ter um gosto decente."
    samantha "Nossa, obrigada! Eu também gostei muito de conversar com você!"
    samantha "Você é realmente muito inteligente, Katia. Aprendi muito sobre cinema hoje!"
    samantha "É tipo quando você joga um RPG e encontra um NPC que te ensina coisas incríveis!"

    katia "Tsc... claro que sou. E para de me elogiar, é constrangedor."
    katia "Mas... se você quiser, posso te ensinar mais sobre cinema. Não que eu me importe."

    samantha "Nossa, que legal! Eu adoraria aprender com você!"
    samantha "E talvez eu possa te mostrar alguns jogos que têm narrativas incríveis? Quem sabe você goste!"
    samantha "Tipo Persona 5, que tem uma história incrível, ou até um RPG de mesa! É tipo ser a mestra de uma aventura!"

    katia "Hmpf... jogos? Sério que você ainda está insistindo nisso?"
    katia "Mas... se for para educar você sobre cinema de verdade, talvez eu aceite."

    # Crescimento mútuo
    narrator "Era como se cada uma tivesse encontrado algo que não sabia que estava procurando."
    narrator "Katia descobrindo que há valor no entusiasmo genuíno, Samantha descobrindo que há profundidade na análise crítica."

    menu:
        "Agradecer a Katia pelo convite":
            $ points_katia += 3
            show katia blush at left
            narrator "Agradeci a Katia pela oportunidade de assistir o filme juntos."
            katia "Tsc... eu que agradeço por ter vindo. Mas não se acostuma, tá?"
            katia "N-não é como se eu tivesse gostado da sua companhia ou qualquer coisa assim!"
            katia "É só que... foi menos chato do que eu esperava. Nada mais que isso!"
            samantha "Nossa, que legal! Vocês são muito legais! Obrigada por me incluírem!"

        "Agradecer a Samantha por se juntar a vocês":
            $ points_samantha += 3
            narrator "Agradeci a Samantha por ter se juntado ao grupo."
            samantha "Foi ótimo! Obrigada por me incluir. Vocês são divertidos."
            katia "Tsc... você não é tão irritante quanto parecia. Mas não se acostuma."

        "Sugerir um próximo encontro para assistir outro filme":
            $ points_katia += 1
            $ points_samantha += 1
            show katia blush at left
            narrator "Sugeri que assistissem outro filme juntas no futuro."
            katia "Se for um filme decente... talvez eu aceite."
            katia "N-não é como se eu estivesse ansiosa para sair com você novamente ou qualquer coisa assim!"
            katia "É só que... você tem um gosto razoável. Nada mais que isso!"
            samantha "Vamos sim! Já quero montar um cronograma de filmes cult!"
            samantha "E talvez possamos jogar algo depois? Tenho vários jogos com narrativas incríveis!"

        "Propor uma colaboração entre as duas":
            $ points_katia += 2
            $ points_samantha += 2
            show katia blush at left
            narrator "Sugeri que Katia e Samantha colaborassem em algum projeto."
            katia "Hmpf... colaboração? Como assim?"
            samantha "Nossa, que ideia legal! Podemos fazer um canal no YouTube sobre cinema e jogos!"
            samantha "Ou até um podcast! Tipo 'Cinema e RPG' ou 'Filmes e Animes'! Seria épico!"
            katia "Tsc... canal no YouTube? Sério que você está sugerindo isso?"
            samantha "Ah, mas seria legal! Você pode falar sobre cinema, eu sobre jogos e animes, e a gente pode fazer conexões entre os dois!"
            samantha "Tipo analisar como Akira influenciou Cyberpunk, ou como Studio Ghibli inspirou vários jogos!"
            katia "Hmpf... talvez... se for para educar as pessoas sobre cinema de verdade..."

    # Memória compartilhada especial
    $ add_shared_memory("cinema_gaming_connection", ["katia", "samantha"], "O momento em que descobrimos que cinema e jogos podem se complementar perfeitamente")

    hide katia
    hide samantha
    narrator "A noite foi cheia de conversas, provocações e risadas. O tipo de encontro que deixa saudade — e vontade de repetir."
    narrator "Era como se tivéssemos descoberto uma nova forma de ver o entretenimento - não como opostos, mas como complementos."
    narrator "Katia aprendendo a valorizar o entusiasmo genuíno, Samantha aprendendo a valorizar a análise crítica."

    return