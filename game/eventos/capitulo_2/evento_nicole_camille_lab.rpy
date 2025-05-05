label evento_nicole_camille_lab:
    scene bg botanic_lab with dissolve
    show nicole neutral at left
    show camille happy at right

    narrator "O laboratório de sustentabilidade estava calmo, com plantas, protótipos e quadros brancos cobertos de ideias."

    narrator "Nicole digitava algo em seu notebook com foco absoluto, enquanto Camille organizava algumas amostras de materiais recicláveis."

    camille "Ah, que bom que você veio! Estamos tentando montar um pitch pro nosso projeto ecológico — mas a Nicole tá um pouquinho... intensa hoje."

    nicole "Intensa? Não. Apenas eficiente. Temos um prazo e eu não vou deixar isso falhar."

    camille "Claro, claro… 'eficiente'. Você parece mais uma CEO em treinamento do que uma estudante."

    nicole "E qual o problema nisso? Resultados são o que importam."

    narrator "Me aproximei com curiosidade. O projeto envolvia um sistema automatizado de monitoramento de resíduos para o campus, misturando sensores e gamificação para incentivar reciclagem."

    narrator "Nicole me lançou um olhar avaliador, como se estivesse decidindo se eu seria útil ou não."

    nicole "Você entende algo disso? Se sim, ótimo. Se não, tente não atrapalhar."

    menu:
        "Analisar com atenção e elogiar o trabalho da Nicole":
            $ points_nicole += 1
            narrator "Analisei cuidadosamente o código e destaquei o quão bem estruturado estava."
            nicole "Bom. Reconhecimento é importante, mas não se esqueça de apontar melhorias também."

        "Fazer um comentário técnico detalhado para impressionar":
            $ points_nicole += 1
            narrator "Fiz um comentário técnico sobre como otimizar os loops de verificação de dados."
            nicole "Interessante. Não é perfeito, mas é uma ideia sólida. Continue assim."

        "Perguntar como ela planeja apresentar o projeto":
            $ points_nicole += 1
            nicole "Apresentação é tudo. Se não conseguimos vender a ideia, não importa o quão boa ela seja."

    camille "Ela é assim o tempo todo, sabia? Sempre pensando em resultados."

    show nicole neutral

    nicole "E qual o problema nisso? Se você quer mudar o mundo, precisa ser prática. Emoções não resolvem problemas."

    narrator "Camille riu, mas eu percebi que Nicole estava falando sério. Ela parecia determinada, mas havia algo mais por trás de sua postura rígida."

    narrator "Decidi ajudar com a parte de design do projeto também."

    menu:
        "Sugerir uma identidade visual divertida e chamativa":
            $ points_camille += 1
            camille "Isso! Algo que prenda a atenção. Você tem boas ideias criativas!"
            nicole "Desde que não comprometa a funcionalidade, pode funcionar."

        "Oferecer ajuda com o layout e usabilidade do sistema":
            $ points_nicole += 1
            nicole "Finalmente alguém que entende o valor da funcionalidade. Gosto disso."

        "Deixar Camille liderar a estética e apenas observar":
            camille "Tá tudo bem, posso cuidar disso sozinha. Mas obrigada por confiar em mim."
            nicole "Desde que ela entregue algo funcional, não vejo problema."

    narrator "Passamos a tarde revisando conceitos de energia, analisando sensores e adaptando o design. Nicole era direta e exigente, mas também eficiente."

    nicole "Bom trabalho. Isso está começando a parecer algo que vale a pena apresentar."

    camille "Tradução: 'obrigada pela ajuda, foi legal passar esse tempo com você'."

    show nicole neutral

    nicole "Eu não disse isso. Mas... sim, foi útil ter você aqui."

    narrator "Nicole parecia desconfortável em admitir, mas havia um leve sorriso em seu rosto. Camille apenas piscou para mim com cumplicidade."

    narrator "Ao final do dia, tínhamos protótipos melhores, ideias refinadas — e, de algum modo, nos aproximamos mais."

    hide nicole
    hide camille
    jump segundo_dia_interacoes
