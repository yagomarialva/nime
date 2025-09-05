label capitulo10:
    if "capitulo10" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo10")
    
    scene bg republica_vazia with fade
    narrator "É a última semana do semestre. A república começa a esvaziar. Caixas se acumulam. Paredes perdem os quadros e bilhetes. Cada passo soa como uma despedida não dita."
    
    # Momento emocional de despedida
    call emotional_moment("final_goodbye_beginning", None, "Início da despedida da república") from _call_emotional_moment_cap10_1
    
    narrator "Era um momento de transição, onde os corações se preparavam para dizer adeus ao lar que haviam construído juntos."

    show nicole neutral at left
    nicole "Estamos seguindo o cronograma, mas emocionalmente... estamos atrasados."
    nicole "Esta casa se tornou mais que um lugar para morar. Se tornou nossa família."
    $ add_affinity_points("nicole", 3, "Liderança na despedida")
    hide nicole

    show katia neutral at center
    katia "Esse plano de fundo vai render um curta sobre fim de ciclos."
    katia "N-não é como se eu estivesse triste ou qualquer coisa assim! É só que... momentos como este são especiais."
    $ add_affinity_points("katia", 3, "Vulnerabilidade na despedida")
    hide katia

    show camille gentle at right
    camille "O cheiro da casa vai mudar... Mas a vibração ficará."
    camille "A energia que criamos aqui continuará a nos conectar, mesmo quando estivermos longe."
    $ add_affinity_points("camille", 3, "Conexão espiritual na despedida")
    hide camille

    show larissa happy at left
    larissa "Quero fazer agachamento emocional e físico com todo mundo antes do fim."
    larissa "Vamos mostrar que somos uma família forte, mesmo na despedida!"
    $ add_affinity_points("larissa", 3, "Energia na despedida")
    hide larissa

    show samantha happy at center
    samantha "A gente devia ter salvado mais momentos com clipes de voz…"
    samantha "Mas as memórias que criamos aqui são mais valiosas que qualquer save file."
    $ add_affinity_points("samantha", 3, "Criatividade na despedida")
    hide samantha

    show huey gentle at right
    huey "Última arte antes da parede ser pintada de branco. Adeus, memória viva."
    huey "Cada pincelada conta uma história, cada história nos une para sempre."
    $ add_affinity_points("huey", 3, "Visão artística da despedida")
    hide huey

    # Segue para os eventos de despedida automaticamente
    jump capitulo10_samantha

label capitulo10_samantha:
    show samantha happy at center
    narrator "Você ajuda Samantha a salvar os dados dos jogos antigos no computador."
    samantha "Esses jogos são como memórias vivas. Cada escolha, cada vitória... é como se a gente pudesse reviver tudo."
    '[nome]' "E agora você pode guardar tudo isso pra sempre."
    samantha "Obrigada por me ajudar. Você é o melhor parceiro de guilda que eu poderia pedir."
    
    # Momento emocional com Samantha
    call emotional_moment("goodbye_samantha", None, "Despedida especial com Samantha") from _call_emotional_moment_cap10_2
    
    $ add_shared_memory("final_goodbye_samantha", ["samantha"], "Despedida final com Samantha")
    $ add_affinity_points("samantha", 6, "Momento especial de despedida")
    
    jump capitulo10_katia

label capitulo10_katia:
    show katia neutral at center
    narrator "Você ajuda Katia a embalar livros enquanto discutem finais de filmes."
    katia "Sabe o que eu odeio? Finais abertos. Mas... às vezes, eles são os mais reais."
    '[nome]' "Talvez porque a vida nunca tem um ponto final definitivo."
    katia "Hmpf. Filosófico demais pra mim. Mas... obrigada por estar aqui."
    
    # Momento emocional com Katia
    call emotional_moment("goodbye_katia", None, "Despedida especial com Katia") from _call_emotional_moment_cap10_3
    
    $ add_shared_memory("final_goodbye_katia", ["katia"], "Despedida final com Katia")
    $ add_affinity_points("katia", 6, "Momento especial de despedida")
    
    jump capitulo10_huey

