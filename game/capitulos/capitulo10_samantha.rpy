label capitulo10_samantha:
    scene bg quarto with dissolve
    
    narrator "Eram três da manhã. O quarto estava iluminado apenas pelo brilho azul do monitor. Samantha digitava furiosamente."
    
    show samantha sad at center
    
    samantha "Droga, erro de sintaxe na linha 402! Por que o compilador me odeia?!"
    
    mc "Você gastou a semana inteira subindo de elo naquele torneio. O projeto de banco de dados é pra amanhã às oito."
    
    narrator "Ela deitou a cabeça no teclado, gerando uma linha de 'ghjkghjk'."
    
    samantha "Eu não vou conseguir. Meu cérebro tá rodando em 5 frames por segundo. A RAM esgotou."
    
    mc "Tira a cabeça do teclado. Eu faço o café, você foca na lógica. Eu vou ler a documentação do servidor pra você."
    
    narrator "Ela me olhou, os olhos vermelhos de sono."
    
    samantha "Isso é trabalho braçal de suporte. Eu não posso te pedir isso."
    
    mc "Você não pediu. O player 2 entrou na partida. Bora salvar esse save file."
    
    $ init_sequence_game()
label loop_sequence_samantha:
    call screen minigame_sequence
    
    if _return == "lose":
        samantha "Syntax Error! O servidor vai cair!"
        mc "Calma, dá um rollback de 10 segundos. Foca na sintaxe, eu canto as linhas."
        $ init_sequence_game()
        jump loop_sequence_samantha
        
    scene black with fade
    
    narrator "A noite foi movida a cafeína, salgadinhos de queijo e debug de código. Quando o sol nasceu, o botão de 'Upload' foi clicado com sucesso."
    
    scene bg sala_jantar with dissolve
    
    show samantha happy at center
    
    narrator "Dois dias depois, as notas saíram no sistema da universidade."
    
    samantha "Aprovada com nota 8.8. Meu Deus. Nós zeramos a prova."
    
    mc "Eu te disse que a gente conseguia."
    
    narrator "Ela fechou o notebook com força e pulou no meu pescoço. Eu tropecei pra trás com o impacto."
    
    samantha "Você tem noção do quão épico você foi? Ninguém, em toda a minha lista de contatos, faria um all-nighter lendo documentação de MySQL por mim."
    
    mc "Eu não sou um contato qualquer."
    
    samantha "Não. Você é o contato mais importante."
    
    narrator "Ela segurou o meu rosto com as duas mãos e me beijou, rápido no começo, e depois com uma intensidade que fez meu coração acelerar."
    
    samantha "Que tal um jogo em co-op agora? Mas dessa vez... sem monitores."
    
    call end_of_chapter_validation("capitulo11")
