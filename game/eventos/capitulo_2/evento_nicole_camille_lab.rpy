label evento_nicole_camille_lab:
    scene bg lab with dissolve
    show nicole annoyed at left
    show camille happy at right

    narrator "O laboratório de sustentabilidade estava calmo, com plantas, protótipos e quadros brancos cobertos de ideias."

    narrator "Nicole digitava algo em seu notebook com intensidade, enquanto Camille organizava algumas amostras de materiais recicláveis."

    camille "Ah, que bom que você veio! Estamos tentando montar um pitch pro nosso projeto ecológico — mas a Nicole tá um pouquinho... teimosa hoje."

    nicole "Eu não tô teimosa. Só tô tentando manter o padrão mínimo de lógica nesse caos."

    camille "Claro, claro… 'padrão mínimo de lógica'. Você tá bem tsun hoje, Nic."

    show nicole blush

    nicole "N-não inventa apelido idiota. Só quero que isso funcione direito, ok?"

    narrator "Me aproximei com curiosidade. O projeto envolvia um sistema automatizado de monitoramento de resíduos para o campus, misturando sensores e gamificação para incentivar reciclagem."

    narrator "Nicole me lançou um olhar desconfiado, mas não resistiu em me mostrar o progresso do código."

    nicole "Você entende um pouco disso, né? Dá uma olhada aqui... não que eu precise da sua ajuda, só... quero ver se você acha algo óbvio."

    menu:
        "Analisar com atenção e elogiar o trabalho da Nicole":
            $ pontos_nicole += 1
            narrator "Analisei cuidadosamente o código e destaquei o quão bem estruturado estava."
            nicole "E-eu sei... eu sou boa nisso. Mas... valeu."
            show nicole smile

        "Brincar dizendo que está cheio de erros para provocá-la":
            narrator "Brinquei dizendo que o código tinha vários erros, só para provocá-la."
            nicole "Q-QUÊ?! Você tá de zoeira? Eu revisei isso três vezes!"
            narrator "Ela bufou, mas havia um leve sorriso escondido no canto da boca."

        "Fazer um comentário técnico detalhado para impressionar":
            $ pontos_nicole += 1
            narrator "Fiz um comentário técnico sobre como otimizar os loops de verificação de dados."
            nicole "Hmm... interessante. Não é uma ideia ruim. Me surpreendeu, viu."

    camille "Ela só age assim com quem ela gosta. Tipo um gato de laboratório."

    show nicole embarrassed

    nicole "C-Camille! Você pode parar de dizer bobagens por cinco minutos?"

    narrator "Camille riu, e eu aproveitei para ajudar com a parte de design do projeto também."

    menu:
        "Sugerir uma identidade visual divertida e chamativa":
            $ pontos_camille += 1
            camille "Isso! Algo que prenda a atenção. Você tem boas ideias criativas!"
        
        "Oferecer ajuda com o layout e usabilidade do sistema":
            $ pontos_nicole += 1
            nicole "Finalmente alguém que entende o valor da funcionalidade! Gosto disso."

        "Deixar Camille liderar a estética e apenas observar":
            camille "Tá tudo bem, posso cuidar disso sozinha. Mas obrigada por confiar em mim."

    narrator "Passamos a tarde revisando conceitos de energia, analisando sensores e adaptando o design. Apesar das alfinetadas ocasionais, Nicole parecia mais leve do que o habitual."

    nicole "Você é menos inútil do que eu imaginava..."

    camille "Tradução: 'obrigada pela ajuda, foi legal passar esse tempo com você'."

    narrator "Nicole bufou, mas não desmentiu. Camille apenas piscou para mim com cumplicidade."

    narrator "Ao final do dia, tínhamos protótipos melhores, ideias refinadas — e, de algum modo, nos aproximamos mais."

    hide nicole
    hide camille
    jump segundo_dia_interacoes
