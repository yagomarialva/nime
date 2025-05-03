label capitulo8:
    scene bg republica_noite with fade
    narrator "Três dias se passaram desde a notificação da universidade. A república da Rua Aurora fervilha de ideias, reuniões e noites mal dormidas. O prazo final para apresentar a defesa está próximo."

    show nicole neutral at left
    nicole "Temos 48 horas para enviar um documento oficial com o pedido de permanência. E não vamos conseguir sem trabalho sério."

    show camille neutral at center
    camille "Mas também não sem verdade emocional. Precisamos que eles sintam."

    show katia neutral at right
    katia "A universidade quer números? Vamos dar emoção crua em imagens. Tipo um soco narrativo."

    show huey neutral at left
    huey "A arte vive aqui. Nos nossos pratos, nas paredes, nos gestos. Isso... tem que ser visto."

    show samantha neutral at center
    samantha "Já montei as cenas da rotina. Vai parecer um slice of life real."

    show larissa happy at right
    larissa "Se eu tiver que correr até o reitor e fazer uma pirueta, eu faço!"

    menu:
        "Vídeo emocional (Huey, Camille, Samantha)":
            $ points_huey += 1
            $ points_camille += 1
            $ points_samantha += 1
            narrator "O grupo decide criar um vídeo emocional que capture a essência da república."
            jump cena2_divisao_tarefas
        "Dossiê produtivo e acadêmico (Nicole, Katia)":
            $ points_nicole += 1
            $ points_katia += 1
            narrator "O grupo decide criar um dossiê detalhado e acadêmico para impressionar a universidade."
            jump cena2_divisao_tarefas
        "Apresentação esportiva e cotidiana (Larissa, Samantha, Huey)":
            $ points_larissa += 1
            $ points_samantha += 1
            $ points_huey += 1
            narrator "O grupo decide criar uma apresentação que mostre a rotina e o espírito esportivo da república."
            jump cena2_divisao_tarefas
        "Defesa ao vivo, interativa (Nicole, Camille, Protagonista)":
            $ points_nicole += 1
            $ points_camille += 1
            narrator "O grupo decide fazer uma defesa ao vivo, interativa, para engajar a audiência."
            jump cena2_divisao_tarefas

label cena2_divisao_tarefas:
    narrator "Com a escolha feita, os moradores se dividem em grupos. O protagonista pode escolher com quem deseja trabalhar para preparar uma parte essencial."

    menu:
        "Trabalhar com Nicole":
            jump parceria_nicole
        "Trabalhar com Samantha":
            jump parceria_samantha
        "Trabalhar com Huey":
            jump parceria_huey
        "Trabalhar com Camille":
            jump parceria_camille
        "Trabalhar com Katia":
            jump parceria_katia
        "Trabalhar com Larissa":
            jump parceria_larissa

label parceria_nicole:
    show nicole neutral at center
    narrator "Nicole está tensa, rabiscando o quadro branco com ideias e cálculos."
    nicole "Preciso que revise isso. E que pense como um avaliador burocrático… não como alguém emocionalmente envolvido."
    menu:
        "Apoiar racionalmente":
            $ points_nicole += 1
            "[nome]" "Claro. Vamos focar nos detalhes técnicos."
            nicole "Obrigada. Isso vai ajudar muito."
            jump cena3_ultima_noite
        "Elogiar seu esforço":
            $ points_nicole += 2
            "[nome]" "Você está fazendo um trabalho incrível. Estou impressionado."
            nicole "Obrigada... isso significa muito para mim."
            jump cena3_ultima_noite
        "Fazer piada":
            $ points_nicole -= 1
            "[nome]" "Você está levando isso muito a sério. Relaxa um pouco."
            nicole "Não é hora para piadas. Precisamos ser sérios."
            jump cena3_ultima_noite

