label capitulo12_camille:
    scene bg casa_interior with fade
    
    narrator "Encontrei Camille sentada no chão da sala, cercada por caixas de papelão."
    
    narrator "Ela estava guardando seus cristais, incensos, tarôs e mapas astrais. Seu rosto estava apático, sem a serenidade habitual."
    
    show camille sad at center
    
    mc "Camille? Você tá de mudança?"
    
    camille "Estou empacotando o lixo. A mentora Esmeralda... o centro espiritual que eu frequentava..."
    
    narrator "Ela me entregou o celular. A tela mostrava uma reportagem investigativa. O centro era uma fraude colossal. A 'mentora' roubava o dinheiro dos jovens para comprar imóveis."
    
    camille "Ela dizia que eu tinha um dom cósmico. Era mentira. Tudo que eu acredito é uma mentira. Não existe magia, não existe energia. Apenas pessoas estúpidas como eu, sendo enganadas."
    
    narrator "Ela jogou brutalmente um cristal na caixa, rachando a pedra."
    
    camille "Vou aceitar a oferta da minha família. Trabalhar no escritório corporativo. É o mundo real."
    
    menu:
        "A magia nunca foi dela. A magia está na forma linda como você vê e cuida do mundo.":
            $ store.status_camille = "romance"
            mc "Esmeralda era uma fraude, mas você não é."
            mc "Lembra de quando você acalmou a casa inteira? Ou das coisas maravilhosas que você faz pela gente?"
            
            show camille blush
            camille "Mas... os cristais não curam nada..."
            mc "Talvez não. Mas a sua empatia cura."
            narrator "Ela parou de guardar as coisas. As lágrimas rolaram soltas, mas, dessa vez, de alívio. Ela afundou no meu abraço."
            
        "Focar na vida adulta: Talvez seja melhor. O escritório vai te dar estabilidade.":
            $ store.status_camille = "amizade"
            mc "A vida corporativa não é tão ruim. Pelo menos você terá um salário garantido e não será mais enganada."
            
            show camille neutral
            camille "É. Estabilidade. Sem ilusões."
            narrator "Ela fechou a caixa com fita adesiva. Ela estava segura, mas a Camille vibrante e mística havia desaparecido para sempre."
            
        "Invalidar a crença dela: Eu sempre soube que isso de cristais era uma grande bobagem. Demorou pra acordar.":
            $ store.status_camille = "ruina"
            mc "Sinceramente? Isso tudo sempre foi charlatanismo. Que bom que você finalmente abriu os olhos pra realidade."
            
            show camille angry
            camille "Você... você achava que eu era uma idiota o tempo todo?"
            narrator "Ela me olhou com uma frieza que eu nunca tinha visto nela."
            camille "Sai. Não toque nas minhas caixas. Não toque em mim."
            
    scene black with fade
    call end_of_chapter_validation("capitulo13")
