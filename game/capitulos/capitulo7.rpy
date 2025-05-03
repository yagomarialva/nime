label capitulo7:
    scene bg republica_manha with fade
    narrator "Uma semana após o Festival das Estações, a rotina volta... mas algo mudou na república. Os olhares são mais longos, os silêncios mais densos, e as conversas carregam intenções novas."

    show camille gentle at left
    camille "Os ciclos se movem... E agora, algo está girando diferente."

    show nicole neutral at center
    nicole "É só consequência. Tudo que começa a importar, exige mais da gente."

    show samantha sad at right
    samantha "...Alguém sonhou com o grupo sendo separado também, ou só eu?"

    narrator "Você reflete sobre seu relacionamento com as garotas. Se já iniciou uma rota romântica, a relação começa a se manifestar publicamente. Se não, pequenos gestos revelam uma tensão crescente."

    jump cena2_desafios_convivencia

label cena2_desafios_convivencia:
    scene bg sala_reuniao with dissolve
    narrator "A direção da faculdade anuncia que uma repórter virá visitar a república para fazer uma matéria especial. O grupo precisa organizar a casa, montar um projeto coletivo e escolher quem vai dar entrevista."

    show nicole neutral at left
    nicole "Óbvio que alguém articulado precisa representar. Isso define nossa imagem."

    show katia neutral at center
    katia "Imagem ou autenticidade? Eu voto por não fingir."

    show camille gentle at right
    camille "Talvez devêssemos nos alinhar energeticamente antes. A repórter vai sentir o clima."

    menu:
        "Escolher Nicole":
            $ points_nicole += 1
            $ points_katia -= 1
            "[nome]" "Nicole tem razão. Precisamos de alguém articulado."
            nicole "Obrigada. Vou garantir que nossa imagem seja impecável."
            jump cena3_duvidas_crescem
        "Escolher Katia":
            $ points_katia += 1
            $ points_nicole -= 1
            "[nome]" "Katia está certa. Precisamos ser autênticos."
            katia "Finalmente alguém que entende. Vamos mostrar quem realmente somos."
            jump cena3_duvidas_crescem
        "Escolher Samantha":
            $ points_samantha += 1
            "[nome]" "Samantha pode representar bem o grupo."
            samantha "Eu? Tá bom, vou tentar não estragar tudo."
            jump cena3_duvidas_crescem
        "Escolher Camille":
            $ points_camille += 1
            "[nome]" "Camille pode trazer uma energia única para a entrevista."
            camille "Vou fazer o meu melhor para representar todos nós."
            jump cena3_duvidas_crescem
        "[nome] se oferece":
            "[nome]" "Eu posso fazer isso. Quero representar todos nós."
            narrator "O grupo concorda, e você se prepara para a entrevista."
            jump cena3_duvidas_crescem

label cena3_duvidas_crescem:
    narrator "À noite, a personagem com quem você iniciou uma relação amorosa te chama para uma conversa mais séria."

    if romance_camille:
        jump cena3_camille
    elif romance_samantha:
        jump cena3_samantha
    elif romance_nicole:
        jump cena3_nicole
    elif romance_katia:
        jump cena3_katia
    elif romance_huey:
        jump cena3_huey
    elif romance_larissa:
        jump cena3_larissa
    else:
        jump cena4_convite_externo

label cena3_camille:
    show camille gentle at center
    narrator "Camille te chama para uma conversa na sala de meditação."
    camille "É estranho. Quando estou com você, sinto que o tempo para. E isso... me dá medo."
    menu:
        "Sinto o mesmo. Mas vale a pena.":
            $ points_camille += 2
            "[nome]" "Eu sinto o mesmo. Mas acho que vale a pena."
            camille "Obrigada. Você me faz acreditar que o universo nos uniu por um motivo."
            jump cena4_convite_externo
        "Ainda estou entendendo.":
            $ points_camille += 1
            "[nome]" "Ainda estou tentando entender tudo isso."
            camille "Eu entendo. O tempo nos guiará."
            jump cena4_convite_externo
        "Não sei se é o certo agora.":
            $ points_camille -= 2
            "[nome]" "Não sei se é o certo agora."
            camille "Entendi. Talvez o universo tenha outros planos."
            jump cena4_convite_externo

