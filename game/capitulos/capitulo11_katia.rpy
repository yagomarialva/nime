label capitulo11_katia:
    scene bg cinema with fade
    
    narrator "Para a Katia, não havia feriado sem uma maratona de filmes clássicos que entravam em cartaz nos cinemas antigos."
    
    show katia happy at center
    
    katia "Eles vão passar uma cópia restaurada de 'Casablanca'. É histórico. E ter você aqui pra assistir comigo... torna isso um evento canônico na minha vida."
    mc "Pipoca grande e dois refrigerantes. Só não vale me dar uma aula no meio do filme."
    
    narrator "Sentamos nas cadeiras vermelhas de veludo. O filme começou, mas nossa atenção estava dividida entre a tela e o balde gigante de pipoca no nosso colo."
    
    $ init_popcorn()
label loop_popcorn_katia:
    call screen minigame_popcorn
    
    if _return == "lose":
        katia "Você pegou toda a pipoca amanteigada e eu fiquei com fome! Presta atenção!"
        mc "Foi sem querer! Deixa eu arrumar isso."
        $ init_popcorn()
        jump loop_popcorn_katia
        
    narrator "Nossas mãos se esbarraram dentro do balde."
    
    show katia blush at center
    katia "..."
    mc "..."
    
    narrator "Ela não tirou a mão. Em vez disso, entrelaçou os dedos nos meus. Casablanca continuava rodando na tela, em preto e branco."
    
    katia "O Humphrey Bogart tem estilo... mas eu prefiro o seu."
    
    scene bg cinema with dissolve
    narrator "No escuro do cinema, o beijo teve o gosto salgado de pipoca e a doçura de um romance de Hollywood. Foi o nosso próprio roteiro perfeito."
    
    call end_of_chapter_validation("capitulo12")
