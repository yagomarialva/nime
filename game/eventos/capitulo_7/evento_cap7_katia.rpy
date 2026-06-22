label evento_cap7_katia:
    scene bg praia_areia with dissolve
    
    narrator "Na varanda esburacada da cabana, Katia segurava a jaqueta de couro que sempre usa."
    
    show katia bikini at center
    
    narrator "Ela cheirou o tecido escuro. O cheiro forte de fuligem não saía por nada."
    
    mc "Lavou com água do mar?"
    
    katia "Lavei. Esfreguei com areia. Deixei no vento. O cheiro de queimado não sai."
    
    narrator "Ela apertou a jaqueta contra o peito, os olhos brilhando de fúria contida."
    
    katia "Sabe por que a Rua Aurora importava tanto pra mim? Eu já dormi no chão frio do metrô. Já dormi em pensão onde o dono me assediava. A casa... era a minha fortaleza. Minha porta tinha tranca dupla."
    
    katia "O fogo levou o primeiro lugar no mundo onde eu não precisava dormir com uma faca debaixo do travesseiro."
    
    mc "A gente vai voltar pra lá, Katia."
    
    menu:
        "O mundo é cruel mesmo. (Poupar energia)":
            mc "Nada dura para sempre. Tem que se adaptar de novo."
            katia "É. Essa é a regra das ruas, né?"
            narrator "Ela vestiu a jaqueta fedendo a fumaça e se afastou."
            $ add_affinity_points("katia", -5)
            
        "Prometer restaurar as trancas. (Gastar 15 Energia e 20 Criatividade)":
            if store.player_stats["energy"] >= 15 and store.player_stats["creativity"] >= 20:
                $ update_player_stat("energy", -15)
                mc "Aquela tranca dupla não vai ser nada perto do que eu vou instalar pra você."
                katia "Do que você tá falando?"
                mc "Eu tirei a planta do quarto queimado antes de sairmos. Vamos desenhar uma estante falsa embutida. O seu novo quarto não vai ter só uma tranca, vai ter uma parede secreta."
                narrator "Peguei um graveto e desenhei o projeto arquitetônico maluco na madeira da varanda."
                narrator "Katia acompanhou o desenho, e o rosto endurecido dela foi suavizando."
                katia "Uma porta falsa por trás de uma prateleira de livros? Isso é estúpido... e perfeito."
                narrator "Ela abriu um sorriso largo."
                katia "Eu vou cobrar essa porta, admin. Não vá quebrar a promessa."
                $ add_affinity_points("katia", 25)
            else:
                mc "Queria ter uma ideia melhor pra consertar sua porta, mas minha cabeça tá travada."
                katia "Não precisa prometer o que não pode cumprir. Relaxa."
                
    hide katia
    return