label cena3_samantha:
    show samantha nervous at center
    narrator "Samantha te chama para uma conversa no sofá da sala, segurando um controle de videogame."
    samantha "Eu fico pensando... se a gente fosse personagens, você teria escolhido minha rota?"
    menu:
        "Claro, você é especial para mim.":
            $ points_samantha += 2
            "[nome]" "Claro. Você é especial para mim."
            samantha "Sério?! Isso foi tipo... um crítico de afeto. Obrigada."
            jump cena4_convite_externo
        "Ainda estou tentando entender isso.":
            $ points_samantha += 1
            "[nome]" "Ainda estou tentando entender tudo isso."
            samantha "Tudo bem. Eu posso esperar. Só não demore muito, tá?"
            jump cena4_convite_externo
        "Não sei se é o certo agora.":
            $ points_samantha -= 2
            "[nome]" "Não sei se é o certo agora."
            samantha "Ah... entendi. Tá tudo bem. Boa noite."
            jump cena4_convite_externo

label cena3_nicole:
    show nicole neutral at center
    narrator "Nicole te chama para uma conversa na cozinha, enquanto organiza uma planilha no tablet."
    nicole "Eu não sou boa com essas coisas... mas acho que preciso de uma resposta. O que você quer de nós?"
    menu:
        "Quero estar ao seu lado.":
            $ points_nicole += 2
            "[nome]" "Quero estar ao seu lado."
            nicole "Então tá. Vamos documentar isso com exclusividade."
            narrator "Nicole sorriu levemente, e o momento parecia mais importante do que qualquer cálculo."
            jump cena4_convite_externo
        "Ainda estou tentando entender isso.":
            $ points_nicole += 1
            "[nome]" "Ainda estou tentando entender tudo isso."
            nicole "Tempo é um recurso não-renovável... mas se for você, eu invisto."
            jump cena4_convite_externo
        "Não sei se é o certo agora.":
            $ points_nicole -= 2
            "[nome]" "Não sei se é o certo agora."
            nicole "Entendido. Silêncio também é uma resposta."
            narrator "Nicole ajustou os óculos e voltou ao trabalho, sem dizer mais nada."
            jump cena4_convite_externo

label cena3_katia:
    show katia neutral at center
    narrator "Katia te chama para uma conversa no corredor, encostada na parede com os braços cruzados."
    katia "Você tem esse talento estranho de... me deixar menos cínica. Não sei se gosto disso."
    menu:
        "Talvez porque eu me importo com você.":
            $ points_katia += 2
            "[nome]" "Talvez porque eu me importo com você."
            katia "Você é mais idiota do que eu pensava... mas obrigada por isso."
            narrator "Katia desviou o olhar, mas havia um leve sorriso em seu rosto."
            jump cena4_convite_externo
        "Ainda estou tentando entender isso.":
            $ points_katia += 1
            "[nome]" "Ainda estou tentando entender tudo isso."
            katia "Tá, mas não me faça esperar muito. Não sou boa com paciência."
            jump cena4_convite_externo
        "Não sei se é o certo agora.":
            $ points_katia -= 2
            "[nome]" "Não sei se é o certo agora."
            katia "Ah, claro. Esquece que eu disse qualquer coisa."
            narrator "Katia saiu, tentando esconder sua frustração."
            jump cena4_convite_externo

