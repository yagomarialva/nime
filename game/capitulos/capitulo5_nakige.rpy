# capitulo5_nakige.rpy - MOMENTO EMOCIONAL CENTRAL DA HISTÓRIA

# === MOMENTO NAKIGE ESTRATÉGICO - PONTO DE VIRADA EMOCIONAL ===
label capitulo5_momento_reflexao:
    
    # Configuração atmosférica para o momento
    scene bg casa_noite with dissolve
    # play music "emotional_theme.ogg" fadein 2.0  # Arquivo de música opcional
    
    narrator "Era uma das últimas noites de maio. A casa estava em silêncio, mas minha mente fervilhava de pensamentos."
    narrator "Há algumas semanas, éramos apenas estranhos jogados juntos pelo acaso."
    narrator "Agora... éramos algo mais. Uma família escolhida, talvez."
    
    # Momento de reflexão profunda do protagonista
    scene bg quarto_protagonista with dissolve
    
    narrator "Sentado na cama, folheei as fotos no meu celular - momentos capturados nessas semanas intensas."
    narrator "A primeira foto no café com Nicole e Camille... O sorriso de Larissa após vencer no vôlei..."
    narrator "A expressão concentrada de Katia editando um de seus filmes... Samantha explicando D&D com paixão..."
    narrator "E Huey... sempre Huey, vendo arte onde outros viam apenas objetos comuns."
    
    # === REALIZAÇÃO EMOCIONAL (TÉCNICA NAKIGE) ===
    call emotional_moment("realization", None, "Consciência sobre a importância das conexões formadas") from _call_emotional_moment_cap5_nakige_1
    
    narrator "Foi então que a realização me atingiu como uma onda:"
    narrator "Eu não estava mais aprendendo apenas sobre arte ou comunicação na faculdade."
    narrator "Estava aprendendo sobre conexão humana. Sobre como pessoas diferentes podem se completar."
    narrator "Sobre como o amor - em todas as suas formas - pode surgir nos momentos mais inesperados."
    
    # Batida na porta - momento de vulnerabilidade compartilhada
    # play sound "knock.ogg"  # Arquivo de som opcional
    narrator "Uma batida suave na porta interrompeu meus pensamentos."
    
    # A personagem com maior afinidade aparece para um momento íntimo
    $ afinidades = {
        "camille": points_camille,
        "samantha": points_samantha,
        "nicole": points_nicole,
        "katia": points_katia,
        "huey": points_huey,
        "larissa": points_larissa
    }
    $ personagem_especial = max(afinidades, key=afinidades.get)
    
    if afinidades[personagem_especial] >= 20:
        if personagem_especial == "camille":
            jump momento_camille_vulnerabilidade
        elif personagem_especial == "samantha":
            jump momento_samantha_vulnerabilidade
        elif personagem_especial == "nicole":
            jump momento_nicole_vulnerabilidade
        elif personagem_especial == "katia":
            jump momento_katia_vulnerabilidade
        elif personagem_especial == "huey":
            jump momento_huey_vulnerabilidade
        elif personagem_especial == "larissa":
            jump momento_larissa_vulnerabilidade
    else:
        jump momento_coletivo_vulnerabilidade

# === MOMENTOS INDIVIDUAIS DE VULNERABILIDADE ===
label momento_camille_vulnerabilidade:
    show camille sad at center
    camille "Posso entrar? Eu... senti que você estava pensando em algo importante."
    "[nome]" "Como você sempre sabe essas coisas?"
    
    call emotional_moment("vulnerability", "camille", "Camille compartilha seus medos sobre ser aceita") from _call_emotional_moment_cap5_nakige_2
    
    camille "Às vezes eu me sinto como se vivesse em um mundo diferente de todo mundo..."
    camille "Como se as coisas que vejo e sinto fossem 'loucura' para os outros."
    camille "Mas com vocês... pela primeira vez me sinto... normal. Aceita."
    
    narrator "Lágrimas começaram a formar nos olhos de Camille, e meu coração se apertou."
    
    menu:
        "Abraçá-la e dizer que ela é especial exatamente como é":
            $ feedback = add_affinity_points("camille", 15, "Momento de aceitação profunda")
            $ growth = trigger_character_growth("camille", "confidence")
            narrator "[feedback]"
            narrator "[growth]"
            camille "Obrigada... por me ver de verdade."
            
        "Dividir suas próprias inseguranças com ela":
            $ feedback = add_affinity_points("camille", 12, "Vulnerabilidade mútua")
            $ player_empathy_level += 10
            narrator "Abri meu coração sobre minhas próprias dúvidas e medos."
            camille "Não estamos sozinhos em nossas estranhezas..."
    
    $ add_shared_memory("midnight_vulnerability", ["camille"], "A noite em que compartilhamos nossas vulnerabilidades mais profundas")
    
    jump momento_final_nakige

