label evento_nicole_biblioteca:
    scene bg biblioteca with dissolve
    
    narrator "Livros de Direito Civil estavam espalhados pelo chão da biblioteca como se tivessem explodido."
    
    show nicole sad at center
    
    narrator "Nicole estava com olheiras fundas, segurando a cabeça enquanto lia furiosamente a décima página do regimento interno da universidade."
    
    mc "Você não dormiu desde que ela foi embora, não é?"
    
    nicole "Dormir não acha brechas legais. Se eu não provar que sou independente até as cinco da tarde, os advogados dela entram com a petição de remoção do edital."
    
    narrator "Ela jogou o livro na mesa, frustrada."
    
    nicole "É inútil. O edital protege minorias sociais e estudantes de baixa renda. A declaração do imposto de renda da minha mãe me joga no 1%% mais rico do país. Eles só vão ver os números. Nunca vão ver que eu não tenho um centavo meu e que se eu voltar pra lá... a minha vida acaba."
    
    menu:
        "Isso é problema de rico. (Poupar energia)":
            mc "Bom, pelo menos se você for expulsa, você vai pra uma mansão, e não pra debaixo da ponte."
            narrator "Nicole olhou pra mim com uma dor tão crua que eu me arrependi no momento seguinte."
            nicole "Tem gaiolas que são de ouro. Mas não deixam de ser gaiolas. Vá embora."
            $ add_affinity_points("nicole", -15)
            
        "Ajudar na Pesquisa (Requer 15 Energia e 10 Intelecto)":
            if store.player_stats["energy"] >= 15 and store.player_stats["intelligence"] >= 10:
                $ update_player_stat("energy", -15)
                mc "Larga esse livro. A regra de baixa renda do edital tem uma cláusula de rompimento de vínculo familiar por abandono afetivo ou financeiro material."
                narrator "Sentei ao lado dela, puxando os papéis."
                mc "Ela bloqueou seus cartões hoje. Oficialmente, e de forma documental, a partir de hoje você não recebe absolutamente nenhum sustento da sua família."
                
                narrator "Precisamos conectar as cláusulas corretas para montar a defesa."
                call screen minigame_memoria(45.0)
                $ success = _return
                
                if success:
                    narrator "Os olhos da Nicole brilharam. Uma centelha de esperança pela primeira vez."
                    nicole "Mas... os advogados dela podem rebater."
                    mc "Eles teriam que provar repasse financeiro. Se você abdicar oficialmente da conta conjunta em cartório hoje à tarde, não existe mais prova de repasse."
                    narrator "Nicole me abraçou. Foi um reflexo involuntário. Ela agarrou meus ombros e enterrou o rosto no meu casaco, soluçando baixinho."
                    nicole "Obrigada... Meu Deus, obrigada..."
                    $ add_affinity_points("nicole", 25)
                else:
                    narrator "Eu embaralhei os papéis, perdendo o raciocínio no meio do cansaço."
                    nicole "Tudo bem, a gente tentou... Acho que não adianta forçar a barra. Os advogados dela vão encontrar um jeito de rebater..."
                    mc "Sinto muito, Nicole. Mas vamos pensar em algo."
            else:
                mc "Eu queria te ajudar com a papelada, mas essas letras estão dançando na minha frente e eu não lembro nada de direito..."
                nicole "Tudo bem. A culpa é minha por estar nessa situação. Pode descansar."
                
    hide nicole
    return
