# Minigame do Pincel/Caneta Mágica (Comédia)
screen minigame_caneta():
    modal True
    zorder 200
    
    default clicks_necessarios = 20
    default clicks_atuais = 0
    default tempo_restante = 5.0
    
    timer 0.1 repeat True action If(tempo_restante > 0, SetScreenVariable("tempo_restante", tempo_restante - 0.1), Return(False))
    
    add Solid("#000000cc")
    
    vbox:
        xalign 0.5
        yalign 0.1
        text "Pegue a caneta do Professor Wendell antes que ele assine!" size 40 color "#ffffff" bold True
        text "Cliques (Puxões): [clicks_atuais] / [clicks_necessarios]" size 30 color "#ffcc00"
        text "Tempo: [tempo_restante:.1f]s" size 30 color "#ff5555"
        
    imagebutton:
        idle "gui/button/choice_idle_background.png"
        hover "gui/button/choice_hover_background.png"
        xalign 0.5
        yalign 0.5
        action If(clicks_atuais < clicks_necessarios, SetScreenVariable("clicks_atuais", clicks_atuais + 1), Return(True))
        
    if clicks_atuais >= clicks_necessarios:
        timer 0.1 action Return(True)


label evento_cap8_wendell:
    scene bg predio_adm with dissolve
    
    narrator "Cheguei ao escritório do Prof. Wendell para entregar o relatório de segurança do piso do segundo andar."
    
    narrator "Quando abri a porta, ele estava com uma caneta-tinteiro prateada erguida sobre um formulário com o carimbo vermelho gigante dizendo 'INTERDITADO'."
    
    mc "Professor, não!"
    
    wendell "Admin! Eu preciso encaminhar os papéis pro reitor hoje se vocês não mostrarem avanço na obra!"
    
    narrator "O bico da caneta tocou no papel."
    
    call screen minigame_caneta
    
    if _return:
        narrator "Num pulo desesperado, agarrei o tubo da caneta dele como num cabo de guerra."
        
        wendell "O que você está fazendo?! Solte a minha tinteiro importada!"
        
        mc "O relatório do piso diz que a viga não sofreu calor! Só precisamos de mais 24 horas pra limpar o mofo e pintar!"
        
        narrator "Puxei a caneta com tudo. O professor escorregou da cadeira e a caneta voou pela sala, caindo dentro de um vaso de plantas."
        
        wendell "Minha Montblanc!"
        
        narrator "Ele correu para cavoucar a terra do vaso."
        
        wendell "Vocês são loucos. Todos vocês."
        
        mc "Loucos e com as vigas intactas. Nos dê o resto da semana, por favor."
        
        narrator "Wendell soprou a terra da caneta. Ele suspirou, derrotado, mas vi a sombra de um pequeno sorriso no canto da boca dele."
        
        wendell "Só porque minha caneta falhou agora. Tenham tudo pintado até sexta-feira."
        
        mc "Obrigado, chefe."
        
    else:
        narrator "Tentei arrancar a caneta dele, mas fui devagar demais. Ele assinou a primeira página."
        wendell "Muito tarde. Eu não deveria atrasar os processos burocráticos."
        narrator "Isso não nos expulsa ainda, mas deixou a situação muito mais perigosa."
        $ update_player_stat("energy", -10)
        
    return
