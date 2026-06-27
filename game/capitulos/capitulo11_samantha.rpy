label capitulo11_samantha:
    scene bg fliperama with fade
    
    narrator "O fliperama da cidade era barulhento, cheio de neon e cheirava a pizza barata. Ou seja, o paraíso da Samantha."
    
    show samantha happy at center
    
    samantha "Player 2, prepare-se para ser destruído no Air Hockey. E depois, eu vou zerar aquela máquina de tiro."
    mc "Você não ganha nem de um bot no easy. Hoje eu vou carregar você."
    
    narrator "Gastamos horas nos jogos. Mas no final, ela parou de frente para a temida máquina de garra."
    
    show samantha neutral at center
    samantha "Aquela pelúcia de slime ali. Ela é uma montaria épica de nível 80. Eu. Preciso. Dela."
    mc "Essas máquinas são programadas pra roubar nosso dinheiro. Mas deixa comigo, eu pego."
    
    $ init_claw_machine()
label loop_claw_samantha:
    call screen minigame_claw
    
    if _return == "lose":
        samantha "A garra não tem força de grip! É pay-to-win! Coloca mais uma ficha, tenta de novo!"
        $ init_claw_machine()
        jump loop_claw_samantha
        
    narrator "A garra metálica desceu exatamente no centro de gravidade da pelúcia."
    
    show samantha blush
    samantha "Drop lendário! Você conseguiu!"
    
    narrator "Eu entreguei a pelúcia para ela. Ela abraçou o bicho, e então me olhou de um jeito diferente. O brilho dos fliperamas refletia nos óculos dela."
    
    mc "Consigo trocar esse loot por um beijo?"
    samantha "Troca justa. Aceitar trade."
    
    scene bg fliperama with dissolve
    narrator "Ela me puxou pela gola da camisa. Foi desajeitado, rápido e perfeito. Um verdadeiro 'Achievement Unlocked'."
    
    call end_of_chapter_validation("capitulo12")
