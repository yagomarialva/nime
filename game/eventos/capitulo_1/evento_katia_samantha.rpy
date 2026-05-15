# === EVENTO CINEMA: KATIA E SAMANTHA ===
# Tema: O escape da realidade e o choque de mídias

label evento_katia_samantha:
    scene bg cinema with fade
    
    narrator "O cinema universitário cheirava a assentos mofados e pipoca requentada. Na fileira do fundão, Katia estava sentada rígida, iluminada levemente pela luz do projetor não focado."
    narrator "Duas fileiras abaixo no corredor lateral, iluminada apenas pelo forte brilho fosforescente de um console portátil, estava Samantha."
    
    show katia neutral at left
    show samantha neutral at right
    
    katia "O brilho emitido por aquela placa de processamento portátil está quebrando a estética umbrosa do ambiente."
    samantha "S-sério? Porque o filme nem começou e meus saves offline só precisam de um recuo na gama... Espera."
    
    narrator "Samantha escorregou o dedão e o console emitiu um alto som de morte 8-bits."
    samantha "Ai, meu Deus."
    
    katia "Uma tragédia interativa e pixelada. Era previsível se você tentou desviar olhando pro teto focado lá no fundo. A falta de atenção é fatal."
    katia "E eu digo o mesmo para você, que acabou de entrar."
    
    narrator "Katia virou as pupilas duras e afiadas na minha direção, sem virar o pescoço."
    
    mc "Achei que o espaço estivesse reservado apenas para rituais de silêncio e games portáteis."
    samantha "E-ei... não quebra a party. Eu já baixei o brilho e morri."
    
    narrator "Sentei distante de ambas, deixando o eco vazio do teatro pesar. Katia mantinha os braços fortemente cruzados. Samantha escondia o rosto sob o visor transparente de seu fone de ouvido."
    narrator "Nenhuma delas queria estar aqui especificamente com outra pessoa. Elas só não queriam estar em nenhum outro lugar."
    
    katia "Eles acham que escapismo exige telas ou drogas."
    katia "Eles não têm a capacidade de absorver luto sem piscar, como as películas da Nouvelle Vague."
    
    samantha "Bom... a lore complexa pode substituir luto. Eu acho. Tem dor numa queda de framerate quando seu save corrompe na última hora."
    samantha "S-só quem perde setenta horas de imersão sabe."
    
    menu:
        "Questionar o vazio":
            $ points_katia += 2
            mc "A questão é: o que vocês tanto tentam fugir ficando sozinhas no escuro?"
            katia "Do óbvio. Das perguntas idiotas como as suas."
            
        "Fingir imersão":
            $ points_samantha += 2
            narrator "Fiquei quieto, ouvindo os cliques plásticos que Samantha fazia no controle, como para preencher um silêncio hostil."
            samantha "Você... entende que eu morri, né? A tela de You Died dói."
            katia "Tsk. Dramaticidade de polígonos."
            
    narrator "Elas não eram compatíveis em nada além de uma desesperada aversão ao contato físico real do mundo lá de fora."
    
    mc "Pelo menos no cinema e no jogo a história vai ter um final, mesmo se vocês morrerem antes."
    
    narrator "Katia mordeu a parte de trás do lábio inferior por uma leve fração de segundo."
    katia "Se não tiver roteiro ruim, sim. Eu exijo roteiro sem ganchos abertos e falsas esperanças."
    
    samantha "Vou tentar dar respawn aqui na próxima rodada..."
    narrator "Elas voltaram à sua bolha intransponível. A conexão aqui parecia impossível, isolada por camadas espessas de medo e celulóide."
    
    return