label capitulo5:
    scene bg cidade_entardecer with fade
    narrator "A cidade de Solária é tomada por um raro fenômeno astronômico: um eclipse parcial visível ao entardecer. A faculdade propõe uma atividade coletiva de observação, e todos os moradores da república são convidados."

    show camille happy at left
    camille "Eclipses são portais de transformação… precisamos receber essa energia com intenção!"
    
    show katia neutral at center
    katia "Se não for um eclipse invertendo o tempo, vou continuar atrasada pra aula de roteiro."

    show nicole neutral at right
    nicole "Não esqueçam de levar os óculos de proteção. Eu comprei 10 unidades."

    show larissa happy at left
    larissa "Será que consigo correr assistindo o eclipse?"

    show samantha happy at center
    samantha "Gente! Estão fazendo uma gincana temática no campus! Tem caça ao tesouro com enigmas de RPG!"

    show huey neutral at right
    huey "Quero pintar isso… com vocês."

    hide camille
    hide katia
    hide nicole
    hide larissa
    hide samantha
    hide huey

    narrator "O protagonista pode escolher com quem compartilhar o evento do eclipse. A escolha define diálogos únicos e momentos de possível avanço romântico, dependendo da afinidade (mínimo 5 pontos)."

    menu:
        "Observar o eclipse com Camille":
            if points_camille >= 5:
                jump eclipse_camille
            else:
                narrator "Você não tem afinidade suficiente com Camille para este momento."
                jump capitulo5
        "Participar da gincana com Samantha":
            if points_samantha >= 5:
                jump eclipse_samantha
            else:
                narrator "Você não tem afinidade suficiente com Samantha para este momento."
                jump capitulo5
        "Ajudar Nicole a organizar a segurança da atividade":
            if points_nicole >= 5:
                jump eclipse_nicole
            else:
                narrator "Você não tem afinidade suficiente com Nicole para este momento."
                jump capitulo5
        "Acompanhar Larissa numa corrida leve durante o fenômeno":
            if points_larissa >= 5:
                jump eclipse_larissa
            else:
                narrator "Você não tem afinidade suficiente com Larissa para este momento."
                jump capitulo5
        "Fazer uma pintura colaborativa com Huey":
            if points_huey >= 5:
                jump eclipse_huey
            else:
                narrator "Você não tem afinidade suficiente com Huey para este momento."
                jump capitulo5
        "Assistir ao eclipse com Katia em silêncio":
            if points_katia >= 5:
                jump eclipse_katia
            else:
                narrator "Você não tem afinidade suficiente com Katia para este momento."
                jump capitulo5


label capitulo5_decisao_fim_de_semana:
    narrator "Após o evento do eclipse, você reflete sobre os momentos compartilhados e como eles aproximaram você dos outros."
    jump cena3_bilhete_anonimo



label cena4_tarde_estudo:
    scene bg sala_comum with dissolve
    narrator "Com provas chegando, a casa decide fazer uma sessão de estudos. O protagonista pode escolher uma companheira de estudos."

    menu:
        "Estudar com Samantha":
            $ points_samantha += 1
            jump estudar_samantha
        "Estudar com Nicole":
            $ points_nicole += 1
            jump estudar_nicole
        "Estudar com Huey":
            $ points_huey += 1
            jump estudar_huey
        "Estudar com Camille":
            $ points_camille += 1
            jump estudar_camille
        "Estudar com Katia":
            $ points_katia += 1
            jump estudar_katia
        "Estudar com Larissa":
            $ points_larissa += 1
            jump estudar_larissa

