label evento_huey_katia_feira:
    scene bg museum_hall with fade
    show huey neutral at left
    show katia neutral at right

    narrator "Huey me convidou para visitar uma feira de arte independente no centro da cidade. Katia também decidiu se juntar, curiosa para explorar o trabalho de artistas emergentes."

    huey "Essa feira é incrível. É como se cada obra tivesse uma energia única, conectando o artista ao público."

    katia "Hmph, não espere que eu fique impressionada tão facilmente. Mas... talvez haja algo interessante por aqui."

    narrator "Com Huey admirando a energia das obras e Katia tentando esconder seu entusiasmo, eu sabia que seria uma experiência interessante."

    menu:
        "Explorar as obras com Huey e discutir as energias transmitidas":
            $ points_huey += 1
            huey "Você percebeu como essa pintura parece vibrar? É como se tivesse vida própria."
            narrator "Huey parecia encantado com a energia das obras e adorava compartilhar suas percepções."

        "Perguntar a Katia sobre os estilos artísticos que ela prefere":
            $ points_katia += 1
            katia "Eu gosto de algo que desafie a mente, mas não pense que eu me impressiono facilmente, ok?"
            narrator "Apesar do tom de Katia, era evidente que ela estava interessada nas obras."

        "Sugerir que cada um escolha sua obra favorita e explique o porquê":
            $ points_huey += 1
            $ points_katia += 1
            huey "Essa aqui é minha favorita. Ela transmite uma sensação de calma e equilíbrio."
            katia "Eu escolho essa. A composição é ousada e provocativa. Não que eu me importe tanto assim."

    # Cena 1: Exposição de esculturas
    scene bg sculpture_exhibit with dissolve
    show huey neutral at left
    show katia neutral at right
    narrator "Seguimos para uma área dedicada a esculturas, onde formas abstratas e materiais inusitados chamavam a atenção."

    menu:
        "Perguntar a Huey sobre a energia das esculturas":
            $ points_huey += 1
            huey "Essas esculturas têm uma presença forte. É como se ocupassem mais do que apenas o espaço físico."
            narrator "Huey parecia fascinado pela energia que as esculturas transmitiam."

        "Perguntar a Katia sobre as técnicas usadas nas esculturas":
            $ points_katia += 1
            katia "As técnicas são interessantes, mas não pense que eu estou impressionada ou algo assim!"
            narrator "Katia explicou com entusiasmo, mesmo tentando esconder o quanto gostava do assunto."

        "Sugerir que todos interpretem uma escultura de forma pessoal":
            $ points_huey += 1
            $ points_katia += 1
            huey "Essa escultura me lembra o fluxo da vida. É como se estivesse em constante movimento."
            katia "Eu vejo algo mais sombrio aqui. Talvez uma crítica à sociedade moderna. Não que eu me importe tanto."

    # Cena 2: Exposição de fotografias
    scene bg photo_exhibit with dissolve
    show huey neutral at left
    show katia neutral at right
    narrator "Na área de fotografias, imagens em preto e branco capturavam momentos únicos e emocionantes."

    menu:
        "Discutir com Huey a emoção transmitida pelas fotografias":
            $ points_huey += 1
            huey "Essas fotos têm uma melancolia única. É como se capturassem a essência de um momento perdido."
            narrator "Huey parecia profundamente conectado às emoções transmitidas pelas fotografias."

        "Perguntar a Katia sobre o uso de luz e sombra nas fotos":
            $ points_katia += 1
            katia "A composição é boa, mas eu já vi trabalhos melhores. Não que isso seja ruim, claro."
            narrator "Katia analisou as fotos com um olhar crítico, mas era evidente que estava impressionada."

        "Sugerir que cada um escolha sua foto favorita e explique o porquê":
            $ points_huey += 1
            $ points_katia += 1
            huey "Essa foto me lembra a simplicidade da vida. É reconfortante."
            katia "Eu escolho essa. A tensão entre luz e sombra é fascinante. Não que eu me importe tanto assim."

    # Cena 3: Área interativa
    scene bg interactive_art with dissolve
    show huey neutral at left
    show katia neutral at right
    narrator "Chegamos a uma área interativa, onde os visitantes podiam criar suas próprias obras digitais."

    menu:
        "Criar uma obra digital com Huey":
            $ points_huey += 1
            huey "Isso foi divertido! Sua criatividade é inspiradora."
            narrator "Huey parecia gostar de colaborar em algo criativo."

        "Criar uma obra digital com Katia":
            $ points_katia += 1
            katia "Não pense que eu preciso da sua ajuda ou algo assim! Mas... até que ficou bom."
            narrator "Katia parecia gostar de colaborar, mesmo que tentasse esconder isso."

        "Sugerir que todos criem algo juntos":
            $ points_huey += 1
            $ points_katia += 1
            huey "Adorei a ideia. Trabalhar juntos torna tudo mais especial."
            katia "Hmph, eu acho que posso ajudar... mas só porque eu quero, não porque você pediu!"

    # Cena 4: Café da feira
    scene bg cafeteria with dissolve
    show huey neutral at left
    show katia neutral at right
    narrator "Terminamos a visita no café da feira, onde discutimos nossas impressões sobre o evento."

    menu:
        "Agradecer a Huey por compartilhar suas percepções únicas":
            $ points_huey += 1
            huey "Fico feliz que você tenha gostado. Foi ótimo compartilhar isso com você."
            narrator "Huey parecia satisfeito por ter contribuído para a experiência."

        "Agradecer a Katia por compartilhar suas análises críticas":
            $ points_katia += 1
            katia "Não foi nada demais... mas, bem, fico feliz que você tenha aprendido algo."
            narrator "Katia parecia satisfeita, mesmo tentando esconder seu orgulho."

        "Sugerir que todos visitem outra feira no futuro":
            $ points_huey += 1
            $ points_katia += 1
            huey "Com certeza! Sempre há algo novo para explorar."
            katia "Eu acho que seria interessante... mas não pense que estou ansiosa ou algo assim!"

    hide huey
    hide katia
    narrator "A feira de arte foi uma experiência enriquecedora, fortalecendo os laços entre nós e expandindo nossas perspectivas sobre arte e cultura."
    
    jump capitulo2_final