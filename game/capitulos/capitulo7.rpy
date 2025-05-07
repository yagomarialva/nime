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

    narrator "Após uma breve discussão, o grupo decide que a pessoa mais adequada para representar a república será escolhida com base em quem tem mais afinidade com o grupo."

    # Verifica quem tem mais afinidade
    if points_nicole >= max(points_katia, points_samantha, points_camille, points_huey, points_larissa):
        "[nome]" "Nicole tem razão. Precisamos de alguém articulado."
        nicole "Obrigada. Vou garantir que nossa imagem seja impecável."
        jump cena3_duvidas_crescem
    elif points_katia >= max(points_nicole, points_samantha, points_camille, points_huey, points_larissa):
        "[nome]" "Katia está certa. Precisamos ser autênticos."
        katia "Finalmente alguém que entende. Vamos mostrar quem realmente somos."
        jump cena3_duvidas_crescem
    elif points_samantha >= max(points_nicole, points_katia, points_camille, points_huey, points_larissa):
        "[nome]" "Samantha pode representar bem o grupo."
        samantha "Eu? Tá bom, vou tentar não estragar tudo."
        jump cena3_duvidas_crescem
    elif points_camille >= max(points_nicole, points_katia, points_samantha, points_huey, points_larissa):
        "[nome]" "Camille pode trazer uma energia única para a entrevista."
        camille "Vou fazer o meu melhor para representar todos nós."
        jump cena3_duvidas_crescem
    elif points_huey >= max(points_nicole, points_katia, points_samantha, points_camille, points_larissa):
        "[nome]" "Huey pode trazer uma perspectiva artística e sensível para a entrevista."
        huey "Obrigado. Vou tentar capturar a essência do que somos."
        jump cena3_duvidas_crescem
    elif points_larissa >= max(points_nicole, points_katia, points_samantha, points_camille, points_huey):
        "[nome]" "Larissa pode trazer uma energia vibrante e dinâmica para a entrevista."
        larissa "Sério? Beleza, vou dar o meu melhor!"
        jump cena3_duvidas_crescem
    else:
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
            $ points_camille -= 1
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
    narrator "Um ex da [personagem_evento] aparece na universidade. Ele está participando de um evento na cidade e convida todos… especialmente ela."

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
    narrator "Ela decide ir ao evento, onde seu ex está apresentando uma palestra sobre espiritualidade e conexões humanas. Você decide acompanhá-la para apoiá-la."

    scene bg evento_camille with fade
    narrator "No evento, Camille ouve atentamente enquanto seu ex fala sobre como as energias das pessoas se conectam e se separam ao longo do tempo. Após a palestra, ele se aproxima dela."
    show ex_camille neutral at center
    ex_camille "Camille, é bom te ver. Espero que você ainda acredite que nossas almas estavam destinadas a se encontrar."
    show camille gentle at center
    camille "Talvez estivessem. Mas algumas conexões são feitas para ensinar, não para durar."
    narrator "Camille olha para você, seus olhos brilhando com uma nova certeza."
    camille "[nome], você me mostrou que algumas conexões são mais profundas porque são reais, não porque são idealizadas."
    menu:
        "Segurar a mão dela":
            $ romance_camille = True
            "[nome]" "E eu quero que a nossa conexão continue crescendo."
            camille "Obrigada. Você é a energia que eu quero ao meu lado."
            narrator "Camille sorri suavemente, e o momento entre vocês parece eterno."
            jump cena5_domingo_para_dois
        "Apenas sorrir":
            "[nome]" "..."
            narrator "Camille entende o que você sente, mesmo sem palavras. Ela segura sua mão por um momento antes de voltar ao evento."
            jump cena5_domingo_para_dois

