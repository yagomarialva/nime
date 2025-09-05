label capitulo5:
    if "capitulo5" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo5")
    
    scene bg cidade_entardecer with fade
    narrator "A cidade de Solária é tomada por um raro fenômeno astronômico: um eclipse parcial visível ao entardecer. A faculdade propõe uma atividade coletiva de observação, e todos os moradores da república são convidados."
    
    # Momento emocional de evento especial
    call emotional_moment("special_astronomical_event", None, "Um evento astronômico raro que trará momentos especiais") from _call_emotional_moment_cap5_1
    
    narrator "Havia algo mágico no ar. O eclipse não era apenas um fenômeno astronômico - era uma oportunidade para momentos únicos e conexões especiais."

    show camille happy at left
    camille "Eclipses são portais de transformação… precisamos receber essa energia com intenção!"
    camille "É um momento perfeito para reflexão e conexão. Algo especial está acontecendo."
    $ add_affinity_points("camille", 3, "Conexão espiritual com o eclipse")
    hide camille
    
    show katia neutral at center
    katia "Se não for um eclipse invertendo o tempo, vou continuar atrasada pra aula de roteiro."
    katia "N-não é como se eu estivesse animada ou qualquer coisa assim! É só que... é interessante."
    $ add_affinity_points("katia", 2, "Interesse tsundere no eclipse")
    hide katia

    show nicole neutral at right
    nicole "Não esqueçam de levar os óculos de proteção. Eu comprei 10 unidades."
    nicole "Segurança em primeiro lugar, mas... é um momento único que não devemos desperdiçar."
    $ add_affinity_points("nicole", 3, "Preparação cuidadosa para o evento")
    hide nicole

    show larissa happy at left
    larissa "Será que consigo correr assistindo o eclipse?"
    larissa "Quem sabe a gente não faz uma corrida especial? Seria incrível!"
    $ add_affinity_points("larissa", 3, "Energia contagiante para o evento")
    hide larissa

    show samantha happy at center
    samantha "Gente! Estão fazendo uma gincana temática no campus! Tem caça ao tesouro com enigmas de RPG!"
    samantha "É como se o universo tivesse preparado uma aventura perfeita para nós!"
    $ add_affinity_points("samantha", 3, "Entusiasmo com a gincana")
    hide samantha

    show huey neutral at right
    huey "Quero pintar isso… com vocês."
    huey "Cada pessoa aqui é uma obra de arte, e o eclipse será o cenário perfeito!"
    $ add_affinity_points("huey", 3, "Inspiração artística com o eclipse")
    hide huey

    narrator "O protagonista pode escolher com quem compartilhar o evento do eclipse. A escolha define diálogos únicos e momentos de possível avanço romântico, dependendo da afinidade (mínimo 5 pontos)."

    menu:
        "Observar o eclipse com Camille (Espiritualidade e conexão cósmica)":
            if points_camille >= 5:
                $ add_shared_memory("eclipse_spiritual_moment", ["camille"], "Momento espiritual compartilhado durante o eclipse")
                $ add_affinity_points("camille", 10, "Conexão espiritual profunda")
                jump eclipse_camille
            else:
                narrator "Você não tem afinidade suficiente com Camille para este momento especial."
                jump capitulo5
                
        "Participar da gincana com Samantha (Aventura e diversão)":
            if points_samantha >= 5:
                $ add_shared_memory("eclipse_adventure_moment", ["samantha"], "Aventura em gincana durante o eclipse")
                $ add_affinity_points("samantha", 10, "Aventura compartilhada")
                jump eclipse_samantha
            else:
                narrator "Você não tem afinidade suficiente com Samantha para esta aventura."
                jump capitulo5
                
        "Ajudar Nicole a organizar a segurança da atividade (Responsabilidade e cuidado)":
            if points_nicole >= 5:
                $ add_shared_memory("eclipse_safety_moment", ["nicole"], "Organização de segurança durante o eclipse")
                $ add_affinity_points("nicole", 10, "Responsabilidade compartilhada")
                jump eclipse_nicole
            else:
                narrator "Você não tem afinidade suficiente com Nicole para esta responsabilidade."
                jump capitulo5
                
        "Acompanhar Larissa numa corrida leve durante o fenômeno (Energia e movimento)":
            if points_larissa >= 5:
                $ add_shared_memory("eclipse_energy_moment", ["larissa"], "Corrida especial durante o eclipse")
                $ add_affinity_points("larissa", 10, "Energia compartilhada")
                jump eclipse_larissa
            else:
                narrator "Você não tem afinidade suficiente com Larissa para esta atividade energética."
                jump capitulo5
                
        "Fazer uma pintura colaborativa com Huey (Arte e criatividade)":
            if points_huey >= 5:
                $ add_shared_memory("eclipse_artistic_moment", ["huey"], "Pintura colaborativa durante o eclipse")
                $ add_affinity_points("huey", 10, "Criatividade compartilhada")
                jump eclipse_huey
            else:
                narrator "Você não tem afinidade suficiente com Huey para esta expressão artística."
                jump capitulo5
                
        "Assistir ao eclipse com Katia em silêncio (Intimidade e contemplação)":
            if points_katia >= 5:
                $ add_shared_memory("eclipse_intimate_moment", ["katia"], "Momento íntimo de contemplação durante o eclipse")
                $ add_affinity_points("katia", 10, "Intimidade compartilhada")
                jump eclipse_katia
            else:
                narrator "Você não tem afinidade suficiente com Katia para este momento íntimo."
                jump capitulo5