label cena3_huey:
    show huey gentle at center
    narrator "Huey te chama para uma conversa no jardim, segurando um pequeno caderno de desenhos."
    huey "Eu fico pensando... se eu te mostro tanto de mim, será que você vê o que eu vejo?"
    menu:
        "Eu vejo você, e é lindo.":
            $ points_huey += 2
            "[nome]" "Eu vejo você, e é lindo."
            huey "Obrigada... isso significa muito para mim."
            narrator "Huey sorriu timidamente, e o momento parecia cheio de significado."
            jump cena4_convite_externo
        "Ainda estou tentando entender isso.":
            $ points_huey += 1
            "[nome]" "Ainda estou tentando entender tudo isso."
            huey "Tudo bem. Eu espero. E continuo pintando."
            jump cena4_convite_externo
        "Não sei se é o certo agora.":
            $ points_huey -= 2
            "[nome]" "Não sei se é o certo agora."
            huey "Ah... entendi. Às vezes o silêncio também é arte."
            narrator "Huey fechou o caderno e se afastou em silêncio."
            jump cena4_convite_externo

label cena3_larissa:
    show larissa happy at center
    narrator "Larissa te chama para uma conversa na sala de treino, segurando uma garrafa d’água."
    larissa "Eu não sou boa com palavras, mas... acho que você me faz querer tentar."
    menu:
        "Eu sinto o mesmo por você.":
            $ points_larissa += 2
            "[nome]" "Eu sinto o mesmo por você."
            larissa "Sério?! Uau. Que emoção, hein? Agora só falta você me vencer na corrida."
            narrator "Larissa riu, mas havia algo mais profundo em seu olhar."
            jump cena4_convite_externo
        "Ainda estou tentando entender isso.":
            $ points_larissa += 1
            "[nome]" "Ainda estou tentando entender tudo isso."
            larissa "Tranquilo. A gente fortalece a amizade nos alongamentos."
            jump cena4_convite_externo
        "Não sei se é o certo agora.":
            $ points_larissa -= 2
            "[nome]" "Não sei se é o certo agora."
            larissa "Beleza. Valeu aí."
            narrator "Larissa deu uma risada forçada e voltou ao treino."
            jump cena4_convite_externo

label cena4_convite_externo:
    narrator "Um ex da [personagem_evento] aparece na universidade. Ele(a) está participando de um evento na cidade e convida todos… especialmente ela."

    if personagem_evento == "camille":
        jump convite_camille
    elif personagem_evento == "samantha":
        jump convite_samantha
    elif personagem_evento == "nicole":
        jump convite_nicole
    elif personagem_evento == "katia":
        jump convite_katia
    elif personagem_evento == "huey":
        jump convite_huey
    elif personagem_evento == "larissa":
        jump convite_larissa

label convite_camille:
    show camille gentle at center
    narrator "Camille parece hesitante ao receber o convite."
    camille "O universo testa a frequência quando ela está mais instável."
    menu:
        "Confiar e apoiar":
            $ points_camille += 2
            "[nome]" "Eu confio em você. Vá e aproveite o momento."
            camille "Obrigada. Sua confiança significa muito para mim."
            jump cena5_domingo_para_dois
        "Dizer que se sente desconfortável":
            "[nome]" "Não sei... isso me deixa desconfortável."
            camille "Eu entendo. Vou pensar bem antes de decidir."
            jump cena5_domingo_para_dois
        "Se mostrar indiferente":
            $ points_camille -= 2
            "[nome]" "Faça o que quiser. Não importa para mim."
            camille "Entendi. Obrigada pela sinceridade."
            jump cena5_domingo_para_dois

label convite_samantha:
    show samantha nervous at center
    narrator "Samantha parece surpresa ao receber o convite, mas tenta disfarçar."
    samantha "Ah, claro... ele(a) sempre aparece nos momentos mais aleatórios."
    menu:
        "Confiar e apoiar":
            $ points_samantha += 2
            "[nome]" "Eu confio em você. Vá e aproveite o momento."
            samantha "Obrigada. Você é incrível, sabia?"
            jump cena5_domingo_para_dois
        "Dizer que se sente desconfortável":
            "[nome]" "Não sei... isso me deixa desconfortável."
            samantha "Entendi. Vou pensar bem antes de decidir."
            jump cena5_domingo_para_dois
        "Se mostrar indiferente":
            $ points_samantha -= 2
            "[nome]" "Faça o que quiser. Não importa para mim."
            samantha "Ah... tá. Valeu pela sinceridade, eu acho."
            jump cena5_domingo_para_dois

