label evento_cap7_larissa:
    scene bg praia_mar with dissolve
    
    narrator "A lua iluminava o mar. Encontrei Larissa sentada na areia molhada, com a água batendo na cintura."
    
    show larissa bikini at center
    
    narrator "Ela estava massageando o joelho cirúrgico. A água fria do mar deveria ajudar na inflamação, mas o olhar dela estava distante e pesado."
    
    mc "Fisioterapia noturna?"
    
    larissa "Mais pra afogamento de mágoas."
    
    narrator "Ela suspirou."
    
    larissa "Quando a casa começou a queimar... a Nicole correu pra guiar as meninas. Você chutou a porta pra tirar a Samantha. E eu? Eu congelei. Minha perna me lembrou que eu não sou mais a atleta invencível. Eu sou a garota quebrada que precisa ser escoltada devagar nas escadas enquanto o teto cai."
    
    mc "Larissa..."
    
    menu:
        "O fogo não é uma olimpíada. (Poupar energia)":
            mc "Ninguém espera que você ganhe medalha de resgate de incêndio. Fica tranquila."
            larissa "Não é sobre a medalha. É sobre o peso morto."
            narrator "Ela afundou mais na água, fechando o rosto."
            $ add_affinity_points("larissa", -5)
            
        "Ajudá-la a andar contra as ondas. (Gastar 15 Energia e 10 Físico)":
            if store.player_stats["energy"] >= 15 and store.player_stats["fitness"] >= 10:
                $ update_player_stat("energy", -15)
                mc "Você não é um peso morto. O pilar mental da casa é você. E para a perna..."
                narrator "Entrei na água fria até a cintura, ficando na frente dela."
                mc "Apoia no meu ombro. Vamos andar contra a arrebentação. A resistência da água fortalece o músculo sem impacto na articulação."
                narrator "Ela hesitou, mas agarrou meu ombro. A força do mar nos empurrava, e eu usei todo o meu condicionamento para mantê-la estável."
                larissa "Dói menos... aqui na água."
                mc "A gente vai recuperar esse joelho. E você vai carregar a gente de novo se precisar. Uma perna por vez."
                narrator "Ela me olhou, e um sorriso sincero cortou a expressão de dor. O mar curou um pouco das feridas dela naquela noite."
                $ add_affinity_points("larissa", 25)
            else:
                mc "Queria te ajudar a fazer o exercício na água, mas tô sem energia nenhuma pra segurar a barra agora."
                larissa "Tudo bem. Pode ir dormir."
                
    hide larissa
    return
