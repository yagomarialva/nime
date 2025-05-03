label capitulo9:
    scene bg republica_manha with fade
    narrator "A manhã começa como qualquer outra... até que o e-mail chega. A caixa de entrada da república explode de notificações."

    show nicole neutral at left
    nicole "É... chegou."

    show camille gentle at center
    camille "Que as energias estejam em fluxo…"

    show katia neutral at right
    katia "Se for negativa, eu me mudo pra uma caverna. Ou pro porão do cinema."

    show larissa happy at left
    larissa "Gente, lê logo! Meu sangue tá indo todo pro cérebro!"

    narrator "Você abre o e-mail e lê em voz alta."
    '[nome]' "Após revisão do material enviado e avaliação da relevância cultural e comunitária da residência, a reitoria... autoriza a manutenção da república Rua Aurora."

    show samantha happy at center
    samantha "MISSÃO COMPLETA!"

    show huey gentle at right
    huey "Vamos continuar pintando as manhãs juntos..."

    narrator "Eles se abraçam. Alguns riem. Outros choram. O lar deles, construído com convivência, está salvo."

    # Todos os personagens recebem +1 ponto de afinidade
    $ points_samantha += 1
    $ points_nicole += 1
    $ points_huey += 1
    $ points_camille += 1
    $ points_larissa += 1
    $ points_katia += 1

    # Gesto carinhoso se em rota romântica
    if romance_samantha:
        narrator "Samantha segura sua mão por um momento, sorrindo."
    elif romance_nicole:
        narrator "Nicole olha para você, com um sorriso tímido e prolongado."
    elif romance_huey:
        narrator "Huey toca seu ombro, com um olhar cheio de significado."
    elif romance_camille:
        narrator "Camille fecha os olhos e murmura algo sobre conexões eternas."
    elif romance_larissa:
        narrator "Larissa dá um leve soco no seu braço, rindo."
    elif romance_katia:
        narrator "Katia desvia o olhar, mas você percebe um sorriso sincero."

    jump capitulo9_praia

label capitulo9_praia:
    scene bg praia_chegada with fade
    narrator "Para comemorar, Camille sugere uma escapada. Huey organiza, Larissa aluga uma van, e no sábado, todos partem para a Praia da Lua Clara — famosa por seu pôr do sol lilás."

    show camille gentle at left
    camille "O mar cura. E hoje... a gente merece mergulhar."

    show nicole neutral at center
    nicole "Horário das refeições, revezamento do guarda-sol e tempo livre organizados."

    show samantha happy at right
    samantha "Vai ter RPG na areia, sim!"

    show katia neutral at left
    katia "Sol, suor e sentimentalismo... ótimo roteiro para um drama de verão."

    show huey gentle at center
    huey "Vou pintar vocês no mar. Sem reclamar!"

    show larissa happy at right
    larissa "E vai ter campeonato! Vamo ver quem aguenta a minha cortada!"

    # Todos ganham +1 ponto de afinidade
    $ points_samantha += 1
    $ points_nicole += 1
    $ points_huey += 1
    $ points_camille += 1
    $ points_larissa += 1
    $ points_katia += 1
    $ interacoes_realizadas = []
    jump capitulo9_tarde

label capitulo9_tarde:
    
    if len(interacoes_realizadas) == 6:
        jump capitulo9_fogueira

    # Exibe o menu com as opções restantes
    menu:
        "Caminhada nas pedras com Camille" if "camille" not in interacoes_realizadas:
            $ interacoes_realizadas.append("camille")
            jump capitulo9_camille
        "Aula de vôlei com Larissa" if "larissa" not in interacoes_realizadas:
            $ interacoes_realizadas.append("larissa")
            jump capitulo9_larissa
        "Aquarela na areia com Huey" if "huey" not in interacoes_realizadas:
            $ interacoes_realizadas.append("huey")
            jump capitulo9_huey
        "Construção de castelo com Samantha" if "samantha" not in interacoes_realizadas:
            $ interacoes_realizadas.append("samantha")
            jump capitulo9_samantha
        "Conversa estratégica na sombra com Nicole" if "nicole" not in interacoes_realizadas:
            $ interacoes_realizadas.append("nicole")
            jump capitulo9_nicole
        "Trilha até a falésia com Katia" if "katia" not in interacoes_realizadas:
            $ interacoes_realizadas.append("katia")
            jump capitulo9_katia

