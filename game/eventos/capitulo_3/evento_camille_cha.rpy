label evento_camille_cha:
    scene bg cozinha_escura with dissolve
    
    narrator "A cozinha estava imersa num cheiro adocicado de camomila e algo cítrico."
    
    show camille neutral at center
    
    narrator "Camille estava sentada no escuro, segurando uma caneca quente entre as mãos. A aura de 'guru iluminada' que ela exibia de manhã parecia ter evaporado."
    
    mc "Fazendo poções no escuro?"
    
    camille "Um blend de lavanda e mulungu. Excelente para ansiedade. Pensei em fazer um jarro inteiro para a casa, considerando a frequência caótica de hoje mais cedo."
    
    narrator "Ela deu um gole no chá. O silêncio na cozinha não era tenso, era apenas exausto."
    
    mc "Você não precisa ser a terapeuta do grupo no seu primeiro dia, sabia?"
    
    camille "É instintivo. As pessoas olham para mim e veem a garota zen. A bússola moral que nunca perde o equilíbrio. Minha família, meus amigos... eles jogam o caos deles em cima de mim esperando que eu purifique tudo."
    
    narrator "Ela apoiou o rosto na mão."
    
    camille "Às vezes, eu só queria ter o direito de pirar. De quebrar um prato. De não ter a resposta certa."
    
    menu:
        "O mundo precisa de gente como você. (Poupar energia)":
            mc "É um fardo, mas você é boa nisso. A casa estaria se matando se você não tivesse chegado."
            camille "Eu sei. É o meu karma."
            narrator "Ela sorriu, mas o sorriso não chegou aos olhos. Ela se fechou novamente no seu papel de protetora."
            $ add_affinity_points("camille", 5)
            
        "Pode quebrar o que quiser comigo. (Gastar 20 Energia)":
            if store.player_stats["energy"] >= 20:
                $ update_player_stat("energy", -20)
                mc "Se você quiser jogar uma cadeira pela janela, eu te ajudo a carregar ela. Prometo não julgar sua aura."
                narrator "Camille piscou, surpresa. E então ela riu. Uma risada genuína, sonora e maravilhosamente humana, longe do tom etéreo que ela usava."
                camille "Cuidado com o que oferece. Eu tenho uma mira muito boa para cadeiras."
                mc "Combinado. Aqui comigo você tem folga do trabalho de guru. Pode ser só a Camille."
                narrator "Ela levantou a caneca na minha direção, como num brinde."
                camille "Obrigada. Essa energia... eu gostei bastante."
                $ add_affinity_points("camille", 20)
            else:
                mc "Eu entendo. Queria ficar aqui e conversar sobre isso, mas estou caindo de sono."
                camille "Vá dormir. O corpo físico tem limites. Eu fico bem."
                
    hide camille
    return