label convite_nicole:
    show nicole neutral at center
    narrator "Nicole ajusta os óculos ao receber o convite, tentando esconder qualquer reação."
    nicole "Isso é... inesperado. Mas não impossível de gerenciar."
    menu:
        "Confiar e apoiar":
            $ points_nicole += 2
            "[nome]" "Eu confio em você. Vá e aproveite o momento."
            nicole "Obrigada. Sua confiança é... apreciada."
            jump cena5_domingo_para_dois
        "Dizer que se sente desconfortável":
            "[nome]" "Não sei... isso me deixa desconfortável."
            nicole "Entendido. Vou considerar isso antes de decidir."
            jump cena5_domingo_para_dois
        "Se mostrar indiferente":
            $ points_nicole -= 2
            "[nome]" "Faça o que quiser. Não importa para mim."
            nicole "Entendido. Obrigada pela clareza."
            jump cena5_domingo_para_dois

label convite_katia:
    show katia neutral at center
    narrator "Katia revira os olhos ao receber o convite, mas há algo em seu tom que sugere hesitação."
    katia "Claro que ele(a) aparece agora. É tão típico."
    menu:
        "Confiar e apoiar":
            $ points_katia += 2
            "[nome]" "Eu confio em você. Vá e aproveite o momento."
            katia "Hmpf. Obrigada, eu acho."
            jump cena5_domingo_para_dois
        "Dizer que se sente desconfortável":
            "[nome]" "Não sei... isso me deixa desconfortável."
            katia "Tá, entendi. Vou pensar antes de decidir."
            jump cena5_domingo_para_dois
        "Se mostrar indiferente":
            $ points_katia -= 2
            "[nome]" "Faça o que quiser. Não importa para mim."
            katia "Ah, claro. Valeu pela sinceridade."
            jump cena5_domingo_para_dois

label convite_huey:
    show huey gentle at center
    narrator "Huey segura o convite com cuidado, como se fosse algo frágil."
    huey "Eu não esperava isso... mas talvez seja uma oportunidade."
    menu:
        "Confiar e apoiar":
            $ points_huey += 2
            "[nome]" "Eu confio em você. Vá e aproveite o momento."
            huey "Obrigada. Isso significa muito para mim."
            jump cena5_domingo_para_dois
        "Dizer que se sente desconfortável":
            "[nome]" "Não sei... isso me deixa desconfortável."
            huey "Entendi. Vou pensar bem antes de decidir."
            jump cena5_domingo_para_dois
        "Se mostrar indiferente":
            $ points_huey -= 2
            "[nome]" "Faça o que quiser. Não importa para mim."
            huey "Ah... tá. Obrigada pela sinceridade."
            jump cena5_domingo_para_dois

label convite_larissa:
    show larissa happy at center
    narrator "Larissa ri ao receber o convite, mas há algo em seu olhar que sugere incerteza."
    larissa "Ele(a) sempre aparece nos momentos mais aleatórios. É quase engraçado."
    menu:
        "Confiar e apoiar":
            $ points_larissa += 2
            "[nome]" "Eu confio em você. Vá e aproveite o momento."
            larissa "Obrigada. Você é incrível, sabia?"
            jump cena5_domingo_para_dois
        "Dizer que se sente desconfortável":
            "[nome]" "Não sei... isso me deixa desconfortável."
            larissa "Entendi. Vou pensar bem antes de decidir."
            jump cena5_domingo_para_dois
        "Se mostrar indiferente":
            $ points_larissa -= 2
            "[nome]" "Faça o que quiser. Não importa para mim."
            larissa "Ah... tá. Valeu pela sinceridade, eu acho."
            jump cena5_domingo_para_dois