label capitulo10_huey:
    show huey gentle at center
    narrator "Você ajuda Huey a pintar a parede com uma última arte antes de ser apagada."
    huey "Cada pincelada é como uma memória. Mesmo que desapareça, ela ainda existiu."
    '[nome]' "E você capturou tudo isso de um jeito único."
    huey "Obrigado por pintar isso comigo. Você é uma inspiração."
    
    # Momento emocional com Huey
    call emotional_moment("goodbye_huey", None, "Despedida especial com Huey") from _call_emotional_moment_cap10_4
    
    $ add_shared_memory("final_goodbye_huey", ["huey"], "Despedida final com Huey")
    $ add_affinity_points("huey", 6, "Momento especial de despedida")
    
    jump capitulo10_camille

label capitulo10_camille:
    show camille gentle at center
    narrator "Você queima incensos com Camille enquanto refletem sobre mudanças."
    camille "O cheiro muda, mas a energia permanece. É como se a casa guardasse tudo o que vivemos."
    '[nome]' "E agora, ela vai guardar isso pra sempre."
    camille "Obrigada por estar aqui. Você trouxe equilíbrio pra tudo isso."
    
    # Momento emocional com Camille
    call emotional_moment("goodbye_camille", None, "Despedida especial com Camille") from _call_emotional_moment_cap10_5
    
    $ add_shared_memory("final_goodbye_camille", ["camille"], "Despedida final com Camille")
    $ add_affinity_points("camille", 6, "Momento especial de despedida")
    
    jump capitulo10_nicole

label capitulo10_nicole:
    show nicole neutral at center
    narrator "Você ajuda Nicole a criar etiquetas organizadas para as caixas."
    nicole "Organizar tudo isso é como organizar as memórias. Cada coisa no seu lugar."
    '[nome]' "E você faz isso melhor do que ninguém."
    nicole "Obrigada por me ajudar. Você é... eficiente. E especial."
    
    # Momento emocional com Nicole
    call emotional_moment("goodbye_nicole", None, "Despedida especial com Nicole") from _call_emotional_moment_cap10_6
    
    $ add_shared_memory("final_goodbye_nicole", ["nicole"], "Despedida final com Nicole")
    $ add_affinity_points("nicole", 6, "Momento especial de despedida")
    
    jump capitulo10_larissa

label capitulo10_larissa:
    show larissa happy at center
    narrator "Você treina com Larissa entre as caixas, transformando a despedida em algo físico."
    larissa "Treinar é minha forma de lidar com tudo. Mas... isso aqui é mais difícil do que eu pensei."
    '[nome]' "Você é forte, Larissa. E não precisa carregar tudo sozinha."
    larissa "Obrigada por estar aqui. Você é um parceiro incrível."
    
    # Momento emocional com Larissa
    call emotional_moment("goodbye_larissa", None, "Despedida especial com Larissa") from _call_emotional_moment_cap10_7
    
    $ add_shared_memory("final_goodbye_larissa", ["larissa"], "Despedida final com Larissa")
    $ add_affinity_points("larissa", 6, "Momento especial de despedida")
    
    jump capitulo10_evento_final

label capitulo10_evento_final:
    scene bg republica_noite with fade
    narrator "Na véspera do fim, cada morador sai para resolver sua vida. Você fica sozinho na casa… até que uma porta se abre."
    
    # Momento emocional do evento final
    call emotional_moment("final_night_moment", None, "Momento final da noite na república") from _call_emotional_moment_cap10_8
    
    narrator "Era um momento de reflexão, onde os corações se preparavam para o último encontro."

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
        $ add_shared_memory("final_night_samantha", ["samantha"], "Noite final com Samantha")
        $ add_affinity_points("samantha", 10, "Momento romântico final")
        samantha "No próximo jogo, eu quero começar contigo desde o prólogo."
    else:
        $ add_shared_memory("final_night_samantha", ["samantha"], "Noite final com Samantha")
        $ add_affinity_points("samantha", 6, "Momento de amizade final")
        samantha "Mesmo em partidas separadas… sempre vou torcer pelo seu sucesso crítico."
    jump capitulo10_final

# Final com Nicole
label capitulo10_final_nicole:
    show nicole neutral at center
    narrator "Nicole aparece com um pequeno caderno de anotações nas mãos."
    nicole "Eu fiz uma lista de coisas que quero lembrar sobre hoje... mas nenhuma palavra parece suficiente."
    '[nome]' "Talvez algumas coisas não precisem ser escritas. Só sentidas."
    nicole "Você sempre sabe o que dizer. Obrigada por ser... você."
    if romance_nicole:
        $ add_shared_memory("final_night_nicole", ["nicole"], "Noite final com Nicole")
        $ add_affinity_points("nicole", 10, "Momento romântico final")
        nicole "Eu espero que, mesmo longe, você continue sendo meu ponto de equilíbrio. Porque eu quero ser o seu."
    else:
        $ add_shared_memory("final_night_nicole", ["nicole"], "Noite final com Nicole")
        $ add_affinity_points("nicole", 6, "Momento de amizade final")
        nicole "Mesmo que a gente siga caminhos diferentes, eu sempre vou lembrar de você como alguém especial."
    narrator "Nicole sorri timidamente, e vocês compartilham um momento de silêncio confortável, cheio de significado."
    jump capitulo10_final

