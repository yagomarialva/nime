label capitulo2_crise_conta:
    play music campus_ambient fadein 2.0
    scene bg sala_jantar with fade
    
    narrator "Era o fim da semana. E o apocalipse tinha acabado de ser entregue pelo correio."
    
    show nicole angry at center
    
    narrator "Nicole segurava um boleto impresso como se fosse uma sentença de morte. A mão dela tremia."
    
    nicole "R$ 450,00 de energia elétrica?! Isso é humanamente impossível! O que vocês estão fazendo, enriquecendo urânio nos quartos?!"
    
    show katia neutral at left
    
    katia "O meu ventilador só liga à noite. Pergunta pro ciborgue gamer no segundo andar."
    
    show larissa sad at right
    
    larissa "Eu... eu uso o chuveiro bastante por causa do suor do treino. Mas não achei que seria tanto assim."
    
    nicole "O professor Wendell avisou que a bolsa cobre o aluguel, NÃO o consumo irresponsável de energia! Se a gente não pagar isso até amanhã, o edital inteiro cai."
    
    mc "Nicole, acalma. Quanto cada um tem?"
    
    narrator "Fizemos a matemática. A conta não fechava. Estava faltando uma quantia significativa."
    
    menu:
        "Usar suas economias para salvar a casa (Gastar 100 Money)":
            if store.player_stats["money"] >= 100:
                $ update_player_stat("money", -100)
                mc "Certo. Eu completo o que falta."
                narrator "Nicole olhou para as notas que coloquei na mesa como se fosse o Santo Graal."
                nicole "Você... você vai cobrir o déficit?"
                mc "Não se acostuma. Mês que vem a gente rateia essa merda direito."
                narrator "O suspiro de alívio coletivo foi palpável."
                $ add_affinity_points("nicole", 15)
                $ add_affinity_points("samantha", 10)
                $ add_affinity_points("larissa", 10)
            else:
                mc "Eu ia oferecer para completar, mas eu estou literalmente falido."
                nicole "Ótimo. Então estamos todos despejados."
                narrator "A tensão atingiu o limite crítico. Ninguém falou com ninguém pelo resto do dia."
                $ add_affinity_points("nicole", -10)
                
        "Não pagar. Jogar a responsabilidade para quem gastou.":
            mc "A conta é alta porque a Samantha não desliga o PC e a Larissa toma quatro banhos por dia. As duas que se virem pra pagar o excesso."
            narrator "Katia deu um assovio baixo."
            katia "Brutal. E justo."
            larissa "Mas eu não tenho dinheiro! Minha bolsa atlética mal paga a comida!"
            nicole "Vocês são todos inúteis!"
            narrator "A casa implodiu em gritos. O caos foi absoluto."
            $ add_affinity_points("nicole", -20)
            $ add_affinity_points("larissa", -15)
            $ add_affinity_points("samantha", -15)
            
    # === A CHEGADA DE HUEY ===
    narrator "Estávamos no meio do impasse quando três batidas suaves soaram na porta da frente."
    
    mc "Sério? Mais cobranças agora?"
    
    narrator "Eu fui até a porta e a abri."
    
    show huey sad at center
    
    narrator "Havia uma garota muito baixa na varanda. Ela usava um avental absurdamente manchado de todas as cores de tinta imagináveis."
    narrator "Ela cheirava a terebintina e lavanda."
    
    "???" "O-oi... Meu nome é Aline, mas podem me chamar de Huey... Eu sou a quinta vaga remanescente..."
    
    narrator "Ela olhou para o pandemônio que era a sala de estar, apertou um pincel contra o peito e deu um passo para trás, apavorada."
    
    huey "Ou... talvez eu deva voltar depois..."
    
    mc "Acho que a tinta no seu avental é a única coisa colorida no nosso dia, Huey. Entra."
    
    scene black with fade
    
    narrator "O Capítulo 2 chegou ao fim. Com as contas batendo na porta e cinco gênios desajustados sob o mesmo teto."
    
    if "capitulo3" not in persistent.unlocked_chapters:
        $ persistent.unlocked_chapters.append("capitulo3")
        
    jump capitulo3
