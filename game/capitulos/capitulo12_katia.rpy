label capitulo12_katia:
    scene bg sala_gremio with fade
    
    narrator "A sala do Grêmio Estudantil, que Katia lutou tanto para manter, estava revirada. Homens engravatados carregavam caixas com arquivos."
    
    show katia sad at center
    
    narrator "Katia estava encostada na parede, pálida e segurando um ofício assinado."
    
    mc "Katia! O que tá acontecendo?!"
    
    katia "O novo reitor. Ele baixou uma portaria de emergência cortando as verbas. E a primeira coisa que ele dissolveu foi o Grêmio. E todos os clubes associados."
    
    narrator "Ela olhou para uma caixa no chão, onde os pôsteres do Clube de Cinema estavam jogados."
    
    katia "Ele chamou meu mandato de 'um circo inútil'. É isso. Eu perdi. Dois anos de construção política destruídos por uma canetada de um burocrata."
    
    menu:
        "O reitor deu uma canetada. Mas você tem o povo. Vamos organizar o maior protesto do campus.":
            $ store.status_katia = "romance"
            mc "Ele trancou a sala, mas não trancou a voz dos alunos. Você tem carisma, Katia."
            mc "Vamos pro pátio. Eu serei o seu chefe de gabinete. Vamos fazer barulho até ele recuar."
            
            show katia blush
            katia "Você... você ficaria do meu lado no megafone?"
            mc "Até perdermos a voz."
            narrator "Ela sorriu, e o fogo bélico e apaixonado voltou aos olhos dela. Ela pegou os pôsteres do chão, pronta para a guerra."
            
        "Focar no prático: Acabou, Katia. Foca nas matérias de Direito, esquece a política estudantil.":
            $ store.status_katia = "amizade"
            mc "Você tentou. Mas a reitoria é maior que você. Deixa isso pra lá e foca na OAB."
            
            show katia neutral
            katia "É. Pelo menos meu currículo acadêmico tá intacto."
            narrator "Ela assentiu, entregando os pontos. Ela seria uma excelente advogada, mas a líder estudantil revolucionária havia sido apagada."
            
        "Criticar a gestão dela: Talvez o reitor tenha razão. Você perdeu muito tempo com filmes em vez do orçamento.":
            $ store.status_katia = "ruina"
            mc "Pra ser sincero, o Clube de Cinema era meio inútil pra faculdade. O reitor só foi prático."
            
            show katia angry
            katia "Como é que é?! Você tá defendendo um ditador acadêmico?!"
            narrator "Ela amassou o ofício e jogou na minha direção."
            katia "Você é um vendido igual a eles. Sai da minha frente. Nunca mais se intrometa nos meus assuntos."
            
    scene black with fade
    call end_of_chapter_validation("capitulo13")