label momento_samantha_vulnerabilidade:
    show samantha sad at center
    samantha "Ei... não consegui dormir. Você também está acordado?"
    
    call emotional_moment("vulnerability", "samantha", "Samantha revela pressões sobre suas ambições") from _call_emotional_moment_cap5_nakige_3
    
    samantha "Sabe... às vezes me pergunto se eu não estou tentando demais ser a garota animada o tempo todo."
    samantha "Como se fosse minha obrigação sempre levantar o astral de todo mundo..."
    samantha "Mas e quando eu precisar de alguém? Quem vai levantar o MEU astral?"
    
    narrator "Era a primeira vez que via Samantha tão vulnerável. Meu coração se partiu um pouco."
    
    menu:
        "Assegurar que ela pode contar comigo sempre":
            $ feedback = add_affinity_points("samantha", 15, "Promessa de apoio incondicional")
            $ growth = trigger_character_growth("samantha", "wisdom")
            samantha "Isso... isso significa tudo para mim."
            
        "Lembrar momentos em que ela foi forte sem forçar":
            $ feedback = add_affinity_points("samantha", 12, "Reconhecimento de sua autenticidade")
            samantha "Você realmente me vê, não é? A pessoa real por trás da máscara alegre."
    
    jump momento_final_nakige

# === MOMENTO FINAL NAKIGE - CLÍMAX EMOCIONAL ===
label momento_final_nakige:
    scene bg casa_sala_noite with fade
    
    # Todas as garotas se reúnem espontaneamente
    show nicole neutral at center
    show katia neutral at left
    show samantha happy at right
    
    hide nicole
    hide katia
    hide samantha
    
    show larissa neutral at center
    show huey neutral at left
    show camille gentle at right
    
    narrator "Como se fosse por magia, todas as garotas apareceram na sala comum."
    narrator "Nenhuma palavra foi dita, mas todas sabíamos que algo especial estava acontecendo."
    
    nicole "Engraçado... nenhuma de nós conseguiu dormir hoje."
    katia "Talvez seja porque todos sentimos que algo está mudando."
    larissa "Esta casa... vocês... mudaram tudo para mim."
    huey "Eu nunca me senti tão... compreendida antes."
    samantha "É como se tivéssemos encontrado nossa verdadeira família."
    camille "As energias aqui... elas estão dizendo que este momento é sagrado."
    
    # === CRESCIMENTO COLETIVO (MOMENTO MAIS PODEROSO) ===
    call emotional_moment("realization", None, "Reconhecimento mútuo do amor familiar que foi construído") from _call_emotional_moment_cap5_nakige_4
    
    narrator "O silêncio que se seguiu foi quebrado apenas pelos soluços contidos."
    narrator "Não eram lágrimas de tristeza - eram lágrimas de gratidão pura."
    narrator "Gratidão por termos encontrado uns aos outros."
    narrator "Gratidão por este momento perfeito que jamais seria esquecido."
    
    # Todas crescem como pessoas
    $ trigger_character_growth("nicole", "wisdom")
    $ trigger_character_growth("katia", "wisdom") 
    $ trigger_character_growth("samantha", "wisdom")
    $ trigger_character_growth("larissa", "wisdom")
    $ trigger_character_growth("huey", "wisdom")
    $ trigger_character_growth("camille", "wisdom")
    $ add_affinity_points("nicole", 10, "Momento de conexão familiar")
    $ add_affinity_points("katia", 10, "Momento de conexão familiar")
    $ add_affinity_points("samantha", 10, "Momento de conexão familiar")
    $ add_affinity_points("larissa", 10, "Momento de conexão familiar")
    $ add_affinity_points("huey", 10, "Momento de conexão familiar")
    $ add_affinity_points("camille", 10, "Momento de conexão familiar")
    
    # Memória mais importante do jogo
    $ add_shared_memory("family_realization", ["nicole", "katia", "samantha", "larissa", "huey", "camille"], "A noite em que descobrimos que éramos uma família")
    
    show screen emotional_moment_notification("💖 Vocês descobriram que o amor não precisa ser romântico para ser eterno...")
    pause 4.0
    hide screen emotional_moment_notification
    
    narrator "Naquela noite, todos dormimos na sala, espalhados em sofás e almofadas."
    narrator "Porque ninguém queria quebrar a magia daquele momento."
    narrator "Porque havíamos descoberto que 'lar' não é um lugar - são as pessoas que escolhemos amar."
    
    scene black with fade
    centered "{color=#FFD700}Este momento ficará para sempre gravado em seus corações...{/color}"
    
    return

# === MOMENTO COLETIVO PARA BAIXA AFINIDADE ===
label momento_coletivo_vulnerabilidade:
    narrator "Ouvi vozes baixas vindo da sala."
    scene bg casa_sala_noite with dissolve
    
    narrator "Todas as garotas estavam reunidas, conversando em tons sussurrados."
    narrator "Ao me ver, elas sorriram e me convidaram para sentar com elas."
    
    call emotional_moment("realization", None, "Consciência de que ainda há muito para descobrir sobre cada uma") from _call_emotional_moment_cap5_nakige_5
    
    narrator "Naquele momento, percebi que ainda havia muito para aprender sobre cada uma delas."
    narrator "E que talvez, o verdadeiro tesouro não fosse encontrar o amor romântico..."
    narrator "Mas sim construir laços genuínos que durassem além da faculdade."
    
    $ add_affinity_points("nicole", 5, "Momento de conexão coletiva")
    $ add_affinity_points("katia", 5, "Momento de conexão coletiva")
    $ add_affinity_points("samantha", 5, "Momento de conexão coletiva")
    $ add_affinity_points("larissa", 5, "Momento de conexão coletiva")
    $ add_affinity_points("huey", 5, "Momento de conexão coletiva")
    $ add_affinity_points("camille", 5, "Momento de conexão coletiva")
    
    jump momento_final_nakige