label capitulo9_camille:
    show camille gentle at center
    narrator "Você e Camille caminham pelas pedras, com o vento bagunçando os cabelos dela."
    camille "Às vezes me pergunto… se algumas almas se encontram vida após vida."
    '[nome]' "Você acha que a gente já se conheceu antes?"
    camille "Talvez. Ou talvez só tenha sido bom o bastante pra parecer eterno agora."

    if romance_camille:
        narrator "Camille segura sua mão e, por um momento, o mundo parece parar. Vocês compartilham um beijo suave."
    elif points_camille >= 5:
        narrator "Camille sorri e abraça você, um gesto cheio de significado."
    else:
        narrator "Camille fala sobre conexões espirituais, deixando você inspirado."

    jump capitulo9_tarde

label capitulo9_larissa:
    show larissa happy at center
    narrator "Você e Larissa estão na quadra improvisada na areia, com uma bola de vôlei entre vocês."
    larissa "Vamos lá! Quero ver se você consegue bloquear minha cortada!"
    '[nome]' "Eu vou tentar, mas não prometo nada."
    larissa "Sem desculpas! Aqui é treino sério!"
    
    if romance_larissa:
        narrator "Depois de uma partida intensa, Larissa sorri e se aproxima. Ela toca seu braço e, por um momento, vocês compartilham algo mais profundo."
    elif points_larissa >= 5:
        narrator "Larissa ri e dá um leve soco no seu ombro. 'Você tá melhorando, hein!'"
    else:
        narrator "Larissa dá algumas dicas sobre vôlei, e vocês terminam a partida com risadas e aprendizado."

    jump capitulo9_tarde

label capitulo9_huey:
    show huey gentle at center
    narrator "Você e Huey estão sentados na areia, com pincéis e aquarelas espalhados ao redor."
    huey "Eu quero capturar o movimento das ondas... mas também o que elas fazem a gente sentir."
    '[nome]' "Isso é... profundo. Você sempre pensa assim?"
    huey "A arte é sobre sentir. E você me inspira a sentir mais."

    if romance_huey:
        narrator "Huey sorri timidamente e mostra um retrato que ele fez de você. 'Espero que goste... é como eu vejo você.'"
    elif points_huey >= 5:
        narrator "Huey mostra um desenho das ondas e explica como ele tentou capturar o momento. 'Obrigado por estar aqui comigo.'"
    else:
        narrator "Huey fala sobre as cores e formas, e você se sente inspirado pela paixão dele pela arte."

    jump capitulo9_tarde

label capitulo9_samantha:
    show samantha happy at center
    narrator "Você e Samantha estão na areia, construindo um castelo com torres e muralhas."
    samantha "Se isso fosse um jogo, a gente já teria desbloqueado o troféu de 'melhor castelo'."
    '[nome]' "Com certeza. Mas acho que precisamos de uma ponte levadiça."
    samantha "Boa ideia! E talvez um dragão pra proteger o tesouro."

    if romance_samantha:
        narrator "Samantha olha para você e sorri. 'Você é o melhor parceiro de guilda que eu poderia ter.'"
    elif points_samantha >= 5:
        narrator "Samantha ri e dá um high-five em você. 'A gente arrasou nesse castelo!'"
    else:
        narrator "Samantha fala sobre como jogos e criatividade ajudam a construir coisas incríveis, e você se sente inspirado."

    jump capitulo9_tarde

label capitulo9_nicole:
    show nicole neutral at center
    narrator "Você e Nicole estão sentados sob um guarda-sol, com uma brisa suave passando por vocês."
    nicole "Eu não gosto muito de areia... mas gosto da sua companhia."
    '[nome]' "Então, vou considerar isso um elogio."
    nicole "Considere. Mas não se acostume."

    if romance_nicole:
        narrator "Nicole olha para você, corando levemente. 'Obrigada por estar aqui. Isso significa muito pra mim.'"
    elif points_nicole >= 5:
        narrator "Nicole sorri e ajusta os óculos. 'Acho que você é a única pessoa com quem eu consigo relaxar assim.'"
    else:
        narrator "Nicole fala sobre como a organização do dia foi importante, e você percebe o quanto ela se importa com os detalhes."

    jump capitulo9_tarde

