label evento_katia_nicole_cultura:
    scene bg museum_hall with fade
    show katia neutral at left
    show nicole neutral at right

    narrator "Katia me convidou para visitar uma exposição cultural no museu da cidade. Nicole também decidiu se juntar, interessada em explorar as conexões entre arte e negócios."

    katia "Não pense que eu te chamei porque queria sua companhia ou algo assim... Só achei que você poderia aprender alguma coisa aqui."

    nicole "Acho que vai ser interessante ver como cada um interpreta as obras. A arte sempre tem algo a ensinar."

    narrator "Com Katia tentando esconder seu entusiasmo e Nicole trazendo sua visão prática, eu sabia que seria uma experiência única."

    menu:
        "Explorar a exposição com Katia e discutir os temas sociais das obras":
            $ points_katia += 1
            katia "Hmph, você realmente notou isso? Não é como se eu estivesse impressionada ou algo assim..."
            narrator "Apesar do tom de Katia, era evidente que ela gostava de compartilhar suas interpretações."

        "Conversar com Nicole sobre o impacto econômico da arte":
            $ points_nicole += 1
            nicole "A arte tem um valor imensurável, mas também pode ser uma ferramenta poderosa para gerar mudanças econômicas."
            narrator "Nicole trouxe uma perspectiva prática e interessante para a conversa."

        "Sugerir uma discussão sobre como a arte conecta pessoas de diferentes origens":
            $ points_katia += 1
            $ points_nicole += 1
            katia "Eu acho que isso é óbvio... mas, bem, talvez você tenha um ponto."
            nicole "E é por isso que ela é tão importante em campanhas de engajamento social."

    # Cena 1: Sala de esculturas
    scene bg museum_sculpture with dissolve
    narrator "Seguimos para a sala de esculturas, onde peças tridimensionais contavam histórias profundas."

    menu:
        "Perguntar a Katia sobre as técnicas usadas nas esculturas":
            $ points_katia += 1
            katia "Você realmente quer saber? Bem, eu posso explicar, mas não espere que eu seja sua professora ou algo assim!"
            narrator "Katia explicou com entusiasmo, mesmo tentando esconder o quanto gostava do assunto."

        "Perguntar a Nicole como essas peças poderiam ser usadas em campanhas sociais":
            $ points_nicole += 1
            nicole "Essas esculturas poderiam ser o centro de uma campanha para conscientização. Elas têm um impacto visual forte."
            narrator "Nicole parecia inspirada pelas possibilidades práticas das obras."

        "Sugerir que cada um interprete uma escultura de forma pessoal":
            $ points_katia += 1
            $ points_nicole += 1
            katia "Hmph, eu posso fazer isso, mas não espere que minha interpretação seja simples como a sua."
            nicole "Isso é interessante. Mostra como a arte pode ser subjetiva e universal ao mesmo tempo."

    # Cena 2: Sala de pinturas
    scene bg museum_paintings with dissolve
    narrator "Na sala de pinturas, obras vibrantes e cheias de emoção decoravam as paredes."

    menu:
        "Discutir com Katia o uso de cores nas pinturas":
            $ points_katia += 1
            katia "As cores aqui são... bem, elas são boas, eu acho. Não que eu me importe tanto assim!"
            narrator "Mesmo tentando disfarçar, Katia parecia encantada com a paleta de cores das pinturas."

        "Perguntar a Nicole sobre o valor histórico das obras":
            $ points_nicole += 1
            nicole "Essas pinturas são um registro visual da história. Elas têm um valor cultural e econômico imenso."
            narrator "Nicole trouxe uma perspectiva interessante sobre o impacto histórico das obras."

        "Sugerir que cada um escolha sua pintura favorita e explique o porquê":
            $ points_katia += 1
            $ points_nicole += 1
            katia "Eu não tenho que te explicar nada, mas... essa aqui é minha favorita. A composição é impactante, ok?"
            nicole "Eu gosto dessa. Ela transmite uma mensagem clara e poderosa."

    # Cena 3: Sala interativa
    scene bg museum_interactive with dissolve
    narrator "Chegamos a uma sala interativa, onde os visitantes podiam criar suas próprias obras digitais."

    menu:
        "Criar uma obra digital com Katia":
            $ points_katia += 1
            katia "Não pense que eu preciso da sua ajuda ou algo assim! Mas... até que ficou bom."
            narrator "Katia parecia gostar de colaborar, mesmo que tentasse esconder isso."

        "Discutir com Nicole como a tecnologia pode ampliar o alcance da arte":
            $ points_nicole += 1
            nicole "A tecnologia é uma ferramenta incrível para democratizar o acesso à arte."
            narrator "Nicole parecia animada com as possibilidades tecnológicas no mundo da arte."

        "Sugerir que todos criem algo juntos":
            $ points_katia += 1
            $ points_nicole += 1
            katia "Hmph, eu acho que posso ajudar... mas só porque eu quero, não porque você pediu!"
            nicole "Isso será interessante. Vamos ver o que conseguimos fazer juntos."

    # Cena 4: Café do museu
    scene bg museum_cafe with dissolve
    narrator "Terminamos a visita no café do museu, onde discutimos nossas impressões sobre a exposição."

    menu:
        "Agradecer a Katia por compartilhar suas interpretações artísticas":
            $ points_katia += 1
            katia "Não foi nada demais... mas, bem, fico feliz que você tenha aprendido algo."
            narrator "Katia parecia satisfeita, mesmo tentando esconder seu orgulho."

        "Agradecer a Nicole por trazer uma perspectiva prática e inspiradora":
            $ points_nicole += 1
            nicole "Obrigada! Foi ótimo discutir essas ideias com você."
            narrator "Nicole parecia contente por ter contribuído com sua visão prática."

        "Sugerir que todos visitem outra exposição no futuro":
            $ points_katia += 1
            $ points_nicole += 1
            katia "Eu acho que seria interessante... mas não pense que estou ansiosa ou algo assim!"
            nicole "Adorei a ideia. Vamos planejar isso em breve."

    hide katia
    hide nicole
    narrator "O passeio cultural foi uma experiência enriquecedora, fortalecendo os laços entre nós e expandindo nossas perspectivas sobre arte e cultura."
    jump terceiro_dia_escolha