label capitulo10_larissa:
    scene bg sala_jantar with dissolve
    
    narrator "A sala estava coberta de livros de anatomia, fisiologia e estatística desportiva."
    
    show larissa sad at center
    
    narrator "Larissa encarava um caderno com uma expressão de dor física maior do que qualquer treino que eu já a vi fazer."
    
    larissa "Eu odeio o ciclo de Krebs. Por que eu preciso saber a rota metabólica do oxigênio se eu só quero jogar a bola pro outro lado da rede?!"
    
    mc "Porque se você reprovar em Fisiologia, você perde a bolsa de esportes. E se perder a bolsa, você perde a vaga na casa."
    
    narrator "Ela bateu a cabeça na mesa, espalhando os lápis."
    
    larissa "Eu devia desistir. Eu sou boa na quadra, não na biblioteca. O Professor Wendell vai rir da minha cara quando ler essa prova."
    
    narrator "Sentei na cadeira ao lado dela e puxei o livro grosso para mim."
    
    mc "Levanta a cabeça, capitã. Você não desistiu quando a parede pegou fogo, não vai desistir pro ciclo de Krebs."
    
    narrator "Ela me olhou, com os olhos castanhos cansados."
    
    mc "A gente vai transformar isso num treino. Cada página lida e entendida, você ganha pontos. E eu aposto que você não consegue me vencer na revisão."
    
    larissa "Você tá me desafiando pra um x1 de biologia?"
    
    mc "Valendo a sua permanência na casa. E talvez um prêmio bônus."
    
    narrator "Um sorriso competitivo surgiu no rosto dela. O desespero foi substituído por foco puro."
    
    larissa "Pode vir."
    
    $ init_memory_game()
    
label loop_memoria_larissa:
    call screen minigame_memory
    
    if _return == "match":
        if memory_pairs_found == 1:
            mc "A mitocôndria é a respiração celular!"
            larissa "Certo, energia pra célula. Próximo!"
        elif memory_pairs_found == 2:
            mc "O ciclo de Krebs acontece na matriz mitocondrial!"
            larissa "Matriz... ok, entendi."
        elif memory_pairs_found == 3:
            mc "O DNA fica no núcleo."
            larissa "Sopa de letrinhas guardada no cofre, anotei."
        elif memory_pairs_found == 4:
            mc "E a célula inteira é a base de tudo."
            larissa "Eu consegui! Eu memorizei!"
            
        $ store.memory_dialogue_pending = False
        if memory_pairs_found < 4:
            jump loop_memoria_larissa
    
    scene black with fade
    
    narrator "Passamos três madrugadas estudando. Quando a sexta-feira de provas chegou, Larissa entrou na sala de cabeça erguida."
    narrator "E quando a nota saiu... 8.5."
    
    scene bg ginasio with dissolve
    
    show larissa happy at center
    
    larissa "EU PASSEI! EU PASSEI!"
    
    narrator "Ela correu na minha direção, me abraçou e me ergueu do chão, girando."
    
    mc "Larissa... eu tô... sem ar!"
    
    narrator "Ela me colocou no chão, mas não me soltou. Nossos rostos estavam próximos, e o sorriso dela era brilhante."
    
    larissa "Você salvou minha vida estudantil. Como eu pago essa dívida?"
    
    mc "Bom, eu mencionei um prêmio bônus..."
    
    narrator "Antes que eu terminasse a frase, ela puxou a gola da minha camisa e me deu um beijo rápido e energético, mas com um calor que me deixou tonto."
    
    larissa "Tá pago. E a gente ainda tem um encontro pra marcar."
    
    call end_of_chapter_validation("capitulo11")