label parceria_samantha:
    show samantha neutral at center
    narrator "Samantha está sentada no sofá, com um controle de videogame na mão e anotações espalhadas ao redor."
    samantha "Eu tô tentando montar isso como se fosse um jogo... mas parece que o boss final é impossível."
    menu:
        "Ajudar com estratégias práticas":
            $ points_samantha += 1
            "[nome]" "Talvez se você dividir o problema em partes menores, fique mais fácil."
            samantha "Boa ideia! Obrigada, player dois."
            jump cena3_ultima_noite
        "Elogiar sua criatividade":
            $ points_samantha += 2
            "[nome]" "Você é incrível. Transformar isso em um jogo é genial."
            samantha "Sério?! Isso foi tipo... um crítico de afeto. Obrigada."
            jump cena3_ultima_noite
        "Fazer piada":
            $ points_samantha -= 1
            "[nome]" "Talvez você só precise de um cheat code."
            samantha "Haha... engraçado. Mas isso não ajuda muito."
            jump cena3_ultima_noite

label parceria_huey:
    show huey gentle at center
    narrator "Huey está no jardim, cercada por pincéis e tintas, trabalhando em um grande mural."
    huey "Eu quero que isso capture a essência da república... mas parece que sempre falta algo."
    menu:
        "Oferecer ideias para o mural":
            $ points_huey += 1
            "[nome]" "Talvez você possa incluir algo que represente cada um de nós."
            huey "Boa ideia. Isso pode dar mais vida à pintura."
            jump cena3_ultima_noite
        "Elogiar sua arte":
            $ points_huey += 2
            "[nome]" "Sua arte já é incrível. Você sempre consegue transmitir tanto sentimento."
            huey "Obrigada... isso significa muito para mim."
            jump cena3_ultima_noite
        "Fazer piada":
            $ points_huey -= 1
            "[nome]" "Talvez você só precise de mais tinta."
            huey "Haha... engraçado. Mas isso não resolve o problema."
            jump cena3_ultima_noite

label parceria_camille:
    show camille gentle at center
    narrator "Camille está na sala de meditação, cercada por cristais e incensos, com um caderno aberto à sua frente."
    camille "Eu quero que isso reflita a energia da casa... mas sinto que ainda não está completo."
    menu:
        "Oferecer apoio emocional":
            $ points_camille += 1
            "[nome]" "Talvez você só precise de um pouco mais de tempo. Estou aqui para ajudar."
            camille "Obrigada. Sua presença já é suficiente."
            jump cena3_ultima_noite
        "Elogiar sua sensibilidade":
            $ points_camille += 2
            "[nome]" "Você tem uma sensibilidade única. Tenho certeza de que vai ficar perfeito."
            camille "Obrigada. Isso significa muito para mim."
            jump cena3_ultima_noite
        "Fazer piada":
            $ points_camille -= 1
            "[nome]" "Talvez você só precise de um cristal maior."
            camille "Haha... engraçado. Mas isso não ajuda muito."
            jump cena3_ultima_noite

label parceria_katia:
    show katia neutral at center
    narrator "Katia está no quarto, rabiscando freneticamente em um caderno, com papéis espalhados por toda parte."
    katia "Eu tô tentando escrever algo que capture o que essa casa significa... mas tá difícil."
    menu:
        "Oferecer ideias para o roteiro":
            $ points_katia += 1
            "[nome]" "Talvez você possa escrever sobre como cada um de nós contribui para a república."
            katia "Hmpf. Não é uma ideia ruim. Vou pensar nisso."
            jump cena3_ultima_noite
        "Elogiar sua escrita":
            $ points_katia += 2
            "[nome]" "Você é uma roteirista incrível. Tenho certeza de que vai ficar ótimo."
            katia "Hmpf. Não se ache. Mas... obrigada."
            jump cena3_ultima_noite
        "Fazer piada":
            $ points_katia -= 1
            "[nome]" "Talvez você só precise de um pouco mais de drama."
            katia "Haha... engraçado. Mas isso não resolve nada."
            jump cena3_ultima_noite

