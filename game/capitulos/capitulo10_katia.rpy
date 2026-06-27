label capitulo10_katia:
    scene bg biblioteca with dissolve
    play music "music/biblioteca.mp3" fadein 1.0
    
    narrator "A biblioteca do campus parecia uma panela de pressão prestes a explodir, e o epicentro era a mesa de Katia."
    
    show katia angry at center
    
    narrator "Ela estava cercada por doze pilhas perfeitas de anotações. Seus olhos tremiam de exaustão."
    
    katia "Se eu tirar 9.9 em Direito Administrativo, o comitê de reitoria não vai me indicar pro estágio de honra. Eu preciso do 10."
    
    mc "Katia, você já leu a mesma página cinco vezes nos últimos dez minutos."
    
    katia "A culpa não é minha se o parágrafo não está fixando! Eu só preciso de mais café."
    
    narrator "Antes que ela pudesse pegar o copo térmico, eu puxei a cadeira dela para trás e fechei o livro pesado."
    
    mc "Acabou. Você atingiu o limite de saturação."
    
    katia "O que você pensa que tá fazendo?! Devolve meu material!"
    
    mc "A gente vai pro quarto. E nós vamos assistir a um filme."
    
    narrator "Os olhos dela quase pularam do rosto."
    
    katia "Você tá insano?! Faltam 14 horas pra prova!"
    
    mc "E você não vai conseguir fazer a prova se tiver um colapso nervoso no meio da sala. Katia... você ama cinema. Quando foi a última vez que você viu um filme sem tentar criticar, só pra relaxar?"
    
    narrator "A raiva dela vacilou, dando lugar a uma vulnerabilidade rara."
    
    katia "Eu... eu não posso falhar. Eu não posso ser uma decepção."
    
    mc "O único jeito de você falhar é quebrando. Deixa eu cuidar de você, só hoje."
    
    $ init_clicker_game()
label loop_clicker_katia:
    call screen minigame_clicker
    
    if _return == "lose":
        katia "NÃO! DEIXA ESSES PAPÉIS AÍ, EU AINDA VOU LER O PRECEDENTE STF 432!"
        mc "Katia, me dá isso aqui. Tenta de novo, me entrega essas pastas!"
        $ init_clicker_game()
        jump loop_clicker_katia
        
    scene black with fade
    
    narrator "Nós sentamos no chão do quarto, encostados na cama. Coloquei o clássico favorito dela para rodar no projetor portátil: Cidadão Kane. Sem anotações. Sem estudos."
    narrator "No meio do filme, a respiração dela ficou pesada. A presidente do grêmio acadêmico havia capotado no meu ombro, finalmente descansando."
    
    scene bg predio_adm with dissolve
    
    show katia blush at center
    
    narrator "Dias depois, ela saiu da sala do Professor Wendell segurando o boletim."
    
    mc "E aí?"
    
    katia "Eu tirei 9.8. Eu perdi o décimo porque não citei uma jurisprudência irrelevante."
    
    mc "Ah. Eu sinto muito."
    
    katia "E eu... não me importo. Eles me deram a vaga no estágio mesmo assim. O 10.0 não era obrigatório."
    
    narrator "Ela se aproximou de mim, segurando firme as alças da mochila."
    
    katia "Eu percebi que tentar ser perfeita estava me matando. E... dormir no seu ombro foi a melhor escolha acadêmica que eu já fiz."
    
    mc "Isso é quase romântico, vindo de você."
    
    katia "Cala a boca."
    
    narrator "Ela segurou a gola da minha camisa, me puxou para perto e calou minha boca com a dela. Um beijo dominante, doce e com sabor de alívio."
    
    katia "Hoje à noite. O Poderoso Chefão, Parte 1. Não se atrase."
    
    call end_of_chapter_validation("capitulo11")
