label capitulo14_katia:
    scene bg casa_interior with fade
    
    narrator "A sala estava limpa. Tudo estava dentro da lei e das regras, do jeito que Katia sempre tentou impor."
    
    show katia neutral at center
    
    if status_katia == "amizade":
        narrator "Ela fechou sua maleta de advogada recém-comprada."
        katia "As chaves estão com o síndico. Nenhuma pendência."
        mc "Sempre organizada."
        katia "O mundo não perdoa quem atrasa. Boa sorte na sua vida, player."
        narrator "Nós trocamos um aperto de mãos formal. A política estudantil ficou no passado, e nossa amizade esfriou para algo puramente acadêmico."
        
    elif status_katia == "romance":
        narrator "Katia estava na frente da porta da sala. Ela tirou o broche oficial de 'Presidente do Grêmio Estudantil' da gola do blazer."
        show katia happy
        mc "Guardando os troféus de guerra?"
        katia "Pendurando as chuteiras."
        narrator "Ela pendurou o broche na maçaneta da porta, deixando-o lá para os próximos moradores."
        show katia blush
        katia "Sabe qual foi a maior vitória política da minha vida nesses anos todos?"
        mc "Derrubar o reitor maluco?"
        katia "Não."
        narrator "Ela sorriu, puxou as lapelas do meu casaco e me beijou com a paixão de quem não precisava mais fingir ser feita de ferro."
        katia "Foi conquistar o seu coração no meio desse caos todo."
        mc "Você teve a maioria absoluta dos votos."
        
    scene black with fade
    centered "{i}Alguns anos depois...{/i}"
    call end_of_chapter_validation("capitulo15")
