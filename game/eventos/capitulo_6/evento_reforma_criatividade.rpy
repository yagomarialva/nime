label evento_reforma_criatividade:
    scene bg quintal with dissolve
    
    narrator "O quintal virou um canteiro de obras. Madeiras e lonas espalhadas por todo canto."
    
    show huey neutral at left
    show larissa sad at right
    
    larissa "Ok, as madeiras eu consegui carregar da caçamba. Mas como a gente vai prender isso no teto sem uma furadeira profissional?"
    
    huey "A física das lajes exige triangulação... Mas esteticamente, essas vigas cruas ofendem a harmonia do ambiente."
    
    mc "Huey, a gente só quer que o teto não caia na nossa cabeça. A estética fica pra depois."
    
    menu:
        "Ligar pra um profissional e gastar dinheiro. (Gastar 100 Dinheiro)":
            if store.player_stats["money"] >= 100:
                $ update_player_stat("money", -100)
                mc "Eu não sei construir nada. Toma aqui, vou pagar aquele pedreiro da esquina pra prender as madeiras."
                larissa "Isso quebra o espírito 'Do It Yourself', mas beleza."
                narrator "O teto foi estabilizado, mas as finanças doerão."
                $ add_affinity_points("larissa", 5)
            else:
                mc "Eu queria pagar um cara, mas tô liso."
                larissa "Então mexe os braços, novato."
                
        "Usar geometria artística para prender as vigas. (Gastar 15 Energia e 20 Criatividade)":
            if store.player_stats["energy"] >= 15 and store.player_stats["creativity"] >= 20:
                $ update_player_stat("energy", -15)
                mc "Espera. E se não precisarmos furar a parede portante? Huey, se pegarmos aquele bambu ali e cruzarmos com as ripas usando nós de amarração da quadra..."
                narrator "Larissa me olhou perplexa. Huey de repente abriu um sorriso radiante."
                huey "Geometria orgânica! Sim! Uma estrutura retesada e flexível. O teto não vai ficar preso, ele vai flutuar de forma segura!"
                narrator "Nós três trabalhamos duro por duas horas. O teto não apenas ficou seguro usando nós industriais que Larissa conhecia, mas Huey transformou a lona de proteção numa cabana artística que lembrava o teto de um circo."
                larissa "Eu tô genuinamente impressionada."
                $ add_affinity_points("larissa", 15)
                $ add_affinity_points("huey", 15)
            else:
                mc "Eu queria fazer uma amarração inteligente, mas minha cabeça tá um branco total. Não tenho a menor ideia de como ligar isso."
                larissa "Sem problemas. Deixa que eu prego tudo."
                
    hide huey
    hide larissa
    return