label capitulo9_katia:
    show katia neutral at center
    narrator "Você e Katia estão subindo uma trilha até a falésia, com o som das ondas ao fundo."
    katia "Se isso fosse um filme, esse seria o momento em que o [nome] faz uma grande revelação."
    '[nome]' "E você? Qual seria sua grande revelação?"
    katia "Que eu odeio clichês... mas talvez goste de momentos como esse."

    if romance_katia:
        narrator "Katia para por um momento e olha para você. 'Não vou dizer que isso é especial... mas talvez seja.'"
    elif points_katia >= 5:
        narrator "Katia sorri de lado. 'Você é menos irritante do que eu pensei. Isso é um elogio.'"
    else:
        narrator "Katia fala sobre como momentos simples podem ser os mais significativos, e você sente que a entende melhor."

    jump capitulo9_tarde

label capitulo9_fogueira:
    scene bg fogueira_noite with fade
    narrator "À noite, o grupo monta uma fogueira. Risos, batidas na perna, violão desafinado, biscoitos queimados e segredos partilhados."

    show nicole neutral at left
    nicole "Acho que... isso é o mais perto de paz que já estive."

    show huey gentle at center
    huey "Essas cores dançam como a gente hoje dançou o dia inteiro."

    show katia neutral at right
    katia "Isso é conteúdo demais pra não virar roteiro."

    show camille gentle at left
    camille "Promete que a gente se encontra sempre, mesmo depois?"

    show larissa happy at center
    larissa "Eu prometo. Com sangue de atleta."

    show samantha happy at right
    samantha "Você prometeu me escolher na próxima campanha..."

    if romance_samantha:
        narrator "Samantha se aproxima e vocês compartilham um momento íntimo à parte."
    elif romance_nicole:
        narrator "Nicole senta ao seu lado, e vocês trocam olhares significativos."
    elif romance_huey:
        narrator "Huey mostra um desenho que fez de você, cheio de detalhes."
    elif romance_camille:
        narrator "Camille segura sua mão e murmura algo sobre eternidade."
    elif romance_larissa:
        narrator "Larissa desafia você para uma corrida até a beira do mar."
    elif romance_katia:
        narrator "Katia compartilha um segredo que ela nunca contou a ninguém."

    jump capitulo9_amanhecer

label capitulo9_amanhecer:
    scene bg praia_amanhecer with fade
    narrator "O sol começa a nascer. Todos ainda sonolentos, cobertos de areia e lembranças. Você caminha sozinho até o mar."

    # Exibe todas as interações de amizade (onde romance_<personagem> é False)
    if not romance_nicole:
        show nicole neutral at left
        narrator "Nicole se aproxima, ajustando os óculos enquanto observa o mar."
        nicole "Eu nunca fui boa em dizer essas coisas, mas... obrigada por tudo. Você me mostrou que nem tudo precisa ser tão calculado. Às vezes, só estar presente já é suficiente."
        '[nome]' "Você também me ensinou muito, Nicole. Obrigado por ser você."
        nicole "Bem... acho que isso significa que somos uma boa equipe."

    if not romance_samantha:
        show samantha happy at center
        narrator "Samantha aparece com um sorriso radiante, segurando um cobertor enrolado nos ombros."
        samantha "Ei, parceiro de guilda! Só queria dizer que você é o melhor companheiro de aventuras que eu poderia pedir. Obrigada por sempre estar ao meu lado."
        '[nome]' "E você é a pessoa mais criativa e divertida que eu conheço. Obrigado por tornar tudo mais leve."
        samantha "Ah, para! Você vai me fazer chorar... ou talvez só rir mais alto."

    if not romance_huey:
        show huey gentle at right
        narrator "Huey se aproxima, segurando seu caderno de desenhos, com um sorriso sereno."
        huey "Eu queria te mostrar isso... é um desenho que fiz de todos nós. Você está bem no centro, porque foi você que manteve tudo unido."
        '[nome]' "Huey, isso é incrível. Obrigado por capturar algo tão especial."
        huey "Obrigado por ser minha inspiração. Você é uma pessoa única."

    if not romance_camille:
        show camille gentle at left
        narrator "Camille se aproxima, com os olhos brilhando sob a luz do amanhecer."
        camille "Você sente isso? A energia... ela está em paz. E acho que é porque você esteve aqui para equilibrar tudo."
        '[nome]' "Você sempre me fez ver o mundo de uma forma diferente, Camille. Obrigado por isso."
        camille "E você me fez acreditar que algumas conexões são eternas, mesmo sem palavras."

    if not romance_larissa:
        show larissa happy at center
        narrator "Larissa aparece com sua energia contagiante, segurando uma bola de vôlei."
        larissa "Ei, só queria dizer que você é incrível. Não sei como você conseguiu acompanhar meu ritmo, mas você fez isso parecer fácil."
        '[nome]' "Você me ensinou a nunca desistir, Larissa. Obrigado por isso."
        larissa "Ah, para com isso! Mas... obrigada por estar aqui. Você é um amigo incrível."

    if not romance_katia:
        show katia neutral at right
        narrator "Katia se aproxima, com o celular na mão e um sorriso discreto."
        katia "Se você contar pra alguém que eu disse isso, eu nego até o fim, mas... você é uma das pessoas mais importantes que já conheci. Obrigada por tudo."
        '[nome]' "Katia, você é incrível. Obrigado por me deixar fazer parte da sua história."
        katia "Hmpf. Não se ache. Mas... obrigada por estar aqui."

    # Exibe a interação romântica com a personagem escolhida
    if romance_nicole:
        jump capitulo9_final_nicole
    elif romance_samantha:
        jump capitulo9_final_samantha
    elif romance_huey:
        jump capitulo9_final_huey
    elif romance_camille:
        jump capitulo9_final_camille
    elif romance_larissa:
        jump capitulo9_final_larissa
    elif romance_katia:
        jump capitulo9_final_katia

    jump capitulo10

