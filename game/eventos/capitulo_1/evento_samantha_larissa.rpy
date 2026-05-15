# === EVENTO JOGOS: SAMANTHA E LARISSA ===
# Tema: O peso irreal contra a exaustão física que anestesia a dor

label evento_samantha_larissa:
    scene bg arcade with fade
    
    narrator "A sala de lazer da universidade tremia letargicamente. O som polifônico das máquinas de basquete de fliperama era quase insuportável no recinto quente e fechado."
    
    show larissa sad at left
    show samantha neutral at right
    
    narrator "A máquina lançou outra bola artificial. Larissa bateu a bola mecânica de plástico escorregadio contra a borda do aro com tanta fúria que o impacto ecoou além da máquina."
    
    larissa "Zero suor. Zero peso. Sem gravidade de verdade. Que desgraça inútil que anestesia os sentidos."
    
    narrator "Ao lado, em numa cadeira de couro descascada escorada na parede escura, Samantha batia as unhas sobrecrescidas em um teclado customizado iluminado, sem nem olhar pra cima."
    
    samantha "Vocês viciados em dopamina muscular acham que só o suor correndo no supercílio anestesia dor. O input do pixel exige carga cognitiva... algo que te falha agora mesmo."
    
    larissa "Carga do quê? Você fica encurvada criando hérnias cervicais empurrando teclas brilhantes num mundo vazio! Se tomar um soco de verdade da bola, tu não levanta. Só a dor real cala a dor do peito!"
    
    narrator "Samantha parou de digitar, os leds azuis da tela de load tingiam as olheiras profundas em seu rosto pálido."
    
    samantha "E correr vinte quilômetros arrebentando seu oxigênio cala a sua dor, 'campeã' do desespero? Nós só trocamos cansaço mental por tendões rompidos. Eu sei exatamente o que eu jogo. Mas você foge das suas derrotas como uma hiena."
    
    narrator "O silêncio engoliu o apito tosco da máquina de basquete quando a partida eletrônica morreu sem créditos. Larissa parecia pender as mãos prontas para jogar todas aquelas bolas no chão num acesso destrutivo invisível."
    
    mc "Acho que bater nas molas falsas não amorteceu o barulho que vocês tentam ensurdecer lá dentro nem por um minuto."
    
    narrator "As duas garotas não demonstraram choque por mim. Apenas afundaram mais fundo, as peças incompatíveis gritando ao menor toque."
    
    menu:
        "Frieza sobre os motores (Samantha)":
            $ points_samantha += 3
            mc "A mente dela pelo menos domina o jogo falso antes da lixeira mental inundar de angústia. Um passo físico em falso na quadra, Larissa, e você desaba."
            samantha "Checkmate no raciocínio da besta. Pelo menos meus pixels tem botão de pause da angústia."
            larissa "Se esconda num botão de salvar enquanto eu resolvo os problemas com meus próprios pés de forma real, aberração de LCD."
            
        "Defender válvulas exaustoras (Larissa)":
            $ points_larissa += 3
            mc "Cair de queixo pelo menos é ser parte do planeta com os dois pés. O oxigênio queimando purifica os pulmões mortos."
            larissa "Ouviram? Carga viva. Eu enfrento a realidade até sangrar, enquanto você chora por polígonos, garota do teclado."
            samantha "Desgaste biológico puro justificado com poesia esportiva barata. Patético..."
            
    narrator "Larissa girou nos pés do fliperama, o tênis guinchando agudamente, rumando irritantemente e rapidamente para fora do recinto apertado como alguém presa na clausura do tédio."
    narrator "Samantha, afundando mais suas costas fracas no couro esfarrapado da cadeira, recomeçou os cliques mortos e sem ritmo. Exiladas."
    
    return
