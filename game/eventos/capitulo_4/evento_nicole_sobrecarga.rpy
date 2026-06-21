label evento_nicole_sobrecarga:
    scene bg sala_jantar with dissolve
    
    narrator "A pia da cozinha parecia uma escultura moderna de louça suja."
    
    show nicole angry at center
    
    narrator "Nicole esfregava uma panela com uma força assassina. O cabelo perfeitamente arrumado dela tinha mechas soltas presas na testa de suor."
    
    nicole "Isso é insustentável. A Larissa era a responsável pelas compras pesadas e por limpar o quintal. Sem ela, a logística da casa quebrou!"
    
    mc "Ela rompeu os ligamentos, Nicole. Não foi porque ela quis."
    
    nicole "Eu sei disso! Você acha que eu não tenho coração?!"
    
    narrator "Ela largou a esponja. Os ombros dela caíram, exaustos."
    
    nicole "Mas a poeira não tem empatia. O professor Wendell não tem empatia. Se a casa cair aos pedaços, nós vamos para a rua. Eu não posso ir para a rua."
    
    menu:
        "Isso não é problema meu. (Poupar energia)":
            mc "Bom, boa sorte aí com a panela. Vou pro meu quarto."
            nicole "E depois sou eu a sem coração."
            $ add_affinity_points("nicole", -10)
            
        "Pagar a limpeza/comida para aliviar a barra. (Gastar 50 Dinheiro)":
            if store.player_stats["money"] >= 50:
                $ update_player_stat("money", -50)
                mc "Larga a esponja. Eu acabei de pedir um delivery pra casa toda e chamei alguém pra limpar o quintal hoje. Por minha conta."
                narrator "Nicole olhou para mim como se eu tivesse acabado de partir o Mar Vermelho."
                nicole "Você... pagou por isso? Com o seu próprio dinheiro?"
                mc "Eu falei que ia cobrir a parte da Larissa. Vá descansar um pouco."
                narrator "Ela mordeu o lábio inferior, claramente lutando contra a vontade de chorar de alívio, e assentiu silenciosamente."
                $ add_affinity_points("nicole", 20)
            else:
                mc "Eu até pagaria alguém pra fazer isso por você, mas estou tão pobre quanto você."
                nicole "Ótimo. Então pegue um rodo."
                
    hide nicole
    return
