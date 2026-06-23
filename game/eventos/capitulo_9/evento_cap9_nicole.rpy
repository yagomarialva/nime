label evento_cap9_nicole:
    scene bg estacionamento with dissolve
    
    narrator "O estacionamento do campus foi isolado e transformado em uma passarela improvisada. Nicole organizava uma arara gigante de roupas brilhantes."
    
    show nicole happy at center
    
    narrator "Ela estava no seu elemento natural, dando ordens e ajustando tecidos."
    
    mc "A Vogue chegou ao campus."
    
    nicole "O desfile é em uma hora e a minha modelo de manequim sumiu! Eu tô surtando!"
    
    mc "Calma, respira. Como eu te ajudo?"
    
    nicole "Eu preciso de alguém com bom gosto pra combinar os acessórios enquanto eu faço as dobras nas calças."
    
    menu:
        "Passar a bola. (Poupar energia)":
            mc "Moda não é comigo, Nicole. Vou carregar as caixas pesadas pra você."
            nicole "Ai, tá bom, força bruta também serve."
            $ add_affinity_points("nicole", 5)
            
        "Assumir o figurino. (Gastar 15 Energia e 20 Carisma)":
            if store.player_stats["energy"] >= 15 and store.player_stats["charisma"] >= 20:
                $ update_player_stat("energy", -15)
                mc "Ouro com veludo vermelho e prata com seda azul. Deixa os colares comigo."
                narrator "Comecei a separar as peças. Nicole me observou pelo canto do olho, claramente impressionada com a minha rapidez."
                nicole "Pra alguém que só veste camiseta de anime, você tem um senso cromático ótimo."
                mc "A gente aprende as coisas convivendo com a patricinha da casa."
                narrator "Ela riu, jogando o cabelo pra trás."
                nicole "Vem cá, me deixa arrumar essa sua gola amassada."
                narrator "Ela se aproximou, quase encostando no meu peito, e ajustou a gola da minha jaqueta."
                narrator "O perfume caro dela me invadiu. Ela olhou nos meus olhos de perto, sorrindo."
                nicole "Se você quiser, eu faço um projeto inteiro focado só em te arrumar."
                mc "Isso é um flerte ou você só odeia as minhas roupas?"
                nicole "Os dois. E você gosta das duas coisas."
                $ add_affinity_points("nicole", 20)
            else:
                mc "Eu vou acabar estragando essas roupas caras. Melhor eu ficar aqui vigiando."
                nicole "Tudo bem, a intenção é o que conta. E não amassa as camisas ali!"
                $ add_affinity_points("nicole", 10)
                
    hide nicole
    return
