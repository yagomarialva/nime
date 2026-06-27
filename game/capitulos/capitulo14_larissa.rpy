label capitulo14_larissa:
    scene bg casa_interior with fade
    
    narrator "O quarto estava cheio de caixas de papelão."
    
    show larissa neutral at center
    
    if status_larissa == "amizade":
        narrator "Larissa dobrou sua última camisa e fechou a caixa."
        larissa "Acho que é isso. Fim da linha para a Rua Aurora."
        mc "Você vai se mudar pra perto do centro de treinamento?"
        larissa "Sim. Mais prático. Focar na reabilitação."
        narrator "Nós nos abraçamos rapidamente. Uma amizade sólida, mas sem a paixão que um dia tentou nascer."
        larissa "Se cuida, player. A gente se vê por aí."
        
    elif status_larissa == "romance":
        narrator "Larissa estava sentada no sofá velho, o mesmo onde ela dormiu machucada no primeiro dia em que nos conhecemos."
        show larissa happy
        narrator "Ela segurava a medalha de ouro da faculdade na mão."
        larissa "Lembra quando a gente quase se matou por um pedaço de pizza nessa mesma sala?"
        mc "Eu lembro que você era a pessoa mais competitiva do mundo."
        narrator "Ela riu, levantou e jogou a medalha no meu colo."
        mc "O que é isso?"
        larissa "Você sabe que eu odeio perder, né? Mas eu acho que o melhor troféu que eu ganhei nessa faculdade não foi do vôlei."
        show larissa blush
        larissa "Foi você."
        narrator "Eu puxei ela pela cintura, e nós nos beijamos no meio da sala vazia, ignorando as caixas de mudança."
        larissa "Nós vamos pra apartamentos diferentes agora... mas você não vai se livrar de mim tão cedo, entendeu?"
        mc "Eu não suportaria se você tentasse."
        
    scene black with fade
    centered "{i}Alguns anos depois...{/i}"
    call end_of_chapter_validation("capitulo15")
