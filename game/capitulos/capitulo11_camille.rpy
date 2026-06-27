label capitulo11_camille:
    scene bg jardim_botanico with fade
    
    narrator "Camille me levou ao Jardim Botânico para a 'festa das luzes solsticiais'. Árvores iluminadas refletiam num lago imenso."
    
    show camille happy at center
    
    camille "As constelações de inverno estão visíveis hoje. Consegue sentir como as energias ficam mais densas com o frio?"
    mc "Tudo que eu sinto é o cheiro de lavanda e o fato de você estar linda essa noite."
    
    show camille blush at center
    camille "Isso... isso não estava nos meus mapas astrais. Você mudou minha rota."
    
    narrator "Ela apontou para o céu estrelado."
    camille "Me mostre. Conecte as estrelas do meu jeito."
    
    $ init_constellation()
label loop_const_camille:
    call screen minigame_constellation
    
    if _return == "lose":
        camille "A energia quebrou. Você perdeu a ordem cósmica. Tente olhar de novo."
        $ init_constellation()
        jump loop_const_camille
        
    narrator "Eu desenhei a constelação imaginária no céu com o dedo, seguindo o padrão que ela me ensinou."
    
    show camille gentle
    camille "Perfeito. As estrelas estão exatamente onde deveriam estar. Nós também."
    
    narrator "Ela se inclinou. Suas roupas cheiravam a incenso, mas seus lábios tinham o gosto doce da maçã do amor que dividimos."
    
    scene bg jardim_botanico with dissolve
    narrator "Sob o céu de inverno, nossos mapas astrais finalmente se alinharam de forma inegável."
    
    call end_of_chapter_validation("capitulo12")
