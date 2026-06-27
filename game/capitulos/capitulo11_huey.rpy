label capitulo11_huey:
    scene bg planetario with fade
    
    narrator "Huey reservou o planetário municipal para nós dois. Uma sessão exclusiva sobre o alinhamento planetário de inverno."
    
    show huey happy at center
    
    huey "A probabilidade de estarmos aqui, observando essa simulação juntos, baseada nas decisões caóticas do semestre passado, é de 0.003%%."
    mc "Ou seja, foi o destino."
    
    show huey neutral at center
    huey "O conceito de destino é estatisticamente falho. Foi... uma escolha."
    
    narrator "Ela apontou para o projetor central."
    huey "Eu estou tentando alinhar os projetores para mostrar as órbitas corretas. Você pode me ajudar com a calibração?"
    
    $ init_orbits()
label loop_orbits_huey:
    call screen minigame_orbits
    
    if _return == "lose":
        huey "Os vetores colidiram. A gravidade falhou. Precisamos recalibrar e tentar o alinhamento de novo."
        $ init_orbits()
        jump loop_orbits_huey
        
    narrator "O projetor zumbiu e, de repente, todo o teto foi preenchido por um mar perfeito de estrelas e planetas perfeitamente alinhados."
    
    show huey blush at center
    huey "As órbitas... estão estáveis. Exatamente como deveriam."
    
    mc "Igual a gente."
    
    narrator "Ela olhou para as estrelas, e depois para mim. Ela desligou seu relógio de batimentos cardíacos."
    
    huey "Hoje, eu não quero métricas."
    
    scene bg planetario with dissolve
    narrator "Nos beijamos sob o universo projetado. Foi lógico, foi perfeito, e desafiou todas as fórmulas que ela conhecia."
    
    call end_of_chapter_validation("capitulo12")
