label evento_cap8_cozinha:
    scene bg cozinha com dissolve
    
    narrator "A cozinha da casa parecia um campo de batalha, mas não pelas obras. Havia poeira branca voando por todo lado."
    
    show larissa sad at left
    show camille neutral at right
    
    narrator "Larissa segurava uma colher de pau como se fosse uma espada. Camille estava de olhos fechados, segurando um pacote de farinha rasgado."
    
    mc "Que... que caos é esse?"
    
    larissa "Eu ia fazer um lanche proteico pra quem tá carregando entulho lá em cima. A Camille achou que a farinha integral tinha energia estagnada!"
    
    camille "E tinha! A fábrica onde foi embalada claramente possui bloqueios industriais severos. Eu estava aerando a farinha para libertar o chi!"
    
    narrator "Eu passei a mão no rosto. Eu estava coberto de gesso, e agora, de farinha também."
    
    menu:
        "Mandar limparem. (Poupar energia)":
            mc "Eu não ligo pro Chi da farinha. Limpem essa bagunça antes que o cimento seque lá na sala."
            larissa "Ok, ok, mestre de obras. Já vamos limpar."
            $ add_affinity_points("camille", -5)
            $ add_affinity_points("larissa", -5)
            
        "Entrar na guerra. (Gastar 15 Energia e 20 Carisma)":
            if store.player_stats["energy"] >= 15 and store.player_stats["charisma"] >= 20:
                $ update_player_stat("energy", -15)
                mc "Aerar a farinha, é? Deixa eu ver se os ovos também precisam ter o Chi libertado."
                narrator "Eu peguei um ovo cru e ameacei jogar na cabeça da Larissa."
                larissa "NÃO OUSA!"
                narrator "Larissa riu e jogou um punhado de farinha na minha cara. Camille abriu um sorriso raro e jogou um pouco de água no meu ombro."
                camille "Água limpa a aura. E cria uma pasta excelente com farinha no seu cabelo."
                narrator "Nós rimos alto no meio daquela bagunça, sujos de massa de construção e bolo cru. A ameaça de perder a casa estava lá, mas naquele momento, só importava a nossa risada na cozinha."
                $ add_affinity_points("camille", 25)
                $ add_affinity_points("larissa", 25)
            else:
                mc "Eu não tenho energia pra separar briga mística de confeitaria agora. Pelo amor de Deus, só não sujem a sala que eu acabei de varrer."
                
    hide larissa
    hide camille
    return
