label capitulo8:
    if "capitulo8" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo8")
    
    scene bg republica_noite with fade
    narrator "Três dias se passaram desde a notificação da universidade. A república da Rua Aurora fervilha de ideias, reuniões e noites mal dormidas. O prazo final para apresentar a defesa está próximo."
    
    # Momento emocional de urgência
    call emotional_moment("final_defense_preparation", None, "Preparação final para a defesa da república") from _call_emotional_moment_cap8_1
    
    narrator "Era o momento decisivo. Tudo o que havíamos construído juntos seria testado em uma única apresentação."

    show nicole neutral at left
    nicole "Temos 48 horas para enviar um documento oficial com o pedido de permanência. E não vamos conseguir sem trabalho sério."
    nicole "Mas também precisamos mostrar que somos mais que números. Somos uma família."
    $ add_affinity_points("nicole", 3, "Liderança na defesa da república")
    hide nicole

    show camille neutral at center
    camille "Mas também não sem verdade emocional. Precisamos que eles sintam."
    camille "A energia desta casa é única. Ela precisa ser sentida, não apenas explicada."
    $ add_affinity_points("camille", 3, "Conexão espiritual com a defesa")
    hide camille

    show katia neutral at right
    katia "A universidade quer números? Vamos dar emoção crua em imagens. Tipo um soco narrativo."
    katia "N-não é como se eu me importasse com o que pensam ou qualquer coisa assim! É só que... esta casa é especial."
    $ add_affinity_points("katia", 3, "Paixão pela defesa da república")
    hide katia

    show huey neutral at left
    huey "A arte vive aqui. Nos nossos pratos, nas paredes, nos gestos. Isso... tem que ser visto."
    huey "Cada pincelada, cada riso, cada momento compartilhado... tudo isso é arte."
    $ add_affinity_points("huey", 3, "Visão artística da defesa")
    hide huey

    show samantha neutral at center
    samantha "Já montei as cenas da rotina. Vai parecer um slice of life real."
    samantha "Mas também quero mostrar como cada um de nós contribui para essa história."
    $ add_affinity_points("samantha", 3, "Criatividade na defesa")
    hide samantha

    show larissa happy at right
    larissa "Se eu tiver que correr até o reitor e fazer uma pirueta, eu faço!"
    larissa "Esta casa é nossa família. Vou lutar por ela com tudo que tenho."
    $ add_affinity_points("larissa", 3, "Determinação na defesa")
    hide larissa

    menu:
        "Vídeo emocional (Huey, Camille, Samantha)":
            $ add_shared_memory("defense_strategy_emotional", ["huey", "camille", "samantha"], "Estratégia de defesa emocional escolhida")
            $ add_affinity_points("huey", 6, "Estratégia de defesa emocional")
            $ add_affinity_points("camille", 6, "Estratégia de defesa emocional")
            $ add_affinity_points("samantha", 6, "Estratégia de defesa emocional")
            narrator "O grupo decide criar um vídeo emocional que capture a essência da república."
            jump cena2_divisao_tarefas
        "Dossiê produtivo e acadêmico (Nicole, Katia)":
            $ add_shared_memory("defense_strategy_academic", ["nicole", "katia"], "Estratégia de defesa acadêmica escolhida")
            $ add_affinity_points("nicole", 6, "Estratégia de defesa acadêmica")
            $ add_affinity_points("katia", 6, "Estratégia de defesa acadêmica")
            narrator "O grupo decide criar um dossiê detalhado e acadêmico para impressionar a universidade."
            jump cena2_divisao_tarefas
        "Apresentação esportiva e cotidiana (Larissa, Samantha, Huey)":
            $ add_shared_memory("defense_strategy_sports", ["larissa", "samantha", "huey"], "Estratégia de defesa esportiva escolhida")
            $ add_affinity_points("larissa", 6, "Estratégia de defesa esportiva")
            $ add_affinity_points("samantha", 6, "Estratégia de defesa esportiva")
            $ add_affinity_points("huey", 6, "Estratégia de defesa esportiva")
            narrator "O grupo decide criar uma apresentação que mostre a rotina e o espírito esportivo da república."
            jump cena2_divisao_tarefas
        "Defesa ao vivo, interativa (Nicole, Camille, Protagonista)":
            $ add_shared_memory("defense_strategy_interactive", ["nicole", "camille"], "Estratégia de defesa interativa escolhida")
            $ add_affinity_points("nicole", 6, "Estratégia de defesa interativa")
            $ add_affinity_points("camille", 6, "Estratégia de defesa interativa")
            narrator "O grupo decide fazer uma defesa ao vivo, interativa, para engajar a audiência."
            jump cena2_divisao_tarefas