label convite_samantha:
    show samantha nervous at center
    narrator "Samantha parece surpresa ao receber o convite, mas tenta disfarçar."
    samantha "Ah, claro... ele sempre aparece nos momentos mais aleatórios."
    narrator "No evento, seu ex está organizando um campeonato de videogame. Samantha decide participar, e você a acompanha para torcer por ela."

    scene bg evento_samantha with fade
    narrator "Samantha joga com intensidade, derrotando vários oponentes até chegar à final. Seu ex, que também está competindo, a enfrenta na última partida."
    show ex_samantha smug at center
    ex_samantha "Você sempre foi boa, Sam. Mas será que consegue me vencer agora?"
    show samantha determined at center
    samantha "Eu não preciso provar nada para você. Mas vou ganhar, só para deixar claro."
    narrator "Samantha vence a partida com uma jogada brilhante. Após o jogo, ela se aproxima de você, ainda segurando o controle."
    samantha "[nome], você é a única pessoa que me faz sentir que sou mais do que uma jogadora. Com você, eu sou eu mesma."
    menu:
        "Abraçá-la":
            $ romance_samantha = True
            "[nome]" "E você é a pessoa que eu quero ao meu lado, em qualquer jogo."
            samantha "Sério?! Isso foi tipo... um crítico de afeto. Obrigada por me escolher."
            narrator "Samantha sorri, e vocês compartilham um momento de pura conexão."
            jump cena5_domingo_para_dois
        "Dar um sorriso de apoio":
            "[nome]" "..."
            narrator "Samantha entende o que você sente e sorri de volta, mas o momento parece incompleto."
            jump cena5_domingo_para_dois

label convite_nicole:
    show nicole neutral at center
    narrator "Nicole ajusta os óculos ao receber o convite, tentando esconder qualquer reação."
    nicole "Isso é... inesperado. Mas não impossível de gerenciar."
    narrator "No evento, seu ex está apresentando um projeto de tecnologia inovadora. Nicole decide ir para avaliar o trabalho, e você a acompanha."

    scene bg evento_nicole with fade
    narrator "Nicole observa atentamente enquanto seu ex apresenta gráficos e estatísticas. Após a apresentação, ele se aproxima dela."
    show ex_nicole confident at center
    ex_nicole "Nicole, você sempre foi a mente mais brilhante que conheci. Espero que ainda pense em mim quando vê algo bem organizado."
    show nicole neutral at center
    nicole "Eu penso em eficiência, não em nostalgia. E, sinceramente, já encontrei alguém que entende isso melhor do que você."
    narrator "Nicole olha para você, ajustando os óculos com um leve sorriso."
    nicole "[nome], você é a única variável que faz minha equação funcionar."
    menu:
        "Segurar sua mão":
            $ romance_nicole = True
            "[nome]" "E eu quero continuar sendo parte da sua equação."
            nicole "Então tá. Vamos documentar isso como um momento único."
            narrator "Nicole sorri levemente, e o momento parece mais importante do que qualquer cálculo."
            jump cena5_domingo_para_dois
        "Apenas sorrir":
            "[nome]" "..."
            narrator "Nicole entende o que você sente, mas volta a focar no evento, como se algo tivesse ficado por dizer."
            jump cena5_domingo_para_dois

label convite_katia:
    show katia neutral at center
    narrator "Katia revira os olhos ao receber o convite, mas há algo em seu tom que sugere hesitação."
    katia "Claro que ele aparece agora. É tão típico."
    narrator "No evento, seu ex está exibindo um curta-metragem que dirigiu. Katia decide ir para criticar, e você a acompanha."

    scene bg evento_katia with fade
    narrator "Katia assiste ao curta com atenção, mas seu olhar crítico é evidente. Após a exibição, seu ex se aproxima dela."
    show ex_katia smug at center
    ex_katia "Então, o que achou? Ainda acha que eu não sei contar histórias?"
    show katia neutral at center
    katia "Você melhorou. Mas ainda falta algo... talvez autenticidade."
    narrator "Katia olha para você, seus olhos suavizando por um momento."
    katia "[nome], você é a única pessoa que me faz acreditar que histórias podem ser reais."
    menu:
        "Concordar com ela":
            $ romance_katia = True
            "[nome]" "E eu quero continuar escrevendo essa história com você."
            katia "Hmpf. Não se ache. Mas... obrigada por isso."
            narrator "Katia desvia o olhar, mas há um leve sorriso em seu rosto."
            jump cena5_domingo_para_dois
        "Ficar em silêncio":
            "[nome]" "..."
            narrator "Katia finge que não se importa, mas o momento parece incompleto."
            jump cena5_domingo_para_dois

