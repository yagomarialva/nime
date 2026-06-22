label evento_cap7_samantha:
    scene bg praia_cabana with dissolve
    
    narrator "A noite caiu, mas o barulho das ondas ainda era muito alto. Na varanda da casa de praia velha, Samantha estava encolhida no canto mais escuro possível."
    
    show samantha bikini at center
    
    narrator "Ela estava com os braços abraçando o corpo e a respiração ofegante."
    
    mc "O mundo aberto é grande demais?"
    
    samantha "Muito brilho, muito áudio sobreposto... Muitos NPCs que não seguem scripts lógicos..."
    
    narrator "A agorafobia dela tinha engolido suas defesas sociais. Sem o 'Bunker' (quarto escuro) e o PC, a realidade crua da praia era insuportável."
    
    menu:
        "Tenta fechar os olhos. (Poupar energia)":
            mc "Fica tranquila. Fica de olhos fechados até o sol nascer."
            samantha "Isso só amplifica a fobia... Meu cérebro cria renders de coisas piores."
            narrator "Ela tapou os ouvidos e se fechou em posição fetal."
            $ add_affinity_points("samantha", -5)
            
        "Fazer uma interface mental pra ela. (Gastar 15 Energia e 20 Inteligência)":
            if store.player_stats["energy"] >= 15 and store.player_stats["intelligence"] >= 20:
                $ update_player_stat("energy", -15)
                mc "Você tá renderizando o mapa inteiro de uma vez, Samantha. Isso derruba o frame rate do seu cérebro."
                narrator "Sentei ao lado dela e apontei pro céu escuro do mar."
                mc "Diminui o 'Draw Distance'. Foca ali naquelas três luzes brilhantes no oceano. São barcos de pesca."
                narrator "Ela piscou, tentando fixar o olhar nas luzes."
                mc "Reduz a barra de áudio master na sua mente. Isola os canais. O barulho de fundo é ruído branco, como uma fan de computador velha. Ouve só as três luzes."
                narrator "A respiração dela foi se acalmando, espelhando os conceitos de hardware que ela dominava e traduzindo para a vida real."
                samantha "Reduzindo Draw Distance... Reduzindo texturas volumétricas..."
                narrator "Os ombros dela caíram. A crise de pânico recuou."
                samantha "Obrigada por instalar o patch de otimização no meu cérebro, admin."
                narrator "Ela apoiou a cabeça de leve no meu ombro."
                $ add_affinity_points("samantha", 25)
            else:
                mc "Eu queria te ajudar, mas eu não sei o que fazer. Minha cabeça tá vazia."
                samantha "Sistema corrompido... Desculpe."
                
    hide samantha
    return
