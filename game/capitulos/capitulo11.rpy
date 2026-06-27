label capitulo11:
    if "capitulo11" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo11")
        
    scene bg casa_interior with fade
    
    narrator "Dezembro chegou. As provas finais ficaram para trás."
    
    narrator "A república, que antes era uma zona de guerra acadêmica e um canteiro de obras, finalmente encontrou paz."
    
    narrator "Mas a paz tem o seu preço: o silêncio. As garotas começaram a arrumar as malas para visitar suas famílias durante o recesso de fim de ano."
    
    if not hasattr(store, 'escolha_fogos'):
        $ escolha_fogos = "grupo"
        
    if escolha_fogos == "harem" or escolha_fogos == "grupo":
        narrator "No entanto, este ano, havia um consenso não dito."
        
        show katia neutral at left
        show larissa happy at right
        
        katia "Minha família vai viajar para a Europa, mas eu disse a eles que preciso organizar os arquivos do grêmio."
        larissa "E eu falei pro meu pai que os treinos de vôlei não podem parar. Até no frio."
        
        hide katia
        hide larissa
        show nicole happy at left
        show camille gentle at right
        
        nicole "Achei que o flat que minha mãe queria alugar era luxuoso, mas descobri que a companhia daqui é mais exclusiva."
        camille "As energias desta casa estão alinhadas demais para serem quebradas no solstício de inverno."
        
        hide nicole
        hide camille
        show samantha happy at left
        show huey neutral at right
        
        samantha "O ping do servidor é melhor aqui. E o evento de Natal do meu MMO começou hoje."
        huey "A probabilidade estatística de eu ter um colapso por tédio na casa dos meus pais é de 99.8%%."
        
        hide samantha
        hide huey
        
        narrator "Resumindo: todo mundo mentiu para as famílias para passar o 'Natal dos Órfãos' na república. E eu não poderia estar mais feliz."
        jump capitulo11_harem
        
    else:
        narrator "As despedidas foram longas. Abraços apertados, promessas de mandar mensagens todo dia e ameaças de quem deixasse a pia suja enquanto estivessem fora."
        
        narrator "Logo, a casa enorme de cinco quartos abrigava apenas duas pessoas."
        
        narrator "Eu. E a pessoa por quem meu coração batia mais forte."
        
        if escolha_fogos == "larissa":
            jump capitulo11_larissa
        elif escolha_fogos == "camille":
            jump capitulo11_camille
        elif escolha_fogos == "samantha":
            jump capitulo11_samantha
        elif escolha_fogos == "katia":
            jump capitulo11_katia
        elif escolha_fogos == "nicole":
            jump capitulo11_nicole
        elif escolha_fogos == "huey":
            jump capitulo11_huey