# Final com Huey
label capitulo10_final_huey:
    show huey gentle at center
    narrator "Huey aparece com um quadro recém-pintado, ainda com as mãos manchadas de tinta."
    huey "Eu pintei isso para você. É como eu vejo a gente... juntos, mesmo quando estamos longe."
    '[nome]' "Huey, isso é lindo. Obrigado por capturar algo tão especial."
    huey "Você sempre foi minha maior inspiração. Obrigado por me fazer acreditar na beleza das conexões."
    if romance_huey:
        $ add_shared_memory("final_night_huey", ["huey"], "Noite final com Huey")
        $ add_affinity_points("huey", 10, "Momento romântico final")
        huey "Eu quero que você saiba... você é a cor mais vibrante da minha vida."
    else:
        $ add_shared_memory("final_night_huey", ["huey"], "Noite final com Huey")
        $ add_affinity_points("huey", 6, "Momento de amizade final")
        huey "Mesmo que a gente siga caminhos diferentes, você sempre será parte da minha paleta."
    narrator "Huey entrega o quadro a você, e vocês compartilham um momento de pura emoção e gratidão."
    jump capitulo10_final

# Final com Camille
label capitulo10_final_camille:
    show camille gentle at center
    narrator "Camille aparece com um pequeno cristal na mão, refletindo a luz do amanhecer."
    camille "Este cristal... ele guarda energia. Quero que você o leve, para lembrar que sempre estaremos conectados."
    '[nome]' "Camille, isso é lindo. Obrigado por sempre trazer equilíbrio para tudo."
    camille "Você também trouxe luz para minha vida. Obrigada por ser uma alma tão especial."
    if romance_camille:
        $ add_shared_memory("final_night_camille", ["camille"], "Noite final com Camille")
        $ add_affinity_points("camille", 10, "Momento romântico final")
        camille "Eu acredito que nossas almas se encontrarão de novo, vida após vida. Mas, por enquanto, quero aproveitar cada momento com você."
    else:
        $ add_shared_memory("final_night_camille", ["camille"], "Noite final com Camille")
        $ add_affinity_points("camille", 6, "Momento de amizade final")
        camille "Mesmo que nossos caminhos se separem, saiba que você sempre terá um lugar especial na minha energia."
    narrator "Camille coloca o cristal em sua mão, e vocês compartilham um momento de serenidade e conexão."
    jump capitulo10_final

# Final com Larissa
label capitulo10_final_larissa:
    show larissa happy at center
    narrator "Larissa aparece com uma bola de vôlei nas mãos e um sorriso determinado."
    larissa "Ei, antes de irmos... que tal uma última partida? Só para garantir que você não esqueça como perder para mim."
    '[nome]' "Eu nunca vou esquecer, Larissa. Você sempre me ensinou a dar o meu melhor."
    larissa "Você é tão bobo... mas é por isso que eu gosto de você."
    if romance_larissa:
        $ add_shared_memory("final_night_larissa", ["larissa"], "Noite final com Larissa")
        $ add_affinity_points("larissa", 10, "Momento romântico final")
        larissa "Eu quero que você saiba... você é meu parceiro favorito, dentro e fora da quadra."
    else:
        $ add_shared_memory("final_night_larissa", ["larissa"], "Noite final com Larissa")
        $ add_affinity_points("larissa", 6, "Momento de amizade final")
        larissa "Mesmo que a gente siga caminhos diferentes, você sempre será meu parceiro de treino favorito."
    narrator "Vocês jogam juntos uma última vez, rindo e compartilhando a energia contagiante de Larissa."
    jump capitulo10_final