label cena5_domingo_para_dois:
    narrator "Por acaso ou destino, você e [personagem_evento] acabam ficando sozinhos em casa por um dia. A energia muda."

    if personagem_evento == "camille":
        jump domingo_camille
    elif personagem_evento == "samantha":
        jump domingo_samantha
    elif personagem_evento == "nicole":
        jump domingo_nicole
    elif personagem_evento == "katia":
        jump domingo_katia
    elif personagem_evento == "huey":
        jump domingo_huey
    elif personagem_evento == "larissa":
        jump domingo_larissa

label domingo_camille:
    show camille gentle at center
    narrator "Você e Camille passam o dia meditando e conversando sobre o universo."
    camille "Sabe... às vezes, sinto que o tempo para quando estamos juntos."
    menu:
        "Concordar e se aproximar":
            $ romance_camille = True
            "[nome]" "Eu sinto o mesmo. É como se o universo conspirasse a nosso favor."
            camille "Talvez ele esteja. Obrigada por estar aqui."
            narrator "Vocês compartilham um momento de conexão profunda."
            jump cena_final_escolha_silenciosa
        "Ficar em silêncio":
            "[nome]" "..."
            narrator "Camille observa você em silêncio, mas o momento parece incompleto."
            jump cena_final_escolha_silenciosa

label domingo_samantha:
    show samantha nervous at center
    narrator "Você e Samantha passam o dia jogando videogame e conversando sobre estratégias."
    samantha "Sabe... às vezes, parece que você é meu player dois na vida real."
    menu:
        "Concordar e se aproximar":
            $ romance_samantha = True
            "[nome]" "E você é minha melhor aliada. Sempre."
            samantha "Sério?! Isso foi tipo... um crítico de afeto. Obrigada."
            narrator "Vocês compartilham um momento de conexão especial, como se fossem uma dupla imbatível."
            jump cena_final_escolha_silenciosa
        "Ficar em silêncio":
            "[nome]" "..."
            narrator "Samantha olha para você, esperando uma resposta, mas volta a focar no jogo."
            jump cena_final_escolha_silenciosa

label domingo_nicole:
    show nicole neutral at center
    narrator "Você e Nicole passam o dia organizando a casa e discutindo ideias para projetos futuros."
    nicole "Sabe... trabalhar com você é eficiente. Mas também... confortável."
    menu:
        "Concordar e se aproximar":
            $ romance_nicole = True
            "[nome]" "Eu sinto o mesmo. Trabalhar com você é sempre especial."
            nicole "Então tá. Vamos documentar isso como um momento único."
            narrator "Nicole sorriu levemente, e o momento parecia mais importante do que qualquer planilha."
            jump cena_final_escolha_silenciosa
        "Ficar em silêncio":
            "[nome]" "..."
            narrator "Nicole ajusta os óculos e volta a trabalhar, mas o silêncio entre vocês pareceu estranho."
            jump cena_final_escolha_silenciosa

label domingo_katia:
    show katia neutral at center
    narrator "Você e Katia passam o dia assistindo a filmes antigos e discutindo sobre eles."
    katia "Sabe... você é a única pessoa com quem eu consigo assistir isso sem me irritar."
    menu:
        "Concordar e se aproximar":
            $ romance_katia = True
            "[nome]" "Talvez porque eu gosto de estar com você, mesmo que você finja que não gosta."
            katia "Hmpf. Não se ache. Mas... obrigada."
            narrator "Katia desviou o olhar, mas havia um leve sorriso em seu rosto."
            jump cena_final_escolha_silenciosa
        "Ficar em silêncio":
            "[nome]" "..."
            narrator "Katia olha para você, esperando uma resposta, mas finge que não se importa."
            jump cena_final_escolha_silenciosa

