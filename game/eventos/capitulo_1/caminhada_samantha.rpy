# === ESCAPE PARA O MUNDO REAL COM SAMANTHA ===
label capitulo1_caminhada_samantha:
    scene bg campus_night with fade
    show samantha sad at center
    
    narrator "Samantha praticamente correu pelos primeiros cem metros até sumirmos do perímetro da festa. Seu peito subia e descia bruscamente."
    
    samantha "M-meu Deus. Como as pessoas suportam essa densidade de NPCs com áudio bugado?"
    
    narrator "Ela estava brincando em linguagem gamer, mas seus ombros caídos denunciavam uma exaustão física real. A barra social dela havia negativado."
    
    mc "Não acho que eles escurecem os olhos sob as luzes da estroboscópica como nós fazemos."
    
    samantha "E-eles gostam. De verdade. Parecem se recarregar disso."
    
    narrator "Eu caminhei sempre a um braço e meio de distância. Não queria forçar contato visual ou proximidade, sabendo que ela só precisava do escuro."
    
    menu:
        "Silêncio absoluto":
            $ points_samantha += 3
            narrator "Fiz do trajeto um grande campo silencioso. Nem uma palavra trocada. Apenas fomos e pronto."
            samantha "Você... é um bom suporte. Calibração perfeita."
            
        "Falar sobre baterias":
            $ points_samantha += 2
            mc "Você não precisava ter ido à quest principal se estava sem stamina nos níveis anteriores."
            samantha " FOMO, sabe? O terrível medo de perder a lore."
            
        "Afirmar que a tirei de lá":
            $ points_samantha += 1
            mc "Bom, agora o cenário engavetou a festa. Pode suspirar."
            samantha "S-suspirei mentalmente."
            
    scene bg house_exterior_night with fade
    narrator "Quando ela avistou os números fluorescentes do interfone de seu bloco universitário, sua respiração finalmente se normalizou."
    
    samantha "Eu estava sendo devorada lá dentro... e seria estúpido ir embora sozinha esbarrando em bêbados nos corredores."
    narrator "Ela segurou o colar em seu pescoço."
    samantha "Obrigada pelo ponto de salvamento. Prometo não abusar dos buffs com tanta frequência."
    
    narrator "Samantha correu para dentro num tropeço nervoso. Fiquei ali ouvindo a porta fechar em um clique seco, como um aviso de tela apagada."
    jump capitulo1_quarta_escolha
