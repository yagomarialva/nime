label capitulo11_nicole:
    scene bg restaurante_chique with fade
    
    narrator "Nicole reservou uma mesa no restaurante mais caro e exclusivo da cidade. Eu estava de terno, me sentindo um pinguim fora do gelo."
    
    show nicole happy at center
    
    nicole "Relaxe. A chave da alta sociedade é fingir que você é dono do lugar."
    mc "Diz a garota que morre de medo da mãe cortar a mesada."
    
    show nicole blush at center
    nicole "Shhh! Não arruine a minha fachada aristocrática."
    
    narrator "O garçom chegou com uma sequência absurda de pratos que eu nem sabia pronunciar. E, com eles, um verdadeiro arsenal de talheres."
    
    $ init_etiquette()
label loop_etiq_nicole:
    call screen minigame_etiquette
    
    if _return == "lose":
        nicole "Você pegou o garfo de sobremesa para comer o peixe! A aristocracia chora! Tenta de novo, disfarça!"
        $ init_etiquette()
        jump loop_etiq_nicole
        
    narrator "Sobrevivi ao jantar sem cometer uma gafe diplomática. Nicole parecia genuinamente impressionada."
    
    show nicole happy
    nicole "Sabe... eu achei que ia precisar te ensinar boas maneiras, mas você se saiu bem. Quase um Lord."
    mc "Eu faço qualquer coisa pra ver esse seu sorriso convencido."
    
    narrator "Ela corou. Por baixo da pose de garota intocável, havia alguém que só queria ser amada de verdade."
    
    scene bg restaurante_chique with dissolve
    narrator "Eu paguei a conta (com todas as minhas economias do semestre). Quando saímos, ela me puxou pelo paletó e me deu um beijo com gosto de vinho caro. O melhor investimento da minha vida."
    
    call end_of_chapter_validation("capitulo12")
