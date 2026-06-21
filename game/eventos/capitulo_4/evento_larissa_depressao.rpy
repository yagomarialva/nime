label evento_larissa_depressao:
    # Como não há background específico do quarto da Larissa definido nas imagens com esse nome explícito, 
    # usaremos casa_interior ou quarto_protagonista genérico, mas vamos criar o clima.
    scene bg casa_interior with dissolve
    
    narrator "A porta do quarto da Larissa estava encostada. Bati de leve e entrei."
    
    show larissa sad at center
    
    narrator "O quarto cheirava a pomada muscular e poeira. Ela estava sentada na cama, a perna esticada sobre um travesseiro, usando uma tala imensa."
    narrator "Os troféus de atletismo dela estavam todos virados para a parede."
    
    larissa "Veio me dar o sermão do 'vai ficar tudo bem'?"
    
    mc "Não. Vim ver se você ainda sabe respirar."
    
    larissa "Respirar eu sei. Eu só não sei... pra quê. Sem a corrida, eu sou só uma garota burra que ocupa espaço."
    
    narrator "A voz dela falhou. A energia contagiante tinha sido esvaziada."
    
    menu:
        "Dizer que a vida é mais que corrida. (Poupar energia)":
            mc "Você ainda tem a gente. O edital não vai te expulsar porque você machucou o joelho."
            larissa "Eu sei disso. Mas a caridade não devolve as minhas pernas."
            narrator "Ela virou o rosto para a parede, encerrando a conversa."
            $ add_affinity_points("larissa", -5)
            
        "Ficar em silêncio e apenas fazer companhia. (Gastar 20 Energia)":
            if store.player_stats["energy"] >= 20:
                $ update_player_stat("energy", -20)
                narrator "Eu puxei uma cadeira e sentei do lado da cama dela. Não falei nada. Apenas fiquei ali."
                narrator "O silêncio pesou no início. Ela chorou baixinho, virada para o canto."
                narrator "Depois de quase duas horas, gastando toda a minha manhã ali, ela finalmente olhou para mim. Os olhos estavam vermelhos."
                larissa "Obrigada por não dizer que tudo acontece por um motivo. Se alguém me dissesse isso hoje, eu acho que bateria com a muleta na cara da pessoa."
                mc "Boa escolha de arma."
                narrator "Ela deu um meio sorriso. Fraquinho. Mas verdadeiro."
                $ add_affinity_points("larissa", 20)
            else:
                mc "Eu queria poder sentar aqui e conversar, mas estou caindo de sono agora..."
                larissa "Tudo bem. Pode ir. Eu não sou uma boa companhia mesmo."
                
    hide larissa
    return
