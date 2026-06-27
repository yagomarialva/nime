label capitulo11_larissa:
    scene bg cidade_neve with fade
    
    narrator "A cidade estava decorada para o fim de ano. Larissa sugeriu algo diferente: a pista de patinação no gelo temporária no centro da cidade."
    
    show larissa happy at center
    
    larissa "Eu domino as quadras! Pular 1 metro e cortar uma bola a 100km/h? Fácil. Quanto mais difícil pode ser andar no gelo?"
    
    narrator "Cinco minutos depois..."
    
    show larissa blush at center
    
    larissa "Me segura! Me segura pelo amor de Deus, eu não sinto minhas pernas!"
    mc "Cadê a dominadora das quadras? Segura na minha mão e tenta manter o eixo."
    
    $ init_ice_skating()
label loop_ice_larissa:
    call screen minigame_ice_skating
    
    if _return == "lose":
        narrator "Larissa escorregou e nos puxou para o chão frio em um emaranhado de pernas."
        larissa "Ai! Meu cóccix! De novo, me puxa pra cima!"
        $ init_ice_skating()
        jump loop_ice_larissa
        
    narrator "Conseguimos manter o equilíbrio por tempo suficiente para darmos uma volta inteira na pista."
    
    show larissa happy
    larissa "Viu? Eu disse que pegava o jeito."
    
    narrator "Ela estava de mãos dadas comigo. Seus dedos estavam gelados, mas suas bochechas estavam coradas."
    mc "Acho que a gente pegou o jeito juntos."
    
    larissa "Sabe... eu gostei da vista daqui. Perto de você."
    
    narrator "Nós paramos no centro da pista. Sob as luzes de Natal, eu a puxei para perto."
    
    scene bg cidade_neve with dissolve
    narrator "Foi o nosso primeiro beijo sem a pressão de jogos ou estudos. Apenas nós dois, deslizando na pista."
    
    call end_of_chapter_validation("capitulo12")
