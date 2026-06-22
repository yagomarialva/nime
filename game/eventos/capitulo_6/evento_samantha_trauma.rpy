label evento_samantha_trauma:
    scene bg sala_jantar with dissolve
    
    narrator "Como o segundo andar foi selado, a sala de jantar virou nosso acampamento coletivo. Colchões no chão e roupas de cama empilhadas."
    
    show samantha sad at center
    
    narrator "Samantha estava abraçando os joelhos num canto escuro, com os fones de ouvido desligados no pescoço."
    
    mc "Perder o 'bunker' pegou pesado, né?"
    
    samantha "Meu espaço seguro virou carvão. Meu setup tá fedendo a fumaça."
    
    narrator "Ela tremia levemente. Ter que conviver em espaço aberto com outras pessoas vinte e quatro horas por dia estava destruindo os limites sociais dela."
    
    menu:
        "Você acostuma com a gente dormindo aqui. (Poupar energia)":
            mc "É temporário. Você sobrevive dormindo no chão da sala com as meninas."
            samantha "Você diz isso como se fosse fácil ter a Katia roncando e a Nicole reclamando o tempo todo..."
            narrator "Ela colocou os fones de volta, isolando-se completamente."
            $ add_affinity_points("samantha", -5)
            
        "Fazer uma cabana de cobertores. (Gastar 15 Energia e 10 Carisma)":
            if store.player_stats["energy"] >= 15 and store.player_stats["charisma"] >= 10:
                $ update_player_stat("energy", -15)
                mc "Você não perdeu o bunker. Você só vai fazer um upgrade pra um bunker tático e portátil."
                narrator "Eu peguei o varal de chão desmontável, estiquei os cobertores mais grossos por cima dele e coloquei perto do sofá, criando uma tenda fechada no meio da sala."
                mc "Entra. O controle de acesso é seu. Ninguém perturba o QG da tenda."
                narrator "Ela olhou pra tenda e depois pra mim. Os olhos dela encheram d'água."
                samantha "Um spawn point... temporário."
                narrator "Ela rastejou pra dentro da cabana, puxando o notebook, e finalmente relaxou os ombros. Da escuridão debaixo da coberta, ouvi uma voz suave."
                samantha "Obrigada, admin..."
                $ add_affinity_points("samantha", 25)
            else:
                mc "Eu queria poder fazer algo pra te isolar, mas eu não sei conversar e tô cansado demais agora."
                samantha "Eu sei. Fica tranquilo. Eu lido com meus debuffs de sanidade."
                
    hide samantha
    return
