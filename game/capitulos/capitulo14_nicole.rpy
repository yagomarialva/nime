label capitulo14_nicole:
    scene bg cozinha with fade
    
    narrator "A cozinha, que foi cenário de tantos desastres culinários de Nicole, agora estava vazia."
    
    show nicole neutral at center
    
    if status_nicole == "amizade":
        narrator "Nicole vestia um casaco de grife impecável. Uma limusine preta já a aguardava do lado de fora."
        nicole "A mamãe mandou o motorista. Eu vou direto pro conselho de administração."
        mc "Boa viagem de volta pro seu mundo, Nicole."
        nicole "Obrigada. Foi... uma experiência interessante."
        narrator "Ela não me olhou nos olhos. A vergonha de ter abandonado sua independência ainda pesava. Fomos amigos, mas nunca poderíamos ser iguais."
        
    elif status_nicole == "romance":
        narrator "Nicole estava sentada na bancada. Ela bebia de uma caneca um café preto passado num coador barato."
        show nicole happy
        mc "Você tomando café barato? O mundo realmente acabou."
        nicole "Sabe o que é engraçado? Esse café tem o gosto infinitamente melhor do que o de qualquer cafeteria gourmet de Paris."
        mc "Porque você pagou com o seu próprio salário."
        narrator "Ela desceu da bancada e se aninhou nos meus braços. A garota esnobe e insuportável do primeiro dia havia desaparecido completamente."
        show nicole blush
        nicole "Eu cheguei nessa casa achando que eu era melhor que todos vocês."
        nicole "Mas a verdade é que eu não sabia nada sobre a vida real. E você me ensinou a viver de verdade."
        mc "Você foi a melhor aluna que eu já tive."
        narrator "Nós nos beijamos com sabor de café simples e promessas de futuro."
        
    scene black with fade
    centered "{i}Alguns anos depois...{/i}"
    call end_of_chapter_validation("capitulo15")
