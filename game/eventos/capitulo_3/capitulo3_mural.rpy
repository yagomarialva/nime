label capitulo3_mural:
    play music campus_ambient fadein 2.0
    scene bg sala_jantar with fade
    
    narrator "A sala estava forrada com jornais velhos. A parede outrora pálida e deprimente estava agora dividida em fita crepe."
    
    show nicole neutral at right
    
    nicole "Temos quatro horas antes que o professor Wendell venha inspecionar a casa. Huey, o comando é seu. Por favor, não destrua o nosso teto."
    
    show huey neutral at left
    
    huey "A arte não destrói. Ela... reorganiza a dor."
    
    show larissa happy at center
    
    larissa "Isso aí! Vamos reorganizar a dor com rolos de tinta! Eu começo!"
    
    narrator "Larissa mergulhou um rolo imenso no balde de tinta amarela e girou para a parede com o ímpeto de quem vai sacar uma bola de vôlei."
    
    narrator "O resultado foi desastroso."
    
    mc "Larissa, cuidado--!"
    
    narrator "O cabo do rolo bateu no balde de magenta, que voou pelo ar e espatifou no chão, espirrando tinta nas pernas de Nicole e Katia."
    
    show nicole angry at right
    
    nicole "O MEU UNIFORME! Larissa, você é um elefante numa loja de cristais!"
    
    katia "Droga, Larissa! Era só passar a porra do rolo na parede!"
    
    show larissa sad at center
    
    larissa "Desculpa! Eu... eu calculei mal a força. Meu joelho cedeu de novo e eu..."
    
    camille "Respirem. Onde há caos, há fertilidade para o novo."
    
    samantha "Isso é um evento Quick Time! Alguém aperta [[X] para limpar!"
    
    narrator "Eu olhei para Huey, esperando que ela entrasse em pânico com a destruição do seu ambiente de trabalho."
    narrator "Em vez disso, os olhos dela estavam cravados na poça de tinta magenta se misturando com os respingos amarelos no jornal."
    
    huey "É... é violento. Mas tem calor. Tem vida."
    
    narrator "Ela largou os pincéis caros que Nicole tinha comprado. Abaixou-se, sujou as duas mãos de tinta do chão e foi até a parede."
    narrator "Smack!"
    
    huey "Vocês estão com medo de se sujar. Esse é o problema."
    
    mc "Eu não acredito que vou fazer isso..."
    
    narrator "Eu afundei minhas mãos na tinta e bati na parede ao lado da marca da Huey."
    
    narrator "Uma por uma, o choque foi passando. Até Nicole, depois de um longo suspiro derrotado, tirou as luvas e sujou as mãos. Nós passamos as próximas três horas transformando a parede num caos de cores, risadas e tinta voando."
    
    scene bg casa_interior with fade
    
    narrator "Quando terminamos, parecíamos figurantes de um filme de guerra colorida. O mural não era nada clássico. Era abstrato, vivo, quase selvagem. O professor Wendell certamente teria um infarto, ou nos daria um dez."
    
    narrator "O silêncio confortável caiu sobre a casa. Fui até o corredor pegar algumas toalhas."
    
    play sound "ringtone.ogg"
    
    narrator "O toque estridente de um celular cortou o silêncio. Vinha do corredor."
    
    narrator "Espiei pela fresta. Larissa estava de costas, o celular pressionado na orelha. A postura sempre ereta dela estava curvada."
    
    larissa "Sim, doutor. Eu sei o que a ressonância disse, mas... não pode ser cirúrgico."
    
    narrator "A voz dela tremia de um jeito que eu nunca tinha ouvido. O tom vibrante tinha sumido completamente."
    
    larissa "Se eu operar o joelho agora, eu perco a temporada. Eu perco o patrocínio. Eu... perco tudo."
    
    narrator "Ela escorregou pela parede até sentar no chão, abraçando as pernas pintadas de amarelo."
    
    larissa "Por favor, tem que ter outro jeito..."
    
    scene black with fade
    
    narrator "O Capítulo 3 chegou ao fim."
    
    if "capitulo4" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo4")
        
    return