label parceria_larissa:
    show larissa happy at center
    narrator "Larissa está na sala de treino, fazendo flexões enquanto pensa em ideias para a apresentação."
    larissa "Eu tô tentando pensar em algo que mostre nossa energia... mas parece que tá faltando algo."
    menu:
        "Oferecer ideias para a apresentação":
            $ points_larissa += 1
            "[nome]" "Talvez você possa mostrar como todos nós trabalhamos juntos como um time."
            larissa "Boa ideia! Isso pode funcionar."
            jump cena3_ultima_noite
        "Elogiar sua energia":
            $ points_larissa += 2
            "[nome]" "Você é incrível. Sua energia é contagiante."
            larissa "Obrigada. Isso significa muito para mim."
            jump cena3_ultima_noite
        "Fazer piada":
            $ points_larissa -= 1
            "[nome]" "Talvez você só precise de mais flexões."
            larissa "Haha... engraçado. Mas isso não ajuda muito."
            jump cena3_ultima_noite

label cena3_ultima_noite:
    narrator "A noite antes da entrega chega. A república está em silêncio. Cada quarto aceso guarda emoções, expectativas... e medo de perder algo precioso."

    menu:
        "Visitar o quarto de Samantha":
            jump capitulo8_quarto_samantha
        "Visitar o quarto de Nicole":
            jump capitulo8_quarto_nicole
        "Visitar o quarto de Huey":
            jump capitulo8_quarto_huey
        "Visitar o quarto de Camille":
            jump capitulo8_quarto_camille
        "Visitar o quarto de Larissa":
            jump capitulo8_quarto_larissa
        "Visitar o quarto de Katia":
            jump capitulo8_quarto_katia

label capitulo8_quarto_samantha:
    show samantha neutral at center
    narrator "Samantha está sentada no chão, cercada por controles e anotações."
    samantha "Se tudo mudar... posso salvar a gente num slot diferente?"
    menu:
        "Se declarar":
            $ romance_samantha = True
            "[nome]" "Prefiro jogar nesse aqui, com você."
            samantha "Sério?! Isso foi tipo... um crítico de afeto. Obrigada."
            jump cena4_entrega
        "Abraçá-la":
            $ points_samantha += 1
            "[nome]" "Você está indo muito bem. Estamos juntos nisso."
            samantha "Obrigada. Isso significa muito para mim."
            jump cena4_entrega
        "Dizer que é tarde":
            narrator "Você decide não dizer nada e volta para o seu quarto."
            jump cena4_entrega

label capitulo8_quarto_nicole:
    show nicole neutral at center
    narrator "Nicole está sentada à mesa, revisando anotações e ajustando gráficos no tablet."
    nicole "Você acha que isso vai ser suficiente? Ou estamos apenas tentando evitar o inevitável?"
    menu:
        "Elogiar seu trabalho":
            $ romance_nicole = True
            "[nome]" "Seu trabalho é incrível. Você está carregando todos nós."
            nicole "Obrigada... isso significa muito para mim."
            jump cena4_entrega
        "Oferecer ajuda prática":
            $ points_nicole += 1
            "[nome]" "Deixe-me ajudar. Podemos revisar juntos."
            nicole "Obrigada. Isso vai ajudar bastante."
            jump cena4_entrega
        "Dizer que é tarde":
            narrator "Você decide não dizer nada e volta para o seu quarto."
            jump cena4_entrega

label capitulo8_quarto_huey:
    show huey gentle at center
    narrator "Huey está sentada no chão, cercada por pincéis e tintas, com um quadro inacabado à sua frente."
    huey "Eu queria que essa pintura capturasse tudo... mas parece que sempre falta algo."
    menu:
        "Elogiar sua arte":
            $ romance_huey = True
            "[nome]" "Sua arte já diz tudo. Ela é incrível, como você."
            huey "Obrigada... isso significa muito para mim."
            jump cena4_entrega
        "Oferecer inspiração":
            $ points_huey += 1
            "[nome]" "Talvez você só precise de um pouco mais de tempo. Estou aqui para ajudar."
            huey "Obrigada. Isso me ajuda a continuar."
            jump cena4_entrega
        "Dizer que é tarde":
            narrator "Você decide não dizer nada e volta para o seu quarto."
            jump cena4_entrega