label domingo_huey:
    show huey gentle at center
    narrator "Você e Huey passam o dia pintando juntos e conversando sobre arte."
    huey "Sabe... quando você está aqui, as cores parecem mais vivas."
    menu:
        "Concordar e se aproximar":
            $ romance_huey = True
            "[nome]" "Talvez porque você me inspira a ver o mundo de um jeito diferente."
            huey "Obrigada... isso significa muito para mim."
            narrator "Huey sorriu timidamente, e o momento parecia cheio de significado."
            jump cena_final_escolha_silenciosa
        "Ficar em silêncio":
            "[nome]" "..."
            narrator "Huey olha para você, mas volta a focar na pintura, como se algo tivesse ficado por dizer."
            jump cena_final_escolha_silenciosa

label domingo_larissa:
    show larissa happy at center
    narrator "Você e Larissa passam o dia treinando juntos e conversando sobre metas."
    larissa "Sabe... você é a única pessoa que eu deixo me acompanhar no treino."
    menu:
        "Concordar e se aproximar":
            $ romance_larissa = True
            "[nome]" "Talvez porque eu quero estar ao seu lado, em qualquer ritmo."
            larissa "Sério?! Uau. Que emoção, hein? Agora só falta você me vencer na corrida."
            narrator "Larissa riu, mas havia algo mais profundo em seu olhar."
            jump cena_final_escolha_silenciosa
        "Ficar em silêncio":
            "[nome]" "..."
            narrator "Larissa olha para você, esperando uma resposta, mas volta a focar no treino."
            jump cena_final_escolha_silenciosa

label cena_final_escolha_silenciosa:
    narrator "Antes de dormir, o protagonista recebe uma mensagem de texto. Só uma frase, de [personagem_evento]"

    if personagem_evento == "camille":
        "[nome]" "Você sente quando alguém pensa em você à distância?"
    elif personagem_evento == "samantha":
        "[nome]" "Acabei de perder um boss... mas acho que ganhei uma mensagem importante."
    elif personagem_evento == "nicole":
        "[nome]" "A planilha ficou incompleta. Faltava você."
    elif personagem_evento == "katia":
        "[nome]" "Apaguei e reescrevi essa mensagem quatro vezes. Então... boa noite, idiota."
    elif personagem_evento == "huey":
        "[nome]" "Amanhã eu vou te mostrar a pintura. Só se você prometer não rir."
    elif personagem_evento == "larissa":
        "[nome]" "Se amanhã você quiser correr... me espera, tá?"

    menu:
        "Responder de forma afetuosa":
            narrator "Você responde com carinho, e a conexão entre vocês parece crescer ainda mais."
            jump cena_extra_madrugada
        "Responder com emoji simples":
            narrator "Você responde com um emoji simples. A mensagem é recebida, mas sem muito impacto."
            jump cena_extra_madrugada
        "Não responder":
            $ points[personagem_evento] -= 1
            narrator "Você decide não responder. A personagem parece distante no dia seguinte."
            jump cena_extra_madrugada

label cena_extra_madrugada:
    narrator "Mais tarde, no silêncio da madrugada, o som de uma leve batida na porta ecoa pelo quarto. Uma das garotas aparece, com olhos sinceros."

    if personagem_evento == "camille":
        jump madrugada_camille
    elif personagem_evento == "samantha":
        jump madrugada_samantha
    elif personagem_evento == "nicole":
        jump madrugada_nicole
    elif personagem_evento == "katia":
        jump madrugada_katia
    elif personagem_evento == "huey":
        jump madrugada_huey
    elif personagem_evento == "larissa":
        jump madrugada_larissa

