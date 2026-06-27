label capitulo15_katia:
    if status_katia == "amizade":
        scene bg escritorio with fade
        narrator "A cerimônia de casamento de Katia foi tão elegante quanto fria."
        narrator "O noivo era sócio sênior de um escritório de advocacia. Eles formavam uma parceria corporativa impecável. O beijo deles no altar parecia a assinatura de um contrato."
        narrator "Katia apertou minha mão na saída da igreja, um sorriso diplomático no rosto."
        narrator "Ela havia chegado ao topo do mundo jurídico, inabalável, mas desprovida do fogo caótico que a tornava humana."
        jump creditos_finais
        
    elif status_katia == "romance":
        scene bg comicio with fade
        narrator "A praça da cidade estava lotada. Balões, bandeiras e uma multidão barulhenta."
        narrator "O locutor gritava no sistema de som: 'Senhoras e senhores, a vereadora mais jovem e mais combativa da nossa história, Katia!'"
        show katia happy at center
        narrator "Ela usava um terninho impecável, descendo do palanque suada, rouca, mas sorrindo como uma leoa que havia acabado de vencer uma caçada."
        mc "A multidão comeu na sua mão. E nós passamos de 10 mil votos nas urnas. É a vitória oficial."
        show katia blush
        narrator "Ela me puxou para trás da van de som, longe dos repórteres, prendendo-me contra a lataria do carro."
        katia "Nós passamos de 10 mil. Eu sou vereadora."
        mc "E eu sou um chefe de gabinete muito bem casado."
        narrator "Ela riu, me puxando pelo colarinho. O beijo foi rápido, intenso, e carregado da mesma adrenalina das brigas no grêmio estudantil."
        katia "O poder não significa nada sem você comigo nos bastidores. A lei que eu não quebro nunca é a de voltar para casa pra você."
        narrator "E a política da nossa vida juntos estava apenas no primeiro mandato."
        jump creditos_finais
