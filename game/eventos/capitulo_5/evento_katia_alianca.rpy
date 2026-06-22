label evento_katia_alianca:
    scene bg cozinha_escura with dissolve
    
    narrator "Um cheiro de queimado terrível invadia o corredor."
    
    show katia angry at center
    
    narrator "Katia estava tossindo no meio de uma nuvem de fumaça cinza, batendo uma toalha perto da panela."
    
    mc "Katia! Você tá invocando demônios?"
    
    katia "Cala a boca! O azeite ferveu rápido demais."
    
    narrator "Olhei pra tábua de cortar. Havia vegetais perfeitamente (ou quase) picados e uma receita aberta no celular. Ratatouille."
    
    mc "Desde quando você faz pratos franceses requintados? Seu café da manhã é Red Bull com Doritos."
    
    katia "É pra... ela. Pra patricinha da sala."
    
    narrator "Katia desviou o olhar, as orelhas ligeiramente vermelhas."
    
    katia "A idiota não desce pra comer há dois dias. Se ela morrer de inanição, aquela mãe bruxa dela ganha. Eu só não quero que a bruxa ganhe."
    
    menu:
        "Ela nem vai notar o esforço. (Poupar energia)":
            mc "Sinceramente, a Nicole não parece o tipo de pessoa que come gororoba queimada. Deixa isso pra lá."
            katia "Sabe de uma coisa? Você tem razão. Pra que me importar com o paladar da realeza?"
            narrator "Ela jogou tudo no lixo, frustrada."
            $ add_affinity_points("katia", -10)
            
        "Me dá a faca. Vamos consertar isso. (Gastar 15 Energia)":
            if store.player_stats["energy"] >= 15:
                $ update_player_stat("energy", -15)
                mc "O fogo tava muito alto e você não secou a abobrinha. Sai da frente. Eu pico os tomates, você faz o molho em fogo médio."
                narrator "Katia bufou, mas me entregou a faca sem reclamar."
                katia "Não espalha isso por aí. Eu tenho uma reputação de misantropa pra manter."
                mc "O seu segredo está seguro comigo. É muito legal da sua parte fazer isso."
                katia "Eu só não gosto de intimidação. A velha acha que pode comprar as pessoas."
                narrator "Passamos uma hora na cozinha em um silêncio muito confortável. Quando o prato saiu, não tinha gosto de fumaça."
                $ add_affinity_points("katia", 20)
            else:
                mc "Eu até te ajudaria a salvar o almoço, mas eu mal consigo parar em pé."
                katia "Relaxa, inútil. Eu me viro. Pode ir dormir."
                
    hide katia
    return
