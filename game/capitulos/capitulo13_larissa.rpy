label capitulo13_larissa:
    if status_larissa == "ruina":
        scene bg quadra with fade
        narrator "O ginásio estava lotado para a grande final. Larissa forçou a barra. Ela jogou."
        narrator "No terceiro set, o estalo no joelho dela ecoou mais alto que a torcida. Ela caiu, e não levantou mais."
        scene bg hospital_quarto with dissolve
        narrator "O rompimento foi total. A carreira acabou ali."
        show larissa sad at center
        larissa "Eu fui teimosa... E você deixou eu ser."
        larissa "Eu não te culpo pelo que aconteceu com o meu joelho. A culpa foi da minha própria arrogância."
        larissa "Mas olhar pra você agora só me traz dor e lembranças de um sonho que eu destruí."
        larissa "Acho que o melhor pra nós dois é seguirmos caminhos separados."
        narrator "E assim ela fez. Nós nunca mais nos falamos."
        scene black with fade
        centered "{b}FIM DE JOGO - CAMINHO RUÍM (Larissa){/b}"
        return
        
    elif status_larissa == "amizade":
        scene bg quadra with fade
        narrator "Larissa desistiu da final por ordens médicas. O time perdeu."
        show larissa neutral at center
        narrator "Ela estava nas arquibancadas do meu lado. Segura fisicamente, mas o olhar vazio mostrava que a chama competitiva havia morrido."
        larissa "Pelo menos eu posso andar normalmente. Foi a escolha mais lógica."
        mc "Sim. Foi racional."
        narrator "Nós éramos amigos. Sobrevivemos à crise, mas o romance e a paixão que sentíamos desapareceram no ar frio daquele ginásio."
        call end_of_chapter_validation("capitulo14")
        
    elif status_larissa == "romance":
        scene bg quadra with fade
        narrator "O ginásio estava explodindo de barulho. A final estava no último set."
        show larissa happy at center
        narrator "Larissa não estava em quadra. Ela estava na beira da linha, vestindo um casaco com as cores do time, gritando ordens como a nova auxiliar técnica."
        larissa "Abre o bloqueio! Cobre a diagonal!"
        narrator "A estratégia dela foi impecável. A nossa levantadora cravou o último ponto. O ginásio foi à loucura."
        narrator "No meio da comemoração, Larissa correu na minha direção e pulou nos meus braços."
        show larissa blush
        larissa "Nós ganhamos! Eu mudei de posição, mas o time ainda precisa de mim!"
        mc "Eu sempre disse que você nasceu pra liderar."
        narrator "Ela segurou meu rosto, ofegante."
        larissa "E eu não conseguiria ter visto isso sem você. Obrigada por não me deixar desistir."
        narrator "Ela me beijou ali mesmo, na frente de todo o ginásio. O joelho dela estava fraco, mas o futuro dela nunca pareceu tão forte."
        call end_of_chapter_validation("capitulo14")