label capitulo9_final_nicole:
    show nicole neutral at center
    narrator "Nicole se aproxima em silêncio, com o som das ondas preenchendo o espaço entre vocês."
    nicole "Acordei com barulho de passos... e achei que fosse um ladrão de dados. Mas era só você."
    '[nome]' "Não consegui dormir. Minha mente está cheia... mas você me acalma."
    nicole "Você sempre sabe o que dizer. É estranho... mas acho que nunca me senti tão segura com alguém."
    menu:
        "Confessar que quer estar com ela":
            $ romance_nicole = True
            "[nome]" "Nicole, eu quero estar com você. Não só agora, mas sempre."
            nicole "Sempre? Isso é... mais do que eu esperava. Mas acho que eu também quero isso."
            narrator "Nicole se aproxima e, com um sorriso tímido, vocês compartilham um beijo sob o céu estrelado."
            jump capitulo10
        "Dizer que está em paz só com a presença":
            $ points_nicole += 1
            "[nome]" "Só estar aqui com você já é suficiente. Você é meu ponto de equilíbrio."
            nicole "Isso é... bom de ouvir. Obrigada por ser você."
            narrator "Nicole segura sua mão por um momento, e vocês ficam em silêncio, apreciando a companhia um do outro."
            jump capitulo10
        "Permanecer em silêncio":
            narrator "Vocês ficam em silêncio, mas o olhar de Nicole diz tudo. A conexão entre vocês se aprofunda sem a necessidade de palavras."
            jump capitulo10

label capitulo9_final_samantha:
    show samantha happy at center
    narrator "Samantha se aproxima, segurando um cobertor e olhando para o mar com um sorriso suave."
    samantha "Você... não conseguiu dormir também?"
    '[nome]' "Não. Mas acho que é porque eu queria estar aqui com você."
    samantha "Você é tão bobo... mas eu gosto disso."
    menu:
        "Confessar que quer estar com ela":
            $ romance_samantha = True
            "[nome]" "Samantha, eu quero estar com você. Você faz tudo parecer mais divertido, mais leve."
            samantha "Sério?! Isso foi tipo... um crítico de afeto. E eu aceito. Obrigada por me escolher."
            narrator "Samantha se aproxima e, com um sorriso radiante, vocês compartilham um beijo cheio de alegria e carinho."
            jump capitulo10
        "Dizer que está em paz só com a presença":
            $ points_samantha += 1
            "[nome]" "Só estar aqui com você já é suficiente. Você faz tudo parecer mais especial."
            samantha "Você é o melhor parceiro de guilda que eu poderia ter. Obrigada por isso."
            narrator "Samantha se aconchega ao seu lado, e vocês compartilham um momento tranquilo sob o céu estrelado."
            jump capitulo10
        "Permanecer em silêncio":
            narrator "Vocês ficam em silêncio, mas o sorriso de Samantha diz tudo. A conexão entre vocês é inegável."
            jump capitulo10