label cena2_divisao_tarefas:
    narrator "Com a escolha feita, os moradores se dividem em grupos. O protagonista pode escolher com quem deseja trabalhar para preparar uma parte essencial."
    
    # Momento emocional de colaboração
    call emotional_moment("collaborative_work", None, "Trabalho colaborativo para a defesa da república") from _call_emotional_moment_cap8_2
    
    narrator "Era um momento de união, onde cada pessoa contribuía com seus talentos únicos para um objetivo comum."

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
            $ add_shared_memory("partnership_nicole", ["nicole"], "Parceria com Nicole na defesa")
            $ add_affinity_points("nicole", 4, "Apoio racional na parceria")
            "[nome]" "Claro. Vamos focar nos detalhes técnicos."
            nicole "Obrigada. Isso vai ajudar muito."
            jump cena3_ultima_noite
        "Elogiar seu esforço":
            $ add_shared_memory("partnership_nicole", ["nicole"], "Parceria com Nicole na defesa")
            $ add_affinity_points("nicole", 6, "Elogio sincero na parceria")
            "[nome]" "Você está fazendo um trabalho incrível. Estou impressionado."
            nicole "Obrigada... isso significa muito para mim."
            jump cena3_ultima_noite
        "Fazer piada":
            $ add_shared_memory("partnership_nicole", ["nicole"], "Parceria com Nicole na defesa")
            $ add_affinity_points("nicole", 2, "Piada inadequada na parceria")
            "[nome]" "Você está levando isso muito a sério. Relaxa um pouco."
            nicole "Não é hora para piadas. Precisamos ser sérios."
            jump cena3_ultima_noite

label parceria_samantha:
    show samantha neutral at center
    narrator "Samantha está sentada no sofá, com um controle de videogame na mão e anotações espalhadas ao redor."
    samantha "Eu tô tentando montar isso como se fosse um jogo... mas parece que o boss final é impossível."
    menu:
        "Ajudar com estratégias práticas":
            $ add_shared_memory("partnership_samantha", ["samantha"], "Parceria com Samantha na defesa")
            $ add_affinity_points("samantha", 4, "Ajuda estratégica na parceria")
            "[nome]" "Talvez se você dividir o problema em partes menores, fique mais fácil."
            samantha "Boa ideia! Obrigada, player dois."
            jump cena3_ultima_noite
        "Elogiar sua criatividade":
            $ add_shared_memory("partnership_samantha", ["samantha"], "Parceria com Samantha na defesa")
            $ add_affinity_points("samantha", 6, "Elogio à criatividade na parceria")
            "[nome]" "Você é incrível. Transformar isso em um jogo é genial."
            samantha "Sério?! Isso foi tipo... um crítico de afeto. Obrigada."
            jump cena3_ultima_noite
        "Fazer piada":
            $ add_shared_memory("partnership_samantha", ["samantha"], "Parceria com Samantha na defesa")
            $ add_affinity_points("samantha", 2, "Piada inadequada na parceria")
            "[nome]" "Talvez você só precise de um cheat code."
            samantha "Haha... engraçado. Mas isso não ajuda muito."
            jump cena3_ultima_noite

label parceria_huey:
    show huey gentle at center
    narrator "Huey está no jardim, cercada por pincéis e tintas, trabalhando em um grande mural."
    huey "Eu quero que isso capture a essência da república... mas parece que sempre falta algo."
    menu:
        "Oferecer ideias para o mural":
            $ add_shared_memory("partnership_huey", ["huey"], "Parceria com Huey na defesa")
            $ add_affinity_points("huey", 4, "Ideias criativas na parceria")
            "[nome]" "Talvez você possa incluir algo que represente cada um de nós."
            huey "Boa ideia. Isso pode dar mais vida à pintura."
            jump cena3_ultima_noite
        "Elogiar sua arte":
            $ add_shared_memory("partnership_huey", ["huey"], "Parceria com Huey na defesa")
            $ add_affinity_points("huey", 6, "Elogio à arte na parceria")
            "[nome]" "Sua arte já é incrível. Você sempre consegue transmitir tanto sentimento."
            huey "Obrigada... isso significa muito para mim."
            jump cena3_ultima_noite
        "Fazer piada":
            $ add_shared_memory("partnership_huey", ["huey"], "Parceria com Huey na defesa")
            $ add_affinity_points("huey", 2, "Piada inadequada na parceria")
            "[nome]" "Talvez você só precise de mais tinta."
            huey "Haha... engraçado. Mas isso não resolve o problema."
            jump cena3_ultima_noite

