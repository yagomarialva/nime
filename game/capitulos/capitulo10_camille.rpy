label capitulo10_camille:
    scene bg quarto with dissolve
    
    narrator "O cheiro de sálvia dominava o quarto da Camille. Ela estava meditando no centro de um círculo de cristais."
    
    show camille neutral at center
    
    mc "A prova de Filosofia Moderna é amanhã, Camille. Seus cadernos estão intactos."
    
    camille "Os iluministas tentaram categorizar a alma em caixas racionais. Eu me recuso a alimentar essa egregora limitante."
    
    mc "A egregora limitante do Professor Wendell vai te dar um zero se você não escrever sobre Kant."
    
    narrator "Ela abriu os olhos lentamente. Havia frustração real sob a fachada zen."
    
    camille "Eles não avaliam o que eu sei, [nome]. Eles avaliam se eu sei papagaiar o que homens engravatados disseram há séculos. Não é justo com o meu dom."
    
    narrator "Sentei no chão, de frente pra ela, quebrando a borda do círculo de cristais."
    
    mc "Você tá certa. A academia às vezes sufoca o espírito. Mas você não vai deixar um pedaço de papel te tirar daqui, vai?"
    
    mc "Nós lutamos muito por essa casa. Pensa na prova não como uma submissão, mas como um jogo de espelhos. Escreva o que eles querem ler, e proteja o seu santuário interno."
    
    narrator "Ela olhou para o livro de Kant, e depois para mim."
    
    camille "Uma proteção mística disfarçada de resposta acadêmica..."
    
    mc "Exato. Vem, eu te ajudo a conjurar esse feitiço."
    
    $ init_focus_game()
label loop_foco_camille:
    call screen minigame_focus
    
    if _return == "lose":
        camille "Minha energia dispersou... Kant está nublando meu terceiro olho."
        mc "Respira fundo. Centraliza. Vamos tentar de novo."
        $ init_focus_game()
        jump loop_foco_camille
        
    scene black with fade
    
    narrator "Nós lemos e discutimos teorias a noite inteira, transformando conceitos densos em metáforas que a mente mística de Camille conseguia digerir."
    narrator "E funcionou. O boletim dela marcou 9.0 em Filosofia."
    
    scene bg jardim_campus with dissolve
    
    show camille gentle at center
    
    narrator "Eu a encontrei perto do lago, queimando a prova antiga com um isqueiro."
    
    mc "Eu acho que isso é vandalismo acadêmico."
    
    camille "É purificação. A nota cumpriu seu propósito material. Agora estou liberando a energia."
    
    narrator "Ela pisou nas cinzas e se virou para mim."
    
    camille "Você foi o meu âncora essa semana. Sem você, eu teria flutuado pra longe dessa casa."
    
    mc "Eu não ia deixar você ir."
    
    narrator "Ela sorriu, um sorriso suave e raro. Seus braços se envolveram no meu pescoço, e ela me beijou com uma lentidão hipnótica, cheirando a lavanda e fumaça."
    
    camille "Meu futuro nunca esteve tão claro. E você está nele."
    
    call end_of_chapter_validation("capitulo11")