label capitulo8_quarto_camille:
    show camille gentle at center
    narrator "Camille está sentada no chão, com cristais e incensos ao seu redor, os olhos fechados em meditação."
    camille "Você sente isso? A energia da casa... ela está vibrando diferente."
    menu:
        "Concordar e se conectar":
            $ romance_camille = True
            "[nome]" "Eu sinto. E acho que é porque estamos todos juntos nisso."
            camille "Obrigada. Você sempre sabe o que dizer."
            jump cena4_entrega
        "Oferecer apoio":
            $ points_camille += 1
            "[nome]" "Se precisar de algo, estou aqui. Sempre."
            camille "Obrigada. Sua presença já é suficiente."
            jump cena4_entrega
        "Dizer que é tarde":
            narrator "Você decide não dizer nada e volta para o seu quarto."
            jump cena4_entrega

label capitulo8_quarto_larissa:
    show larissa happy at center
    narrator "Larissa está fazendo alongamentos no chão, com uma garrafa d’água ao lado."
    larissa "Achei que talvez... a gente pudesse fazer flexão emocional juntos."
    menu:
        "Entrar na brincadeira":
            $ romance_larissa = True
            "[nome]" "Conta comigo. Até a última repetição."
            larissa "Sério?! Uau. Que emoção, hein? Agora só falta você me vencer na corrida."
            jump cena4_entrega
        "Elogiar sua dedicação":
            $ points_larissa += 1
            "[nome]" "Você é incrível. Sua energia é contagiante."
            larissa "Obrigada. Isso significa muito para mim."
            jump cena4_entrega
        "Dizer que é tarde":
            narrator "Você decide não dizer nada e volta para o seu quarto."
            jump cena4_entrega

label capitulo8_quarto_katia:
    show katia neutral at center
    narrator "Katia está sentada à mesa, rabiscando algo em um caderno, mas para quando você entra."
    katia "Eu... tava terminando um roteiro. Sobre uma casa. Sete moradores. Um deles... achava que ninguém notava o quanto ele se importava."
    menu:
        "Perguntar se é sobre você":
            $ romance_katia = True
            "[nome]" "Era sobre mim?"
            katia "Talvez. Ou talvez eu só tava usando o drama pra lidar com o medo."
            narrator "Katia desviou o olhar, mas havia um leve sorriso em seu rosto."
            jump cena4_entrega
        "Elogiar sua criatividade":
            $ points_katia += 1
            "[nome]" "Você é uma roteirista incrível. Isso vai ser incrível."
            katia "Hmpf. Não se ache. Mas... obrigada."
            jump cena4_entrega
        "Dizer que é tarde":
            narrator "Você decide não dizer nada e volta para o seu quarto."
            jump cena4_entrega

label cena4_entrega:
    narrator "Na manhã seguinte, a entrega é feita. O campus observa a defesa com atenção. O grupo apresenta com coração, lógica e verdade."

    show professor_wendell neutral at center
    professor_wendell "Vocês não defenderam um espaço. Defenderam uma ideia. Uma comunidade."

    # Verificar se pelo menos 3 personagens têm afinidade >= 5
    if (points_samantha >= 5) + (points_nicole >= 5) + (points_huey >= 5) + (points_camille >= 5) + (points_larissa >= 5) + (points_katia >= 5) >= 3:
        narrator "A campanha foi um sucesso. A república permanece unida."
        $ sucesso_campanha = True
    else:
        narrator "A campanha teve falhas. A universidade ainda considera a separação."
        $ sucesso_campanha = False

    jump cena_final_espera

label cena_final_espera:
    narrator "À noite, todos se reúnem na varanda da casa. O céu está limpo. As mãos se tocam por acaso. Os olhares dizem o que as palavras não conseguem."

    menu:
        "Escolher Samantha":
            jump final_samantha
        "Escolher Nicole":
            jump final_nicole
        "Escolher Huey":
            jump final_huey
        "Escolher Camille":
            jump final_camille
        "Escolher Larissa":
            jump final_larissa
        "Escolher Katia":
            jump final_katia