label parceria_camille:
    show camille gentle at center
    narrator "Camille está na sala de meditação, cercada por cristais e incensos, com um caderno aberto à sua frente."
    camille "Eu quero que isso reflita a energia da casa... mas sinto que ainda não está completo."
    menu:
        "Oferecer apoio emocional":
            $ add_shared_memory("partnership_camille", ["camille"], "Parceria com Camille na defesa")
            $ add_affinity_points("camille", 4, "Apoio emocional na parceria")
            "[nome]" "Talvez você só precise de um pouco mais de tempo. Estou aqui para ajudar."
            camille "Obrigada. Sua presença já é suficiente."
            jump cena3_ultima_noite
        "Elogiar sua sensibilidade":
            $ add_shared_memory("partnership_camille", ["camille"], "Parceria com Camille na defesa")
            $ add_affinity_points("camille", 6, "Elogio à sensibilidade na parceria")
            "[nome]" "Você tem uma sensibilidade única. Tenho certeza de que vai ficar perfeito."
            camille "Obrigada. Isso significa muito para mim."
            jump cena3_ultima_noite
        "Fazer piada":
            $ add_shared_memory("partnership_camille", ["camille"], "Parceria com Camille na defesa")
            $ add_affinity_points("camille", 2, "Piada inadequada na parceria")
            "[nome]" "Talvez você só precise de um cristal maior."
            camille "Haha... engraçado. Mas isso não ajuda muito."
            jump cena3_ultima_noite

label parceria_katia:
    show katia neutral at center
    narrator "Katia está no quarto, rabiscando freneticamente em um caderno, com papéis espalhados por toda parte."
    katia "Eu tô tentando escrever algo que capture o que essa casa significa... mas tá difícil."
    menu:
        "Oferecer ideias para o roteiro":
            $ add_shared_memory("partnership_katia", ["katia"], "Parceria com Katia na defesa")
            $ add_affinity_points("katia", 4, "Ideias criativas na parceria")
            "[nome]" "Talvez você possa escrever sobre como cada um de nós contribui para a república."
            katia "Hmpf. Não é uma ideia ruim. Vou pensar nisso."
            jump cena3_ultima_noite
        "Elogiar sua escrita":
            $ add_shared_memory("partnership_katia", ["katia"], "Parceria com Katia na defesa")
            $ add_affinity_points("katia", 6, "Elogio à escrita na parceria")
            "[nome]" "Você é uma roteirista incrível. Tenho certeza de que vai ficar ótimo."
            katia "Hmpf. Não se ache. Mas... obrigada."
            jump cena3_ultima_noite
        "Fazer piada":
            $ add_shared_memory("partnership_katia", ["katia"], "Parceria com Katia na defesa")
            $ add_affinity_points("katia", 2, "Piada inadequada na parceria")
            "[nome]" "Talvez você só precise de um pouco mais de drama."
            katia "Haha... engraçado. Mas isso não resolve nada."
            jump cena3_ultima_noite

label parceria_larissa:
    show larissa happy at center
    narrator "Larissa está na sala de treino, fazendo flexões enquanto pensa em ideias para a apresentação."
    larissa "Eu tô tentando pensar em algo que mostre nossa energia... mas parece que tá faltando algo."
    menu:
        "Oferecer ideias para a apresentação":
            $ add_shared_memory("partnership_larissa", ["larissa"], "Parceria com Larissa na defesa")
            $ add_affinity_points("larissa", 4, "Ideias criativas na parceria")
            "[nome]" "Talvez você possa mostrar como todos nós trabalhamos juntos como um time."
            larissa "Boa ideia! Isso pode funcionar."
            jump cena3_ultima_noite
        "Elogiar sua energia":
            $ add_shared_memory("partnership_larissa", ["larissa"], "Parceria com Larissa na defesa")
            $ add_affinity_points("larissa", 6, "Elogio à energia na parceria")
            "[nome]" "Você é incrível. Sua energia é contagiante."
            larissa "Obrigada. Isso significa muito para mim."
            jump cena3_ultima_noite
        "Fazer piada":
            $ add_shared_memory("partnership_larissa", ["larissa"], "Parceria com Larissa na defesa")
            $ add_affinity_points("larissa", 2, "Piada inadequada na parceria")
            "[nome]" "Talvez você só precise de mais flexões."
            larissa "Haha... engraçado. Mas isso não ajuda muito."
            jump cena3_ultima_noite

