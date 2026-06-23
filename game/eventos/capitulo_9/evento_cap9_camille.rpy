label evento_cap9_camille:
    scene bg jardim_campus with dissolve
    
    narrator "O jardim do campus cheirava a incenso de sândalo. Camille havia montado uma tenda roxa com cortinas de miçangas."
    
    show camille neutral at center
    
    narrator "Ela estava embaralhando um deck de cartas de Tarô com a destreza de um crupiê de Las Vegas."
    
    mc "O negócio tá indo bem, mística?"
    
    camille "Os astros estão alinhados, mas as mentes destas pessoas estão nubladas. Um garoto acabou de perguntar se o Tarô previa a nota dele em Cálculo II."
    
    mc "E previa?"
    
    camille "A carta da 'Torre' é bem universal para destruição total. Mas sente-se. Preciso praticar uma leitura de aura combinada."
    
    menu:
        "Ficar de fora. (Poupar energia)":
            mc "Eu sou meio cético, Camille. Prefiro ajudar a vender os amuletos ali fora."
            camille "O ceticismo é só um escudo para o medo do desconhecido. Mas a ajuda é bem-vinda."
            $ add_affinity_points("camille", 5)
            
        "Ler o futuro. (Gastar 15 Energia e 20 Inteligência)":
            if store.player_stats["energy"] >= 15 and store.player_stats["intelligence"] >= 20:
                $ update_player_stat("energy", -15)
                mc "Leia meu futuro, então. Vamos ver se eu sobrevivo ao final do semestre."
                narrator "Ela pediu que eu estendesse a mão. Seus dedos longos e finos traçaram as linhas da minha palma."
                narrator "A pele dela era fria, mas causava arrepios quentes pelo meu braço."
                camille "Linha da vida forte. Linha do coração... confusa. Muitas conexões recentes. A casa nova abriu caminhos pra você."
                mc "O que quer dizer 'confusa'?"
                camille "Quer dizer que seu coração está sendo puxado para vários lados. Talvez... um desses lados seja mais místico do que você imagina."
                narrator "Ela levantou o olhar, e seus olhos negros fixaram nos meus. Foi impossível desviar."
                mc "Isso soa como um flerte disfarçado de leitura mística."
                camille "As cartas não flertam. Elas apenas revelam as verdades que a gente tenta esconder."
                narrator "Eu passei o resto da tarde na barraca dela. O incenso nunca cheirou tão bem."
                $ add_affinity_points("camille", 20)
            else:
                mc "Sabe, eu não quero saber se vou reprovar em alguma matéria. Deixa o mistério rolar."
                camille "Uma escolha sábia. O fardo do conhecimento não é para todos."
                $ add_affinity_points("camille", 10)
                
    hide camille
    return
