# === EVENTO KATIA E SAMANTHA - MASTER EDITION (CORRIGIDO) ===
# Tema: Alta Cultura vs Cultura Pop

label evento_katia_samantha:
    # Pequeno ganho de afinidade inicial apenas pelo encontro
    $ points_katia += 1
    
    # Usando o cenário definido em scenarios.rpy 
    scene bg cinema with dissolve
    
    # Atmosfera antes da ação
    narrator "A sala de cinema estava mergulhada na penumbra. O cheiro de pipoca amanteigada lutava contra o odor de carpete antigo."
    narrator "Eu procurava meu lugar, mas parecia que alguém já tinha reivindicado o território ao lado."

    # Usando 'katia angry' pois não há 'annoyed' definido 
    show katia angry at left
    
    # Katia resmungando sozinha
    katia "Tsc. Inacreditável. Trouxeram nachos. Para um filme expressionista de três horas, alguém teve a audácia de trazer nachos."
    
    narrator "A garota de óculos ao meu lado anotava furiosamente em um caderno, sem nem levantar os olhos para a tela."
    
    # O MC toma a iniciativa
    mc "Com licença... acho que a poltrona ao lado é minha. Espero que meu silêncio seja aprovado pela crítica."
    
    # Mudança para neutro ao reconhecer o jogador 
    show katia neutral
    
    katia "Ah. É você. [nome], certo?"
    katia "Se veio assistir 'O Silêncio do Vazio', espero que tenha lido a tese do diretor antes. Não é obra para amadores."
    
    # Samantha entra (Genki Girl) 
    show samantha happy at right with moveinright
    
    samantha "Licença! Licença! Uau, desculpa o atraso! A fila da pipoca estava uma quest de nível final!"
    
    # O conflito imediato
    show katia angry
    
    katia "Shhh! O trailer nem começou e você já está quebrando a imersão diegética."
    
    samantha "Oh! Oi, [nome]! E... oi, garota séria! Caramba, esse cinema é retrô mesmo, né? Parece aquela cutscene de abertura de jogo pós-apocalíptico!"
    
    katia "Pós-apocalíptico...? Este é o último bastião de projeção em 35mm da cidade. Não compare com joguinhos."
    
    samantha "Eh? Mas jogos são arte também! A narrativa ambiental aqui é incrível."
    
    narrator "Katia parecia prestes a ter um colapso nervoso. Samantha sorria, alheia ao ódio que emanava da poltrona ao lado."
    
    # === MENU DE ESCOLHA 1 ===
    menu:
        "Elogiar a estética da película (Apoiar Katia)":
            $ points_katia += 3
            
            mc "Sabe, Katia... tem algo nessa granulação do 35mm. O digital é muito limpo, mas a película tem uma textura orgânica."
            
            # Expressão definida em 
            show katia blush
            katia "Hmpf..."
            katia "Pelo menos alguém aqui tem olhos funcionais. A textura é a alma da memória. O digital é apenas... dados frios."

        "Comparar o enredo com jogos complexos (Apoiar Samantha)":
            $ points_samantha += 3
            
            mc "Sinceramente, Samantha, essa vibe me lembra muito 'Bioshock'. Aquele clima que conta a história do lugar sem dizer uma palavra."
            
            # Mantendo 'happy' pois não há 'stars_eyes' 
            show samantha happy
            samantha "SIM! Exatamente! É a 'narrativa emergente'! Sabia que você ia entender a referência!"
            
            # Usando 'angry' para desgosto/disgust 
            show katia angry
            katia "Você acabou de comparar arquitetura clássica com... um jogo de tiro?"

        "Pedir foco no filme (Neutro)":
            $ points_katia += 1
            $ points_samantha += 1
            
            mc "Ei, as luzes estão apagando. Vamos deixar a obra falar por si mesma agora, ok?"
            
            show katia neutral
            katia "Finalmente. Respeito ao ritual."
            show samantha neutral
            samantha "Ops! *Zip*. Modo furtivo ativado."

    # === TRANSIÇÃO DE TEMPO ===
    # Usando cenário definido em scenarios.rpy 
    scene bg cinema_lobby with fade
    
    narrator "Duas horas de silêncios longos e metáforas visuais depois..."
    
    show katia neutral at left
    # Usando neutral para 'thinking' 
    show samantha neutral at right
    
    samantha "..."
    katia "..."
    
    samantha "Então... o protagonista estava morto o tempo todo ou foi um glitch na simulação?"
    
    katia "Não é um 'glitch'. É uma alegoria existencialista sobre a incapacidade de comunicação."
    
    samantha "Hmmm. Profundo. Tipo quando seu save corrompe e você perde 50 horas de progresso. Aquele vazio no peito... é existencialismo puro."
    
    # Momento de virada
    show katia neutral
    
    narrator "Katia parou de limpar seus óculos por um segundo."
    
    katia "Essa... foi uma analogia vulgar. Mas... não totalmente imprecisa."
    katia "A sensação de perda irreversível de dados... Suponho que seja uma forma moderna de luto."
    
    show samantha happy
    samantha "Viu?! A gente sente a mesma coisa! Só usamos controles diferentes!"
    
    # === MENU DE ESCOLHA 2 ===
    menu:
        "Argumentar sobre a agência do jogador (Apoiar Jogos)":
            $ points_samantha += 2
            
            mc "Acho que a Samantha tem um ponto. No jogo, você sente culpa porque *você* tomou a decisão."
            
            samantha "Isso! A culpa é sua, a vitória é sua. A imersão é total!"
            
            katia "Interessante... A responsabilidade do espectador tornada ativa. Hmmm."

        "Defender a visão do Diretor (Apoiar Cinema)":
            $ points_katia += 2
            
            mc "Mas Katia está certa sobre a visão única. A arte não é uma democracia."
            
            katia "Exato. Você não 'escolhe' o final de uma sinfonia."
            
            samantha "Mas e os mods? A comunidade criando junto... isso não é bonito também?"

        "Propor o Desafio da Mídia Cruzada (União)":
            $ points_katia += 2
            $ points_samantha += 2
            
            mc "Ok, tive uma ideia. Katia joga um jogo narrativo, Samantha assiste um clássico cult. E a gente debate."
            
            show samantha happy
            samantha "Aceito! Vou trazer meu console portátil!"
            
            show katia blush
            katia "Eu não possuo... consoles. Mas... se for para fins de análise comparativa..."
            katia "Talvez eu tolere a experiência."

    # === FECHAMENTO DO EVENTO ===
    
    narrator "Saímos do cinema sob a luz dos postes de rua."
    
    show katia angry
    katia "Não pense que isso muda minha opinião. Cinema ainda é superior."
    show katia neutral
    katia "Mas... suas observações não foram completamente descartáveis hoje."
    
    show samantha happy
    samantha "Yay! Na próxima, vou te mostrar trilhas sonoras de RPG!"
    
    katia "Não force a amizade."
    
    mc "Acho que isso é um começo."
    
    # Memória compartilhada
    $ add_shared_memory("clash_of_arts", ["katia", "samantha"], "Debate sobre existencialismo e saves corrompidos.")

    return