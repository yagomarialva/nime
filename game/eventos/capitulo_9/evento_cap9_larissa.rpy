label evento_cap9_larissa:
    scene bg ginasio with dissolve
    
    narrator "O ginásio estava barulhento. A barraca da Larissa era, na verdade, apenas uma mesa de madeira robusta com um cartaz: 'Derrote a Fera e Ganhe um Doce'."
    
    show larissa happy at center
    
    narrator "Larissa acabara de derrotar um calouro do time de futebol americano. Ele saiu esfregando o pulso, chocado."
    
    larissa "Próximo! O algodão doce não vai se comer sozinho!"
    
    mc "Precisa de ajuda aí, campeã?"
    
    larissa "Você! Chegou bem na hora. Senta aí. Preciso de um aquecimento."
    
    mc "Eu? Eu não sou do time de futebol."
    
    larissa "Não importa. Eu pego leve. Se você ganhar, o algodão doce é seu."
    
    menu:
        "Desistir. (Poupar energia)":
            mc "Não quero quebrar meu braço, Larissa. Eu só vim trazer umas garrafas d'água."
            larissa "Fraco! Mas valeu pela água."
            $ add_affinity_points("larissa", 5)
            
        "Enfrentar a Fera. (Gastar 15 Energia e 20 Físico)":
            if store.player_stats["energy"] >= 15 and store.player_stats["fitness"] >= 20:
                $ update_player_stat("energy", -15)
                mc "Prepara o algodão doce. Eu ajudei a lixar as paredes de casa, meus braços estão de aço."
                narrator "Sentei na frente dela. Nossas mãos se apertaram."
                narrator "O toque da mão da Larissa era firme, calejado do boxe, mas estranhamente quente."
                narrator "Katia, que passava por ali, gritou: 'Vai, Larissa! Quebra ele!'"
                narrator "Nós fizemos força. Eu resisti o máximo que pude. Por um segundo, vi Larissa corar pelo esforço... ou talvez por eu estar segurando a mão dela com tanta força."
                larissa "Você... tá mais forte... do que eu pensava!"
                narrator "No fim, ela ainda venceu, mas suou."
                larissa "Justo. Você não quebrou fácil. Toma um algodão doce pela bravura."
                narrator "Ela me entregou o doce, ainda ofegante, com um sorriso brilhante que fez meu coração errar a batida."
                $ add_affinity_points("larissa", 20)
            else:
                mc "Eu ia tentar, mas meus braços ainda tão doendo da lixa do Professor Wendell."
                larissa "Hahaha! Deixa pra próxima então. Fica no balcão cobrando os tickets pra mim."
                $ add_affinity_points("larissa", 10)
                
    hide larissa
    return
