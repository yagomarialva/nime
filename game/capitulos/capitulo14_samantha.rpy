label capitulo14_samantha:
    scene bg quarto_samantha with fade
    
    narrator "O quarto estava escuro pela primeira vez em anos. Todos os LEDs e monitores haviam sido desligados e encaixotados."
    
    show samantha neutral at center
    
    if status_samantha == "amizade":
        narrator "Samantha estava fechando uma mochila."
        samantha "Hora do reset de servidor."
        mc "A empresa já mandou as passagens?"
        samantha "Já. Amanhã eu começo a codar software de banco de dados. Muito empolgante."
        narrator "Nós fizemos um toque de mãos platônico. Ela seguiu para sua nova vida segura, porém sem graça."
        
    elif status_samantha == "romance":
        narrator "Samantha estava segurando uma velha placa-mãe verde na mão, limpando a poeira."
        show samantha happy
        samantha "Sabe o que é isso?"
        mc "Lixo eletrônico?"
        samantha "A placa do servidor onde a gente derrubou os haters na noite de lançamento."
        narrator "Ela guardou a placa cuidadosamente na mochila, como se fosse um artefato lendário."
        show samantha blush
        samantha "Eles dizem que jogos cooperativos são difíceis porque dependem de sincronia."
        samantha "Nós dois conseguimos platinar essa faculdade, e sem nenhum lag de conexão."
        mc "Nós formamos uma ótima party."
        narrator "Ela me beijou com carinho no escuro do quarto vazio."
        samantha "A gente pode ir pra servidores diferentes agora... Mas eu sempre vou guardar um slot de coop pra você."
        
    scene black with fade
    centered "{i}Alguns anos depois...{/i}"
    call end_of_chapter_validation("capitulo15")
