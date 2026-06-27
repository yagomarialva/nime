label capitulo11_harem:
    scene bg casa_natal with fade
    
    narrator "A Rua Aurora estava decorada com luzes pisca-pisca de qualidade duvidosa e uma árvore de Natal torta montada pela Samantha."
    
    narrator "A mesa estava cheia. Katia comprou rabanadas, Camille fez um ponche 'energizante', Larissa trouxe panetones, Nicole exigiu taças de cristal, e Huey calculou as fatias perfeitamente iguais do peru."
    
    show katia happy at left
    show nicole neutral at right
    
    katia "Atenção, república! Chegou a hora do caos absoluto. O Amigo Oculto!"
    nicole "Lembrando que eu estabeleci um teto de gastos. Se alguém me der algo barato, eu expulso da casa."
    
    hide katia
    hide nicole
    
    narrator "O problema: eu comprei presentes para todas as seis garotas, mas guardei todos em caixas iguais. Agora eu não sabia qual era qual."
    mc "Okay, foco. Eu sei o que cada uma quer."
    
    $ init_secret_santa()
label loop_santa_harem:
    call screen minigame_secret_santa
    
    if _return == "lose":
        narrator "Eu dei o presente errado! Uma confusão enorme se formou, com reclamações e trocas."
        mc "Pausa! Foi um teste! Devolve tudo, vamos tentar de novo!"
        $ init_secret_santa()
        jump loop_santa_harem
        
    narrator "Consegui distribuir tudo perfeitamente. A alegria foi geral."
    
    narrator "Mais tarde, quando a ceia acabou e algumas já estavam roncando no sofá da sala devido ao ponche da Camille..."
    
    narrator "Eu fui até a varanda pegar um ar frio."
    
    narrator "Uma por uma, em momentos diferentes, elas vieram até a varanda para agradecer. Um beijo roubado debaixo do visco improvisado da porta."
    
    scene bg casa_natal with dissolve
    narrator "Seis beijos. Seis segredos sob o céu de inverno. Eu não sabia como iria sobreviver ao próximo semestre, mas ali, no Natal, eu era o cara mais sortudo do mundo."
    
    call end_of_chapter_validation("capitulo12")
