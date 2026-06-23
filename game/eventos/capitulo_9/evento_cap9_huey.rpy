label evento_cap9_huey:
    scene bg corredor_salas with dissolve
    
    narrator "O corredor do pavilhão de artes estava incrivelmente silencioso comparado ao resto do festival."
    
    show huey neutral at center
    
    narrator "Huey estava sentada no chão, perfeitamente alinhada com os azulejos, montando uma estrutura colossal usando apenas palitos de sorvete."
    
    mc "Isso parece frágil."
    
    huey "A fragilidade é apenas uma ilusão. Uma ponte de treliça distribui o peso igualmente pelos nós. Se a gravidade permitir, isso vai suportar até cinco quilos."
    
    mc "A arte da engenharia. Precisa de uma mão com a cola quente?"
    
    huey "Sim. Mas a precisão requerida é de milímetros. A cola derrete em três segundos."
    
    menu:
        "Ficar apenas observando. (Poupar energia)":
            mc "Minha precisão motora é de um elefante. Vou ficar de guarda pra ninguém chutar."
            huey "Aceitável. A segurança do perímetro é crucial."
            $ add_affinity_points("huey", 5)
            
        "Ajudar na ponte. (Gastar 15 Energia e 20 Inteligência)":
            if store.player_stats["energy"] >= 15 and store.player_stats["intelligence"] >= 20:
                $ update_player_stat("energy", -15)
                mc "Eu entendo de ângulos retos. Me dá essa pistola de cola."
                narrator "Sentei no chão ao lado dela, cruzando as pernas. Ela segurava as peças minúsculas enquanto eu aplicava gotas perfeitas de cola quente."
                narrator "Trabalhamos em um silêncio sincronizado que só a Huey conseguia proporcionar."
                narrator "Em um movimento, nossos ombros se tocaram. Ela não se afastou."
                huey "A sua geometria motora é eficiente."
                mc "Acho que a gente faz uma boa dupla de montagem."
                huey "Estatísticas confirmam uma taxa de sucesso de 92%% quando operamos juntos."
                narrator "Ela olhou pro lado, e eu vi o menor dos sorrisos no canto da boca dela."
                mc "Os outros 8%% são falhas catastróficas?"
                huey "Os outros 8%% são momentos em que o fator humano... causa variações não mapeadas no meu sistema."
                $ add_affinity_points("huey", 20)
            else:
                mc "Eu não lembro nada de trigonometria, vou acabar torto."
                huey "Reconhecer as próprias limitações é o primeiro passo da sabedoria matemática."
                $ add_affinity_points("huey", 10)
                
    hide huey
    return
