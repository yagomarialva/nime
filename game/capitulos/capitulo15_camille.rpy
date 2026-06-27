label capitulo15_camille:
    if status_camille == "amizade":
        scene bg cafe with fade
        narrator "O café chique no centro financeiro era barulhento demais."
        show camille neutral at center
        narrator "Camille usava um blazer muito caro, checando planilhas no tablet enquanto tomava um espresso duplo. Não havia pedras místicas ou sorrisos acolhedores. Apenas uma gerente de RH absurdamente eficiente."
        camille "Demiti três pessoas do setor ontem. A reestruturação da empresa me exige resultados limpos e sem emoção."
        mc "Você parece exausta, Camille."
        camille "Eu estou lucrando. Isso que importa."
        narrator "Dividimos a conta do café. Ela saiu apressada para uma reunião de diretoria, afundada no mar cinzento do corporativismo, tendo deixado sua mágica no passado distante da Rua Aurora."
        jump creditos_finais
        
    elif status_camille == "romance":
        scene bg quarto_camille with fade
        narrator "A luz do sol entrava pela janela, refletindo nos prismas pendurados e espalhando arco-íris pelas paredes verdes do nosso quarto."
        show camille happy at center
        narrator "Camille estava sentada no tapete, com os olhos fechados, segurando uma ametista polida."
        mc "A meditação matinal terminou?"
        show camille blush
        camille "Sim. Eu estava alinhando minhas próprias energias antes de ir para o Centro Comunitário. Teremos vinte jovens na terapia de grupo hoje."
        narrator "Eu sentei ao lado dela, abraçando-a pelos ombros. Camille havia encontrado seu próprio caminho. Ela mesclou sua espiritualidade autêntica com terapia real, guiando jovens desamparados."
        mc "Nenhum charlatão por perto, certo?"
        camille "Nunca mais. Eu sou a minha própria bússola agora."
        narrator "Ela se virou, colocou a pedra sobre a mesa e me beijou lentamente, enchendo o ambiente com o cheiro adocicado de sálvia."
        camille "E você, meu amor... Você é o meu norte magnético. Minha casa. Minha alma gêmea."
        narrator "Longe das falsas promessas, o nosso universo particular era a coisa mais real que eu já havia sentido."
        jump creditos_finais
