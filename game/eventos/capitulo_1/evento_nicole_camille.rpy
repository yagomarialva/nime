label evento_nicole_camille:
    
    # === PRIMEIRO ENCONTRO - CONHECENDO NICOLE E CAMILLE ===
    $ feedback_nicole = add_affinity_points("nicole", 5, "Primeira conversa profunda")
    $ feedback_camille = add_affinity_points("camille", 5, "Primeira conexão espiritual")
    
    scene bg library with dissolve
    narrator "Entrei na biblioteca da universidade, procurando um lugar silencioso para estudar. O ambiente estava calmo, com poucos estudantes e uma atmosfera que convidava à concentração."
    narrator "Encontrei uma mesa vazia próxima a uma estante de livros sobre comunicação e psicologia. Foi então que percebi que não estava sozinho..."

    # Apresentação natural da Nicole
    show nicole neutral at left
    nicole "Desculpe, posso me sentar aqui? Esta mesa tem uma boa iluminação para leitura."
    nicole "Sou Nicole, estudo comunicação estratégica e análise de dados comportamentais."
    nicole "Estou trabalhando em um projeto sobre metodologias de autoconhecimento profissional... é fascinante como podemos quantificar o crescimento pessoal."
    
    narrator "Nicole organizou seus materiais com precisão metódica - cadernos, canetas coloridas, até um laptop com gráficos complexos na tela."
    narrator "Sua abordagem era sistemática, mas havia algo genuíno em sua paixão pelos dados e pela estrutura."

    # Apresentação natural da Camille
    show camille gentle at right
    camille "Nossa, que energia interessante vocês têm aqui... posso me juntar a vocês?"
    camille "Sou Camille, estudo conexões energéticas e práticas de mindfulness."
    camille "Senti uma vibração muito boa vindo desta mesa... como se vocês estivessem falando sobre algo importante."
    
    narrator "Camille chegou com passos suaves, carregando um caderno de anotações e alguns cristais pequenos."
    narrator "Havia algo sereno em sua presença, como se ela trouxesse calma para o ambiente."
    
    # Apresentação do jogador
    narrator "Me apresentei brevemente, explicando que era novo na universidade e estava explorando diferentes áreas de estudo."
    narrator "Ambas pareceram interessadas em conhecer minha perspectiva sobre os temas que estavam discutindo."
    
    nicole "Que interessante! E qual sua abordagem para autoconhecimento? Você prefere métodos estruturados ou mais intuitivos?"
    nicole "Estou organizando um projeto para ajudar pessoas a encontrarem seu propósito profissional de forma mais consciente."
    nicole "A ideia é criar uma metodologia que combine análise de mercado com autoconhecimento profundo."
    
    camille "Que energia interessante você tem... posso sentir que você está em um momento de descoberta."
    camille "O propósito tem uma energia própria, sabem? Quando alguém encontra sua verdadeira vocação, isso ressoa de uma forma que números não conseguem capturar."
    
    nicole "Camille, entendo seu ponto, mas precisamos de dados concretos, métricas, resultados mensuráveis. Como vamos medir o sucesso se não tivermos indicadores claros?"
    
    camille "Nicole, nem tudo na vida pode ser medido com números! Existe uma intuição, uma energia que guia as pessoas... quando você sente que algo está certo, isso tem valor."
    
    nicole "Mas como vamos convencer empresas ou mentores sem dados sólidos? Eles precisam ver retorno, crescimento, engajamento..."
    
    camille "Talvez o problema seja justamente tentar convencer pessoas que só pensam em números. O propósito verdadeiro encontra seu caminho naturalmente."
    
    narrator "O silêncio se estendeu por alguns segundos enquanto ambas processavam os argumentos uma da outra."
    narrator "Senti que esta conversa estava se tornando algo especial... não era apenas sobre projetos - era sobre duas visões de mundo muito diferentes tentando se entender."
    narrator "E eu estava no meio, observando como duas abordagens aparentemente opostas podiam coexistir."

    # Primeira rodada de escolhas - Primeiro encontro
    menu:
        "Perguntar a Nicole sobre como medir o impacto emocional":
            $ points_nicole += 1
            narrator "Nicole pausou para pensar, organizando mentalmente suas ideias."
            nicole "Boa pergunta! Podemos usar pesquisas de satisfação, feedback qualitativo, indicadores de engajamento..."
            nicole "Mas você tem razão, o impacto emocional é mais complexo. Talvez precisemos de métricas híbridas."
            camille "Isso... isso faz sentido. Talvez possamos encontrar uma forma de quantificar o que sentimos."

        "Falar com Camille sobre como a energia se manifesta na prática":
            $ points_camille += 1
            camille "Você sente quando algo está 'certo', sabe? É como uma vibração que te guia..."
            camille "Quando estou criando, às vezes as ideias fluem de uma forma que não consigo explicar racionalmente."
            nicole "Interessante... eu nunca pensei nisso dessa forma. Como você diferencia intuição de impulso?"

        "Sugerir unir dados objetivos com percepções subjetivas":
            $ points_nicole += 1
            $ points_camille += 1
            narrator "Ambas parecem intrigadas pela ideia de combinar abordagens."
            nicole "Isso... isso poderia funcionar. Dados para validar, intuição para guiar."
            camille "Sim! Como se os números confirmassem o que já sentimos que é verdade."

        "Compartilhar sua própria perspectiva sobre autoconhecimento":
            $ points_nicole += 1
            $ points_camille += 1
            narrator "Compartilhei minha própria visão sobre autoconhecimento, tentando encontrar um meio termo."
            nicole "Interessante perspectiva... você parece equilibrar bem os dois lados."
            camille "Sinto que você tem uma energia muito equilibrada... como se conseguisse ver o valor em ambas as abordagens."

        "Perguntar como Nicole lida com situações onde os dados não explicam tudo":
            $ points_nicole += 1
            nicole "Hmm... confesso que isso me incomoda. Prefiro ter controle total sobre as variáveis."
            nicole "Mas ultimamente tenho percebido que nem tudo pode ser previsto ou medido."
            camille "E isso te assusta?"
            nicole "Um pouco... mas também é libertador, de certa forma."

        "Perguntar a ambas como lidam com incertezas":
            $ points_nicole += 1
            $ points_camille += 1
            nicole "Eu tento criar planos B, C, D... mas às vezes é exaustivo."
            camille "Eu respiro fundo e confio que o caminho certo vai se revelar. A incerteza pode ser uma professora."
            narrator "Ambas compartilharam suas estratégias para lidar com o desconhecido, cada uma com sua abordagem única."

    narrator "Com cada troca de ideia, sentíamos que havia algo especial naquela conversa."
    narrator "O ambiente da biblioteca parecia ter se transformado em um espaço de descoberta mútua."
    
    nicole "É fascinante como conseguimos conversar sobre temas tão complexos logo no primeiro encontro..."
    nicole "Sabia que muitas pessoas desistem de seguir seus sonhos por falta de apoio emocional e financeiro?"
    nicole "É frustrante ver potencial sendo desperdiçado por falta de estrutura."
    
    camille "A estrutura importa, mas não pode sufocar a essência. Quando corpo e mente estão alinhados, o propósito floresce naturalmente."
    camille "Talvez o problema seja que estamos tentando encaixar a vocação em moldes que não foram feitos para ela."
    camille "E é incrível como você consegue ver o valor em ambas as perspectivas... isso é raro."

    # Segunda rodada de escolhas
    menu:
        "Propor uma ideia para um evento colaborativo sobre propósito profissional":
            $ points_nicole += 1
            $ points_camille += 1
            narrator "Sugeri um evento que combinasse networking profissional com momentos de conexão espiritual."
            nicole "Adorei a ideia! Podemos ter workshops de análise de mercado e também sessões de autoconhecimento."
            camille "Perfeito! Um espaço onde pessoas podem se conectar tanto profissional quanto espiritualmente."
            nicole "E podemos medir o sucesso tanto pelo número de conexões feitas quanto pela satisfação dos participantes."

        "Perguntar sobre os desafios que enfrentaram em seus projetos":
            $ points_nicole += 1
            $ points_camille += 1
            nicole "Meu maior desafio é equilibrar a parte comercial com a autenticidade. Às vezes sinto que estou vendendo minha alma."
            camille "Eu entendo... às vezes é difícil explicar para as pessoas que o que faço tem valor real, mesmo que não seja tangível."
            nicole "Exato! Como você coloca preço em algo que vem do coração?"
            camille "E como você convence alguém de que sua intuição vale mais que um relatório de mercado?"

        "Compartilhar uma experiência pessoal sobre propósito":
            $ points_nicole += 1
            $ points_camille += 1
            narrator "Compartilhei uma experiência onde encontrei meu propósito de forma inesperada."
            nicole "Isso é lindo... às vezes as melhores descobertas vêm quando menos esperamos."
            camille "Exato! O propósito tem seus próprios ritmos. Não podemos forçá-lo, só podemos estar abertos para recebê-lo."
            nicole "Talvez seja isso que eu estava perdendo... tentando controlar demais o processo de autoconhecimento."

        "Discutir como a tecnologia pode ajudar pessoas a encontrarem seu propósito":
            $ points_nicole += 1
            $ points_camille += 1
            nicole "A tecnologia pode ser uma ponte incrível entre pessoas e oportunidades. Plataformas de networking, testes vocacionais..."
            camille "Sim, mas tem que ser usada com intenção. Não pode ser só mais uma ferramenta vazia."
            nicole "Concordo. A tecnologia deve amplificar a conexão humana, não substituí-la."
            camille "Exato! Como usar algoritmos para conectar pessoas que realmente se ressoam entre si."

        "Perguntar sobre como equilibrar vida pessoal e profissional":
            $ points_nicole += 1
            $ points_camille += 1
            nicole "Essa é a parte mais difícil... quando você ama o que faz, a linha entre trabalho e vida pessoal desaparece."
            camille "E quando você trabalha com energia e intuição, não dá para 'desligar' no final do dia."
            nicole "Exato! Como você separa sua paixão da sua profissão quando elas são a mesma coisa?"
            camille "Acho que o segredo é não tentar separar, mas sim integrar tudo de forma harmoniosa."

    narrator "Depois de mais uma rodada de café, as ideias começaram a tomar formas mais concretas."
    narrator "O ambiente da cafeteria parecia ter se transformado em um espaço de brainstorming criativo."
    
    camille "Eu sonho em criar um espaço holístico para pessoas. Um lugar onde a energia flui naturalmente."
    camille "Imagine um local onde pessoas podem se conectar, meditar, descobrir seu propósito... sem pressão, sem julgamento."
    
    nicole "E eu penso em uma plataforma com cursos e consultorias que ajudem a profissionalizar sem perder a essência humana."
    nicole "Mas agora estou vendo que talvez precisemos de algo mais... integrado. Menos separação entre o espiritual e o prático."

    # Terceira rodada de escolhas
    menu:
        "Discutir como medir o sucesso de projetos holísticos":
            $ points_camille += 1
            camille "O sucesso não é só números... é sobre transformação, sobre pessoas se sentindo completas."
            camille "Como você mede uma vida que mudou? Como você quantifica uma alma que encontrou seu propósito?"
            nicole "Isso é profundo... talvez precisemos de indicadores mais sutis. Relatos de vida, histórias de transformação..."
            camille "Exato! Números podem contar uma história, mas as histórias das pessoas contam a verdade."

        "Explorar como dados podem validar experiências subjetivas":
            $ points_nicole += 1
            nicole "Podemos criar métricas para medir bem-estar, satisfação, crescimento pessoal..."
            nicole "Pesquisas de qualidade de vida, indicadores de saúde mental, níveis de engajamento criativo..."
            camille "Interessante... talvez possamos usar dados para validar o que já sentimos que é verdade."
            nicole "Sim! Como se os números confirmassem a magia que já sabemos que existe."

        "Sugerir uma série de vídeos com entrevistas sobre diferentes abordagens":
            $ points_nicole += 1
            $ points_camille += 1
            narrator "Sugeri uma série documental mostrando diferentes perspectivas sobre criatividade e sucesso."
            nicole "Adorei! Podemos entrevistar artistas que usam dados, outros que confiam na intuição..."
            camille "E mostrar como cada abordagem tem seu valor. Não precisa ser uma ou outra."
            nicole "Exato! A diversidade de perspectivas é o que torna a arte tão rica."

        "Contar sobre uma experiência onde a intuição te guiou":
            $ points_camille += 1
            narrator "Compartilhei um momento onde confiei na intuição e deu certo de forma inesperada."
            camille "Exato! Às vezes você sabe que algo vai dar certo antes mesmo de ter os dados..."
            camille "É como se o universo já estivesse te mostrando o caminho, só precisamos estar abertos para ver."
            nicole "Isso me faz pensar... talvez eu tenha perdido algumas oportunidades por ser muito analítica."

        "Falar sobre o papel da intuição em decisões importantes":
            $ points_nicole += 1
            $ points_camille += 1
            nicole "Ultimamente tenho percebido que minhas melhores decisões vêm de uma combinação de dados e intuição."
            camille "Isso é lindo... quando você consegue integrar os dois, aí que a magia acontece."
            nicole "Exato! Os dados me dão segurança, mas a intuição me dá direção."
            camille "E quando os dois se alinham, é como se tudo fizesse sentido de uma forma que não conseguimos explicar."

    narrator "Por um momento, todos ficaram em silêncio, contemplando o que poderia surgir se unissem forças."
    narrator "O ar parecia carregado de possibilidades, como se estivéssemos prestes a descobrir algo importante."

    camille "Já pensou se tudo isso fosse mais do que ideias soltas? E se fosse o início de algo real?"
    camille "Algo que realmente pudesse ajudar pessoas a encontrarem seu caminho criativo..."
    
    nicole "Talvez devêssemos pilotar uma iniciativa em conjunto... uma incubadora de projetos conscientes."
    nicole "Um lugar onde dados e intuição pudessem trabalhar juntos, não em oposição."
    
    narrator "Ambas se olharam com uma expressão de surpresa e excitação."
    
    # Transição para um espaço neutro - biblioteca
    scene bg library with dissolve
    show nicole neutral at left
    show camille neutral at right

    narrator "A biblioteca estava silenciosa, com luzes suaves e uma atmosfera que convidava à reflexão profunda."
    narrator "Parecia o lugar perfeito para dar vida às ideias que estavam brotando entre nós."

    camille "A energia aqui está ótima hoje. Perfeita pra fluidez criativa."
    camille "Sinto que este é o lugar certo para explorarmos essas ideias de forma mais profunda."
    
    nicole "Trouxe alguns materiais pra gente experimentar. A ideia é deixar a intuição guiar."
    nicole "Mas também quero ver como podemos documentar e estruturar o que surgir aqui."

    menu:
        "Explorar os materiais com Nicole":
            $ points_nicole += 1
            narrator "Nicole espalhou diversos objetos na mesa: papéis, canetas, questionários, até alguns dispositivos eletrônicos."
            nicole "Esses materiais nos ajudam a organizar pensamentos. O autoconhecimento começa quando a gente escuta o que nossa intuição tem a dizer."
            nicole "Cada ferramenta tem sua própria forma de nos ajudar a descobrir nosso propósito."
            camille "Que interessante... nunca pensei nas ferramentas como tendo personalidade própria."

        "Participar de uma meditação guiada com Camille":
            $ points_camille += 1
            narrator "Camille se acomodou em uma posição confortável e me convidou a fazer o mesmo."
            camille "Feche os olhos. Respire... Sinta seu propósito surgir de dentro para fora."
            camille "Não force nada, apenas permita que as respostas fluam naturalmente."
            nicole "Isso é... relaxante. Nunca tinha tentado meditar antes de refletir sobre meu futuro."

        "Observar as duas trabalhando antes de agir":
            $ points_nicole += 1
            $ points_camille += 1
            narrator "Assisti enquanto Camille traçava padrões em aquarela e Nicole fazia anotações meticulosas."
            narrator "Era como ver duas linguagens diferentes conversando sem palavras."
            narrator "Camille trabalhava com movimentos fluidos e orgânicos, enquanto Nicole criava estruturas organizadas e lógicas."

    narrator "A sessão avançava, e as ideias começaram a tomar forma. O silêncio da biblioteca parecia amplificar nossa criatividade."
    narrator "Camille propôs uma dinâmica em grupo, com uma energia que contagiava."

    camille "Vamos fazer uma atividade conjunta. Cada um contribui com algo espontâneo, sem julgar, só sentindo."
    camille "A ideia é deixar o autoconhecimento fluir sem barreiras, sem medo de errar."
    
    nicole "Adorei a ideia! Vou tentar me soltar mais, deixar a intuição me guiar."
    nicole "Mas também quero documentar o processo... para entender como isso funciona."

    menu:
        "Contribuir com uma ideia sobre energia e dados":
            $ points_camille += 1
            narrator "Escrevi algumas ideias sobre como medir energia através de dados, tentando encontrar uma ponte entre os dois mundos."
            narrator "Camille sorriu ao ler, reconhecendo a tentativa de integração."
            camille "Isso é lindo... você está tentando traduzir o que sinto em algo que Nicole possa entender."
            nicole "E está funcionando! Consigo ver como os dados podem validar essas sensações."

        "Desenhar um diagrama sobre intuição vs. lógica":
            $ points_nicole += 1
            narrator "Usei cores fortes para criar um diagrama que mostrava a interseção entre intuição e dados."
            narrator "Nicole elogiou a clareza visual, enquanto Camille se emocionou com a representação."
            nicole "Isso é incrível! Visualmente fica muito claro como os dois se complementam."
            camille "E as cores... elas transmitem a energia que sinto quando os dois se alinham."

        "Fazer uma colagem com diferentes abordagens":
            $ points_nicole += 1
            $ points_camille += 1
            narrator "Criei uma colagem misturando elementos analíticos e intuitivos."
            narrator "A mistura de abordagens provocou reações diversas. As duas pareciam intrigadas com minha composição."
            nicole "Isso representa perfeitamente o que estamos tentando fazer... integrar sem perder a essência de cada parte."
            camille "E é lindo ver como elementos aparentemente opostos podem coexistir harmoniosamente."

    narrator "Ao final, Camille sugeriu compartilharmos o que sentimos durante o processo."
    narrator "O momento parecia sagrado, como se estivéssemos prestes a descobrir algo importante sobre nós mesmas."

    menu:
        "Falar sobre como unir intuição e dados":
            $ points_camille += 1
            narrator "Compartilhei como estava aprendendo a valorizar tanto a lógica quanto a intuição."
            camille "Isso é lindo. Unir diferentes perspectivas é também curar... curar a divisão que criamos em nossas próprias mentes."
            nicole "E é libertador... não precisamos escolher entre ser analítica ou intuitiva. Podemos ser ambas."

        "Refletir sobre propósito de projetos conscientes":
            $ points_nicole += 1
            narrator "Refleti sobre como projetos conscientes precisam ter um propósito maior que apenas resultados."
            nicole "Saber o 'porquê' dá direção ao nosso fazer. Esse espaço foi poderoso porque nos lembrou do nosso propósito."
            camille "Exato... quando trabalhamos com propósito, a energia flui naturalmente e os resultados vêm."

        "Agradecer pela experiência e escutar":
            $ points_nicole += 1
            $ points_camille += 1
            narrator "Agradeci pela experiência e me coloquei em modo de escuta ativa."
            narrator "Ouvi as reflexões de ambas com atenção. A gratidão pairava no ar, junto com uma sensação de conexão profunda."
            nicole "Obrigada por me ensinar que não preciso escolher entre ser prática e ser sensível."
            camille "E obrigada por me mostrar que dados podem ser uma ferramenta de validação, não de limitação."

    # === MOMENTO DE CONEXÃO PROFUNDA - PRIMEIRO ENCONTRO ===
    scene bg library with fade
    show nicole happy at left
    show camille gentle at right
    
    narrator "O silêncio que se seguiu não era vazio - era repleto de compreensão mútua."
    narrator "Senti que algo fundamental havia mudado entre nós três naquele momento."
    
    # Camille revela algo pessoal (desenvolvimento de personagem)
    camille "Vocês sabem... é estranho, mas sinto que posso confiar em vocês."
    camille "Desde pequena, sinto as energias ao meu redor, mas sempre achei que era 'estranha' demais..."
    camille "As pessoas me olhavam como se eu estivesse inventando coisas, então aprendi a guardar isso para mim."
    
    # Nicole mostra crescimento emocional
    nicole "Camille... eu sempre fui tão focada em números e resultados que esqueci da magia por trás das conexões humanas."
    nicole "Hoje você me lembrou de algo que eu tinha perdido... a capacidade de sentir, de confiar na intuição."
    nicole "E me fez perceber que não preciso escolher entre ser analítica e ser sensível."
    
    # Momento de conexão mútua
    call emotional_moment("vulnerability", "camille", "Camille se abre sobre suas inseguranças espirituais") from _call_emotional_moment_evento_nc_2
    
    narrator "As lágrimas que rolaram não eram de tristeza, mas de alívio e compreensão."
    narrator "Era como se cada uma de nós tivesse encontrado uma parte de si mesma que não sabia que estava perdida."
    
    # Crescimento mútuo dos personagens
    $ growth_camille = trigger_character_growth("camille", "confidence")
    $ growth_nicole = trigger_character_growth("nicole", "empathy")
    
    narrator "[growth_camille]"
    narrator "[growth_nicole]"
    
    # Promessa de continuidade (foreshadowing)
    scene bg campus_sunset with fade
    show nicole happy at left
    show camille gentle at right
    
    narrator "Saímos da biblioteca com o sol se pondo, criando um cenário dourado que parecia abençoar nosso momento de conexão."
    
    camille "Obrigada por... por me ouvirem de verdade. Por não me julgarem."
    camille "Nunca imaginei que poderia encontrar pessoas que entendessem essa parte de mim."
    
    nicole "E eu agradeço por me ensinar que dados e intuição não precisam ser inimigos."
    nicole "Acho que este é só o começo de algo muito especial... algo que pode realmente fazer a diferença."
    
    narrator "Ambas se abraçaram, e eu me juntei ao abraço, sentindo a energia de conexão genuína entre nós."
    
    show screen emotional_moment_notification("💫 Uma amizade verdadeira começou a florescer...")
    pause 3.0
    hide screen emotional_moment_notification
    
    # Memória compartilhada especial
    $ add_shared_memory("conscious_awakening", ["nicole", "camille"], "O momento em que descobrimos a magia da conexão entre dados e energia")

    hide nicole
    hide camille
    narrator "Saí da biblioteca com o coração aquecido e a mente cheia de possibilidades."
    narrator "Esta não foi apenas uma tarde de conversas - foi o nascimento de algo que mudaria todos nós."
    narrator "Era como se tivéssemos descoberto uma nova forma de ver o mundo, onde lógica e intuição dançavam juntas em perfeita harmonia."

    jump capitulo1_segunda_escolha
