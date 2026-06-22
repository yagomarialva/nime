label evento_cap7_huey:
    # Usando quintal como placeholder de praia ou cena generica
    scene bg praia_areia with dissolve
    
    narrator "A areia quente entrava entre meus dedos. Afastada da farofa principal, encontrei Huey."
    
    show huey bikini at center
    
    narrator "Ela estava de joelhos na areia úmida, segurando um baldinho de plástico rosa. Ela olhava para a água, depois para a areia, completamente paralisada."
    
    mc "Deu tela azul no cérebro da artista?"
    
    huey "Há muito movimento... O mar não fica parado pra eu processar a refração. Como eu posso moldar algo na areia se o modelo de inspiração é caótico?"
    
    mc "A ideia de um castelo de areia é que ele é temporário, Huey. Você não pinta ele, você esculpe."
    
    menu:
        "Fazer um morrinho básico e acabou. (Poupar energia)":
            mc "Olha, enche o balde, vira de cabeça pra baixo, tá pronto. Castelo minimalista."
            narrator "Huey encarou o morrinho de areia que eu fiz com profunda decepção artística."
            huey "Isso... isso ofende a simetria da natureza. Eu não me associo a esse monte de sujeira."
            $ add_affinity_points("huey", -10)
            
        "Ajudar a planejar um castelo de verdade. (Gastar 15 Energia e 20 Criatividade)":
            if store.player_stats["energy"] >= 15 and store.player_stats["creativity"] >= 20:
                $ update_player_stat("energy", -15)
                mc "Esquece o mar, Huey. Olha pra areia. A gente vai criar torres escoradas em arcos góticos concêntricos."
                narrator "Eu peguei um graveto e desenhei uma planta baixa complexa na areia úmida."
                mc "A gente cava um fosso ao redor para que a maré alimente o sistema de defesa, e não destrua o castelo. Usamos a concha para a textura das ameias."
                narrator "A mente de Huey voltou a funcionar a mil por hora. Os olhos dela brilharam."
                huey "Sim! A criatividade da impermanência! Nós seremos os deuses da sílica!"
                narrator "Nós passamos as próximas duas horas focados. Sujos de areia, sob o sol forte, erguemos uma réplica de areia de um forte medieval que fez até os turistas pararem para tirar foto."
                narrator "Huey deu um sorriso enorme, um raro momento de pura alegria focada."
                $ add_affinity_points("huey", 25)
            else:
                mc "Eu queria te ajudar a construir uma maravilha de areia, mas minha imaginação esgotou depois daquele incêndio."
                huey "O fogo queima as sinapses criativas... Descanse."
                
    hide huey
    return