label cena5_confronto_silencioso:
    scene bg sala_jantar with dissolve
    narrator "Durante o jantar, Nicole e Katia têm um desentendimento sobre regras de convivência. O clima fica tenso."

    show nicole neutral at left
    show katia neutral at right

    nicole "Se você não quer respeitar as regras da casa, deveria pelo menos respeitar os outros."
    narrator "Nicole falou com um tom frio, mas firme, enquanto olhava diretamente para Katia."

    show katia angry at right
    katia "Eu respeito quem me respeita. Mas ditadora eu não sou obrigada a aturar."
    narrator "Katia respondeu cerrando os olhos, sua voz carregada de irritação."

    show camille gentle at center
    camille "Essa energia… está muito pesada."
    narrator "Camille tentou aliviar o clima, mas sua voz parecia perdida no meio da tensão."

    show samantha angry at left
    samantha "Gente, será que dá pra resolver isso sem transformar o jantar em um campo de batalha?"
    narrator "Samantha olhou de um lado para o outro, claramente desconfortável com a situação."

    show larissa neutral at right
    larissa "Talvez a gente devesse focar em comer e deixar as discussões pra depois."
    narrator "Larissa tentou mudar de assunto, mas sua tentativa foi ignorada."

    show huey neutral at center
    huey "Conflitos podem ser resolvidos com diálogo... se todos estiverem dispostos a ouvir."
    narrator "Huey falou calmamente, mas parecia hesitante em se envolver diretamente."

    menu:
        "Defender Nicole":
            $ points_nicole += 1
            $ points_katia -= 1
            jump defender_nicole
        "Defender Katia":
            $ points_katia += 1
            $ points_nicole -= 1
            jump defender_katia
        "Pedir calma e tentar mediar":
            $ points_camille += 1
            if points_nicole > points_katia:
                $ points_nicole += 1
            else:
                $ points_katia += 1
            jump mediar_conflito
        "Ficar neutro":
            jump ficar_neutro

label cena_final_suspiros_noturnos:
    scene bg quarto_protagonista_noite with dissolve
    narrator "À noite, você se deita pensando em tudo que mudou desde que chegou à república. As interações, os momentos compartilhados, e as emoções que começaram a surgir."
    narrator "Ao fechar os olhos, você escuta passos suaves se aproximando."

    # Determina a personagem com maior afinidade
    $ afinidades = {
        "camille": points_camille,
        "samantha": points_samantha,
        "nicole": points_nicole,
        "katia": points_katia,
        "huey": points_huey,
        "larissa": points_larissa
    }
    $ personagem_noturna = max(afinidades, key=afinidades.get)

    # Verifica quem aparece com base na maior afinidade
    if personagem_noturna == "camille":
        jump suspiros_camille
    elif personagem_noturna == "samantha":
        jump suspiros_samantha
    elif personagem_noturna == "nicole":
        jump suspiros_nicole
    elif personagem_noturna == "katia":
        jump suspiros_katia
    elif personagem_noturna == "huey":
        jump suspiros_huey
    elif personagem_noturna == "larissa":
        jump suspiros_larissa

label suspiros_camille:
    show camille gentle at center
    narrator "Camille aparece na porta do seu quarto, hesitante, mas com um leve sorriso."
    camille "Estava sentindo uma energia estranha… queria ver se você também sentia."
    "[nome]" "Energia estranha? Talvez seja só o cansaço do dia."
    camille "Talvez... mas achei que seria bom conversar com você. Sua presença é... reconfortante."
    narrator "Camille entrou no quarto e se sentou ao seu lado, seus olhos brilhando à luz suave da lua."
    camille "Você já sentiu que algumas conexões são... inevitáveis? Como se o universo estivesse nos guiando?"
    "[nome]" "Talvez. Mas acho que algumas conexões são especiais porque escolhemos torná-las assim."
    narrator "Camille sorriu, e por um momento, o silêncio entre vocês parecia cheio de significado. Ela segurou sua mão, seus dedos entrelaçando-se suavemente."
    camille "Obrigada por me ouvir. Você é... especial."
    narrator "Antes de sair, Camille se inclinou levemente, seus olhos encontrando os seus por um instante que parecia eterno."
    $ points_camille += 1
    jump capitulo5_conclusao

label suspiros_samantha:
    show samantha nervous at center
    narrator "Samantha aparece na porta do seu quarto, segurando um travesseiro e parecendo um pouco nervosa."
    samantha "Não consigo dormir. Você... se importa se eu ficar um pouco aqui?"
    "[nome]" "Claro que não. Entre."
    narrator "Samantha se sentou no chão ao lado da cama, falando sobre coisas aleatórias para distrair a mente. Sua risada suave preencheu o quarto."
    samantha "Você sabia que eu sempre fico pensando demais à noite? É como se minha mente não desligasse."
    "[nome]" "Talvez você só precise de alguém para compartilhar esses pensamentos."
    narrator "Samantha olhou para você, seus olhos brilhando com uma mistura de vulnerabilidade e gratidão."
    samantha "Você é... diferente. No bom sentido. É fácil estar perto de você."
    narrator "Ela se aproximou um pouco mais, apoiando a cabeça no colchão enquanto olhava para você. Por um momento, o mundo parecia mais simples."
    samantha "Obrigada por me ouvir. Boa noite... e obrigada por ser você."
    $ points_samantha += 1
    jump capitulo5_conclusao

