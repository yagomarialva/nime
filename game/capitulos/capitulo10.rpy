label capitulo10:
    scene bg republica_vazia with fade
    narrator "É a última semana do semestre. A república começa a esvaziar. Caixas se acumulam. Paredes perdem os quadros e bilhetes. Cada passo soa como uma despedida não dita."

    show nicole neutral at left
    nicole "Estamos seguindo o cronograma, mas emocionalmente... estamos atrasados."

    show katia neutral at center
    katia "Esse plano de fundo vai render um curta sobre fim de ciclos."

    show camille gentle at right
    camille "O cheiro da casa vai mudar... Mas a vibração ficará."

    show larissa happy at left
    larissa "Quero fazer agachamento emocional e físico com todo mundo antes do fim."

    show samantha happy at center
    samantha "A gente devia ter salvado mais momentos com clipes de voz…"

    show huey gentle at right
    huey "Última arte antes da parede ser pintada de branco. Adeus, memória viva."

    # Segue para os eventos de despedida automaticamente
    jump capitulo10_samantha

label capitulo10_samantha:
    show samantha happy at center
    narrator "Você ajuda Samantha a salvar os dados dos jogos antigos no computador."
    samantha "Esses jogos são como memórias vivas. Cada escolha, cada vitória... é como se a gente pudesse reviver tudo."
    '[nome]' "E agora você pode guardar tudo isso pra sempre."
    samantha "Obrigada por me ajudar. Você é o melhor parceiro de guilda que eu poderia pedir."
    jump capitulo10_katia

label capitulo10_katia:
    show katia neutral at center
    narrator "Você ajuda Katia a embalar livros enquanto discutem finais de filmes."
    katia "Sabe o que eu odeio? Finais abertos. Mas... às vezes, eles são os mais reais."
    '[nome]' "Talvez porque a vida nunca tem um ponto final definitivo."
    katia "Hmpf. Filosófico demais pra mim. Mas... obrigada por estar aqui."
    jump capitulo10_huey

label capitulo10_huey:
    show huey gentle at center
    narrator "Você ajuda Huey a pintar a parede com uma última arte antes de ser apagada."
    huey "Cada pincelada é como uma memória. Mesmo que desapareça, ela ainda existiu."
    '[nome]' "E você capturou tudo isso de um jeito único."
    huey "Obrigado por pintar isso comigo. Você é uma inspiração."
    jump capitulo10_camille

label capitulo10_camille:
    show camille gentle at center
    narrator "Você queima incensos com Camille enquanto refletem sobre mudanças."
    camille "O cheiro muda, mas a energia permanece. É como se a casa guardasse tudo o que vivemos."
    '[nome]' "E agora, ela vai guardar isso pra sempre."
    camille "Obrigada por estar aqui. Você trouxe equilíbrio pra tudo isso."
    jump capitulo10_nicole

label capitulo10_nicole:
    show nicole neutral at center
    narrator "Você ajuda Nicole a criar etiquetas organizadas para as caixas."
    nicole "Organizar tudo isso é como organizar as memórias. Cada coisa no seu lugar."
    '[nome]' "E você faz isso melhor do que ninguém."
    nicole "Obrigada por me ajudar. Você é... eficiente. E especial."
    jump capitulo10_larissa

label capitulo10_larissa:
    show larissa happy at center
    narrator "Você treina com Larissa entre as caixas, transformando a despedida em algo físico."
    larissa "Treinar é minha forma de lidar com tudo. Mas... isso aqui é mais difícil do que eu pensei."
    '[nome]' "Você é forte, Larissa. E não precisa carregar tudo sozinha."
    larissa "Obrigada por estar aqui. Você é um parceiro incrível."
    jump capitulo10_evento_final

label capitulo10_evento_final:
    scene bg republica_noite with fade
    narrator "Na véspera do fim, cada morador sai para resolver sua vida. Você fica sozinho na casa… até que uma porta se abre."

    # Determina a personagem de maior afinidade
    if points_samantha >= 6 and points_samantha == max(points_samantha, points_nicole, points_huey, points_camille, points_larissa, points_katia):
        jump capitulo10_final_samantha
    elif points_nicole >= 6 and points_nicole == max(points_samantha, points_nicole, points_huey, points_camille, points_larissa, points_katia):
        jump capitulo10_final_nicole
    elif points_huey >= 6 and points_huey == max(points_samantha, points_nicole, points_huey, points_camille, points_larissa, points_katia):
        jump capitulo10_final_huey
    elif points_camille >= 6 and points_camille == max(points_samantha, points_nicole, points_huey, points_camille, points_larissa, points_katia):
        jump capitulo10_final_camille
    elif points_larissa >= 6 and points_larissa == max(points_samantha, points_nicole, points_huey, points_camille, points_larissa, points_katia):
        jump capitulo10_final_larissa
    elif points_katia >= 6 and points_katia == max(points_samantha, points_nicole, points_huey, points_camille, points_larissa, points_katia):
        jump capitulo10_final_katia
    else:
        jump capitulo10_despedida

