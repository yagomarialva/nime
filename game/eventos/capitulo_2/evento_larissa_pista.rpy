label evento_larissa_pista:
    scene bg quadra with dissolve
    
    narrator "O sol escaldante do meio-dia fritava o asfalto da pista de corrida da quadra da faculdade."
    narrator "Qualquer pessoa normal estaria almoçando, mas Larissa já estava na sua décima volta. O suor pingava do seu rosto, e o rabo de cavalo balançava como um pêndulo."
    
    show larissa happy at center
    
    mc "Você tem um reator nuclear escondido no lugar do coração, não é?"
    
    larissa "Haha! Quase! Se eu parar de me mexer, o enferruja. Quer apostar uma corrida?!"
    
    narrator "O sorriso dela era gigantesco. Energético. Perfeito demais."
    
    menu:
        "Nem fodendo. Fica pra próxima.":
            mc "Eu prefiro minha pulsação no ritmo normal, obrigado. Continua aí."
            larissa "Fraquinho! Te vejo na casa!"
            $ add_affinity_points("larissa", -5)
            
        "Apostado. Mas eu vou devagar. (Gastar 20 Energia)":
            if store.player_stats["energy"] >= 20:
                $ update_player_stat("energy", -20)
                mc "Ok, mas eu aviso que se eu desmaiar, a culpa é sua."
                narrator "Nós corremos. Larissa estava sempre alguns metros à frente, voando pela pista."
                narrator "Mas quando finalmente passamos da linha de chegada, notei algo bizarro."
                narrator "Larissa parou de forma abrupta e torceu o rosto. A mão dela voou direto para o joelho direito, apertando a rótula com uma força assustadora."
                mc "Você... tá legal?"
                narrator "No instante em que me ouviu, ela soltou o joelho e abriu aquele mesmo sorriso elétrico de antes."
                larissa "Perfeita! Venci você, não venci? Precisa de mais cardio, parceiro!"
                narrator "Ela estava mentindo. Os olhos dela estavam marejados de dor."
                $ add_affinity_points("larissa", 20)
            else:
                mc "Se eu correr dois metros com a energia que eu tenho agora, eu desabo na pista."
                larissa "Tudo bem, a gente tenta quando você estiver com a bateria cheia!"
                
    hide larissa
    return
