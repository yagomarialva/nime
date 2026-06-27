label capitulo12_harem:
    scene bg sala_reuniao with fade
    
    narrator "O conselho de ética da universidade parecia um tribunal. Uma mesa oval, seis membros do conselho severos, e o reitor liderando a reunião."
    
    narrator "Do outro lado, estávamos nós. As seis garotas, o professor Wendell (suando frio), e eu."
    
    show katia sad at left
    show nicole sad at right
    
    reitor "O Edital de Convívio Experimental da Rua Aurora foi denunciado por uma fraternidade de elite. Eles alegam barulho, festas inadequadas, falta de decoro estudantil e até... acusações de que um único aluno sustenta relações românticas com todas as residentes simultaneamente."
    
    reitor "Isso fere os princípios da moralidade da nossa instituição. O edital será cancelado e a propriedade será repassada à Fraternidade Alfa imediatamente."
    
    hide katia
    hide nicole
    
    narrator "As garotas entraram em choque. Katia tentou argumentar as leis, mas foi silenciada. Nicole ofereceu dinheiro, mas foi repreendida."
    
    reitor "A palavra final é minha. A menos que alguém tenha uma defesa irrefutável sobre por que essa casa... disfuncional... merece existir."
    
    narrator "Todos olharam para mim."
    
    menu:
        "Defender o caos: Somos disfuncionais, sim. Mas somos uma família, e nós gabaritamos as provas finais provando que o edital é um sucesso acadêmico e emocional.":
            $ store.status_harem = "romance"
            mc "Seu reitor, com todo o respeito. Festas ocorreram? Sim. O convívio é caótico? Sim."
            mc "Mas olhe as notas. Larissa gabaritou anatomia. Huey entregou as melhores pinturas do curso. Katia estabilizou o grêmio. Camille, Samantha e Nicole fecharam o semestre com honras."
            mc "A Rua Aurora não é só um dormitório. É um sistema de suporte. Nós salvamos uns aos outros."
            
            narrator "As garotas seguraram minhas mãos por debaixo da mesa."
            reitor "A excelência acadêmica não pode ser ignorada... O edital será mantido."
            narrator "Gritamos de alegria. Nós vencemos o sistema juntos."
            
        "Aceitar a derrota passivamente: Nós causamos muitos problemas. Acho que a fraternidade merece a casa.":
            $ store.status_harem = "amizade"
            mc "Sendo sincero, não temos defesa. Nós realmente causamos muito barulho. É justo que entreguemos a casa."
            
            narrator "As garotas me olharam com decepção profunda."
            reitor "Decisão sensata. Desocupem o imóvel em 30 dias."
            narrator "Nós empacotamos tudo e cada um foi morar em cantos opostos da cidade. A amizade continuou em um grupo de WhatsApp, mas a magia da convivência havia morrido."
            
        "Salvar a própria pele: Eu fui forçado a morar com essas malucas pelo edital! A culpa é delas!":
            $ store.status_harem = "ruina"
            mc "Reitor, eu sou uma vítima aqui! Eu fui jogado numa casa com seis garotas caóticas. Elas que organizavam as festas!"
            
            narrator "O silêncio mortal que recaiu sobre nós foi pior que qualquer punição."
            reitor "Desocupem a casa. Quanto a você, garoto, espero que arrume alojamento rápido."
            narrator "Nas ruas, minhas malas foram jogadas na calçada pela Samantha. Nenhuma delas olhou para trás. Fui exilado do grupo para sempre."
            
    scene black with fade
    call end_of_chapter_validation("capitulo13")
