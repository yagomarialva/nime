# script.rpy
image bg room = "images/cenarios/room.jpg"
image p happy = "images/characters/personagem_happy.png"
# image bg park 

label start:
    scene bg room with fade
    show p happy at center

    p "Olá, seja bem-vindo ao meu jogo!"
    p "Está é a faculdade sexo, você quer conhecer alguns pontos dela comigo cara ?!"
    menu:
            "Vamos ao parque!":
                p "Ótimo! Vamos ao parque!"
                # jump park
                jump capitulo2
            "Vamos ao shopping!":
                p "Interessante, vamos ao shopping!"
                # jump shopping
                jump capitulo2
            "Vamos a Cafeteria !":
                p " Uau estva precisando de um coffee YEAHHHH " 
            
        

        
    jump capitulo1
