label capitulo10_harem:
    scene bg sala_jantar with dissolve
    
    narrator "A Semana de Provas Finais. O Professor Wendell ameaçou despejar quem reprovasse."
    
    narrator "Eu não tinha escolhido uma única garota no telhado durante os fogos. Eu escolhi todas elas. E agora, o peso dessa escolha caiu sobre meus ombros na forma de um cronograma impossível."
    
    mc "Ok, pessoal! Atenção!"
    
    show larissa happy at left
    show samantha happy at right
    
    narrator "Larissa, Samantha, Camille, Nicole, Katia e Huey olharam pra mim. Todas desesperadas por motivos diferentes."
    
    mc "Nós somos uma família. Se uma cai, todas caem. E eu não vou deixar o Professor Wendell chutar ninguém."
    
    mc "Larissa, você estuda anatomia com a Katia. Ela é disciplinada e vai te forçar a ler. Katia, quando você surtar de estresse, a Larissa te obriga a correr no quarteirão pra liberar endorfina."
    
    hide larissa
    hide samantha
    
    show katia blush at left
    show larissa happy at right
    
    katia "Isso... na verdade, é um plano tático razoável."
    larissa "Fechado! Se ela tentar ler jurisprudência depois das 22h, eu amarro ela numa cadeira."
    
    hide katia
    hide larissa
    
    mc "Camille, sua prova de filosofia é abstrata, e a Huey precisa relaxar o cérebro das exatas lendo coisas humanas. Vocês duas vão fazer debate socrático na varanda."
    
    show camille gentle at left
    show huey neutral at right
    
    huey "Ouvir os argumentos místicos dela vai forçar meu cérebro a encontrar falhas lógicas. É um excelente exercício de depuração de código mental."
    camille "E eu vou inundar seu espírito de luz. Namastê."
    
    hide camille
    hide huey
    
    mc "Nicole, eu vou revisar Relações Internacionais com você, e a Samantha vai ajudar a criar mapas mentais coloridos no tablet."
    
    show nicole happy at left
    show samantha happy at right
    
    nicole "Desde que os mapas mentais combinem com a minha paleta de cores..."
    samantha "Eu vou fazer em neon e estética Cyberpunk. Ponto final."
    
    hide nicole
    hide samantha
    
    $ init_harem_game()
label loop_harem_game:
    call screen minigame_harem
    
    if _return == "lose":
        narrator "O caos venceu. Uma das garotas teve um colapso e puxou o resto pro buraco."
        mc "Não! Reagrupem! Voltem pros postos, vamos tentar de novo!"
        $ init_harem_game()
        jump loop_harem_game
        
    scene black with fade
    
    narrator "Foi o caos mais absoluto. Eu dormi uma média de 3 horas por noite."
    narrator "Fiz litros de café, mediei brigas por apostilas, apaguei incêndios emocionais e ouvi choros de desespero à meia-noite."
    
    scene bg sala_jantar with dissolve
    
    narrator "Sexta-feira. O dia D. As notas foram afixadas."
    
    show katia happy at left
    show larissa happy at right
    
    katia "O boletim de todo mundo... a média mais baixa foi o 7.5 da Larissa."
    larissa "7.5 É VITÓRIA NA PRORROGAÇÃO, BEBÊ!"
    
    show nicole happy
    show samantha happy
    show camille gentle
    show huey gentle
    
    narrator "A sala explodiu em comemoração."
    
    nicole "Nós conseguimos. Pelo menos mais um semestre de caos nessa casa."
    
    narrator "Eu estava tão cansado que mal conseguia ficar em pé."
    
    mc "Viu? Eu disse que a gente... ia..."
    
    narrator "Minhas pernas cederam. O cansaço finalmente me pegou."
    
    scene black with fade
    
    narrator "Quando abri os olhos, eu estava deitado no sofá. Havia um cobertor pesado sobre mim."
    
    scene bg sala_jantar with dissolve
    
    narrator "Todas as seis garotas estavam espalhadas pela sala. Samantha dormia no tapete. Larissa estava no puf. Camille meditava silenciosamente, enquanto Katia, Nicole e Huey organizavam uma bandeja cheia de comida pra mim."
    
    mc "Gente..."
    
    narrator "Elas olharam pra mim. Os sorrisos eram radiantes e cheios de carinho."
    
    katia "Você acordou. Idiota irresponsável. Você zerou sua barra de energia por nossa causa."
    
    nicole "Mas... obrigada. Você salvou essa casa inteira."
    
    narrator "Huey sentou na borda do sofá, segurando uma caneca quente."
    
    huey "Você é o núcleo processador central desta residência. Agora, descanse. Nós cuidamos do sistema."
    
    narrator "Eu fechei os olhos de novo, com o cheiro da comida, do café e de lavanda."
    
    narrator "Eu não estava sozinho. E eu tinha a melhor família bagunçada do mundo."
    
    call end_of_chapter_validation("capitulo11")
