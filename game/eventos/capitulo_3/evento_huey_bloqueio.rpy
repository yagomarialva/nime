label evento_huey_bloqueio:
    scene bg quintal with dissolve
    
    narrator "O quintal estava silencioso. Huey estava sentada na grama, cercada por dezenas de potes de tinta abertos, mas o pincel na mão dela estava completamente seco."
    
    show huey neutral at center
    
    mc "Problemas para domar o 'desespero de 1970' da parede?"
    
    huey "O problema não é a parede. São as tintas."
    
    narrator "Ela levantou um tubo de acrílico azul."
    
    huey "Isso se chama 'Azul Cerúleo'. Mas quando eu olho pra Nicole, a energia dela é um azul... agudo. Cortante como gelo. Esse azul do tubo é redondo. Não machuca ninguém."
    
    mc "Você está tentando pintar a gente no mural?"
    
    huey "Vocês são as cores que eu tenho. A Larissa é um amarelo que cega. A Samantha é um cinza estático de televisão quebrada. Mas eu não consigo replicar isso com potes genéricos da papelaria. Falta alma."
    
    menu:
        "Isso é só desculpa para não pintar. Faz com o que tem. (Poupar energia)":
            mc "Huey, o professor Wendell não liga pra alma. Ele liga pra tinta na parede. Só desenha umas flores e vamos acabar com isso."
            narrator "Huey piscou, como se eu tivesse acabado de sugerir um sacrifício humano."
            huey "Flores...? Sem... propósito?"
            narrator "Ela abraçou os joelhos. A conexão tinha sido cortada."
            $ add_affinity_points("huey", -10)
            
        "Então vamos criar as cores certas. (Gastar 15 Energia e 10 Intelecto)":
            if store.player_stats["energy"] >= 15 and store.player_stats["intelligence"] >= 10:
                $ update_player_stat("energy", -15)
                mc "Se o azul da Nicole é gelo e o amarelo da Larissa cega, então precisamos misturar o oposto nelas pra equilibrar."
                narrator "Eu me ajoelhei na grama, pegando o tubo de azul redondo e pingando uma gota de preto fosco e cinza metálico."
                mc "Tenta esse. Frio, eficiente e meio assustador. Igualzinho à síndica."
                narrator "Os olhos da Huey brilharam. Foi como se um farol tivesse acendido dentro dela."
                huey "Sim! Sim, a textura está perfeita! A refração da luz... você tem um olho sensível para os tons escondidos."
                $ add_affinity_points("huey", 20)
            else:
                mc "Eu queria te ajudar a misturar isso, mas minha cabeça dói só de pensar em teoria das cores agora."
                huey "Tudo bem. A arte requer que a mente esteja afinada... descanse."
                
    hide huey
    return