label cena3_ultima_noite:
    narrator "A noite antes da entrega chega. A república está em silêncio. Cada quarto aceso guarda emoções, expectativas... e medo de perder algo precioso."
    
    # Momento emocional da última noite
    call emotional_moment("last_night_before_delivery", None, "Última noite antes da entrega da defesa") from _call_emotional_moment_cap8_3
    
    narrator "Era um momento de reflexão, onde os corações se abriam e os laços se fortaleciam antes do momento decisivo."

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
            $ add_shared_memory("last_night_visit_samantha", ["samantha"], "Visita da última noite com Samantha")
            $ add_affinity_points("samantha", 8, "Declaração de amor na última noite")
            "[nome]" "Prefiro jogar nesse aqui, com você."
            samantha "Sério?! Isso foi tipo... um crítico de afeto. Obrigada."
            jump cena4_entrega
        "Abraçá-la":
            $ add_shared_memory("last_night_visit_samantha", ["samantha"], "Visita da última noite com Samantha")
            $ add_affinity_points("samantha", 4, "Apoio emocional na última noite")
            "[nome]" "Você está indo muito bem. Estamos juntos nisso."
            samantha "Obrigada. Isso significa muito para mim."
            jump cena4_entrega
        "Dizer que é tarde":
            $ add_shared_memory("last_night_visit_samantha", ["samantha"], "Visita da última noite com Samantha")
            $ add_affinity_points("samantha", 2, "Resposta neutra na última noite")
            narrator "Você decide não dizer nada e volta para o seu quarto."
            jump cena4_entrega

label capitulo8_quarto_nicole:
    show nicole neutral at center
    narrator "Nicole está sentada à mesa, revisando anotações e ajustando gráficos no tablet."
    nicole "Você acha que isso vai ser suficiente? Ou estamos apenas tentando evitar o inevitável?"
    menu:
        "Elogiar seu trabalho":
            $ romance_nicole = True
            $ add_shared_memory("last_night_visit_nicole", ["nicole"], "Visita da última noite com Nicole")
            $ add_affinity_points("nicole", 8, "Declaração de amor na última noite")
            "[nome]" "Seu trabalho é incrível. Você está carregando todos nós."
            nicole "Obrigada... isso significa muito para mim."
            jump cena4_entrega
        "Oferecer ajuda prática":
            $ add_shared_memory("last_night_visit_nicole", ["nicole"], "Visita da última noite com Nicole")
            $ add_affinity_points("nicole", 4, "Apoio prático na última noite")
            "[nome]" "Deixe-me ajudar. Podemos revisar juntos."
            nicole "Obrigada. Isso vai ajudar bastante."
            jump cena4_entrega
        "Dizer que é tarde":
            $ add_shared_memory("last_night_visit_nicole", ["nicole"], "Visita da última noite com Nicole")
            $ add_affinity_points("nicole", 2, "Resposta neutra na última noite")
            narrator "Você decide não dizer nada e volta para o seu quarto."
            jump cena4_entrega

label capitulo8_quarto_huey:
    show huey gentle at center
    narrator "Huey está sentada no chão, cercada por pincéis e tintas, com um quadro inacabado à sua frente."
    huey "Eu queria que essa pintura capturasse tudo... mas parece que sempre falta algo."
    menu:
        "Elogiar sua arte":
            $ romance_huey = True
            $ add_shared_memory("last_night_visit_huey", ["huey"], "Visita da última noite com Huey")
            $ add_affinity_points("huey", 8, "Declaração de amor na última noite")
            "[nome]" "Sua arte já diz tudo. Ela é incrível, como você."
            huey "Obrigada... isso significa muito para mim."
            jump cena4_entrega
        "Oferecer inspiração":
            $ add_shared_memory("last_night_visit_huey", ["huey"], "Visita da última noite com Huey")
            $ add_affinity_points("huey", 4, "Apoio emocional na última noite")
            "[nome]" "Talvez você só precise de um pouco mais de tempo. Estou aqui para ajudar."
            huey "Obrigada. Isso me ajuda a continuar."
            jump cena4_entrega
        "Dizer que é tarde":
            $ add_shared_memory("last_night_visit_huey", ["huey"], "Visita da última noite com Huey")
            $ add_affinity_points("huey", 2, "Resposta neutra na última noite")
            narrator "Você decide não dizer nada e volta para o seu quarto."
            jump cena4_entrega

