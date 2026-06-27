label capitulo12_larissa:
    scene bg quadra with fade
    
    narrator "O campeonato universitário final. O passaporte de Larissa para a liga profissional."
    
    narrator "Eu estava nas arquibancadas assistindo aos treinos intensos, quando ouvi um estalo agoniante, seguido por um grito."
    
    narrator "Larissa caiu na quadra, segurando o joelho que já havia sido operado."
    
    scene bg hospital_quarto with fade
    
    narrator "Horas depois, o silêncio do quarto de hospital era ensurdecedor. O médico havia acabado de sair após dar o veredito."
    
    show larissa sad at center
    
    larissa "Ele disse que... se eu jogar a final na semana que vem, meu ligamento pode se romper de vez. Eu posso mancar pro resto da vida."
    
    mc "Larissa..."
    
    larissa "Mas o olheiro do time profissional vai estar lá! É a minha chance! A chance pela qual eu dei meu sangue!"
    
    narrator "Ela apertou os lençóis, chorando de raiva e frustração."
    
    larissa "O que eu faço? Se eu não jogar, minha carreira acabou antes mesmo de começar."
    
    menu:
        "O vôlei não é só estar na quadra. Você nasceu para liderar. Seja a técnica do time.":
            $ store.status_larissa = "romance"
            mc "Seu corpo não aguenta, mas sua mente sim. Você conhece as fraquezas e forças de cada jogadora."
            mc "Seja a técnica. Mostre pro olheiro que você é brilhante dentro e fora da quadra."
            
            show larissa blush
            larissa "Você acha... acha que eu conseguiria liderar as meninas do banco?"
            mc "Eu sei que sim. Você lidera essa casa inteira."
            narrator "Ela apertou minha mão. A ideia de um novo propósito reacendeu a luz nos olhos dela."
            
        "Apoiar o sonho cegamente: Se é o seu sonho, eu te ajudo a amarrar a faixa no joelho e jogar.":
            $ store.status_larissa = "ruina"
            mc "Você é a melhor. Talvez o médico esteja exagerando. Se é o seu sonho, jogue."
            
            show larissa angry
            larissa "Você tá falando sério?! Ele disse que eu posso ficar manca! E você quer que eu corra esse risco?!"
            narrator "Ela soltou minha mão violentamente."
            larissa "Eu preciso de alguém com a cabeça no lugar, não alguém que me empurre pro precipício. Sai daqui. Quero ficar sozinha."
            
        "Focar apenas na saúde: Esqueça o vôlei. A sua saúde é mais importante.":
            $ store.status_larissa = "amizade"
            mc "Desista do campeonato. É triste, mas não vale a sua saúde física. Foque nos estudos normais."
            
            show larissa sad
            larissa "Desistir... Claro. É a coisa lógica a se fazer."
            narrator "Ela suspirou, o brilho competitivo sumindo completamente dos olhos dela. Nós evitaríamos o pior, mas eu sabia que uma parte dela havia morrido ali."
            
    scene black with fade
    call end_of_chapter_validation("capitulo13")
