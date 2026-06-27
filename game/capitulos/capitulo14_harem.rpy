label capitulo14_harem:
    scene bg rua_aurora with fade
    
    if status_harem == "amizade":
        narrator "Eu parei na calçada da Rua Aurora pela última vez. A fraternidade alfa já estava tirando nossas coisas."
        narrator "As seis garotas haviam ido embora na noite anterior."
        narrator "A magia se quebrou muito rápido quando percebemos que teríamos que sobreviver separados. Não éramos tão fortes quanto achávamos sem a proteção daquela casa velha."
        narrator "Suspirei, segurei a alça da minha mochila e fui procurar o meu caminho solitário para a vida adulta."
        
    elif status_harem == "romance":
        scene bg sala_estar_baguncada with fade
        
        narrator "Alguém lá fora poderia jurar que não estávamos de mudança. Porque nós realmente não estávamos."
        
        show katia happy at left
        show larissa happy at right
        narrator "Katia estava discutindo os termos legais para a compra coletiva do imóvel."
        narrator "Larissa empilhava caixas de pizza numa torre no canto da sala."
        
        hide katia
        hide larissa
        show samantha happy at left
        show nicole happy at right
        narrator "Samantha ligava os consoles na TV da sala, enquanto Nicole reclamava fingidamente do cheiro da pizza barata."
        
        hide samantha
        hide nicole
        show camille blush at left
        show huey blush at right
        narrator "Camille espalhava sálvia pelo ar, e Huey terminava um mural caótico na parede principal."
        
        narrator "Eu observei a cena inteira do sofá. O fim da faculdade não significava o fim da nossa história."
        
        narrator "Elas haviam decidido que, se fôssemos cair no mundo real e assustador dos adultos, nós o faríamos juntos. Todas elas. Comigo."
        narrator "A casa na Rua Aurora não era apenas um experimento de um professor maluco. Era o nosso santuário."
        
    scene black with fade
    centered "{i}Alguns anos depois...{/i}"
    call end_of_chapter_validation("capitulo15")
