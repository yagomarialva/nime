label evento_cap8_biblioteca:
    scene bg biblioteca with dissolve
    
    narrator "A biblioteca do campus cheirava a poeira, mas na mesa do fundo, Samantha e Huey quebravam o silêncio com o barulho alto de um vídeo no YouTube."
    
    show samantha neutral at left
    show huey neutral at right
    
    narrator "O vídeo mostrava um homem de meia idade ensinando a aplicar argamassa."
    
    samantha "Eu não entendo a hitbox desse azulejo. Ele espalha a massa de forma assimétrica e a física do cimento não cola!"
    
    huey "Samantha, você está aplicando regras de renderização poligonal em fluidos não-newtonianos do mundo real. O atrito depende do material."
    
    mc "Como está o projeto da reforma, equipe técnica?"
    
    samantha "Estamos baixando todos os tutoriais de 'Do It Yourself' da internet. Mas a UI do mundo real é muito punitiva."
    
    menu:
        "Isso vai dar muito errado. (Poupar energia)":
            mc "Assistir YouTube não vai fazer a gente construir uma parede de dry-wall. Vamos focar em só pintar o que tá sujo."
            huey "Subestimar a capacidade geométrica humana é um erro."
            $ add_affinity_points("samantha", -5)
            
        "Fazer engenharia reversa. (Gastar 15 Energia e 20 Inteligência)":
            if store.player_stats["energy"] >= 15 and store.player_stats["intelligence"] >= 20:
                $ update_player_stat("energy", -15)
                mc "Esquece a física do vídeo. Pense na casa como um código legado, Samantha. E Huey, pense nas ferramentas como linhas de perspectiva."
                narrator "Peguei o caderno da Huey e comecei a desenhar um grid de alinhamento."
                mc "Nós não vamos 'construir'. Vamos criar uma ilusão ótica. Vamos aplicar gesso apenas nos ângulos de visão do Professor Wendell quando ele entrar pela porta. A gente esconde o dano principal com os móveis."
                samantha "Um truque de câmera! Um culling de oclusão!"
                huey "Enganar os olhos usando geometria e sombra... Sim. Reduz o tempo de obra em 80%% e resolve a parte estética."
                narrator "As duas deram um *high-five* completamente descoordenado, derrubando um estojo de lápis."
                $ add_affinity_points("samantha", 25)
                $ add_affinity_points("huey", 25)
            else:
                mc "Eu ia tentar ajudar vocês a entenderem os cálculos, mas minha cabeça tá doendo só de ver esse vídeo de argamassa."
                samantha "Deixa com o processador duplo aqui. Pode descansar."
                
    hide samantha
    hide huey
    return
