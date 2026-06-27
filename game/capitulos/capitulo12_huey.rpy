label capitulo12_huey:
    scene bg atelie_huey with fade
    
    narrator "O ateliê improvisado de Huey na república estava irreconhecível. As telas coloridas e mágicas que ela pintava estavam todas no chão."
    
    narrator "No cavalete central, havia apenas uma tela inteiramente pintada de cinza escuro."
    
    show huey sad at center
    
    mc "Huey? Por que as suas tintas estão no lixo?"
    
    huey "A galeria nacional respondeu sobre o meu portfólio."
    
    narrator "Ela me entregou uma carta amassada. A crítica do curador era destrutiva. Ele chamava a arte dela de 'infantil, amadora, sem estrutura acadêmica e baseada em uma fantasia patética'."
    
    huey "A magia não existe. O mundo é cinza. Eu sou apenas uma garota desenhando rabiscos idiotas que ninguém quer ver."
    
    narrator "Ela pegou um tubo de tinta preta e ameaçou esguichar na última tela colorida que restava."
    
    menu:
        "Não pinte para a galeria. Pinte para você. Pinte a magia que a gente viveu.":
            $ store.status_huey = "romance"
            mc "Larga essa tinta."
            mc "Eles não entenderam a sua arte porque eles não veem o mundo como você. Eles vivem num escritório sem graça, você vive na Rua Aurora!"
            
            narrator "Peguei um pincel, molhei na tinta amarela e sujei o rosto dela de brincadeira."
            
            mc "A magia existe. Eu sinto toda vez que olho pras suas pinturas... e pra você."
            
            show huey blush
            huey "Você... você não acha meus quadros infantis?"
            mc "Acho eles brilhantes."
            narrator "Ela soltou a tinta preta e me abraçou. Minhas roupas ficaram manchadas, mas o coração dela voltou a bater em cores vibrantes."
            
        "Focar no pragmatismo acadêmico: Talvez você deva estudar as técnicas que eles pedem.":
            $ store.status_huey = "amizade"
            mc "Talvez o curador tenha um ponto sobre a técnica. Se você estudar as regras acadêmicas, talvez eles te aceitem ano que vem."
            
            show huey neutral
            huey "Regras acadêmicas. Sim. Adotar a padronização."
            narrator "Ela guardou as tintas coloridas. Ela começaria a pintar quadros realistas e chatos. O sucesso chegaria, mas ela deixaria de ver magia nas coisas."
            
        "Concordar com a crítica: O curador tem razão. Parecia desenho de criança mesmo.":
            $ store.status_huey = "ruina"
            mc "Sendo sincero, eu não queria te magoar antes, mas o curador tá certo. Parece que você vive num mundo de fantasia."
            
            show huey angry
            huey "..."
            narrator "Ela não gritou. Ela simplesmente pegou a carta, a tela colorida, e jogou tudo no lixo, incluindo o pincel que eu tinha te dado."
            huey "A magia não existe. E você acabou de provar isso. Saia do meu ateliê."
            
    scene black with fade
    call end_of_chapter_validation("capitulo13")
