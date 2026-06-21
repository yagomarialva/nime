label evento_katia_caixas:
    scene bg cinema with dissolve
    
    narrator "O escurinho do cinema universitário era o esconderijo perfeito. Apenas a luz bruxuleante de um projetor exibindo um filme mudo em preto e branco iluminava a sala."
    
    show katia neutral at center
    
    narrator "Katia estava na penúltima fileira, com os pés apoiados na cadeira da frente, os olhos fixos na imagem monocromática."
    
    mc "O expressionismo alemão é o seu esconderijo oficial da restauração da casa?"
    
    katia "O termo correto é 'preservando minha sanidade longe da ditadora impecável'. E se você veio me dar bronca, pode dar meia volta. A Nicole já fez um cronograma de limpeza que incluiu até os rodapés. Quem liga para rodapés?"
    
    mc "Ela parece bem focada em não perder a bolsa."
    
    narrator "Katia bufou, virando o rosto levemente para a tela."
    
    katia "Todo mundo ali precisa daquela casa, gênio. A diferença é que alguns de nós não acham que lamber o chão vai impedir a faculdade de cancelar o projeto quando eles quiserem."
    
    narrator "Ela suspirou, a fachada agressiva cedendo só um pouquinho enquanto o filme ficava mais melancólico."
    
    katia "De qualquer forma... eu deixei minhas caixas de filmes e equipamento lá na porta da casa. São pesadas pra caramba. E não, eu não estou pedindo pra você me ajudar."
    
    menu:
        "Deixar ela se virar. (Poupar energia)":
            mc "Bom, acho que as lentes e os filmes vão ter que criar pernas e subir as escadas sozinhos."
            katia "Hmph. Como se eu precisasse de você. Vai lá viver a sua vida."
            $ add_affinity_points("katia", -5)
            
        "Eu posso te ajudar a subir com isso. (Gastar 15 Energia)":
            if store.player_stats["energy"] >= 15:
                $ update_player_stat("energy", -15)
                mc "Mesmo você não pedindo, eu ajudo você a carregar tudo pro seu quarto. Depois disso, você me deve uma."
                narrator "Katia virou o rosto na direção contrária, cruzando os braços, mas eu consegui notar um leve rubor de alívio."
                katia "B-bom... se você está insistindo tanto assim, não vou te impedir. Mas saiba que eu daria conta sozinha. ...E, hã, obrigada. Mas só um pouco!"
                $ add_affinity_points("katia", 20)
            else:
                mc "Eu até ajudaria, mas eu não consigo nem carregar meu próprio peso hoje."
                katia "Não faz diferença. Eu dou um jeito, como sempre."

    hide katia
    return

label evento_katia_filme:
    scene bg cinema with dissolve
    narrator "Katia estava mais uma vez no escuro do cinema, desta vez assistindo a um clássico de terror cult."
    mc "Vindo procurar dicas de sobrevivência pra nossa casa velha?"
    katia "Se a casa for mal-assombrada, a Nicole com certeza vai querer que o fantasma assine o cronograma de limpeza."
    narrator "Nós rimos juntos, no escuro."
    $ add_affinity_points("katia", 10)
    return