# Final com Katia
label capitulo10_final_katia:
    show katia neutral at center
    narrator "Katia aparece com o celular na mão, gravando um vídeo enquanto se aproxima."
    katia "Se você contar pra alguém que eu disse isso, eu nego até o fim... mas você é uma das pessoas mais importantes que já conheci."
    '[nome]' "Katia, você é incrível. Obrigado por me deixar fazer parte da sua história."
    katia "Hmpf. Não se ache. Mas... obrigada por estar aqui."
    if romance_katia:
        $ add_shared_memory("final_night_katia", ["katia"], "Noite final com Katia")
        $ add_affinity_points("katia", 10, "Momento romântico final")
        katia "Eu quero que você saiba... você é o único clichê que eu aceito na minha vida."
    else:
        $ add_shared_memory("final_night_katia", ["katia"], "Noite final com Katia")
        $ add_affinity_points("katia", 6, "Momento de amizade final")
        katia "Mesmo que a gente siga caminhos diferentes, você sempre será o protagonista de algumas das minhas melhores memórias."
    narrator "Katia desliga o celular e olha para você com um sorriso sincero, compartilhando um momento de conexão verdadeira."
    jump capitulo10_final

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

label capitulo10_final:
    scene bg republica_saida with fade
    narrator "O sol nasce sobre a república vazia, iluminando um novo dia. Enquanto você reflete sobre tudo o que aconteceu, as memórias dos momentos especiais continuam a ecoar em sua mente."
    
    # Momento emocional de reflexão final
    call emotional_moment("final_reflection", None, "Reflexão final sobre a jornada na república") from _call_emotional_moment_cap10_9
    
    narrator "Era um momento de reflexão profunda, onde os corações se abriam e os laços se fortaleciam sob o céu dourado."

    # Retrospectiva dos relacionamentos
    narrator "Enquanto você reflete sobre tudo o que aconteceu, as memórias dos momentos especiais continuam a ecoar em sua mente."

    # Mostrar resumo dos relacionamentos
    $ relationship_summary = get_relationship_summary()
    narrator "Vamos ver como estão os relacionamentos até agora:"
    
    python:
        for summary in relationship_summary:
            renpy.say(narrator, summary)

    # Verificar se pode progredir para o epílogo
    $ can_progress, progress_message = check_chapter_progression_requirement(10)
    
    if can_progress:
        # Momento emocional de realização
        call emotional_moment("final_achievement", None, "Realização de ter criado conexões suficientes para o final") from _call_emotional_moment_cap10_10
        
        narrator "[progress_message]"
        narrator "A jornada na república havia sido mais do que uma experiência de moradia. Foi um momento de transformação, onde os laços se fortaleceram e os corações se abriram."
        
        show samantha happy at left
        samantha "Parece que nossa república realmente nos uniu de uma forma especial, né?"
        hide samantha
        
        show nicole neutral at right
        nicole "Sim, há algo diferente no ar. Como se tivéssemos passado por uma transformação coletiva."
        hide nicole
        
        narrator "Era verdade. A república havia sido mais que um lugar para morar - havia sido um portal de transformação que nos uniu de formas que nunca imaginamos."
        
        jump epilogo
    else:
        # Momento emocional de crescimento
        call emotional_moment("final_growth_opportunity", None, "Oportunidade de crescimento através da reflexão final") from _call_emotional_moment_cap10_11
        
        narrator "[progress_message]"
        narrator "A jornada na república havia sido especial, mas senti que ainda havia muito a descobrir sobre essas pessoas incríveis que haviam se tornado parte da minha vida."
        
        show katia neutral at left
        katia "N-não é como se eu estivesse preocupada ou qualquer coisa assim... mas talvez precisemos de mais tempo para nos conhecer melhor."
        hide katia
        
        show camille gentle at right
        camille "Cada conexão tem seu próprio ritmo. A república foi apenas o início de nossa jornada."
        hide camille
        
        narrator "Ela estava certa. A república havia sido apenas o início. Havia muito mais para descobrir e viver juntos."
        
        menu:
            "Refletir sobre as conexões que ainda precisam ser exploradas":
                narrator "Decidi dedicar mais tempo a conhecer melhor cada pessoa. Cada interação era uma oportunidade de descobrir algo novo."
                jump capitulo10_final
                
            "Aceitar que algumas conexões levam tempo para se desenvolver":
                narrator "Entendi que a pressa não era necessária. As melhores conexões se desenvolvem naturalmente, no seu próprio tempo."
                jump capitulo10_final
                
            "Voltar ao menu principal":
                return
                
            "Tentar o Capítulo 10 novamente":
                jump capitulo10