# Finais individuais (exemplo com Samantha)
label capitulo10_final_samantha:
    show samantha happy at center
    narrator "Samantha aparece com dois controles nas mãos."
    samantha "É a última noite… e a gente ainda não zerou aquele jogo. Quer... terminar comigo?"
    narrator "Vocês jogam juntos, rindo, até a tela final."
    samantha "Você... foi meu player 2 favorito."
    if romance_samantha:
        samantha "No próximo jogo, eu quero começar contigo desde o prólogo."
    else:
        samantha "Mesmo em partidas separadas… sempre vou torcer pelo seu sucesso crítico."
    jump capitulo10_despedida

# Final com Nicole
label capitulo10_final_nicole:
    show nicole neutral at center
    narrator "Nicole aparece com um pequeno caderno de anotações nas mãos."
    nicole "Eu fiz uma lista de coisas que quero lembrar sobre hoje... mas nenhuma palavra parece suficiente."
    '[nome]' "Talvez algumas coisas não precisem ser escritas. Só sentidas."
    nicole "Você sempre sabe o que dizer. Obrigada por ser... você."
    if romance_nicole:
        nicole "Eu espero que, mesmo longe, você continue sendo meu ponto de equilíbrio. Porque eu quero ser o seu."
    else:
        nicole "Mesmo que a gente siga caminhos diferentes, eu sempre vou lembrar de você como alguém especial."
    narrator "Nicole sorri timidamente, e vocês compartilham um momento de silêncio confortável, cheio de significado."
    jump capitulo10_despedida

# Final com Huey
label capitulo10_final_huey:
    show huey gentle at center
    narrator "Huey aparece com um quadro recém-pintado, ainda com as mãos manchadas de tinta."
    huey "Eu pintei isso para você. É como eu vejo a gente... juntos, mesmo quando estamos longe."
    '[nome]' "Huey, isso é lindo. Obrigado por capturar algo tão especial."
    huey "Você sempre foi minha maior inspiração. Obrigado por me fazer acreditar na beleza das conexões."
    if romance_huey:
        huey "Eu quero que você saiba... você é a cor mais vibrante da minha vida."
    else:
        huey "Mesmo que a gente siga caminhos diferentes, você sempre será parte da minha paleta."
    narrator "Huey entrega o quadro a você, e vocês compartilham um momento de pura emoção e gratidão."
    jump capitulo10_despedida

# Final com Camille
label capitulo10_final_camille:
    show camille gentle at center
    narrator "Camille aparece com um pequeno cristal na mão, refletindo a luz do amanhecer."
    camille "Este cristal... ele guarda energia. Quero que você o leve, para lembrar que sempre estaremos conectados."
    '[nome]' "Camille, isso é lindo. Obrigado por sempre trazer equilíbrio para tudo."
    camille "Você também trouxe luz para minha vida. Obrigada por ser uma alma tão especial."
    if romance_camille:
        camille "Eu acredito que nossas almas se encontrarão de novo, vida após vida. Mas, por enquanto, quero aproveitar cada momento com você."
    else:
        camille "Mesmo que nossos caminhos se separem, saiba que você sempre terá um lugar especial na minha energia."
    narrator "Camille coloca o cristal em sua mão, e vocês compartilham um momento de serenidade e conexão."
    jump capitulo10_despedida

# Final com Larissa
label capitulo10_final_larissa:
    show larissa happy at center
    narrator "Larissa aparece com uma bola de vôlei nas mãos e um sorriso determinado."
    larissa "Ei, antes de irmos... que tal uma última partida? Só para garantir que você não esqueça como perder para mim."
    '[nome]' "Eu nunca vou esquecer, Larissa. Você sempre me ensinou a dar o meu melhor."
    larissa "Você é tão bobo... mas é por isso que eu gosto de você."
    if romance_larissa:
        larissa "Eu quero que você saiba... você é meu parceiro favorito, dentro e fora da quadra."
    else:
        larissa "Mesmo que a gente siga caminhos diferentes, você sempre será meu parceiro de treino favorito."
    narrator "Vocês jogam juntos uma última vez, rindo e compartilhando a energia contagiante de Larissa."
    jump capitulo10_despedida

# Final com Katia
label capitulo10_final_katia:
    show katia neutral at center
    narrator "Katia aparece com o celular na mão, gravando um vídeo enquanto se aproxima."
    katia "Se você contar pra alguém que eu disse isso, eu nego até o fim... mas você é uma das pessoas mais importantes que já conheci."
    '[nome]' "Katia, você é incrível. Obrigado por me deixar fazer parte da sua história."
    katia "Hmpf. Não se ache. Mas... obrigada por estar aqui."
    if romance_katia:
        katia "Eu quero que você saiba... você é o único clichê que eu aceito na minha vida."
    else:
        katia "Mesmo que a gente siga caminhos diferentes, você sempre será o protagonista de algumas das minhas melhores memórias."
    narrator "Katia desliga o celular e olha para você com um sorriso sincero, compartilhando um momento de conexão verdadeira."
    jump capitulo10_despedida