label capitulo9_final_huey:
    show huey gentle at center
    narrator "Huey se aproxima, segurando um pequeno caderno de desenhos, com um sorriso tímido."
    huey "Eu ainda não terminei... mas acho que esse traço aqui é você."
    '[nome]' "Você ficou acordado desenhando? Isso é lindo, Huey."
    huey "A arte é como eu expresso o que sinto. E você... você é minha maior inspiração."
    menu:
        "Confessar que quer estar com ele":
            $ romance_huey = True
            "[nome]" "Huey, eu quero estar com você. Você vê o mundo de um jeito que me faz querer ser parte dele."
            huey "Eu... nunca pensei que alguém pudesse dizer isso pra mim. Obrigado por me ver de verdade."
            narrator "Huey se aproxima, e vocês compartilham um beijo suave, cheio de significado e emoção."
            jump capitulo10
        "Dizer que está em paz só com a presença":
            $ points_huey += 1
            "[nome]" "Só estar aqui com você já é suficiente. Você me inspira."
            huey "Isso significa muito pra mim. Obrigado por estar aqui."
            narrator "Huey segura sua mão, e vocês compartilham um momento tranquilo, cercados pelo som das ondas."
            jump capitulo10
        "Permanecer em silêncio":
            narrator "Vocês ficam em silêncio, mas o olhar de Huey transmite tudo o que ele sente. A conexão entre vocês é profunda e sincera."
            jump capitulo10

label capitulo9_final_camille:
    show camille gentle at center
    narrator "Camille se aproxima, com os olhos brilhando sob a luz do amanhecer."
    camille "Você sente isso? A energia... ela está mudando."
    '[nome]' "Sim. Parece que tudo está em equilíbrio agora. Como se fosse o lugar certo para estarmos juntos."
    camille "Talvez seja porque estamos aqui. Juntos. E isso é tudo o que importa."
    menu:
        "Confessar que quer estar com ela":
            $ romance_camille = True
            "[nome]" "Camille, eu quero estar com você. Você me faz acreditar em coisas que eu nunca pensei serem possíveis."
            camille "Você é uma alma especial. Obrigada por me encontrar, vida após vida."
            narrator "Camille segura sua mão e, com um sorriso suave, vocês compartilham um beijo cheio de significado e conexão."
            jump capitulo10
        "Dizer que está em paz só com a presença":
            $ points_camille += 1
            "[nome]" "Só estar aqui com você já é suficiente. Você traz paz ao meu coração."
            camille "E você traz luz ao meu mundo. Obrigada por isso."
            narrator "Camille se aproxima e segura sua mão, e vocês compartilham um momento de pura serenidade."
            jump capitulo10
        "Permanecer em silêncio":
            narrator "Vocês ficam em silêncio, mas o toque de Camille transmite tudo o que as palavras não conseguem expressar."
            jump capitulo10

label capitulo9_final_larissa:
    show larissa happy at center
    narrator "Larissa se aproxima, segurando uma garrafa d’água e sorrindo com entusiasmo."
    larissa "Acha que amanhã a gente pode correr juntos? Ou você vai me deixar na poeira?"
    '[nome]' "Eu acho que vou tentar acompanhar você. Mas, na verdade, só quero estar ao seu lado."
    larissa "Você é tão bobo... mas eu gosto disso."
    menu:
        "Confessar que quer estar com ela":
            $ romance_larissa = True
            "[nome]" "Larissa, eu quero estar com você. Você me faz querer ser melhor, todos os dias."
            larissa  "Sério?! Uau. Isso é... incrível. Eu também quero isso."
            narrator "Larissa se aproxima e, com um sorriso radiante, vocês compartilham um beijo cheio de energia e paixão."
            jump capitulo10
        "Dizer que está em paz só com a presença":
            $ points_larissa += 1
            "[nome]" "Só estar aqui com você já é suficiente. Você ilumina tudo ao seu redor."
            larissa "Você é incrível. Obrigada por estar aqui comigo."
            narrator "Larissa segura sua mão, e vocês compartilham um momento de pura alegria e conexão."
            jump capitulo10
        "Permanecer em silêncio":
            narrator "Vocês ficam em silêncio, mas o sorriso de Larissa diz tudo. A conexão entre vocês é cheia de vida e significado."
            jump capitulo10