label capitulo8_quarto_camille:
    show camille gentle at center
    narrator "Camille está sentada no chão, com cristais e incensos ao seu redor, os olhos fechados em meditação."
    camille "Você sente isso? A energia da casa... ela está vibrando diferente."
    menu:
        "Concordar e se conectar":
            $ romance_camille = True
            $ add_shared_memory("last_night_visit_camille", ["camille"], "Visita da última noite com Camille")
            $ add_affinity_points("camille", 8, "Declaração de amor na última noite")
            "[nome]" "Eu sinto. E acho que é porque estamos todos juntos nisso."
            camille "Obrigada. Você sempre sabe o que dizer."
            jump cena4_entrega
        "Oferecer apoio":
            $ add_shared_memory("last_night_visit_camille", ["camille"], "Visita da última noite com Camille")
            $ add_affinity_points("camille", 4, "Apoio emocional na última noite")
            "[nome]" "Se precisar de algo, estou aqui. Sempre."
            camille "Obrigada. Sua presença já é suficiente."
            jump cena4_entrega
        "Dizer que é tarde":
            $ add_shared_memory("last_night_visit_camille", ["camille"], "Visita da última noite com Camille")
            $ add_affinity_points("camille", 2, "Resposta neutra na última noite")
            narrator "Você decide não dizer nada e volta para o seu quarto."
            jump cena4_entrega

label capitulo8_quarto_larissa:
    show larissa happy at center
    narrator "Larissa está fazendo alongamentos no chão, com uma garrafa d’água ao lado."
    larissa "Achei que talvez... a gente pudesse fazer flexão emocional juntos."
    menu:
        "Entrar na brincadeira":
            $ romance_larissa = True
            $ add_shared_memory("last_night_visit_larissa", ["larissa"], "Visita da última noite com Larissa")
            $ add_affinity_points("larissa", 8, "Declaração de amor na última noite")
            "[nome]" "Conta comigo. Até a última repetição."
            larissa "Sério?! Uau. Que emoção, hein? Agora só falta você me vencer na corrida."
            jump cena4_entrega
        "Elogiar sua dedicação":
            $ add_shared_memory("last_night_visit_larissa", ["larissa"], "Visita da última noite com Larissa")
            $ add_affinity_points("larissa", 4, "Apoio emocional na última noite")
            "[nome]" "Você é incrível. Sua energia é contagiante."
            larissa "Obrigada. Isso significa muito para mim."
            jump cena4_entrega
        "Dizer que é tarde":
            $ add_shared_memory("last_night_visit_larissa", ["larissa"], "Visita da última noite com Larissa")
            $ add_affinity_points("larissa", 2, "Resposta neutra na última noite")
            narrator "Você decide não dizer nada e volta para o seu quarto."
            jump cena4_entrega

label capitulo8_quarto_katia:
    show katia neutral at center
    narrator "Katia está sentada à mesa, rabiscando algo em um caderno, mas para quando você entra."
    katia "Eu... tava terminando um roteiro. Sobre uma casa. Sete moradores. Um deles... achava que ninguém notava o quanto ele se importava."
    menu:
        "Perguntar se é sobre você":
            $ romance_katia = True
            $ add_shared_memory("last_night_visit_katia", ["katia"], "Visita da última noite com Katia")
            $ add_affinity_points("katia", 8, "Declaração de amor na última noite")
            "[nome]" "Era sobre mim?"
            katia "Talvez. Ou talvez eu só tava usando o drama pra lidar com o medo."
            narrator "Katia desviou o olhar, mas havia um leve sorriso em seu rosto."
            jump cena4_entrega
        "Elogiar sua criatividade":
            $ add_shared_memory("last_night_visit_katia", ["katia"], "Visita da última noite com Katia")
            $ add_affinity_points("katia", 4, "Apoio emocional na última noite")
            "[nome]" "Você é uma roteirista incrível. Isso vai ser incrível."
            katia "Hmpf. Não se ache. Mas... obrigada."
            jump cena4_entrega
        "Dizer que é tarde":
            $ add_shared_memory("last_night_visit_katia", ["katia"], "Visita da última noite com Katia")
            $ add_affinity_points("katia", 2, "Resposta neutra na última noite")
            narrator "Você decide não dizer nada e volta para o seu quarto."
            jump cena4_entrega

