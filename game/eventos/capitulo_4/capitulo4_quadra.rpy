label capitulo4_quadra:
    play music campus_ambient fadein 2.0
    scene bg quarto_protagonista with fade
    
    narrator "Chega. O clima na casa estava insuportável. Eu não ia deixar a Larissa morrer no próprio quarto."
    
    narrator "Fui até o quarto dela, agarrei a cadeira de rodas (emprestada da enfermaria) e abri a porta de supetão."
    
    show larissa sad at center
    
    larissa "O que você tá fazendo?"
    
    mc "Te tirando dessa caverna. Senta na cadeira."
    
    larissa "Eu não vou sair daqui! Me deixa em paz!"
    
    mc "Senta na cadeira, Larissa. Ou eu vou te jogar por cima do ombro."
    
    narrator "Ela rosnou, mas a minha expressão não abria margem pra negociação. Ela se ajeitou na cadeira com dificuldade."
    
    scene bg quadra with dissolve
    
    narrator "Empurrei a cadeira até a quadra do campus. O cheiro de borracha e suor pairava no ar."
    
    larissa "Isso é crueldade. Você me trouxe pro único lugar que eu não posso mais usar."
    
    narrator "A voz dela embargou. Ela estava prestes a chorar de novo."
    
    mc "Você não perdeu o seu cérebro, Larissa. O joelho foi pro saco, mas a sua leitura de jogo e sua energia continuam aí."
    
    narrator "Eu tirei meu casaco e fui para a pista."
    
    mc "Eu vou correr. E você vai me treinar. Até eu vomitar."
    
    larissa "Você é louco."
    
    mc "Um, dois, três. Valendo!"
    
    narrator "Eu disparei. Logo na primeira volta, minha postura estava toda torta."
    
    larissa "Abaixa esses ombros! Você tá correndo igual um ganso!"
    
    # === AQUI CHAMA O MINIGAME DA QUADRA SE EXISTIR ===
    # call minigame_quadra
    
    narrator "Foram trinta minutos de tortura. Larissa gritava instruções do lado de fora. A tristeza dela tinha dado lugar ao instinto competitivo."
    
    mc "Arf... arf... tô morto..."
    
    show larissa happy at center
    
    narrator "Eu me joguei no chão, arfando. Quando olhei pra cima, Larissa estava sorrindo. Um sorriso verdadeiro, ainda que contido."
    
    larissa "Você precisa de muito cardio. Mas... você não é o pior aluno que eu já tive."
    
    mc "Viu só? Você ainda tem lugar na quadra."
    
    narrator "Ela limpou uma lágrima fugitiva no canto do olho."
    
    larissa "Obrigada. Por... não desistir de mim."
    
    scene bg casa_noite with fade
    
    narrator "A volta pra casa foi mais leve. Larissa jantou com as outras garotas pela primeira vez em dias. O fardo da depressão dela parecia ter diminuído metade do peso."
    
    narrator "Eu estava prestes a subir pro quarto quando a campainha tocou."
    
    mc "Quem vem à casa da Rua Aurora às onze da noite?"
    
    scene bg casa_interior with dissolve
    
    narrator "Eu abri a porta."
    
    show nicole neutral at right
    
    narrator "Nicole apareceu atrás de mim, segurando uma prancheta. Mas quando ela viu quem estava na porta, a prancheta caiu no chão."
    
    "???" "Essa é a pocilga que você chama de 'projeto independente', Nicole?"
    
    narrator "Uma mulher loira, com um casaco de pele impecável e um olhar frio como gelo cortante, entrou na casa sem pedir licença."
    
    nicole "Mãe... O que você está fazendo aqui?"
    
    "Mãe da Nicole" "Vim buscar minha filha. Chega de brincar de pobreza."
    
    scene black with fade
    
    narrator "O Capítulo 4 chegou ao fim."
    
    if "capitulo5" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo5")
        
    return
