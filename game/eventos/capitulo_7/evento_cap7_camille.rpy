label evento_cap7_camille:
    # Usando ceu_azul ou bg generico para representar o lado da água
    scene bg praia_mar with dissolve
    
    narrator "O som das ondas quebrando quase cobria o batuque insuportável de uma caixa de som JBL."
    
    show camille bikini at center
    
    narrator "Camille estava sentada na posição de lótus, em cima de uma canga, tentando meditar. Mas uma família de turistas barulhentos jogava frescobol perigosamente perto dela."
    
    mc "Seu campo de força espiritual aguenta uma bolinha de borracha na testa?"
    
    camille "Estou tentando transcender a agressão visual da sunga de oncinha do pai da família, mas está sendo o maior teste do meu karma."
    
    narrator "Ela abriu um olho, suspirando. A paz interior dela estava no limite."
    
    menu:
        "Isso é praia, faz parte do pacote. (Poupar energia)":
            mc "Paciência, Camille. Praia é lugar de gente inconveniente. Ou você ignora, ou bota um fone de ouvido."
            camille "O barulho do mar deveria ser de todos... mas vejo que o caos impera. Vou recolher minhas coisas."
            narrator "Ela saiu chateada, perdendo a conexão com o lugar."
            $ add_affinity_points("camille", -5)
            
        "Espantar os turistas educadamente. (Gastar 15 Energia e 20 Carisma)":
            if store.player_stats["energy"] >= 15 and store.player_stats["charisma"] >= 20:
                $ update_player_stat("energy", -15)
                mc "Segura essa energia ruim aí que eu vou resolver. Observe o poder da diplomacia humana."
                narrator "Eu caminhei até a família que jogava frescobol, abri meu melhor e mais charmoso sorriso de morador local e comecei a falar."
                mc "Bom dia, amigos! Vocês não são daqui, né? Ó, só um toque de amigo: a guarda costeira avisou que esse trecho de areia onde vocês tão pisando é ponto cego e tá cheio de buraco de tatuí e ouriço. Tinha uma senhora espetada aqui agora há pouco. O trecho perto do quiosque é mil vezes melhor e a cerveja lá tá nevando!"
                narrator "O Carisma fluiu absurdamente bem. O pai da família concordou, os filhos pegaram a bola e eles migraram como patos 500 metros praia abaixo."
                mc "Área limpa."
                narrator "Camille me olhou com uma expressão de choque puro, e depois gargalhou."
                camille "Você acabou de usar a lábia de um trambiqueiro cósmico para devolver a paz ao meu universo. Eu estou eternamente grata."
                narrator "Ela deu um tapinha na canga ao lado dela. Sentei ali e dividimos o silêncio do mar por horas."
                $ add_affinity_points("camille", 25)
            else:
                mc "Eu ia lá falar com eles, mas eles tão com um cooler de três litros... não tenho coragem de comprar briga."
                camille "Não se desgaste. O mar cura tudo."
                
    hide camille
    return