label cena4_entrega:
    narrator "Na manhã seguinte, a entrega é feita. O campus observa a defesa com atenção. O grupo apresenta com coração, lógica e verdade."
    
    # Momento emocional da entrega
    call emotional_moment("defense_delivery", None, "Entrega da defesa da república") from _call_emotional_moment_cap8_4
    
    narrator "Era o momento decisivo. Tudo o que havíamos construído juntos seria testado em uma única apresentação."

    show professor_wendell neutral at center
    professor_wendell "Vocês não defenderam um espaço. Defenderam uma ideia. Uma comunidade."
    professor_wendell "E isso é algo que não pode ser medido apenas em números."

    # Verificar se pelo menos 3 personagens têm afinidade >= 5
    if (points_samantha >= 5) + (points_nicole >= 5) + (points_huey >= 5) + (points_camille >= 5) + (points_larissa >= 5) + (points_katia >= 5) >= 3:
        narrator "A campanha foi um sucesso. A república permanece unida."
        $ sucesso_campanha = True
        $ add_shared_memory("defense_success", [], "Defesa da república bem-sucedida")
    else:
        narrator "A campanha teve falhas. A universidade ainda considera a separação."
        $ sucesso_campanha = False
        $ add_shared_memory("defense_partial_success", [], "Defesa da república parcialmente bem-sucedida")

    jump cena_final_espera

label cena_final_espera:
    narrator "À noite, todos se reúnem na varanda da casa. O céu está limpo. As mãos se tocam por acaso. Os olhares dizem o que as palavras não conseguem."
    
    # Momento emocional da espera
    call emotional_moment("final_waiting", None, "Espera final pelos resultados da defesa") from _call_emotional_moment_cap8_5
    
    narrator "Era um momento de reflexão, onde os corações se abriam e os laços se fortaleciam antes do momento decisivo."

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
            $ add_shared_memory("final_choice_samantha", ["samantha"], "Escolha final com Samantha")
            $ add_affinity_points("samantha", 10, "Escolha final romântica")
            "[nome]" "Sempre."
            samantha "Obrigada. Você é incrível."
            jump capitulo8_final
        "Não sei. Mas quero tentar.":
            $ add_shared_memory("final_choice_samantha", ["samantha"], "Escolha final com Samantha")
            $ add_affinity_points("samantha", 6, "Escolha final de amizade")
            "[nome]" "Não sei. Mas quero tentar."
            samantha "Isso já é o suficiente para mim."
            jump capitulo8_final
        "Talvez seja hora de salvar e continuar.":
            $ add_shared_memory("final_choice_samantha", ["samantha"], "Escolha final com Samantha")
            $ add_affinity_points("samantha", 3, "Escolha final neutra")
            narrator "Você decide manter as coisas como estão, sem avançar no relacionamento."
            jump capitulo8_final

label final_nicole:
    show nicole neutral at center
    narrator "Nicole está sentada ao seu lado, ajustando os óculos enquanto observa o céu."
    nicole "Você acha que... mesmo com tudo isso, ainda faz sentido continuar?"
    menu:
        "Sempre. Você é incrível.":
            $ romance_nicole = True
            $ add_shared_memory("final_choice_nicole", ["nicole"], "Escolha final com Nicole")
            $ add_affinity_points("nicole", 10, "Escolha final romântica")
            "[nome]" "Sempre. Você é incrível."
            nicole "Obrigada... isso significa muito para mim."
            jump capitulo8_final
        "Não sei. Mas quero tentar.":
            $ add_shared_memory("final_choice_nicole", ["nicole"], "Escolha final com Nicole")
            $ add_affinity_points("nicole", 6, "Escolha final de amizade")
            "[nome]" "Não sei. Mas quero tentar."
            nicole "Isso já é o suficiente para mim."
            jump capitulo8_final
        "Talvez seja melhor focar em outras coisas.":
            $ add_shared_memory("final_choice_nicole", ["nicole"], "Escolha final com Nicole")
            $ add_affinity_points("nicole", 3, "Escolha final neutra")
            narrator "Você decide manter as coisas como estão, sem avançar no relacionamento."
            jump capitulo8_final