label capitulo5_decisao_fim_de_semana:
    narrator "Após o evento do eclipse, você reflete sobre os momentos compartilhados e como eles aproximaram você dos outros."
    jump cena3_bilhete_anonimo



label cena4_tarde_estudo:
    scene bg sala_comum with dissolve
    narrator "Com provas chegando, a casa decide fazer uma sessão de estudos. O protagonista pode escolher uma companheira de estudos."
    
    # Momento emocional de estudo em grupo
    call emotional_moment("study_session", None, "Sessão de estudos que fortalece os laços acadêmicos") from _call_emotional_moment_cap5_2
    
    narrator "Era hora de focar nos estudos, mas também uma oportunidade de se conectar de uma forma diferente - através do conhecimento e do apoio mútuo."

    menu:
        "Estudar com Samantha (Tecnologia e criatividade)":
            $ add_shared_memory("study_session_technology", ["samantha"], "Sessão de estudos focada em tecnologia")
            $ add_affinity_points("samantha", 6, "Estudo colaborativo")
            jump estudar_samantha
            
        "Estudar com Nicole (Estratégia e organização)":
            $ add_shared_memory("study_session_strategy", ["nicole"], "Sessão de estudos focada em estratégia")
            $ add_affinity_points("nicole", 6, "Estudo colaborativo")
            jump estudar_nicole
            
        "Estudar com Huey (Arte e expressão)":
            $ add_shared_memory("study_session_art", ["huey"], "Sessão de estudos focada em arte")
            $ add_affinity_points("huey", 6, "Estudo colaborativo")
            jump estudar_huey
            
        "Estudar com Camille (Espiritualidade e reflexão)":
            $ add_shared_memory("study_session_spirituality", ["camille"], "Sessão de estudos focada em espiritualidade")
            $ add_affinity_points("camille", 6, "Estudo colaborativo")
            jump estudar_camille
            
        "Estudar com Katia (Cinema e arte)":
            $ add_shared_memory("study_session_cinema", ["katia"], "Sessão de estudos focada em cinema")
            $ add_affinity_points("katia", 6, "Estudo colaborativo")
            jump estudar_katia
            
        "Estudar com Larissa (Energia e motivação)":
            $ add_shared_memory("study_session_energy", ["larissa"], "Sessão de estudos focada em energia")
            $ add_affinity_points("larissa", 6, "Estudo colaborativo")
            jump estudar_larissa

