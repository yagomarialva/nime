label evento_cap9_katia:
    scene bg predio_adm with dissolve
    
    narrator "O hall do prédio de administração estava forrado com corações de papel vermelho neon. No meio daquilo tudo, Katia parecia prestes a explodir."
    
    show katia angry at center
    
    narrator "Ela usava uma faixa na cabeça que dizia 'Cupido Oficial'."
    
    katia "O grêmio estudantil me odeia. Eles sabem que eu detesto essas frescuras românticas."
    
    mc "Correio Elegante, Katia? Essa é a coisa mais irônica que eu já vi na faculdade inteira."
    
    katia "Para de rir de mim e pega uma prancheta. Tem vinte bilhetes melosos que eu preciso entregar na praça de alimentação."
    
    menu:
        "Fugir. (Poupar energia)":
            mc "Katia, eu prezo pela minha dignidade. Vou organizar as caixas ali atrás."
            katia "Você me paga. Pode apostar."
            $ add_affinity_points("katia", 5)
            
        "Ajudar o Cupido. (Gastar 15 Energia e 20 Carisma)":
            if store.player_stats["energy"] >= 15 and store.player_stats["charisma"] >= 20:
                $ update_player_stat("energy", -15)
                mc "Me dá isso aqui. Mas eu vou cobrar caro pelo serviço postal do amor."
                narrator "Eu passei a próxima hora lendo os bilhetes ridículos e entregando com um sorriso charmoso."
                narrator "Quando voltei, Katia estava rindo da minha performance teatral."
                katia "Você não tem vergonha nenhuma, né? Você recitou um poema do bilhete pro capitão de xadrez."
                mc "Tudo em nome do amor. Aliás..."
                narrator "Eu puxei um dos cartões em branco de cima da mesa e escrevi algo rápido."
                mc "Eu tenho uma entrega pra Katia."
                narrator "Ela pegou o cartão desconfiada. Leu: 'Seus olhos me dão mais medo que o Professor Wendell, mas eu não consigo parar de olhar'."
                show katia blush
                katia "Seu idiota... isso foi péssimo."
                mc "Eu sei, mas eu tentei."
                katia "Obrigada... por me aturar nesse circo."
                narrator "O tom arrogante dela sumiu, substituído por um sorriso tímido que ela tentou esconder com a prancheta."
                $ add_affinity_points("katia", 20)
            else:
                mc "Eu acho que eu não levo jeito pra entregar essas coisas. Vou ficar aqui vendendo os cartões."
                katia "Só cuida do troco. O resto eu faço."
                $ add_affinity_points("katia", 10)
                
    hide katia
    return