label madrugada_camille:
    show camille neutral at center
    narrator "Camille entra no quarto, sentando no chão e acendendo um incenso discretamente."
    camille "Eu queria que esse momento durasse mais do que uma vida."
    menu:
        "Talvez a gente possa criar esse momento de novo. Sempre.":
            $ romance_camille = True
            "[nome]" "Talvez a gente possa criar esse momento de novo. Sempre."
            camille "Eu adoraria. Obrigada por me deixar fazer parte disso."
            narrator "Camille sorriu suavemente, e o momento parecia cheio de significado."
            jump capitulo7_cliffhanger

label madrugada_samantha:
    show samantha neutral at center
    narrator "Samantha aparece carregando dois controles de videogame, com um sorriso tímido."
    samantha "Se tudo mudar... posso salvar a gente num slot diferente?"
    menu:
        "Prefiro jogar nesse aqui, com você.":
            $ romance_samantha = True
            "[nome]" "Prefiro jogar nesse aqui, com você."
            samantha "Sério?! Isso foi tipo... um crítico de afeto. Obrigada."
            narrator "Vocês compartilham um momento doce e envolvente, como se fossem uma dupla imbatível."
            jump capitulo7_cliffhanger

label madrugada_nicole:
    show nicole neutral at center
    narrator "Nicole entra no quarto e senta à beira da cama, sua voz controlada, mas os olhos revelando algo mais."
    nicole "Você parece tranquilo... enquanto tudo ao nosso redor muda. Como faz isso?"
    menu:
        "Você me faz querer ficar.":
            $ romance_nicole = True
            "[nome]" "Você me faz querer ficar."
            nicole "Então tá. Vamos documentar isso como um momento único."
            narrator "Nicole sorriu levemente, e o momento parecia mais importante do que qualquer planilha."
            jump capitulo7_cliffhanger

label madrugada_katia:
    show katia neutral at center
    narrator "Katia aparece encostada no batente da porta, de braços cruzados, tentando parecer indiferente."
    katia "Se você comentar que eu bati aqui, eu juro que te ignoro o resto da vida."
    menu:
        "Então entra. Eu não falo... só ouço.":
            $ romance_katia = True
            "[nome]" "Então entra. Eu não falo... só ouço."
            katia "Hmpf. Não se ache. Mas... obrigada."
            narrator "Katia desviou o olhar, mas havia um leve sorriso em seu rosto."
            jump capitulo7_cliffhanger

label madrugada_huey:
    show huey neutral at center
    narrator "Huey entra no quarto segurando um croqui inacabado, com traços que parecem familiares."
    huey "Ainda tô desenhando... mas acho que já é você aqui, nesse traço."
    menu:
        "Quero ver você terminar. Comigo aqui.":
            $ romance_huey = True
            "[nome]" "Quero ver você terminar. Comigo aqui."
            huey "Obrigada... isso significa muito para mim."
            narrator "Huey sorriu timidamente, e o momento parecia cheio de significado."
            jump capitulo7_cliffhanger

label madrugada_larissa:
    show larissa neutral at center
    narrator "Larissa aparece segurando uma toalha, recém-saída do banho, com um sorriso brincalhão."
    larissa "Achei que talvez… a gente pudesse fazer flexão emocional juntos."
    larissa "(risos baixos)"
    menu:
        "Conta comigo. Até a última repetição.":
            $ romance_larissa = True
            "[nome]" "Conta comigo. Até a última repetição."
            larissa "Sério?! Uau. Que emoção, hein? Agora só falta você me vencer na corrida."
            narrator "Larissa riu, mas havia algo mais profundo em seu olhar."
            jump capitulo7_cliffhanger

label capitulo7_cliffhanger:
    scene bg republica_noite with fade
    narrator "No final da noite, uma carta da administração da universidade chega... anunciando mudanças inesperadas no programa de moradia da república."

    show nicole angry at center
    nicole "O quê?! Estão planejando redistribuir os moradores em novas casas no semestre seguinte..."

    show camille shocked at left
    camille "O universo está mudando os ventos..."

    narrator "Todos se olham em silêncio, pensando: 'Será que este é nosso último semestre juntos?'"
    jump capitulo8