# Exemplo de final com Samantha
label final_samantha:
    show samantha neutral at center
    narrator "Samantha está abraçando os joelhos, olhando para o céu."
    samantha "Você... ainda quer jogar comigo? Mesmo que o cenário mude?"
    menu:
        "Sempre.":
            $ romance_samantha = True
            "[nome]" "Sempre."
            samantha "Obrigada. Você é incrível."
            jump capitulo8_conclusao
        "Não sei. Mas quero tentar.":
            $ points_samantha += 1
            "[nome]" "Não sei. Mas quero tentar."
            samantha "Isso já é o suficiente para mim."
            jump capitulo8_conclusao
        "Talvez seja hora de salvar e continuar.":
            narrator "Você decide manter as coisas como estão, sem avançar no relacionamento."
            jump capitulo8_conclusao

label final_nicole:
    show nicole neutral at center
    narrator "Nicole está sentada ao seu lado, ajustando os óculos enquanto observa o céu."
    nicole "Você acha que... mesmo com tudo isso, ainda faz sentido continuar?"
    menu:
        "Sempre. Você é incrível.":
            $ romance_nicole = True
            "[nome]" "Sempre. Você é incrível."
            nicole "Obrigada... isso significa muito para mim."
            jump capitulo8_conclusao
        "Não sei. Mas quero tentar.":
            $ points_nicole += 1
            "[nome]" "Não sei. Mas quero tentar."
            nicole "Isso já é o suficiente para mim."
            jump capitulo8_conclusao
        "Talvez seja melhor focar em outras coisas.":
            narrator "Você decide manter as coisas como estão, sem avançar no relacionamento."
            jump capitulo8_conclusao

label final_huey:
    show huey gentle at center
    narrator "Huey está ao seu lado, segurando um pequeno caderno de desenhos."
    huey "Eu ainda não terminei... mas acho que esse traço aqui é você."
    menu:
        "Quero fazer parte disso. Sempre.":
            $ romance_huey = True
            "[nome]" "Quero fazer parte disso. Sempre."
            huey "Obrigada... isso significa muito para mim."
            jump capitulo8_conclusao
        "Não sei. Mas quero tentar.":
            $ points_huey += 1
            "[nome]" "Não sei. Mas quero tentar."
            huey "Isso já é o suficiente para mim."
            jump capitulo8_conclusao
        "Talvez seja melhor deixar como está.":
            narrator "Você decide manter as coisas como estão, sem avançar no relacionamento."
            jump capitulo8_conclusao

label final_camille:
    show camille gentle at center
    narrator "Camille está sentada no chão, com um cristal na mão, olhando para o céu estrelado."
    camille "Você sente isso? A energia... ela está mudando."
    menu:
        "Eu sinto. E quero estar com você.":
            $ romance_camille = True
            "[nome]" "Eu sinto. E quero estar com você."
            camille "Obrigada. Você sempre sabe o que dizer."
            jump capitulo8_conclusao
        "Não sei. Mas quero tentar.":
            $ points_camille += 1
            "[nome]" "Não sei. Mas quero tentar."
            camille "O tempo nos guiará. Obrigada por ser honesto."
            jump capitulo8_conclusao
        "Talvez seja melhor deixar o universo decidir.":
            narrator "Você decide manter as coisas como estão, sem avançar no relacionamento."
            jump capitulo8_conclusao