label cena5_confronto_silencioso:
    scene bg sala_jantar with dissolve
    narrator "Durante o jantar, Nicole e Katia têm um desentendimento sobre regras de convivência. O clima fica tenso."
    
    # Momento emocional de conflito
    call emotional_moment("household_conflict", None, "Conflito que testa os laços da casa") from _call_emotional_moment_cap5_3
    
    narrator "Era um momento que testaria a força dos laços que havíamos construído. Como reagiríamos quando as personalidades colidissem?"

    show nicole neutral at left
    show katia neutral at right

    nicole "Se você não quer respeitar as regras da casa, deveria pelo menos respeitar os outros."
    narrator "Nicole falou com um tom frio, mas firme, enquanto olhava diretamente para Katia."

    show katia angry at right
    katia "Eu respeito quem me respeita. Mas ditadora eu não sou obrigada a aturar."
    katia "N-não é como se eu não me importasse com as regras ou qualquer coisa assim! É só que... você está sendo muito rígida!"
    narrator "Katia respondeu cerrando os olhos, sua voz carregada de irritação, mas também de vulnerabilidade."

    show camille gentle at center
    camille "Essa energia… está muito pesada."
    camille "Talvez possamos encontrar um meio-termo que funcione para todos."
    narrator "Camille tentou aliviar o clima, mas sua voz parecia perdida no meio da tensão."

    show samantha angry at left
    samantha "Gente, será que dá pra resolver isso sem transformar o jantar em um campo de batalha?"
    samantha "Somos uma família, não inimigos!"
    narrator "Samantha olhou de um lado para o outro, claramente desconfortável com a situação."

    show larissa neutral at right
    larissa "Talvez a gente devesse focar em comer e deixar as discussões pra depois."
    larissa "Mas quando resolvermos, vamos resolver juntos, como uma equipe."
    narrator "Larissa tentou mudar de assunto, mas sua tentativa foi ignorada."

    show huey neutral at center
    huey "Conflitos podem ser resolvidos com diálogo... se todos estiverem dispostos a ouvir."
    huey "Cada pessoa aqui tem seu valor e suas necessidades."
    narrator "Huey falou calmamente, mas parecia hesitante em se envolver diretamente."

    menu:
        "Defender Nicole (Apoio à organização)":
            $ add_shared_memory("conflict_support_nicole", ["nicole"], "Apoio a Nicole durante o conflito")
            $ add_affinity_points("nicole", 4, "Apoio durante conflito")
            $ add_affinity_points("katia", -2, "Desacordo durante conflito")
            jump defender_nicole
            
        "Defender Katia (Apoio à flexibilidade)":
            $ add_shared_memory("conflict_support_katia", ["katia"], "Apoio a Katia durante o conflito")
            $ add_affinity_points("katia", 4, "Apoio durante conflito")
            $ add_affinity_points("nicole", -2, "Desacordo durante conflito")
            jump defender_katia
            
        "Pedir calma e tentar mediar (Diplomacia e harmonia)":
            $ add_shared_memory("conflict_mediation", ["camille"], "Mediação do conflito")
            $ add_affinity_points("camille", 6, "Mediação do conflito")
            if points_nicole > points_katia:
                $ add_affinity_points("nicole", 2, "Apreciação pela mediação")
            else:
                $ add_affinity_points("katia", 2, "Apreciação pela mediação")
            jump mediar_conflito
            
        "Ficar neutro (Observação e reflexão)":
            $ add_shared_memory("conflict_neutrality", [], "Neutralidade durante o conflito")
            jump ficar_neutro

label cena_final_suspiros_noturnos:
    scene bg quarto_protagonista_noite with dissolve
    narrator "À noite, você se deita pensando em tudo que mudou desde que chegou à república. As interações, os momentos compartilhados, e as emoções que começaram a surgir."
    
    # Momento emocional de intimidade noturna
    call emotional_moment("nighttime_intimacy", None, "Momento de intimidade noturna que aprofunda as conexões") from _call_emotional_moment_cap5_4
    
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
    $ add_affinity_points("camille", 8, "Intimidade noturna especial")
    jump capitulo5_final

