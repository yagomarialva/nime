label evento_cap9_samantha:
    scene bg biblioteca with dissolve
    
    narrator "A biblioteca do campus abriu o pátio externo para o festival. Samantha havia montado uma LAN party impressionante com monitores CRT e consoles dos anos 90."
    
    show samantha neutral at center
    
    narrator "Ela estava com uma chave de fenda na boca, fuçando na placa-mãe de um Super Nintendo aberto."
    
    mc "Operação a céu aberto?"
    
    samantha "O pino do controle 2 oxidou. Eu tenho dez moleques na fila pra jogar Street Fighter e só um controle tá funcionando."
    
    mc "Como eu ajudo, P2?"
    
    samantha "Preciso de um cabo de cobre limpo e que alguém segure o soldador enquanto eu uno o pino."
    
    menu:
        "Sair de fininho. (Poupar energia)":
            mc "Solda? Eu vou acabar botando fogo no campus e o Wendell me mata. Vou organizar a fila ali."
            samantha "Covarde. Mas obrigada por fazer o crowd control."
            $ add_affinity_points("samantha", 5)
            
        "Fazer a solda. (Gastar 15 Energia e 20 Criatividade)":
            if store.player_stats["energy"] >= 15 and store.player_stats["creativity"] >= 20:
                $ update_player_stat("energy", -15)
                mc "Me dá o soldador. Só me diz onde encostar o ferro."
                narrator "Me abaixei do lado dela. O espaço atrás das mesas era apertado. Nossos joelhos estavam se tocando."
                samantha "Cuidado. Isso aí chega a 300 graus. Encosta bem aqui no pino de cobre."
                narrator "Ela guiou a minha mão com a mão dela. Senti a respiração dela bem próxima do meu ouvido enquanto ela focava no chip."
                samantha "Um pouquinho mais pra esquerda. Isso. Perfeito."
                narrator "O pino brilhou. Ela ligou o console. A tela CRT piscou e o menu do Street Fighter apareceu."
                samantha "GG! Nós fizemos o boot na placa morta!"
                narrator "Ela olhou pra mim com os olhos brilhando de felicidade geek. A distância entre os nossos rostos era quase nula."
                mc "O pino foi fácil. Difícil é ganhar de você depois."
                samantha "Você sempre vai ser meu Player 2 preferido. Mas eu ainda vou te dar um perfect de Chun-Li."
                $ add_affinity_points("samantha", 20)
            else:
                mc "Eu posso arrumar um clipe de papel. Soldador é muito arriscado."
                samantha "Ah, gambiarra de hardware. Um clássico. Pega lá."
                $ add_affinity_points("samantha", 10)
                
    hide samantha
    return
