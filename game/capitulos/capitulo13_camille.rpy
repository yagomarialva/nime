label capitulo13_camille:
    if status_camille == "ruina":
        scene bg casa_interior with fade
        narrator "O quarto da Camille estava assustadoramente quieto."
        narrator "Quando entrei, o cheiro de incenso havia sumido. Havia apenas uma caixa vazia no canto."
        narrator "Ela tinha ido embora sem se despedir, bloqueado meu número e deletado suas redes. Mergulhada no cinismo da mentira que descobriu, ela preferiu se isolar de todos."
        narrator "E de mim."
        scene black with fade
        centered "{b}FIM DE JOGO - CAMINHO RUÍM (Camille){/b}"
        return
        
    elif status_camille == "amizade":
        scene bg escritorio with fade
        narrator "Fui encontrar a Camille no trabalho novo dela, na empresa da família."
        show camille neutral at center
        narrator "Ela usava um terno cinza, os cabelos antes soltos agora estavam amarrados num coque rígido. O sorriso que antes irradiava paz agora era apenas mecânico."
        camille "Oi. Minha pausa é curta, mas obrigada por vir."
        mc "Você parece... estável."
        camille "Eu sou produtiva. Sem misticismo. A vida adulta é assim."
        narrator "Ela havia aceitado a racionalidade fria. Éramos apenas bons amigos em um mundo cinzento."
        call end_of_chapter_validation("capitulo14")
        
    elif status_camille == "romance":
        scene bg parque with fade
        narrator "O campus estava agitado. Perto do lago, uma pequena fila de alunos estressados se formava."
        show camille happy at center
        narrator "Camille estava sentada numa esteira sob a árvore. Sem a guru, sem o charlatanismo. Apenas ela, ouvindo atenciosamente um aluno que chorava sobre as provas finais."
        narrator "Eu me aproximei quando ela terminou o atendimento."
        show camille blush
        camille "Você chegou. Hoje ajudei cinco pessoas a encontrar paz mental sem usar uma única pedra de quartzo falso."
        mc "A sua magia nunca dependeu de uma pedra."
        camille "Eu sei agora. A espiritualidade verdadeira sempre esteve aqui... e a conexão que eu sinto, eu quero construir com as minhas próprias mãos."
        narrator "Ela pegou a minha mão, entrelaçando nossos dedos com uma firmeza nova e gentil."
        camille "E eu quero começar construindo algo com você."
        narrator "Ela encostou a testa na minha, fechando os olhos. O mundo dela estava mais claro e vibrante do que nunca."
        call end_of_chapter_validation("capitulo14")
