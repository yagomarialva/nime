label evento_nicole_limpeza:
    scene bg biblioteca with dissolve
    
    narrator "A biblioteca da Solária era normalmente silenciosa, mas eu podia ouvir o som furioso de páginas sendo viradas vindo da seção de Arquitetura."
    
    show nicole neutral at center
    
    narrator "Nicole estava cercada por cinco livros grossos sobre alvenaria, elétrica e encanamento básico."
    
    mc "Planejando construir um império, Nicole?"
    
    narrator "Ela deu um sobressalto, mas rapidamente recuperou a postura elegante."
    
    nicole "Estou catalogando os reparos necessários na casa da Rua Aurora. Se dependermos apenas do zelador da faculdade, perderemos o edital antes do fim do semestre."
    
    mc "A casa nem é nossa, não acha que está levando isso muito a sério?"
    
    narrator "Os olhos dela faiscaram. Por um segundo, a fachada de perfeição trincou, revelando um pânico genuíno."
    
    nicole "Você não entende. Algumas pessoas não têm um 'Plano B'. Eu preciso dessa casa em perfeitas condições para manter a bolsa."
    
    narrator "Ela empurrou uma lista gigantesca na minha direção. 'CRONOGRAMA DE REFORMAS'."
    
    menu:
        "Isso parece insano. (Recusar ajudar)":
            mc "Olha, eu vou ajudar com o básico, mas não sou pedreiro. Boa sorte."
            narrator "Nicole suspirou, desapontada, e pegou a lista de volta."
            nicole "Claro. Eu devia saber que não podia contar com ninguém além de mim mesma."
            $ add_affinity_points("nicole", -10)
            
        "Isso vai custar minha energia... mas eu ajudo. (Gastar 15 Energia)":
            if store.player_stats["energy"] >= 15:
                $ update_player_stat("energy", -15)
                mc "Certo. Por onde começamos? Eu posso tentar consertar o telhado."
                narrator "A expressão de Nicole suavizou. Foi sutil, mas a tensão nos ombros dela diminuiu consideravelmente."
                nicole "Obrigada. De verdade. Vou anotar seu nome para as telhas, então."
                $ add_affinity_points("nicole", 20)
            else:
                mc "Eu queria ajudar, mas estou exausto demais agora... mal consigo ficar em pé."
                nicole "Tudo bem. Vá descansar. Eu cuido disso."
    
    hide nicole
    return

label evento_nicole_bolsa:
    scene bg lab with dissolve
    narrator "Encontrei Nicole no laboratório, terminando um trabalho. Ela parecia cansada, mas não arredava o pé."
    mc "Ainda aqui?"
    nicole "A média acadêmica não vai se manter sozinha. E se perdermos a casa, eu..."
    narrator "Ela se interrompe, engolindo em seco."
    $ add_affinity_points("nicole", 5)
    return
