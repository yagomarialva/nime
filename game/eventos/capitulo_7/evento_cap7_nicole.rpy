label evento_cap7_nicole:
    scene bg praia_quiosque with dissolve
    
    narrator "A barraca de pastel na beira da praia cheirava a óleo velho e liberdade."
    
    show nicole bikini at center
    
    narrator "Nicole, vestindo óculos escuros imensos, mordeu um pastel de queijo e deixou uma gota de óleo cair na canga."
    
    mc "A patricinha de Ibiza comendo pastel na praia de Maresias. O fim do mundo está próximo?"
    
    nicole "Cala a boca e me passa o caldo de cana."
    
    narrator "Ela deu um longo gole no copo de plástico. E pela primeira vez desde que a conheci, seus ombros não estavam tensos."
    
    nicole "Sabe de uma coisa? Nas férias de verão, minha mãe me levava pros Alpes Suíços ou pras Ilhas Maldivas. Era lindo. Mas eu odiava cada segundo."
    
    mc "Por que?"
    
    nicole "Porque não era férias. Era um desfile militar. Eu tinha que estar maquiada, vestida perfeitamente, sorrir para os executivos associados do meu avô. Cada jantar era um campo minado diplomático."
    
    narrator "Ela olhou para o pastel pela metade."
    
    nicole "Aqui... a casa é velha, a areia tá suja, nós quase morremos queimadas."
    
    menu:
        "Tudo tem um lado ruim. (Poupar energia)":
            mc "Pois é. Tá um caos."
            nicole "Sim... O caos cansa às vezes."
            narrator "Ela voltou a vestir uma máscara um pouco mais apática."
            $ add_affinity_points("nicole", -5)
            
        "Lembrá-la do que importa. (Gastar 15 Energia e 20 Carisma)":
            if store.player_stats["energy"] >= 15 and store.player_stats["charisma"] >= 20:
                $ update_player_stat("energy", -15)
                mc "Mas ninguém aqui tá te avaliando."
                narrator "Eu peguei um pedaço do pastel dela."
                mc "A Katia roubou uma garrafa térmica, a Larissa tá roncando na rede. Você não precisa performar, Nicole. Você pode só existir."
                narrator "Ela me encarou. Por trás dos óculos escuros, vi o brilho de lágrimas."
                nicole "Eu não performei quando puxei a Katia da fumaça na escada. Fui só... eu. Eu salvei a minha casa."
                mc "E agora você tá salvando esse caldo de cana de estragar."
                narrator "Ela riu alto, um som leve que se misturou com as ondas do mar."
                $ add_affinity_points("nicole", 25)
            else:
                mc "Eu queria te consolar, mas tô tonto demais no sol pra achar as palavras certas."
                nicole "Tá tudo bem. Vou voltar pra sombra antes que a gente asse."
                
    hide nicole
    return