label convite_huey:
    show huey gentle at center
    narrator "Huey segura o convite com cuidado, como se fosse algo frágil."
    huey "Eu não esperava isso... mas talvez seja uma oportunidade."
    narrator "No evento, seu ex está exibindo uma galeria de arte com obras que exploram emoções humanas. Huey decide ir para ver as obras, e você o acompanha."

    scene bg evento_huey with fade
    narrator "Huey observa as pinturas com atenção, seus olhos capturando cada detalhe. Após um tempo, seu ex se aproxima dele."
    show ex_huey confident at center
    ex_huey "Huey, você sempre teve um olhar único. Espero que ainda veja algo especial nas minhas obras."
    show huey gentle at center
    huey "Elas são boas. Mas acho que o que vejo agora é diferente... porque encontrei algo mais verdadeiro."
    narrator "Huey olha para você, seus olhos cheios de emoção."
    huey "[nome], você é a inspiração que eu nunca soube que precisava."
    menu:
        "Segurar sua mão":
            $ romance_huey = True
            "[nome]" "E você é a arte mais bonita que eu já vi."
            huey "Obrigada... isso significa muito para mim."
            narrator "Huey sorri timidamente, e o momento entre vocês parece cheio de significado."
            jump cena5_domingo_para_dois
        "Apenas sorrir":
            "[nome]" "..."
            narrator "Huey entende o que você sente, mas volta a observar as pinturas, como se algo tivesse ficado por dizer."
            jump cena5_domingo_para_dois

label convite_larissa:
    show larissa happy at center
    narrator "Larissa ri ao receber o convite, mas há algo em seu olhar que sugere incerteza."
    larissa "Ele sempre aparece nos momentos mais aleatórios. É quase engraçado."
    narrator "No evento, seu ex está organizando uma competição de atletismo. Larissa decide participar, e você a acompanha para torcer por ela."

    scene bg evento_larissa with fade
    narrator "Larissa corre com determinação, superando cada obstáculo com facilidade. Na linha de chegada, seu ex a parabeniza."
    show ex_larissa smug at center
    ex_larissa "Você ainda é incrível, Larissa. Mas será que ainda tem espaço para mim na sua vida?"
    show larissa happy at center
    larissa "Eu sou incrível porque aprendi a correr para frente, não para trás."
    narrator "Larissa olha para você, seu sorriso cheio de energia e sinceridade."
    larissa "[nome], você é a única pessoa que eu quero ao meu lado, em qualquer corrida."
    menu:
        "Abraçá-la":
            $ romance_larissa = True
            "[nome]" "E eu quero correr ao seu lado, em qualquer ritmo."
            larissa "Sério?! Uau. Que emoção, hein? Agora só falta você me vencer na corrida."
            narrator "Larissa ri, mas há algo mais profundo em seu olhar."
            jump cena5_domingo_para_dois
        "Dar um sorriso de apoio":
            "[nome]" "..."
            narrator "Larissa entende o que você sente e sorri de volta, mas o momento parece incompleto."
            jump cena5_domingo_para_dois

label cena5_domingo_para_dois:
    narrator "Por acaso ou destino, você e [personagem_evento] acabam ficando sozinhos em casa por um dia. A energia muda."

    if romance_camille:
        jump domingo_camille
    elif romance_samantha:
        jump domingo_samantha
    elif romance_nicole:
        jump domingo_nicole
    elif romance_katia:
        jump domingo_katia
    elif romance_huey:
        jump domingo_huey
    elif romance_larissa:
        jump domingo_larissa
    else:
        narrator "Algo deu errado. Nenhum romance está ativo."
        return

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