label final_huey:
    show huey gentle at center
    narrator "Huey está ao seu lado, segurando um pequeno caderno de desenhos."
    huey "Eu ainda não terminei... mas acho que esse traço aqui é você."
    menu:
        "Quero fazer parte disso. Sempre.":
            $ romance_huey = True
            $ add_shared_memory("final_choice_huey", ["huey"], "Escolha final com Huey")
            $ add_affinity_points("huey", 10, "Escolha final romântica")
            "[nome]" "Quero fazer parte disso. Sempre."
            huey "Obrigada... isso significa muito para mim."
            jump capitulo8_final
        "Não sei. Mas quero tentar.":
            $ add_shared_memory("final_choice_huey", ["huey"], "Escolha final com Huey")
            $ add_affinity_points("huey", 6, "Escolha final de amizade")
            "[nome]" "Não sei. Mas quero tentar."
            huey "Isso já é o suficiente para mim."
            jump capitulo8_final
        "Talvez seja melhor deixar como está.":
            $ add_shared_memory("final_choice_huey", ["huey"], "Escolha final com Huey")
            $ add_affinity_points("huey", 3, "Escolha final neutra")
            narrator "Você decide manter as coisas como estão, sem avançar no relacionamento."
            jump capitulo8_final

label final_camille:
    show camille gentle at center
    narrator "Camille está sentada no chão, com um cristal na mão, olhando para o céu estrelado."
    camille "Você sente isso? A energia... ela está mudando."
    menu:
        "Eu sinto. E quero estar com você.":
            $ romance_camille = True
            $ add_shared_memory("final_choice_camille", ["camille"], "Escolha final com Camille")
            $ add_affinity_points("camille", 10, "Escolha final romântica")
            "[nome]" "Eu sinto. E quero estar com você."
            camille "Obrigada. Você sempre sabe o que dizer."
            jump capitulo8_final
        "Não sei. Mas quero tentar.":
            $ add_shared_memory("final_choice_camille", ["camille"], "Escolha final com Camille")
            $ add_affinity_points("camille", 6, "Escolha final de amizade")
            "[nome]" "Não sei. Mas quero tentar."
            camille "O tempo nos guiará. Obrigada por ser honesto."
            jump capitulo8_final
        "Talvez seja melhor deixar o universo decidir.":
            $ add_shared_memory("final_choice_camille", ["camille"], "Escolha final com Camille")
            $ add_affinity_points("camille", 3, "Escolha final neutra")
            narrator "Você decide manter as coisas como estão, sem avançar no relacionamento."
            jump capitulo8_final

label final_larissa:
    show larissa happy at center
    narrator "Larissa está ao seu lado, segurando uma garrafa d’água e sorrindo."
    larissa "Acha que amanhã a gente pode correr juntos? Ou você vai me deixar na poeira?"
    menu:
        "Sempre. Você é minha parceira.":
            $ romance_larissa = True
            $ add_shared_memory("final_choice_larissa", ["larissa"], "Escolha final com Larissa")
            $ add_affinity_points("larissa", 10, "Escolha final romântica")
            "[nome]" "Sempre. Você é minha parceira."
            larissa "Sério?! Uau. Que emoção, hein? Agora só falta você me vencer na corrida."
            jump capitulo8_final
        "Não sei. Mas quero tentar.":
            $ add_shared_memory("final_choice_larissa", ["larissa"], "Escolha final com Larissa")
            $ add_affinity_points("larissa", 6, "Escolha final de amizade")
            "[nome]" "Não sei. Mas quero tentar."
            larissa "Isso já é o suficiente para mim."
            jump capitulo8_final
        "Talvez seja melhor manter as coisas como estão.":
            $ add_shared_memory("final_choice_larissa", ["larissa"], "Escolha final com Larissa")
            $ add_affinity_points("larissa", 3, "Escolha final neutra")
            narrator "Você decide manter as coisas como estão, sem avançar no relacionamento."
            jump capitulo8_final

label final_katia:
    show katia neutral at center
    narrator "Katia está encostada no batente da varanda, olhando para o céu com os braços cruzados."
    katia "Se você comentar que eu tô aqui, eu juro que te ignoro o resto da vida."
    menu:
        "Eu não vou comentar. Só quero estar com você.":
            $ romance_katia = True
            $ add_shared_memory("final_choice_katia", ["katia"], "Escolha final com Katia")
            $ add_affinity_points("katia", 10, "Escolha final romântica")
            "[nome]" "Eu não vou comentar. Só quero estar com você."
            katia "Hmpf. Não se ache. Mas... obrigada."
            jump capitulo8_final
        "Não sei. Mas quero tentar.":
            $ add_shared_memory("final_choice_katia", ["katia"], "Escolha final com Katia")
            $ add_affinity_points("katia", 6, "Escolha final de amizade")
            "[nome]" "Não sei. Mas quero tentar."
            katia "Tá. Mas não me faça esperar muito."
            jump capitulo8_final
        "Talvez seja melhor deixar como está.":
            $ add_shared_memory("final_choice_katia", ["katia"], "Escolha final com Katia")
            $ add_affinity_points("katia", 3, "Escolha final neutra")
            narrator "Você decide manter as coisas como estão, sem avançar no relacionamento."
            jump capitulo8_final