label suspiros_nicole:
    show nicole neutral at center
    narrator "Nicole aparece na porta do seu quarto, com os braços cruzados e um olhar pensativo."
    nicole "Você não dormiu ainda, né? Eu... não consegui parar de pensar em hoje."
    "[nome]" "Quer conversar sobre isso?"
    nicole "Talvez... só por um momento."
    narrator "Nicole entrou e se sentou na cadeira ao lado da cama. Ela falou sobre suas preocupações, mas também agradeceu por estar lá para ela."
    nicole "Você é... confiável. Isso é raro."
    "[nome]" "E você é mais incrível do que imagina. Mesmo quando tenta esconder isso."
    narrator "Nicole desviou o olhar, mas você percebeu um leve rubor em suas bochechas. Por um instante, seus olhares se cruzaram, e o silêncio parecia cheio de significado."
    nicole "Boa noite. E... obrigada por me ouvir. Isso significa mais do que você imagina."
    $ points_nicole += 1
    jump capitulo5_conclusao

label suspiros_katia:
    show katia neutral at center
    narrator "Katia aparece na porta do seu quarto, segurando algo nas mãos e evitando contato visual."
    katia "Trouxe isso aqui... pra você. Não é presente, é... sei lá. Só pega."
    "[nome]" "O que é isso?"
    katia "Um DVD. Achei que você gostaria. Mas não significa nada, tá?"
    narrator "Katia entregou o DVD e ficou por alguns minutos, falando sobre o filme e outras coisas aleatórias. Apesar de sua atitude defensiva, havia algo genuíno em suas palavras."
    katia "Você é... diferente. Mas não se ache por isso, tá?"
    narrator "Ela cruzou os braços, mas não se afastou. Pelo contrário, ela ficou ao seu lado, e por um breve momento, seus olhares se encontraram."
    katia "Boa noite. E... não estrague o DVD."
    narrator "Antes de sair, Katia deu um leve sorriso, quase imperceptível, mas cheio de significado."
    $ points_katia += 1
    jump capitulo5_conclusao

label suspiros_huey:
    show huey gentle at center
    narrator "Huey aparece na porta do seu quarto, segurando uma pequena tela pintada à mão."
    huey "Pintei isso. Não tá bom, mas... acho que é você. Em cor."
    "[nome]" "Isso é incrível, Huey. Obrigado por compartilhar isso comigo."
    huey "Eu só... queria expressar algo. E a pintura parecia o jeito certo."
    narrator "Huey ficou por alguns minutos, falando sobre a pintura e o que ela representava. Sua voz era suave, quase como um sussurro."
    huey "Você é... inspirador. Obrigada por me fazer ver o mundo de um jeito diferente."
    narrator "Antes de sair, Huey deu um leve sorriso, e seus olhos brilharam com emoção. Por um instante, parecia que o mundo inteiro cabia naquele olhar."
    $ points_huey += 1
    jump capitulo5_conclusao

label suspiros_larissa:
    show larissa happy at center
    narrator "Larissa aparece na porta do seu quarto, com um copo de água na mão e um sorriso sem jeito."
    larissa "Fui beber água… e acabei aqui. Meio sem querer… posso ficar um pouco?"
    "[nome]" "Claro. Entre."
    narrator "Larissa se sentou na beira da cama, falando sobre o treino do dia e suas metas. Sua energia era contagiante, mesmo à noite."
    larissa "Você é fácil de conversar. É bom ter alguém assim por perto."
    "[nome]" "E você faz tudo parecer mais leve. É inspirador."
    narrator "Larissa riu, mas havia algo mais em seu olhar. Ela deu um leve toque no seu ombro, deixando sua mão ali por um momento mais longo do que o normal."
    larissa "Boa noite. E... obrigada por ser alguém com quem eu posso contar."
    $ points_larissa += 1
    jump capitulo5_conclusao

label mediar_conflito:
    narrator "Você tenta intervir no conflito, buscando uma solução pacífica."
    "[nome]" "Gente, acho que todos temos nossos pontos de vista. Talvez possamos conversar com calma e encontrar um meio-termo."
    show nicole neutral at left
    show katia neutral at right
    nicole "Talvez você tenha razão. Não adianta discutir assim."
    katia "Tá, tudo bem. Mas não vou mudar de ideia tão fácil."
    narrator "Com sua intervenção, o clima na sala pareceu aliviar um pouco. Embora o conflito não tenha sido completamente resolvido, todos voltaram a comer em silêncio."
    jump cena_final_suspiros_noturnos