label capitulo10_despedida:
    scene bg republica_saida with fade
    narrator "Todos estão prontos. A van os espera. A casa está vazia. Um último olhar para trás. O grupo se reúne na sala, onde tantas memórias foram criadas."

    # Despedidas individuais para personagens sem romance
    if not romance_nicole:
        show nicole neutral at left
        narrator "Nicole ajusta os óculos e olha ao redor, tentando esconder a emoção."
        nicole "Nunca pensei que um grupo tão caótico pudesse funcionar tão bem. Vocês são... especiais."
        '[nome]' "E você foi o coração organizador disso tudo, Nicole. Obrigado por tudo."
        show samantha happy at center
        samantha "Nicole, você é a única pessoa que conseguiu organizar até as minhas ideias. Isso é um superpoder."
        nicole "Bem... alguém tinha que fazer isso."

    if not romance_samantha:
        show samantha happy at center
        narrator "Samantha segura um controle de videogame, como se fosse um troféu."
        samantha "Missão: manter contato. Recompensa: corações inteiros."
        '[nome]' "Você sempre fez tudo parecer mais divertido, Samantha. Obrigado por isso."
        show larissa happy at right
        larissa "E você sempre foi a melhor parceira de guilda. Mesmo quando perdia pra mim no vôlei."
        samantha "Ah, Larissa, você só ganhou porque eu deixei."

    if not romance_huey:
        show huey gentle at right
        narrator "Huey segura um caderno de desenhos, com as páginas cheias de memórias."
        huey "Posso pintar essa despedida? Só se alguém prometer voltar."
        '[nome]' "Huey, você capturou a essência de tudo isso. Obrigado por nos dar algo para lembrar."
        show camille gentle at left
        camille "Huey, suas cores sempre trouxeram vida para essa casa. Obrigada por isso."
        huey "E vocês foram minha inspiração. Sempre serão."

    if not romance_camille:
        show camille gentle at left
        narrator "Camille segura um pequeno cristal, refletindo a luz do amanhecer."
        camille "Essa casa... vibrou como família. E isso é algo que nunca vai desaparecer."
        '[nome]' "Você trouxe equilíbrio para tudo, Camille. Obrigado por ser a alma dessa casa."
        show katia neutral at center
        katia "Camille, você é a única pessoa que conseguiu me fazer acreditar em energia. Isso é um milagre."
        camille "E você trouxe uma energia única, Katia. Obrigada por isso."

    if not romance_larissa:
        show larissa happy at center
        narrator "Larissa segura uma bola de vôlei, girando-a entre as mãos."
        larissa "Bora. Ou vou começar a chorar."
        '[nome]' "Você sempre nos lembrou de sermos fortes, Larissa. Obrigado por isso."
        show samantha happy at right
        samantha "E você sempre me fez correr mais rápido, mesmo quando eu só queria sentar e jogar."
        larissa "É porque eu sabia que você podia mais, Samantha."

    if not romance_katia:
        show katia neutral at right
        narrator "Katia segura o celular, gravando um último vídeo da casa e do grupo."
        katia "Alguém anota isso. É final de temporada."
        '[nome]' "Você sempre trouxe um olhar único para tudo, Katia. Obrigado por compartilhar isso conosco."
        show nicole neutral at left
        nicole "E você sempre conseguiu transformar até o caos em algo interessante. Isso é um talento."
        katia "Hmpf. Não se ache, Nicole. Mas... obrigada."

    # Despedida geral
    narrator "O grupo se reúne em um círculo, compartilhando risadas, abraços e promessas de manter contato. Mesmo com caminhos diferentes, algo foi construído ali. Algo que nem o tempo pode apagar."

    show samantha happy at center
    samantha "A gente devia ter gravado mais clipes de voz. Mas acho que as memórias vão ficar."

    show larissa happy at left
    larissa "E se não ficarem, eu vou lembrar vocês com uma partida de vôlei."

    show huey gentle at right
    huey "Ou com uma pintura. Cada um de vocês é uma cor única na minha paleta."

    show camille gentle at left
    camille "E essa energia... ela vai continuar vibrando, mesmo longe."

    show katia neutral at center
    katia "Isso daria um ótimo roteiro. Mas acho que viver foi ainda melhor."

    show nicole neutral at right
    nicole "E, claro, tudo isso só funcionou porque seguimos o cronograma. Mais ou menos."

    narrator "Com risadas e lágrimas, o grupo se despede da casa que foi seu lar. A van os espera. Um último olhar para trás, e eles seguem em frente, levando consigo as memórias e os laços que construíram."

    jump epilogo