label capitulo8_final:
    scene bg republica_noite with fade
    narrator "A noite cai sobre a república da Rua Aurora. O silêncio é preenchido por pensamentos e reflexões sobre tudo o que aconteceu nos últimos dias."
    
    # Momento emocional de reflexão
    call emotional_moment("defense_reflection", None, "Reflexão sobre a defesa da república") from _call_emotional_moment_cap8_6
    
    narrator "Era um momento de reflexão profunda, onde os corações se abriam e os laços se fortaleciam."

    # Retrospectiva baseada no sucesso ou falha da campanha
    if sucesso_campanha:
        narrator "A defesa foi um sucesso. A república permanece unida, e o grupo sente o peso da vitória. Cada esforço, cada palavra dita, contribuiu para esse momento."
        narrator "O reitor reconheceu não apenas o valor do espaço físico, mas também a essência da comunidade que vocês construíram juntos."
    else:
        narrator "Apesar dos esforços, a campanha não foi suficiente para garantir a permanência da república. A separação parece inevitável, e o grupo sente o peso da incerteza."
        narrator "Mesmo assim, há um sentimento de união. Vocês lutaram juntos, e isso criou laços que nem mesmo a distância pode romper."

    # Retrospectiva dos relacionamentos
    narrator "Enquanto você reflete sobre tudo o que aconteceu, as memórias dos momentos especiais continuam a ecoar em sua mente."

    # Mostrar resumo dos relacionamentos
    $ relationship_summary = get_relationship_summary()
    narrator "Vamos ver como estão os relacionamentos até agora:"
    
    python:
        for summary in relationship_summary:
            renpy.say(narrator, summary)

    # Verificar se pode progredir para o próximo capítulo
    $ can_progress, progress_message = check_chapter_progression_requirement(8)
    
    if can_progress:
        # Momento emocional de realização
        call emotional_moment("chapter_achievement", None, "Realização de ter criado conexões suficientes para continuar") from _call_emotional_moment_cap8_7
        
        narrator "[progress_message]"
        narrator "A defesa da república havia sido mais do que uma luta por um espaço físico. Foi uma luta por laços, por histórias, por um lar."
        
        show samantha happy at left
        samantha "Parece que nossa defesa realmente funcionou, né?"
        hide samantha
        
        show nicole neutral at right
        nicole "Sim, há algo diferente no ar. Como se tivéssemos passado por uma transformação coletiva."
        hide nicole
        
        narrator "Era verdade. A defesa havia sido mais que um desafio - havia sido um portal de transformação que nos uniu de formas que nunca imaginamos."
        
        jump capitulo9
    else:
        # Momento emocional de crescimento
        call emotional_moment("growth_opportunity", None, "Oportunidade de crescimento através da reflexão") from _call_emotional_moment_cap8_8
        
        narrator "[progress_message]"
        narrator "A defesa havia sido especial, mas senti que ainda havia muito a descobrir sobre essas pessoas incríveis que haviam se tornado parte da minha vida."
        
        show katia neutral at left
        katia "N-não é como se eu estivesse preocupada ou qualquer coisa assim... mas talvez precisemos de mais tempo para nos conhecer melhor."
        hide katia
        
        show camille gentle at right
        camille "Cada conexão tem seu próprio ritmo. A defesa foi apenas o início de nossa jornada."
        hide camille
        
        narrator "Ela estava certa. A defesa havia sido apenas o início. Havia muito mais para descobrir e viver juntos."
        
        menu:
            "Refletir sobre as conexões que ainda precisam ser exploradas":
                narrator "Decidi dedicar mais tempo a conhecer melhor cada pessoa. Cada interação era uma oportunidade de descobrir algo novo."
                jump capitulo8_final
                
            "Aceitar que algumas conexões levam tempo para se desenvolver":
                narrator "Entendi que a pressa não era necessária. As melhores conexões se desenvolvem naturalmente, no seu próprio tempo."
                jump capitulo8_final
                
            "Voltar ao menu principal":
                return
                
            "Tentar o Capítulo 8 novamente":
                jump capitulo8