label suspiros_samantha:
    show samantha sad at center
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
    $ add_affinity_points("samantha", 8, "Intimidade noturna especial")
    jump capitulo5_final

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
    $ add_affinity_points("nicole", 8, "Intimidade noturna especial")
    jump capitulo5_final

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
    $ add_affinity_points("katia", 8, "Intimidade noturna especial")
    jump capitulo5_final

label suspiros_huey:
    show huey gentle at center
    narrator "Huey aparece na porta do seu quarto, segurando uma pequena tela pintada à mão."
    huey "Pintei isso. Não tá bom, mas... acho que é você. Em cor."
    "[nome]" "Isso é incrível, Huey. Obrigado por compartilhar isso comigo."
    huey "Eu só... queria expressar algo. E a pintura parecia o jeito certo."
    narrator "Huey ficou por alguns minutos, falando sobre a pintura e o que ela representava. Sua voz era suave, quase como um sussurro."
    huey "Você é... inspirador. Obrigada por me fazer ver o mundo de um jeito diferente."
    narrator "Antes de sair, Huey deu um leve sorriso, e seus olhos brilharam com emoção. Por um instante, parecia que o mundo inteiro cabia naquele olhar."
    $ add_affinity_points("huey", 8, "Intimidade noturna especial")
    jump capitulo5_final

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
    $ add_affinity_points("larissa", 8, "Intimidade noturna especial")
    jump capitulo5_final

label defender_nicole:
    narrator "Você decide apoiar Nicole em sua posição sobre organização."
    "[nome]" "Nicole tem razão. Uma casa organizada é fundamental para o bem-estar de todos."
    show nicole happy at left
    nicole "Obrigada por me apoiar. É bom saber que alguém entende a importância da organização."
    show katia angry at right
    katia "Tá, mas não precisa ser tão rígida com tudo!"
    narrator "Nicole sorriu agradecida, enquanto Katia ficou visivelmente irritada. O conflito continuou, mas agora com você claramente do lado de Nicole."
    jump cena_final_suspiros_noturnos

label defender_katia:
    narrator "Você decide apoiar Katia em sua posição sobre flexibilidade."
    "[nome]" "Katia tem um ponto. Às vezes é bom ter um pouco de flexibilidade e espontaneidade."
    show katia happy at right
    katia "Exato! Nem tudo precisa ser tão controlado e previsível."
    show nicole sad at left
    nicole "Mas a organização é importante para que todos possam viver bem aqui..."
    narrator "Katia sorriu satisfeita, enquanto Nicole ficou um pouco decepcionada. O conflito continuou, mas agora com você claramente do lado de Katia."
    jump cena_final_suspiros_noturnos

label ficar_neutro:
    narrator "Você decide não tomar partido no conflito, observando a situação."
    "[nome]" "Acho que cada um tem seus motivos. Vou deixar vocês resolverem isso entre vocês."
    show nicole neutral at left
    show katia neutral at right
    nicole "Entendo. Mas espero que você considere a importância da organização."
    katia "E eu espero que você considere que nem tudo precisa ser tão rígido."
    narrator "Ambas ficaram um pouco decepcionadas com sua neutralidade, mas respeitaram sua decisão. O conflito continuou sem sua participação direta."
    jump cena_final_suspiros_noturnos

label mediar_conflito:
    narrator "Você tenta intervir no conflito, buscando uma solução pacífica."
    "[nome]" "Gente, acho que todos temos nossos pontos de vista. Talvez possamos conversar com calma e encontrar um meio-termo."
    show nicole neutral at left
    show katia neutral at right
    nicole "Talvez você tenha razão. Não adianta discutir assim."
    katia "Tá, tudo bem. Mas não vou mudar de ideia tão fácil."
    narrator "Com sua intervenção, o clima na sala pareceu aliviar um pouco. Embora o conflito não tenha sido completamente resolvido, todos voltaram a comer em silêncio."
    jump cena_final_suspiros_noturnos