label capitulo9_final_katia:
    show katia neutral at center
    narrator "Katia se aproxima, segurando o celular e olhando para o mar com um sorriso discreto."
    katia "Se você comentar que eu tô aqui, eu juro que te ignoro o resto da vida."
    '[nome]' "Eu não vou comentar. Só estou feliz que você está aqui comigo."
    katia "Você é tão irritante... mas acho que eu gosto disso."
    menu:
        "Confessar que quer estar com ela":
            $ romance_katia = True
            "[nome]" "Katia, eu quero estar com você. Você me faz ver o mundo de um jeito que ninguém mais consegue."
            katia  "Hmpf. Não se ache. Mas... obrigada por dizer isso. Eu também quero estar com você."
            narrator "Katia se aproxima e, com um sorriso tímido, vocês compartilham um beijo cheio de emoção e sinceridade."
            jump capitulo10
        "Dizer que está em paz só com a presença":
            $ points_katia += 1
            "[nome]" "Só estar aqui com você já é suficiente. Você é única."
            katia "Tá. Mas não me faça esperar muito. Obrigada por isso."
            narrator "Katia olha para você com um sorriso sincero, e vocês compartilham um momento tranquilo e significativo."
            jump capitulo10
        "Permanecer em silêncio":
            narrator "Vocês ficam em silêncio, mas o olhar de Katia transmite tudo o que ela sente. A conexão entre vocês é profunda e verdadeira."
            jump capitulo10

label capitulo9_final_amizade:
    scene bg praia_amanhecer with fade
    narrator "Com o sol nascendo no horizonte, você se encontra cercado pelas pessoas que fizeram parte dessa jornada. Mesmo sem um romance, os laços de amizade construídos ao longo do tempo são inegáveis."

    # Nicole
    if not romance_nicole:
        show nicole neutral at left
        narrator "Nicole se aproxima, ajustando os óculos enquanto observa o mar."
        nicole "Eu nunca fui boa em dizer essas coisas, mas... obrigada por tudo. Você me mostrou que nem tudo precisa ser tão calculado. Às vezes, só estar presente já é suficiente."
        '[nome]' "Você também me ensinou muito, Nicole. Obrigado por ser você."
        nicole "Bem... acho que isso significa que somos uma boa equipe."

    # Samantha
    if not romance_samantha:
        show samantha happy at center
        narrator "Samantha aparece com um sorriso radiante, segurando um cobertor enrolado nos ombros."
        samantha "Ei, parceiro de guilda! Só queria dizer que você é o melhor companheiro de aventuras que eu poderia pedir. Obrigada por sempre estar ao meu lado."
        '[nome]' "E você é a pessoa mais criativa e divertida que eu conheço. Obrigado por tornar tudo mais leve."
        samantha "Ah, para! Você vai me fazer chorar... ou talvez só rir mais alto."

    # Huey
    if not romance_huey:
        show huey gentle at right
        narrator "Huey se aproxima, segurando seu caderno de desenhos, com um sorriso sereno."
        huey "Eu queria te mostrar isso... é um desenho que fiz de todos nós. Você está bem no centro, porque foi você que manteve tudo unido."
        '[nome]' "Huey, isso é incrível. Obrigado por capturar algo tão especial."
        huey "Obrigado por ser minha inspiração. Você é uma pessoa única."

    # Camille
    if not romance_camille:
        show camille gentle at left
        narrator "Camille se aproxima, com os olhos brilhando sob a luz do amanhecer."
        camille "Você sente isso? A energia... ela está em paz. E acho que é porque você esteve aqui para equilibrar tudo."
        '[nome]' "Você sempre me fez ver o mundo de uma forma diferente, Camille. Obrigado por isso."
        camille "E você me fez acreditar que algumas conexões são eternas, mesmo sem palavras."

    # Larissa
    if not romance_larissa:
        show larissa happy at center
        narrator "Larissa aparece com sua energia contagiante, segurando uma bola de vôlei."
        larissa "Ei, só queria dizer que você é incrível. Não sei como você conseguiu acompanhar meu ritmo, mas você fez isso parecer fácil."
        '[nome]' "Você me ensinou a nunca desistir, Larissa. Obrigado por isso."
        larissa "Ah, para com isso! Mas... obrigada por estar aqui. Você é um amigo incrível."

    # Katia
    if not romance_katia:
        show katia neutral at right
        narrator "Katia se aproxima, com o celular na mão e um sorriso discreto."
        katia "Se você contar pra alguém que eu disse isso, eu nego até o fim, mas... você é uma das pessoas mais importantes que já conheci. Obrigada por tudo."
        '[nome]' "Katia, você é incrível. Obrigado por me deixar fazer parte da sua história."
        katia "Hmpf. Não se ache. Mas... obrigada por estar aqui."

    narrator "Enquanto o sol sobe no céu, você percebe que, independentemente de romances ou destinos, os laços que você construiu com essas pessoas são inquebráveis. E isso é o que realmente importa."

    jump capitulo10