label final_larissa:
    show larissa happy at center
    narrator "Larissa está ao seu lado, segurando uma garrafa d’água e sorrindo."
    larissa "Acha que amanhã a gente pode correr juntos? Ou você vai me deixar na poeira?"
    menu:
        "Sempre. Você é minha parceira.":
            $ romance_larissa = True
            "[nome]" "Sempre. Você é minha parceira."
            larissa "Sério?! Uau. Que emoção, hein? Agora só falta você me vencer na corrida."
            jump capitulo8_conclusao
        "Não sei. Mas quero tentar.":
            $ points_larissa += 1
            "[nome]" "Não sei. Mas quero tentar."
            larissa "Isso já é o suficiente para mim."
            jump capitulo8_conclusao
        "Talvez seja melhor manter as coisas como estão.":
            narrator "Você decide manter as coisas como estão, sem avançar no relacionamento."
            jump capitulo8_conclusao

label final_katia:
    show katia neutral at center
    narrator "Katia está encostada no batente da varanda, olhando para o céu com os braços cruzados."
    katia "Se você comentar que eu tô aqui, eu juro que te ignoro o resto da vida."
    menu:
        "Eu não vou comentar. Só quero estar com você.":
            $ romance_katia = True
            "[nome]" "Eu não vou comentar. Só quero estar com você."
            katia "Hmpf. Não se ache. Mas... obrigada."
            jump capitulo8_conclusao
        "Não sei. Mas quero tentar.":
            $ points_katia += 1
            "[nome]" "Não sei. Mas quero tentar."
            katia "Tá. Mas não me faça esperar muito."
            jump capitulo8_conclusao
        "Talvez seja melhor deixar como está.":
            narrator "Você decide manter as coisas como estão, sem avançar no relacionamento."
            jump capitulo8_conclusao

label capitulo8_conclusao:
    scene bg republica_noite with fade
    narrator "A noite cai sobre a república da Rua Aurora. O silêncio é preenchido por pensamentos e reflexões sobre tudo o que aconteceu nos últimos dias."

    # Retrospectiva baseada no sucesso ou falha da campanha
    if sucesso_campanha:
        narrator "A defesa foi um sucesso. A república permanece unida, e o grupo sente o peso da vitória. Cada esforço, cada palavra dita, contribuiu para esse momento."
        narrator "O reitor reconheceu não apenas o valor do espaço físico, mas também a essência da comunidade que vocês construíram juntos."
    else:
        narrator "Apesar dos esforços, a campanha não foi suficiente para garantir a permanência da república. A separação parece inevitável, e o grupo sente o peso da incerteza."
        narrator "Mesmo assim, há um sentimento de união. Vocês lutaram juntos, e isso criou laços que nem mesmo a distância pode romper."

    # Reflexão sobre as interações com os personagens
    narrator "Você reflete sobre os momentos compartilhados com os moradores da república. Cada conversa, cada escolha, parece ter deixado uma marca."

    if romance_samantha:
        narrator "Samantha mostrou seu lado mais vulnerável, e você percebeu o quanto ela valoriza sua presença. O vínculo entre vocês parece mais forte do que nunca."
    if romance_nicole:
        narrator "Nicole, com sua racionalidade e dedicação, abriu espaço para algo mais pessoal. Você sente que ela confia em você de uma forma especial."
    if romance_huey:
        narrator "Huey, com sua sensibilidade artística, compartilhou um pedaço de sua alma com você. A conexão entre vocês é profunda e inspiradora."
    if romance_camille:
        narrator "Camille, com sua espiritualidade e calma, trouxe uma nova perspectiva para sua vida. O tempo que passaram juntos parece quase mágico."
    if romance_larissa:
        narrator "Larissa, com sua energia e determinação, mostrou que você pode ser parte de sua jornada. O vínculo entre vocês é cheio de vitalidade."
    if romance_katia:
        narrator "Katia, com seu sarcasmo e profundidade, revelou um lado mais sincero. Você sente que ela confia em você de uma forma que poucos conseguem."

    # Reflexão final
    narrator "Enquanto você se deita para dormir, as memórias do capítulo ecoam em sua mente. A defesa da república foi mais do que uma luta por um espaço físico. Foi uma luta por laços, por histórias, por um lar."
    narrator "E, independentemente do resultado, você sabe que esses laços continuarão a crescer, mesmo diante das mudanças que estão por vir."

    jump capitulo9